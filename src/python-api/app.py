from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/learning/*": {"origins": ["http://localhost:8081"]}})

TASKS = {
    "mean-value": {
        "id": "mean-value",
        "title": "Aufgabe: Mittelwert berechnen",
        "learning_goal": "Listen verarbeiten und den arithmetischen Mittelwert robust berechnen",
        "expectation_horizon": (
            "Die Funktion liefert fuer normale Listen den korrekten Mittelwert, "
            "behandelt leere Listen sinnvoll und ist gut lesbar dokumentiert"
        ),
        "function_name": "berechneMittelwert",
        "starter_code": (
            "function berechneMittelwert(werte) {\n"
            "  // TODO: Implementiere den Mittelwert\n"
            "  return 0;\n"
            "}\n"
        ),
        "help_hints": [
            "Gehe schrittweise vor: erst Summe, dann Division durch die Anzahl.",
            "Nutze eine fruehe Rueckgabe fuer den Sonderfall leere Liste.",
            "Teste mit einfachen Eingaben wie [2, 4, 6].",
        ],
        "didactic_steps": [
            "Verstehe die Aufgabe in eigenen Worten.",
            "Formuliere zuerst den Sonderfall, dann den Normalfall.",
            "Pruefe die Loesung mit mindestens drei selbst gewaehlten Beispielen.",
        ],
        "self_check_questions": [
            "Was soll bei einer leeren Liste passieren und warum?",
            "Ist das Ergebnis fuer [10, 20, 30] exakt 20?",
            "Ist dein Code auch fuer Dezimalzahlen nachvollziehbar?",
        ],
        "tests": [
            {
                "description": "normale ganze Zahlen",
                "args": [[2, 4, 6]],
                "expected": 4,
            },
            {
                "description": "gemischte positive Zahlen",
                "args": [[1, 2, 9]],
                "expected": 4,
            },
            {
                "description": "leere Liste",
                "args": [[]],
                "expected": 0,
            },
        ],
    }
}


@app.get("/")
def hello_world():
    return jsonify({"message": "Hallo Welt aus Python"})


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/db")
def db_info():
    return jsonify(
        {
            "mysql_host": os.getenv("MYSQL_HOST", "mysql"),
            "mysql_database": os.getenv("MYSQL_DATABASE", "edu_demo"),
            "mode": "MySQL oder JSON nutzbar",
        }
    )


@app.get("/learning/tasks")
def list_tasks():
    return jsonify(
        [
            {
                "id": task["id"],
                "title": task["title"],
                "learning_goal": task["learning_goal"],
            }
            for task in TASKS.values()
        ]
    )


@app.get("/learning/tasks/<task_id>")
def get_task(task_id: str):
    task = TASKS.get(task_id)
    if not task:
        return jsonify({"error": "task_not_found", "task_id": task_id}), 404
    return jsonify(task)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
