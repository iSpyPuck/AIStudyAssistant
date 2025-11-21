import os
from dotenv import load_dotenv
from openai import OpenAI

# Load env variables from .env
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY missing. Add it to your .env file.")

client = OpenAI(api_key=API_KEY)

def load_behavior():
    with open("behavior.txt", "r") as f:
        return f.read()

def ask_assistant(user_input):
    system_behavior = load_behavior()

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_behavior},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message["content"]

def main():
    print("AI Study Assistant — type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        try:
            answer = ask_assistant(user_input)
            print("\nAssistant:", answer, "\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
