import subprocess
import os
import ollama

def get_latest_git_diff():
    try:
        # Grabs the diff of the latest commit
        result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except Exception:
        # Fallback if it's the very first commit or git isn't ready
        return None

def analyze_commit():
    diff = get_latest_git_diff()
    
    if not diff or not diff.strip():
        # Fallback sample for demonstration if diff is empty
        diff = """
        + async function loadProfile(id) {
        +     let profile;
        +     api.fetch('/user/' + id, (res) => { profile = res; });
        +     return profile;
        + }
        """
        print("[Demo Mode] Using sample staged diff.")

    print("\n--- 1. EduHermes Socratic Review of Staged Commit ---")
    with open("skills/socratic_tutor.md", "r") as f:
        skill_prompt = f.read()

    review = ollama.chat(
        model='gemma4',
        messages=[
            {'role': 'system', 'content': skill_prompt},
            {'role': 'user', 'content': f"Analyze this git commit diff for bugs:\n\n{diff}"}
        ]
    )
    print("\n[EduHermes Feedback]:")
    print(review['message']['content'])

    print("\n--- 2. Background Hermes Agent: Updating Student Skill Profile ---")
    skill_gen = ollama.chat(
        model='gemma4',
        messages=[{
            'role': 'user',
            'content': f"Extract the core concept error from this diff and create a remediation SKILL.md with YAML frontmatter:\n\n{diff}"
        }]
    )

    os.makedirs("skills", exist_ok=True)
    out_file = "skills/remediation_latest_commit.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(skill_gen['message']['content'])
    print(f"\n[Persistent Memory Updated]: Saved to '{out_file}'")

if __name__ == "__main__":
    analyze_commit()