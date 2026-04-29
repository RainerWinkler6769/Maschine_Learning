const API_BASE_URL = "http://localhost:8000";
const SETTINGS_KEY = "elearning-ui-settings-v1";

const DEFAULT_SETTINGS = {
	schoolName: "Meine Schule",
	logoUrl: "",
	headingColor: "#fff7f0",
	bodyColor: "#3a2118",
	accent1: "#8f2d1f",
	accent2: "#f08c1a",
};

let activeTask = null;

function byId(id) {
	return document.getElementById(id);
}

function loadSettings() {
	try {
		const raw = localStorage.getItem(SETTINGS_KEY);
		return raw ? { ...DEFAULT_SETTINGS, ...JSON.parse(raw) } : DEFAULT_SETTINGS;
	} catch (_error) {
		return DEFAULT_SETTINGS;
	}
}

function saveSettings(settings) {
	localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
}

function applySettings(settings) {
	const root = document.documentElement;
	root.style.setProperty("--heading-color", settings.headingColor);
	root.style.setProperty("--body-color", settings.bodyColor);
	root.style.setProperty("--accent-1", settings.accent1);
	root.style.setProperty("--accent-2", settings.accent2);

	byId("message").textContent = `Hallo Welt aus JavaScript - ${settings.schoolName}`;
	byId("banner-subtitle").textContent = "E-Learning Studio - Schuelerzentriert und testbar";

	const logo = byId("school-logo");
	if (settings.logoUrl) {
		logo.src = settings.logoUrl;
		logo.style.display = "block";
	} else {
		logo.style.display = "none";
	}
}

function fillSettingsForm(settings) {
	byId("school-name-input").value = settings.schoolName;
	byId("logo-url-input").value = settings.logoUrl;
	byId("heading-color-input").value = settings.headingColor;
	byId("body-color-input").value = settings.bodyColor;
	byId("accent-1-input").value = settings.accent1;
	byId("accent-2-input").value = settings.accent2;
}

function readSettingsForm() {
	return {
		schoolName: byId("school-name-input").value || DEFAULT_SETTINGS.schoolName,
		logoUrl: byId("logo-url-input").value.trim(),
		headingColor: byId("heading-color-input").value,
		bodyColor: byId("body-color-input").value,
		accent1: byId("accent-1-input").value,
		accent2: byId("accent-2-input").value,
	};
}

function renderTask(task) {
	activeTask = task;
	byId("task-title").textContent = task.title;
	byId("task-goal").textContent = `Lernziel: ${task.learning_goal}`;
	byId("task-expectation").textContent = `Erwartungshorizont: ${task.expectation_horizon}`;
	byId("code-input").value = task.starter_code;
	byId("test-results").innerHTML = "";

	const boxWrap = byId("info-boxes");
	boxWrap.innerHTML = "";

	const hintsBox = createInfoBox(
		"help-hints-box",
		"info-box help-box",
		"Hilfen",
		task.help_hints
	);

	const strategyBox = createInfoBox(
		"didactic-strategy-box",
		"info-box strategy-box",
		"Didaktische Strategie",
		task.didactic_steps
	);

	const checksBox = createInfoBox(
		"selfcheck-box",
		"info-box checks-box",
		"Selbstkontrolle",
		task.self_check_questions
	);

	boxWrap.append(hintsBox, strategyBox, checksBox);
}

function createInfoBox(id, className, title, items) {
	const box = document.createElement("section");
	box.id = id;
	box.className = className;

	const h = document.createElement("h4");
	h.textContent = title;

	const list = document.createElement("ul");
	items.forEach((item) => {
		const li = document.createElement("li");
		li.textContent = item;
		list.appendChild(li);
	});

	box.append(h, list);
	return box;
}

function runBrowserTests(studentCode, task) {
	const results = [];
	let studentFn;

	try {
		const fnFactory = new Function(
			`${studentCode}; return (typeof ${task.function_name} === 'function') ? ${task.function_name} : null;`
		);
		studentFn = fnFactory();
	} catch (error) {
		return [{ ok: false, label: "Syntax", detail: `Syntaxfehler: ${error.message}` }];
	}

	if (typeof studentFn !== "function") {
		return [
			{
				ok: false,
				label: "Funktion",
				detail: `Die Funktion ${task.function_name} wurde nicht gefunden.`,
			},
		];
	}

	task.tests.forEach((t, idx) => {
		try {
			const actual = studentFn(...t.args);
			const ok = JSON.stringify(actual) === JSON.stringify(t.expected);
			results.push({
				ok,
				label: `Test ${idx + 1}`,
				detail: ok
					? `ok - ${t.description}`
					: `fehlgeschlagen - ${t.description}; erwartet ${JSON.stringify(t.expected)}, bekommen ${JSON.stringify(actual)}`,
			});
		} catch (error) {
			results.push({
				ok: false,
				label: `Test ${idx + 1}`,
				detail: `Fehler bei Ausfuehrung: ${error.message}`,
			});
		}
	});

	return results;
}

function renderTestResults(results) {
	const list = byId("test-results");
	list.innerHTML = "";

	results.forEach((r) => {
		const li = document.createElement("li");
		li.className = r.ok ? "result-ok" : "result-bad";
		li.textContent = `${r.ok ? "PASS" : "FAIL"} - ${r.label}: ${r.detail}`;
		list.appendChild(li);
	});
}

async function loadTaskFromApi() {
	const res = await fetch(`${API_BASE_URL}/learning/tasks/mean-value`);
	if (!res.ok) {
		throw new Error(`API Fehler ${res.status}`);
	}
	return res.json();
}

function wireEvents() {
	byId("save-settings-btn").addEventListener("click", () => {
		const settings = readSettingsForm();
		saveSettings(settings);
		applySettings(settings);
	});

	byId("run-tests-btn").addEventListener("click", () => {
		if (!activeTask) return;
		const studentCode = byId("code-input").value;
		const results = runBrowserTests(studentCode, activeTask);
		renderTestResults(results);
	});

	byId("reset-code-btn").addEventListener("click", () => {
		if (!activeTask) return;
		byId("code-input").value = activeTask.starter_code;
		byId("test-results").innerHTML = "";
	});
}

async function bootstrap() {
	const settings = loadSettings();
	fillSettingsForm(settings);
	applySettings(settings);
	wireEvents();

	try {
		const task = await loadTaskFromApi();
		renderTask(task);
	} catch (error) {
		byId("task-title").textContent = "Aufgabe konnte nicht geladen werden";
		byId("task-goal").textContent = "Bitte pruefe, ob die Python-API auf Port 8000 laeuft.";
		byId("task-expectation").textContent = `Details: ${error.message}`;
	}
}

bootstrap();
