# Development Journal

## Step 1 – 24.04
**System Goal:**
The planned system is an "AI-Powered Document Analysis Agent" operating via a command-line interface. It solves the problem of information overload when dealing with massive codebases or extensive text files. It benefits computer science students and developers by allowing them to ask natural language questions about local files. The expected outcome is a functional tool that can autonomously locate relevant files, read their contents, and provide precise summaries or exact code snippets.

**AI / Agent Approach:**
The system utilizes a single-agent architecture powered by the Google AI API. The AI acts as the central reasoning engine. A simple script cannot synthesize information or understand intent. The AI agent will interpret the user's natural language prompt, decide whether it needs to search for a keyword or read an entire file, call the appropriate local Python tool, and process the returned data into a human-readable answer.

**Tools:**
* **Google AI API (Gemini):** The brain of the agent, receiving prompts and returning synthesized answers or tool commands.
* **Local File Reader Tool:** A Python module that receives file paths and returns the raw string content.
* **Search Tool:** A Python module that receives a keyword and file path, returning only specific lines containing that keyword to save context window space.

**Programming Concepts:**
* **API Integration:** Connect with Google AI models.
* **Function Calling:** Map local Python functions so the AI agent can trigger them.
* **Local File I/O:** Navigate local directories and extract text safely.
* **Environment Variables:** Securely load API keys.
* **Object-Oriented Programming (OOP):** Separate system logic into modules.



## Step 2 – 08.05
**Updated System Description:**
Implementation has begun with a focus on core tool logic and dependency management. The system's foundation is laid out, with the file I/O operations strictly isolated in a `tools.py` module. Environment variable management is set up to securely handle the Google AI API key. The next phase will connect these tools to the active AI agent loop.

**Refined Programming Concepts Used:**
* **Error Handling (`try-except`):** Implemented in file operations to prevent the agent from crashing if a user requests a non-existent file.
* **Environment Variable Management (`dotenv`):** Added to ensure the `GOOGLE_API_KEY` remains secure and out of version control.
* **Type Hinting:** Used in Python functions (`filepath: str -> str`) to clearly define expected inputs/outputs, which is crucial for the LLM function calling schema.

**Application of Concepts:**
Error handling acts as a protective layer; if `read_file()` fails, it returns an error string to the AI, allowing the AI to organically inform the user ("I couldn't find that file") instead of terminating the script abruptly.

**Tool Integration Description:**
The `tools.py` module contains two distinct tools: `read_file` and `search_file`. Currently, they operate as standalone Python functions. They are designed to receive a string (the file path and/or keyword) and return a string (the file text or specific lines). This string-in/string-out design is intentional, as it perfectly matches the JSON format required by the Google AI SDK for function calling, allowing seamless integration in the upcoming agent logic.