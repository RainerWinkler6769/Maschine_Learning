#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
format_tests.py – Formatierungsroutine für Test-Markdown-Dokumente.

Anwendung:
    python scripts/format_tests.py                  # alle .md in tests/
    python scripts/format_tests.py pfad/zur/datei.md

Änderungen:
  1. Umlaute im Fließtext (ae→ä, oe→ö, ue→ü, ss→ss) – NICHT im Code
  2. Tabellen mit korrekten, ausgerichteten Trennlinien für Word-Export
  3. Code-Blöcke grau hinterlegt (<pre>-Wrapper mit #f6f8fa)
  4. Antwortbereiche grau hinterlegt (bereits vorhanden, falls fehlend: ergänzt)
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. Umlaut-Korrekturen (nur im Fließtext, nicht im Code)
# ---------------------------------------------------------------------------
# Reihenfolge wichtig: längere Muster zuerst

UMLAUT_MAP = [
    # Groß
    ("Ae",  "Ä"),
    ("Oe",  "Ö"),
    ("Ue",  "Ü"),
    # Klein
    ("ae",  "ä"),
    ("oe",  "ö"),
    ("ue",  "ü"),
]

# Wörter, die ae/oe/ue im Code-Kontext haben (Variablen, Dateinamen, URLs)
# Diese werden NICHT im Fließtext angetastet, wenn sie in Backticks stehen.
INLINE_CODE_RE  = re.compile(r'`[^`]+`')
HTML_ATTR_RE    = re.compile(r'(style|class|href|src)="[^"]*"', re.IGNORECASE)
# Dateinamen/Pfade und underscore_variablen schützen
FILEPATH_RE     = re.compile(r'[\w./\\-]+\.\w{1,5}')   # z.B. haeuser.csv, ../daten/x.py
UNDERSCORE_RE   = re.compile(r'\b\w+(?:ae|oe|ue)\w*_\w+|\b\w+_\w*(?:ae|oe|ue)\w*')  # snake_case


def protect_segments(line: str):
    """Gibt (bereinigte_linie, (start, end, original)) zurück.
    Schützt Inline-Code und HTML-Attribute vor Umlaut-Ersetzung."""
    segments = []
    protected = line

    def replace_with_placeholder(m):
        idx = len(segments)
        placeholder = f"\x00PROT{idx:04d}\x00"
        segments.append((placeholder, m.group(0)))
        return placeholder

    protected = INLINE_CODE_RE.sub(replace_with_placeholder, protected)
    protected = HTML_ATTR_RE.sub(replace_with_placeholder, protected)
    protected = FILEPATH_RE.sub(replace_with_placeholder, protected)
    protected = UNDERSCORE_RE.sub(replace_with_placeholder, protected)
    return protected, segments


def restore_segments(line: str, segments: list) -> str:
    for placeholder, original in segments:
        line = line.replace(placeholder, original)
    return line


def fix_umlauts_in_line(line: str) -> str:
    protected, segments = protect_segments(line)
    for old, new in UMLAUT_MAP:
        protected = protected.replace(old, new)
    return restore_segments(protected, segments)


# ---------------------------------------------------------------------------
# 2. Tabellen-Formatierung → HTML-Tabelle mit sichtbaren Rahmen (Word-kompatibel)
# ---------------------------------------------------------------------------

TABLE_STYLE = (
    'style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; font-size: 11pt;"'
)
TH_STYLE = (
    'style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; '
    'text-align: left; font-weight: bold;"'
)
TD_STYLE = (
    'style="border: 1px solid #000000; padding: 6px 10px; text-align: left; '
    'min-width: 80px;"'
)


def _parse_cells(line: str) -> list:
    """Zerlegt eine Markdown-Tabellenzeile in einzelne Zellen."""
    cells = [c.strip() for c in line.strip().split("|")]
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def _is_separator(cells: list) -> bool:
    return bool(cells) and all(re.fullmatch(r'[-: ]+', c) for c in cells if c)


def format_table(lines: list) -> list:
    """Konvertiert eine Markdown-Tabelle in eine HTML-Tabelle mit Rahmen.
    Umlaute in Zellen werden ebenfalls korrigiert.
    Ergebnis ist direkt per Copy-Paste in Word einfügbar."""
    rows = []
    header = None

    for line in lines:
        cells = _parse_cells(line)
        if not cells:
            continue
        if _is_separator(cells):
            if rows:
                header = rows[-1]  # Zeile vor dem Separator ist Kopfzeile
                rows = rows[:-1]   # Entfernen aus normalen Zeilen
            continue
        # Umlaute in Zellen korrigieren
        cells = [fix_umlauts_in_line(c) for c in cells]
        rows.append(cells)

    # Zusammenbauen
    html_lines = [f'<table {TABLE_STYLE}>']

    if header:
        html_lines.append("  <thead>")
        html_lines.append("    <tr>")
        for cell in header:
            html_lines.append(f"      <th {TH_STYLE}>{cell}</th>")
        html_lines.append("    </tr>")
        html_lines.append("  </thead>")

    html_lines.append("  <tbody>")
    for row in rows:
        html_lines.append("    <tr>")
        for cell in row:
            html_lines.append(f"      <td {TD_STYLE}>{cell}</td>")
        html_lines.append("    </tr>")
    html_lines.append("  </tbody>")
    html_lines.append("</table>")

    return html_lines


# ---------------------------------------------------------------------------
# 3. Code-Block grau hinterlegen
# ---------------------------------------------------------------------------

CODE_OPEN_HTML  = '<div style="background-color: #f0f0f0; padding: 10px 14px; border-radius: 6px; font-family: monospace; border-left: 3px solid #cccccc;">\n\n'
CODE_CLOSE_HTML = '\n</div>\n'

ANSWER_OPEN_HTML = '<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">\n'
ANSWER_CLOSE_HTML = '</div>\n'


# ---------------------------------------------------------------------------
# Hauptverarbeitung
# ---------------------------------------------------------------------------

def process_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    result_lines = []
    in_code_block = False
    code_fence_marker = ""
    in_table = False
    table_buffer = []
    i = 0

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip("\n")

        # --- Code-Block Grenzen erkennen ---
        fence_match = re.match(r'^(`{3,}|~{3,})', line)
        if fence_match:
            marker = fence_match.group(1)
            if not in_code_block:
                # Öffnende Grenze
                in_code_block = True
                code_fence_marker = marker
                # Flush pending table
                if table_buffer:
                    result_lines.extend(ln + "\n" for ln in format_table(table_buffer))
                    table_buffer = []
                    in_table = False
                result_lines.append(CODE_OPEN_HTML)
                result_lines.append(line + "\n")
            elif line.startswith(code_fence_marker):
                # Schließende Grenze
                in_code_block = False
                code_fence_marker = ""
                result_lines.append(line + "\n")
                result_lines.append(CODE_CLOSE_HTML)
            else:
                result_lines.append(line + "\n")
            i += 1
            continue

        # --- Innerhalb Code-Block: keine Umlaut-Ersetzung ---
        if in_code_block:
            result_lines.append(line + "\n")
            i += 1
            continue

        # --- Tabellen sammeln ---
        is_table_line = "|" in line and line.strip().startswith("|")
        if is_table_line:
            in_table = True
            table_buffer.append(line)
            i += 1
            continue
        else:
            if in_table:
                result_lines.extend(ln + "\n" for ln in format_table(table_buffer))
                table_buffer = []
                in_table = False

        # --- Antwortbereiche normalisieren (bestehende divs beibehalten, ggf. ersetzen) ---
        # Altes einfaches div → erweitertes div mit Border
        if line.strip() == '<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px;">':
            result_lines.append(ANSWER_OPEN_HTML)
            i += 1
            continue

        # Bereits korrekt formatiertes ANSWER_OPEN_HTML einfach durchleiten
        if line.strip().startswith('<div style="background-color: #f6f8fa'):
            result_lines.append(line + "\n")
            i += 1
            continue

        # --- Bare "Antwort:" / "Musterlösung:" / "Aufgabenstellung:" → graue Box ---
        ANSWER_MARKERS = re.compile(
            r'^(Antwort|Musterl[oö]sung|Aufgabenstellung)\s*:\s*$', re.IGNORECASE
        )
        if ANSWER_MARKERS.match(line.strip()):
            # Marker-Zeile als fette Überschrift in der Box ausgeben
            label = fix_umlauts_in_line(line.strip())
            result_lines.append(ANSWER_OPEN_HTML)
            result_lines.append(f"**{label}**\n")
            result_lines.append("\n")
            # Alle folgenden Zeilen bis zur nächsten Aufgaben-Überschrift, Code-Fence
            # oder leerem Abschnitt vor nächster ## / ### Überschrift in die Box nehmen
            i += 1
            while i < len(lines):
                peek = lines[i].rstrip("\n")
                # Abbruch bei neuer Überschrift auf gleicher oder höherer Ebene
                if re.match(r'^#{1,3} ', peek):
                    break
                # Abbruch bei Code-Fence (wird separat behandelt)
                if re.match(r'^(`{3,}|~{3,})', peek):
                    break
                # Abbruch bei einem weiteren Antwort-Marker
                if ANSWER_MARKERS.match(peek.strip()):
                    break
                # Abbruch bei bereits geöffnetem div
                if peek.strip().startswith('<div'):
                    break
                result_lines.append(fix_umlauts_in_line(peek) + "\n")
                i += 1
            result_lines.append(ANSWER_CLOSE_HTML)
            result_lines.append("\n")
            continue

        # --- Umlaut-Korrektur im Fließtext ---
        line = fix_umlauts_in_line(line)

        result_lines.append(line + "\n")
        i += 1

    # Noch offene Tabelle schreiben
    if table_buffer:
        result_lines.extend(ln + "\n" for ln in format_table(table_buffer))

    new_text = "".join(result_lines)
    path.write_text(new_text, encoding="utf-8")
    print(f"  ✓  {path}")


def main():
    if len(sys.argv) > 1:
        targets = [Path(p) for p in sys.argv[1:]]
    else:
        repo_root = Path(__file__).parent.parent
        targets = sorted(repo_root.glob("tests/**/*.md"))

    if not targets:
        print("Keine .md-Dateien gefunden.")
        return

    print(f"Verarbeite {len(targets)} Datei(en) …")
    for p in targets:
        try:
            process_file(p)
        except Exception as e:
            print(f"  ✗  {p}: {e}")

    print("\nFertig.")


if __name__ == "__main__":
    main()
