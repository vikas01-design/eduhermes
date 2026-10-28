# 🎓 EduHermes: Autonomous, Self-Evolving Dev Mentor

> **A local-first, autonomous coding mentor that turns failed git commits into active learning moments using Google Gemma 4 and dynamic Agent Skills.**

---

## 📌 What is EduHermes?

Most AI coding assistants act like calculators: when a student runs into a bug, the tool simply dumps the corrected code. This bypasses genuine problem-solving, leads to copy-paste habits, and causes rapid learning decay—especially in academic labs and university environments.

**EduHermes** changes this paradigm. It acts as an autonomous mentor embedded directly into the developer workflow. Whenever a student commits code containing a bug or anti-pattern, EduHermes:
1. **Intercepts the commit diff** automatically via a local Git hook.
2. **Engages Socratically** using a local Google Gemma 4 model, probing the student with targeted questions about their logic rather than leaking the solution.
3. **Evolves autonomously** by authoring persistent, standardized `SKILL.md` study guides in real time, building a personalized curriculum library tailored to that student's specific knowledge gaps.

---

## 💡 Why It Matters & Key Benefits

* **Pedagogy Over Answers (Socratic Guidance):** EduHermes enforces strict mentoring constraints. It identifies logical divergence (e.g., async race conditions, off-by-one errors) and asks guided questions to help students arrive at the fix themselves.
* **100% Offline & Private (Edge Computing):** Runs entirely on local consumer hardware via Ollama and Google Gemma 4. No cloud API keys, zero token fees, and complete data privacy for student code.
* **Autonomous Procedural Memory (`SKILL.md` Standard):** Inspired by the Hermes Agent self-improvement loop and the Agent Skills open standard, the system dynamically authors structured markdown guides with YAML frontmatter whenever recurring gaps are detected.
* **Zero-Friction Workflow:** Students do not need to copy-paste prompts into a web app. Simply running `git commit` triggers the background mentor daemon automatically.

---

## 🏗️ System Architecture
[ Student Code (app.js) ] ──► [ git commit ]
│
▼ (Triggered via .git/hooks/post-commit)
[ EduHermes Engine (edu_hermes.py) ]
│
┌─────────────────────────┴─────────────────────────┐
▼                                                   ▼
[ Socratic Review ]                               [ Procedural Memory ]
• Reads skills/socratic_tutor.md                  • Analyzes root conceptual flaw
• Evaluates diff via local Gemma 4                • Gemma 4 authors new SKILL.md
• Probes student reasoning                        • Saves to skills/remediation_*.md
│                                                   │
└─────────────────────────┬─────────────────────────┘
▼
[ Interactive Streamlit Dashboard ]
• Tab 1: Live Socratic Dialogue & Student Code
• Tab 2: Rendered Persistent Study Guides
• Tab 3: Git History & Inspected Diffs

---

## 🛠️ Tech Stack & Hackathon Integration

* **LLM Engine:** Google Gemma 4 (`gemma4`) running locally on edge via [Ollama](https://ollama.ai).
* **Agent Skills Ecosystem:** Conforms to the open `SKILL.md` standard with YAML metadata, execution constraints, and progressive disclosure.
* **Autonomous Loop:** Hermes Agent procedural memory pattern for dynamic tool/skill generation.
* **Backend:** Python 3, Git Hooks (`post-commit`), and subprocess automation.
* **Frontend:** Streamlit with a custom light card-based UI.

---

## 🚀 Getting Started

### Prerequisites

1. **Python 3.10+** installed.
2. **Git** installed and initialized.
3. **Ollama** installed on your machine.

### 1. Pull the Model & Start Ollama

Make sure Ollama is running and pull Google's Gemma 4:

```bash
ollama run gemma4
(Once loaded, type /bye to exit back to the terminal; the Ollama background daemon will remain active at http://localhost:11434.)

2. Clone the Repository & Install Dependencies
Bash
git clone [https://github.com/](https://github.com/)<your-username>/eduhermes.git
cd eduhermes

pip install ollama streamlit
3. Set Up the Automated Git Hook
To ensure EduHermes automatically evaluates every commit, install the hook:

On Windows (PowerShell):

PowerShell
Set-Content -Path .git\hooks\post-commit -Value "#!/bin/sh`npython edu_hermes.py"
On Linux / macOS:

Bash
echo -e "#!/bin/sh\npython edu_hermes.py" > .git/hooks/post-commit
chmod +x .git/hooks/post-commit
🖥️ Usage & Live Demo
1. Launch the Dashboard
Start the web interface:

Bash
python -m streamlit run dashboard.py
Open your browser to http://localhost:8501.

2. Trigger an Autonomous Evaluation
Introduce code with a logical flaw (e.g., an asynchronous return error or array boundary bug) into app.js:

JavaScript
// app.js
async function fetchScores() {
  let scores;
  setTimeout(() => { scores = [98, 85, 92]; }, 100);
  return scores;
}
Stage and commit the code:

Bash
git add app.js
git commit -m "feat: add asynchronous score fetcher"
3. Observe the Results
In your terminal: The post-commit hook intercepts the diff, triggers local Gemma 4, and authors a new remediation skill file under skills/.

In the Dashboard:

Tab 1 (Student & Mentor Chat): View the flagged code and chat directly with Gemma 4 to reason through the solution Socratically.

Tab 2 (Auto-Generated Study Guides): Review the dynamically generated SKILL.md guide containing core concepts, pitfalls, and targeted exercises.

Tab 3 (Git Hook & Diff): Inspect the raw commit log and git diff that triggered the review.

📜 License
This project is open-source and distributed under the Apache 2.0 License, aligning with the Google Gemma open model ecosystem.
