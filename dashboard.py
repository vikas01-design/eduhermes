import streamlit as st
import os
import subprocess
import glob
import ollama

st.set_page_config(
    page_title="EduHermes | AI Dev Mentor",
    page_icon="🎓",
    layout="wide"
)

# Custom Clean Light CSS Styling
st.markdown("""
<style>
    /* Main App Background & Text */
    .stApp {
        background-color: #ffffff;
        color: #0f172a;
    }
    
    /* Header Card */
    .header-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 24px;
    }
    .header-title {
        font-size: 26px;
        font-weight: 700;
        color: #0f172a;
        margin: 0;
    }
    .header-sub {
        font-size: 14px;
        color: #64748b;
        margin-top: 4px;
    }

    /* Metric Badges */
    div[data-testid="stMetric"] {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 12px 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    div[data-testid="stMetricLabel"] > div {
        color: #64748b;
        font-size: 13px;
        font-weight: 500;
    }
    div[data-testid="stMetricValue"] > div {
        color: #0f172a;
        font-weight: 700;
    }

    /* Clean Tabs */
    button[data-baseweb="tab"] {
        font-size: 15px;
        font-weight: 600;
        color: #64748b;
        padding: 10px 18px;
    }
    button[aria-selected="true"] {
        color: #2563eb !important;
        border-bottom-color: #2563eb !important;
    }

    /* Card Panels */
    .card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.03);
        margin-bottom: 20px;
    }

    /* Chat Messages Light Styling */
    div[data-testid="stChatMessage"] {
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 10px;
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Top Clean Header
st.markdown("""
<div class="header-box">
    <div class="header-title">🎓 EduHermes: Autonomous Dev Mentor</div>
    <div class="header-sub">Local Edge AI (Gemma 4 via Ollama) • Real-time Socratic Tutoring • Self-Authoring Skills</div>
</div>
""", unsafe_allow_html=True)

# Metric Badges
m1, m2, m3 = st.columns(3)
with m1:
    st.metric(label="Inference Engine", value="Gemma 4 (Local Edge)")
with m2:
    st.metric(label="Mentorship Mode", value="Socratic (No Answers)")
with m3:
    skill_count = len(glob.glob("skills/*.md"))
    st.metric(label="Custom Study Guides", value=f"{skill_count} Generated")

st.write("")

# Main Tabs
tab_chat, tab_skills, tab_git = st.tabs([
    "💬 Student & Mentor Chat",
    "📖 Auto-Generated Study Guides",
    "⚙️ Git Hook & Staged Diff"
])

# ----------------- TAB 1: SOCRATIC CHAT -----------------
with tab_chat:
    col_code, col_chat = st.columns([1, 1.2], gap="large")

    with col_code:
        st.markdown("#### 📝 Inspected Student Code (`app.js`)")
        st.caption("Code committed by student containing logical flaws:")
        if os.path.exists("app.js"):
            with open("app.js", "r") as f:
                code_text = f.read()
            st.code(code_text, language="javascript")
        else:
            st.info("No app.js file found.")
        
        st.success("✅ **Socratic Rule Active:** `skills/socratic_tutor.md` guides inquiry without leaking the answer.")

    with col_chat:
        st.markdown("#### 💬 Interactive Discussion")
        st.caption("Ask questions or explain your reasoning:")

        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": "I noticed in your recent commit that `fetchScores()` returns `scores` right away. What value will `scores` hold before the timer finishes?"
                }
            ]

        chat_container = st.container(height=360)
        with chat_container:
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])

        if prompt := st.chat_input("Type your response to EduHermes..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            with chat_container:
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    with st.spinner("Gemma 4 is thinking..."):
                        skill_rules = ""
                        if os.path.exists("skills/socratic_tutor.md"):
                            with open("skills/socratic_tutor.md", "r") as f:
                                skill_rules = f.read()

                        chat_payload = [{"role": "system", "content": skill_rules}]
                        chat_payload.extend(st.session_state.messages)

                        res = ollama.chat(model='gemma4', messages=chat_payload)
                        reply = res['message']['content']
                        st.markdown(reply)
                        st.session_state.messages.append({"role": "assistant", "content": reply})

# ----------------- TAB 2: SKILLS LIBRARY -----------------
with tab_skills:
    st.markdown("#### 🧠 Autonomous Study Guides (`SKILL.md`)")
    st.caption("Dynamically authored whenever student commits faulty logic:")

    all_skills = glob.glob("skills/*.md")
    if all_skills:
        chosen_skill = st.selectbox("Select a generated guide to inspect:", all_skills)
        with open(chosen_skill, "r", encoding="utf-8", errors="ignore") as f:
            guide_content = f.read()

        st.markdown("---")
        st.markdown(guide_content)
    else:
        st.info("No guides generated yet.")

# ----------------- TAB 3: GIT INSPECTOR -----------------
with tab_git:
    st.markdown("#### 🔍 Automated Git Hook Activity")
    st.caption("Triggers on every `git commit` via `.git/hooks/post-commit`:")

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("**Recent Commit Log:**")
        try:
            log_out = subprocess.run(["git", "log", "-n", "5", "--oneline"], capture_output=True, text=True).stdout
            st.code(log_out, language="bash")
        except Exception as e:
            st.error(f"Error: {e}")

    with c2:
        st.markdown("**Inspected Git Diff (HEAD~1):**")
        try:
            diff_out = subprocess.run(["git", "diff", "HEAD~1", "HEAD"], capture_output=True, text=True).stdout
            st.code(diff_out if diff_out.strip() else "Clean working directory.", language="diff")
        except Exception as e:
            st.error(f"Error: {e}")