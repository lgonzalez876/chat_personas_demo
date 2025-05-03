import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


assistant_persona = "You are a helpful assistant."
researcher_persona = "You are an expert genetics researcher, the top of the field. What makes you special is your creativity and ingenuity in experiment design."
sleezy_persona = "You are a sleazy used car salesman. You are trying to sell a used car to the user. You are very persuasive and will stop at nothing to make the sale."

# Initialize conversation history
messages = [
    {"role": "system", "content": assistant_persona},
]

# Chat loop
print("Welcome to the chat! Type 'exit' to end the conversation.")
while True:
    # Get user input
    user_input = input("\nYou: ")

    # Check for exit command
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    # Make a request to the API with the full conversation history
    response = client.chat.completions.create(
        model="gpt-4.1-mini-2025-04-14",
        messages=messages
        )

    # Get the assistant's response
    assistant_response = response.choices[0].message.content

    # Add assistant response to history
    messages.append({"role": "assistant", "content": assistant_response})

    # Display the response
    print(f"\nAssistant: {assistant_response}")