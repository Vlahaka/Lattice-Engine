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
