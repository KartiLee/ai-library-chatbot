# Library Chatbot Prototype using Rasa and Python (Basic Example)

# Step 1: Define NLU Training Data (data/nlu.yml)
nlu_data = """
version: "2.0"
nlu:
- intent: greet
  examples: |
    - hello
    - hi there
    - good morning

- intent: search_book
  examples: |
    - I am looking for a book on AI
    - Find books about machine learning
    - Do you have books on data science?

- intent: goodbye
  examples: |
    - bye
    - goodbye
    - see you later
"""

# Step 2: Define Domain (domain.yml)
domain_data = """
version: "2.0"
intents:
  - greet
  - search_book
  - goodbye

responses:
  utter_greet:
    - text: "Hello! How can I help you today at the library?"

  utter_goodbye:
    - text: "Goodbye! Have a great day."

  utter_search_book:
    - text: "Sure, I can help with that. What topic are you interested in?"

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true
"""

# Step 3: Define Stories (stories.yml)
stories_data = """
version: "2.0"
stories:
- story: book search path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: search_book
  - action: utter_search_book
  - intent: goodbye
  - action: utter_goodbye
"""

# Step 4: Python script to simulate user interaction (demo.py)
def chatbot_response(user_input):
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Hello! How can I help you today at the library?"
    elif "book" in user_input.lower():
        return "Sure, I can help with that. What topic are you interested in?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that. Could you please rephrase?"

# Simulated interaction instead of real input (for environments without stdin)
def run_demo_simulation():
    test_inputs = [
        "Hello",
        "I want a book on AI",
        "Bye"
    ]
    for user in test_inputs:
        print("You:", user)
        print("Bot:", chatbot_response(user))

if __name__ == "__main__":
    run_demo_simulation()
