# AutoFlow Agent

An intelligent AI-powered automation platform that combines web Browse, file management, and Python execution capabilities to autonomously complete complex tasks with built-in success criteria evaluation.



---

## ✨ Features

- **Autonomous Task Execution:** Uses LangGraph state machines to break down and execute complex multi-step tasks.
- **Web Automation:** Integrated Playwright browser automation for web scraping and interaction.
- **Success Criteria Evaluation:** Built-in evaluator that ensures tasks meet specified requirements.
- **Multi-Tool Integration:**
    - Web Browse and navigation
    - File management operations
    - Python code execution
    - Wikipedia research
    - Push notifications
    - Web search capabilities
- **Interactive Chat Interface:** Clean Gradio-based UI for seamless interaction.
- **Memory & Context:** Maintains conversation history and task context across interactions.

---

## 🏗️ Architecture

The project uses a sophisticated agent architecture built on:

- **LangGraph:** State graph management for complex workflows.
- **LangChain:** LLM integration and tool orchestration.
- **Groq:** High-performance LLM inference.
- **Playwright:** Headless browser automation.
- **Gradio:** Modern web interface.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/23shivay/AutoFlow-Agent.git](https://github.com/23shivay/AutoFlow-Agent.git)
   cd AutoFlow-Agent
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Install the browser for Playwright:
   ```bash
   playwright install

4. Create a .env file in the root directory and add your API keys:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   PUSHOVER_TOKEN=your_pushover_token_here
   PUSHOVER_USER=your_pushover_user_key_here
   SERPER_API_KEY=your_serper_api_key_here

5. Running the Application:
   ```bash
    python app.py

 ---

 ##💡 Usage Examples
 
   Example 1: Web Research Task
   Message: "Research the latest developments in AI and create a summary."

   Success Criteria: "Create a comprehensive summary with at least 5 recent developments, including sources."

   Example 2: Data Processing
   Message: "Download weather data and create a visualization."

   Success Criteria: "Generate a graph showing temperature trends with proper labels and save as PNG."

   Example 3: File Management
   Message: "Organize files in the current directory by type."

   Success Criteria: "Create folders for different file types and move files accordingly."
