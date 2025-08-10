AutoFlow Agent
An intelligent AI-powered automation platform that combines web browsing, file management, and Python execution capabilities to autonomously complete complex tasks with built-in success criteria evaluation.

Features
Autonomous Task Execution: Uses LangGraph state machines to break down and execute complex multi-step tasks

Web Automation: Integrated Playwright browser automation for web scraping and interaction

Success Criteria Evaluation: Built-in evaluator that ensures tasks meet specified requirements

Multi-Tool Integration:

Web browsing and navigation

File management operations

Python code execution

Wikipedia research

Push notifications

Web search capabilities

Interactive Chat Interface: Clean Gradio-based UI for seamless interaction

Memory & Context: Maintains conversation history and task context across interactions

Architecture
The project uses a sophisticated agent architecture built on:

LangGraph: State graph management for complex workflows

LangChain: LLM integration and tool orchestration

Groq: High-performance LLM inference

Playwright: Headless browser automation

Gradio: Modern web interface

Quick Start
Prerequisites
Python 3.10+

Git

Installation
Clone the repository

git clone https://github.com/23shivay/AutoFlow-Agent.git
cd AutoFlow-Agent

Install dependencies

pip install -r requirements.txt

Install browser for Playwright

playwright install

Set up environment variables
Create a .env file in the root directory and add your API keys:

GROQ_API_KEY=your_groq_api_key_here
PUSHOVER_TOKEN=your_pushover_token_here
PUSHOVER_USER=your_pushover_user_key_here
SERPER_API_KEY=your_serper_api_key_here

Running the Application
python app.py

The application will launch in your default browser at http://localhost:7860.

🔧 Configuration
Required API Keys
Groq API Key: Get from Groq Console

Pushover (Optional): For push notifications - Pushover.net

Serper API (Optional): For web search - Serper.dev

Environment Setup
The application creates a sandbox directory for file operations. Ensure proper permissions for file read/write operations.

💡 Usage Examples
Example 1: Web Research Task

Message: "Research the latest developments in AI and create a summary"

Success Criteria: "Create a comprehensive summary with at least 5 recent developments, including sources"

Example 2: Data Processing

Message: "Download weather data and create a visualization"

Success Criteria: "Generate a graph showing temperature trends with proper labels and save as PNG"

Example 3: File Management

Message: "Organize files in the current directory by type"

Success Criteria: "Create folders for different file types and move files accordingly"

🛠️ Tools Available
Tool

Description

Web Browser

Navigate websites, extract data, fill forms

File Manager

Read, write, organize files and directories

Python REPL

Execute Python code for calculations and processing

Web Search

Search the internet for information

Wikipedia

Research topics using Wikipedia API

Push Notifications

Send alerts and updates

📊 Project Structure
AutoFlow-Agent/
├── app.py                 # Main Gradio application
├── sidekick.py           # Core agent logic and state management
├── sidekick_tools.py     # Tool definitions and integrations
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── sandbox/              # Working directory for file operations
└── README.md            # This file

🔍 How It Works
User Input: User provides a task and success criteria.

Task Planning: The agent analyzes the request and plans execution steps.

Tool Execution: Agent uses available tools to complete sub-tasks.

Evaluation: Built-in evaluator checks if success criteria are met.

Iteration: If criteria aren't met, agent continues working with feedback.

Completion: Final result is presented to the user.

 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

 Disclaimer
This tool can execute Python code and interact with web browsers. Use responsibly and ensure you have proper permissions for any automated actions performed.

 Contact
For questions or support, please open an issue on GitHub.
Built with  using LangGraph, LangChain, and modern AI technologies.