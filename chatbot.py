import nltk
import spacy

print("Library Chatbot (prototype)")
print("Type 'exit' to end the chat.")

while True:
    try:
        user = input("You: ")
        if user.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        if "book" in user.lower():
            print("Chatbot: You can search for books by title or author. Try 'Find books on AI.'")
        else:
            print("Chatbot: I'm here to help with your library needs.")
    except Exception as e:
        print(f"Chatbot encountered an error: {e}")
