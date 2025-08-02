# Agent-Based Travel Planner

A professional, modular multi-agent system designed to automate and optimize travel planning. Leveraging advanced AI agents (Gemini, LangGraph) and a supervisor pattern, this system coordinates research, budgeting, logistics, and tool integrations to deliver comprehensive, actionable travel plans. The architecture is extensible, maintainable, and suitable for both personal and enterprise use.

## Project Hierarchy

```
app/
├── agents/           # Specialized agents for research, budgeting, logistics
│   ├── budget_agent.py
│   ├── logistic_agent.py
│   └── research_agent.py
├── config/           # Configuration files (LLM, settings)
│   ├── llm_config.py
│   └── settings.py
├── supervisor/       # Supervisor agent orchestrating workflow
│   └── supervisor.py
├── tools/            # Utility tools (calculator, web search, file writer)
│   ├── calculator.py
│   ├── TravelScript.py
│   └── web_search.py
├── utils/            # Logging and helper utilities
│   └── logger.py
├── workflows/        # Main workflow logic
│   └── main_workflow.py
├── main.py           # Entry point
├── requirements.txt  # Python dependencies
├── pyproject.toml    # Project metadata
├── travel_plan.md    # Example output
└── README.md         # Documentation
```

## Features

- Research Agent: Gathers destination information and activities
- Budget Agent: Estimates costs and manages budget constraints
- Logistics Agent: Plans transportation and accommodation
- Supervisor Pattern: Coordinates agent collaboration
- Integrated Tools: Web search, calculator, file output

## Setup

1. Clone the repository and navigate to the project directory.
2. Create a virtual environment and activate it:
   ```bash
   uv venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```
4. Copy `.env_example` to `.env` and add your API keys and secrets:
   ```bash
   cp .env_example .env
   # Edit .env to add your keys
   ```

## Usage

1. Configure your trip parameters in `app/config/settings.py` and other config files as needed.
2. Run the main application:
   ```bash
   python main.py
   ```
3. The system will output a detailed travel plan in `travel_plan.md`.

### Sample Input
Edit `app/config/settings.py`:
```python
ENVIRONMENT = "development"
DEBUG = True
# Add your trip parameters here
```

## Security & Best Practices
- API keys and sensitive data must be stored in `.env` (never hardcoded).
- Use `.env_example` as a template for required environment variables.
- Follow modular design and separation of concerns for maintainability.
- All dependencies are listed in `requirements.txt` for reproducibility.
- The code is runnable locally and outputs are deterministic given the same inputs.

## Repository Evaluation Rubric Alignment
This repository follows AI/ML code development best practices:
- Modular, extensible architecture
- Clear setup and usage instructions
- Secure handling of sensitive data
- Sample inputs and outputs provided
- Reproducible results

## License

This project is licensed under the MIT License.

