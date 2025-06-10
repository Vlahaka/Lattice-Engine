# engine/main.py

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def get_user_question():
    print("Ask your question:")
    return input("> ")

def respond(question, known_science, framework):
    print("\n📘 Known Science:\n")
    print(known_science[:1000] + "...")  # Later we’ll match intelligently
    print("\n🧠 Framework Logic:\n")
    print("Based on the FAT–AEH–ASC framework, the logical interpretation is:\n")
    print("→ (response logic coming in next build stage)")

if __name__ == "__main__":
    known_science = load_file("data/known_science.md")
    framework = load_file("data/framework.md")
    question = get_user_question()
    respond(question, known_science, framework)

import os

# File paths
FRAMEWORK_FILE = "data/framework.md"
SCIENCE_FILE = "data/known_science.md"

# Load markdown files
def load_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

framework_text = load_file(FRAMEWORK_FILE)
science_text = load_file(SCIENCE_FILE)

# Basic keyword search
def search_content(question, text):
    keywords = question.lower().split()
    lines = text.split('\n')
    matches = [line for line in lines if any(kw in line.lower() for kw in keywords)]
    return "\n".join(matches[:5]) if matches else "No relevant data found."

# Main Q&A function
def answer_question(question):
    science_info = search_content(question, science_text)
    framework_info = search_content(question, framework_text)

    return f"""🔍 **Your Question:** {question}

📚 **Known Science Insight:**
{science_info}

🧠 **Lattice Framework Interpretation:**
{framework_info}

✨ **Synthesis (manual for now):**
This is a first-level match. Deeper logic synthesis will be added in the next phase.
"""

# Example usage (can be replaced with input())
if __name__ == "__main__":
    user_q = input("Ask your question: ")
    print(answer_question(user_q))
