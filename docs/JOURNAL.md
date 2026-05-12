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

