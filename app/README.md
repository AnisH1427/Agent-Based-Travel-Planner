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
│   ├── file_writer.py
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

1. Install dependencies using [uv](https://github.com/astral-sh/uv):

   ```bash
   uv pip install -r requirements.txt
   ```

2. Run the main application:

   ```bash
   uv venv .venv
   uv pip install -r requirements.txt
   uv pip run python main.py
   ```

## Usage

Configure your trip parameters in the appropriate config files, then execute the workflow via `main.py`. The system will output a detailed travel plan in `travel_plan.md`.

## License

This project is licensed under the MIT License.

