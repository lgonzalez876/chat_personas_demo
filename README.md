# Persona Chat Demo

This project is a simple demo showing how you can change the personality of the chatbot by changing the system prompt. Its meant to be shared with people with zero AI coding experience, so they can get a feel for how the APIs work, and what the role of a system prompt is. There are three example personas already in the script, including a genetics researcher persona! Try chatting with each persona, or make your own.

You'll quickly see that despite the jokes made about it "prompt engineering" is a real thing, the way you build your prompt can wildly affect your output. You can use prompts to give example outputs, demand a specific format, define personas, or special rules you don't want exposed to the user.

**Note:** This is a great example of why collaboration between subject-matter experts and AI specialists is so powerful. When building complex systems to solve real-world problems, you often need to design prompts that guide the model in how to reason through a task. Experts bring tremendous value here—they can help shape these prompts based on the thought processes they've developed through years of experience.

Also, these bots wont be as powerful as the chatgpt that you see online, with long term memory and web search abilities. Those things have to be built.

To run this project, just run the following from the project root after doing the setup below:
```bash
python persona_chat.py
```

Then take a look at the code, and play around with it!

## Setup Instructions

### Creating a Python Virtual Environment

A virtual environment is an isolated Python environment that allows you to manage project-specific dependencies. You dont strictly need it, but this will help keep your python libraries organized.

#### For macOS/Linux:

1. Open a terminal and navigate to your project directory:
   ```bash
   cd path/to/your/project
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
   When activated, your terminal prompt will change to show the name of the virtual environment.

#### For Windows:

1. Open Command Prompt and navigate to your project directory:
   ```cmd
   cd path\to\your\project
   ```

2. Create a virtual environment:
   ```cmd
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```cmd
   venv\Scripts\activate
   ```
   When activated, your command prompt will be prefixed with `(venv)`.

### Installing Requirements

Once your virtual environment is activated, install the requirements:

```bash
pip install -r requirements.txt
```

This will install the following packages:
- openai: The OpenAI Python client
- requests: For making HTTP requests
- python-dotenv: For loading environment variables from a .env file

### Setting Up Your API Key
First, you'll need to get an [OpenAI API Key](http://platform.openai.com/api-keys). This means you'll need to make a dev account, fund it ($10 will last you a while), and get the key.

1. You need a file called `.env` with is your API key saved in this format:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
To help, I included a file called `.env_example` that already has this template. Just run this to make a renamed copy of the template file:
```bash
cp env_example .env
```
Then fill it in with your API key.

### Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```
