### Setup and Run Example Script

Source: https://docs.agno.com/examples/models/openai/chat/audio-input-and-output-multi-turn

Bash commands to clone the Agno repository, navigate to the cookbook example directory, create a Python virtual environment, and execute the audio multi-turn example. Includes repository setup script execution for dependency installation.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_input_and_output_multi_turn.py
```

--------------------------------

### Setup Agno Quickstart Repository

Source: https://docs.agno.com/examples/basics/agent-with-storage

Bash commands to clone the Agno repository and navigate to the quickstart directory to run the provided examples.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart
```

--------------------------------

### Clone, Setup, and Run Agent OS Example

Source: https://docs.agno.com/examples/agent-os/remote/server

Complete bash workflow for setting up the Agent OS remote example. Clones the repository, navigates to the cookbook example directory, creates a Python virtual environment using the provided setup script, activates it, and runs the server application. Requires git and bash to be installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/remote

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python server.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/models/openai/responses/structured-output

Bash commands to clone the Agno repository, navigate to the cookbook example directory, create a virtual environment, and execute the structured output example. Requires git and Python to be installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Agno Example (Bash)

Source: https://docs.agno.com/examples/workflows/advanced-concepts/previous-step-outputs/access-previous-outputs

This Bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a Python virtual environment using `demo_setup.sh`, activate it, and finally execute the Python script `access_previous_outputs.py`. This is a complete guide to getting the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/previous_step_outputs

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python access_previous_outputs.py
```

--------------------------------

### Setup and Run Agno Quickstart Example

Source: https://docs.agno.com/examples/basics/agent-search-over-knowledge

This bash script demonstrates how to clone the Agno repository, navigate to the quickstart cookbook, initialize a virtual environment, and execute the agent search script. It requires git and a Unix-like environment for the shell scripts.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_search_over_knowledge.py
```

--------------------------------

### Setup and Run O3 Mini Example

Source: https://docs.agno.com/examples/reasoning/models/openai/o3-mini-with-tools

Provides bash commands to clone the Agno repository, navigate to the O3 Mini example directory, create a Python virtual environment, and execute the reasoning agent example. Includes setup script execution for dependency installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python o3_mini_with_tools.py
```

--------------------------------

### Setup and Execution Guide for Docling Reader Async Example

Source: https://docs.agno.com/examples/knowledge/readers/docling-reader-async

Provides the shell commands necessary to prepare the environment, including repository cloning, virtual environment activation, and starting the required PgVector database container.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/05_integrations/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python docling_reader_async.py
```

--------------------------------

### Setup and Run Agno Reasoning Example

Source: https://docs.agno.com/examples/agents/reasoning/basic-reasoning

Clone the Agno repository, navigate to the reasoning cookbook example, create a virtual environment using the provided setup script, and execute the basic reasoning example. This bash script automates the environment setup and dependency installation required to run the reasoning agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/13_reasoning

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_reasoning.py
```

--------------------------------

### Setup and Run Example with Bash

Source: https://docs.agno.com/examples/reasoning/models/deepseek/plan-itinerary

Clones the Agno repository, navigates to the reasoning cookbook example directory, sets up a Python virtual environment, and executes the plan_itinerary.py script. Requires git, bash, and Python to be installed.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/deepseek

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python plan_itinerary.py
```

--------------------------------

### Setup and Run Example Project

Source: https://docs.agno.com/examples/memory/custom-memory-manager

Bash script commands to clone the Agno repository, navigate to the memory examples directory, create a virtual environment, and execute the custom memory manager example. Requires git and Python to be installed.

```Bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/11_memory

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 04_custom_memory_manager.py
```

--------------------------------

### Setup and Run Agno Team Example in Bash

Source: https://docs.agno.com/examples/teams/basics/delegate-to-all-members

Provides shell commands to clone the Agno repository, navigate to the teams quickstart directory, create a Python virtual environment using the provided setup script, and execute the delegate-to-all members example. This ensures all dependencies are properly installed in an isolated environment before running the team collaboration demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 03_delegate_to_all_members.py
```

--------------------------------

### Setup and Execution Guide

Source: https://docs.agno.com/examples/teams/human-in-the-loop/user-input-required

Instructions for cloning the Agno repository, setting up the development environment, and running the user input example.

```APIDOC
## Setup and Run Example

### Prerequisites
- Git installed
- Python 3.8 or higher
- Virtual environment support

### Installation Steps

#### Step 1: Clone Repository
```
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/human_in_the_loop
```

#### Step 2: Setup Virtual Environment
```
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
```
- Runs setup script to configure environment
- Activates Python virtual environment
- Installs required dependencies

#### Step 3: Execute Example
```
python user_input_required.py
```
- Runs the team user input example
- Prompts for required user input fields
- Displays team execution results

### Configuration

#### Database Setup
- **session_table** - Name of database table for sessions
- **db_file** - Path to SQLite database file
- Default: tmp/team_hitl.db

#### Model Configuration
- **model_id** - OpenAI model identifier (e.g., gpt-5.2-mini)
- Configure in Agent and Team instantiation

### Output
- Team execution logs and responses
- User input prompts for required fields
- Final trip planning results with user preferences
```

--------------------------------

### Setup and Run MCP Server Example using Bash

Source: https://docs.agno.com/examples/tools/mcp/sse-transport/server

These bash commands guide the user through setting up the development environment and executing the MCP server example. It involves cloning the `agno` repository, navigating to the specific example directory, creating and activating a Python virtual environment, and finally running the `server.py` script to start the MCP server.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/sse_transport

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python server.py
```

--------------------------------

### Setup and Run Ollama Tool Use Example

Source: https://docs.agno.com/examples/models/ollama/responses/tool-use

Provides bash commands to clone the agno repository, navigate to the Ollama responses example directory, create a virtual environment, and execute the tool use example script. This setup ensures all dependencies are properly installed before running the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Knowledge Instructions Example

Source: https://docs.agno.com/examples/knowledge/quickstart/knowledge-instructions

Shell commands to clone the Agno repository, set up the virtual environment, start the PgVector Docker container, and execute the Python demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 16_knowledge_instructions.py
```

--------------------------------

### Setup and Run MCP Server Example

Source: https://docs.agno.com/examples/tools/mcp/streamable-http-transport/server

Clone the agno repository, navigate to the streamable HTTP transport example directory, create a Python virtual environment using the provided setup script, and execute the server. This sets up all dependencies and starts the MCP server instance.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/streamable_http_transport

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python server.py
```

--------------------------------

### Setup and run Agno Neosantara basic stream example (Bash)

Source: https://docs.agno.com/models/providers/gateways/neosantara/usage/basic-stream

These bash commands guide through the setup process for running the Agno Neosantara streaming example. It includes setting the API key, installing necessary Python dependencies, and executing the main Python script.

```bash
export NEOSANTARA_API_KEY=xxx
```

```bash
uv pip install -U openai agno
```

```bash
python cookbook/90_models/neosantara/basic_stream.py
```

--------------------------------

### Setup and Run Example Project

Source: https://docs.agno.com/examples/teams/structured-input-output/input-formats

Provides shell commands to clone the Agno repository, navigate to the input formats example directory, create a virtual environment, and execute the Python script. Includes setup script execution and environment activation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/structured_input_output

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python input_formats.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/models/openai/responses/tool-use

Bash commands to clone the Agno repository, navigate to the OpenAI responses example directory, create a virtual environment using the demo setup script, and execute the tool_use.py example script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Todoist Agent Example (Bash)

Source: https://docs.agno.com/examples/tools/todoist-tools

This bash script provides a complete setup guide to clone the Agno repository, navigate to the relevant example directory, create and activate a Python virtual environment, and finally execute the `todoist_tools.py` script. This ensures the environment is correctly prepared for running the Todoist agent examples.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python todoist_tools.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/teams/human-in-the-loop/confirmation-required

Bash commands to clone the Agno repository, navigate to the human-in-the-loop example directory, set up a Python virtual environment using the provided setup script, and execute the confirmation_required.py example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/human_in_the_loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python confirmation_required.py
```

--------------------------------

### Setup and Run Example Project

Source: https://docs.agno.com/examples/knowledge/vector-db/cassandra-db/cassandra-db

Bash commands to clone the Agno repository, navigate to the Cassandra example directory, set up a virtual environment, and execute the demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/cassandra_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cassandra_db.py
```

--------------------------------

### Setup and Run Example

Source: https://docs.agno.com/examples/models/google/gemini/structured-output

Bash commands to clone the Agno repository, navigate to the cookbook example directory, set up a Python virtual environment, and execute the structured output example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Agno Background Execution Example

Source: https://docs.agno.com/examples/workflows/advanced-concepts/background-execution/websocket-server

These bash commands provide a complete guide to clone the Agno repository, navigate to the specific example, set up a Python virtual environment, activate it, export a necessary `SECURITY_KEY`, and finally execute the `websocket_server.py` script to start the application.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/background_execution

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export SECURITY_KEY="***"

python websocket_server.py
```

--------------------------------

### Setup and Run Cohere Knowledge Example

Source: https://docs.agno.com/examples/models/cohere/knowledge

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the knowledge example. Includes steps for repository setup and dependency installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cohere

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run Example Project

Source: https://docs.agno.com/examples/teams/session/session-summary

Bash commands to clone the Agno repository, navigate to the session summary example, create a virtual environment, and execute the session_summary.py script. Uses the demo_setup.sh script for environment configuration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/session

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python session_summary.py
```

--------------------------------

### Setup and Run Example - Bash

Source: https://docs.agno.com/examples/teams/state/change-state-on-run

Shell script commands to clone the Agno repository, navigate to the example directory, set up a Python virtual environment, and execute the change_state_on_run.py script. Requires git and Python to be installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/state

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python change_state_on_run.py
```

--------------------------------

### Setup and Run Agno Agent with PostgreSQL Example (Bash)

Source: https://docs.agno.com/memory/working-with-memories/postgres-memory

These bash commands guide through the necessary steps to prepare the environment and execute the Agno agent example. It includes setting the OpenAI API key, installing Python dependencies, and running the main Python script.

```bash
export OPENAI_API_KEY=xxx
```

```bash
uv pip install -U agno openai sqlalchemy 'psycopg[binary]'
```

```bash
python mem-postgres-memory.py
```

--------------------------------

### Setup and Run Image to Text Example

Source: https://docs.agno.com/examples/agents/multimodal/image-to-text

Provides bash commands to clone the Agno repository, navigate to the multimodal agents cookbook example, set up a Python virtual environment, and execute the image to text script. This setup ensures all dependencies are properly installed before running the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/12_multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_to_text.py
```

--------------------------------

### Setup and Run Example Project

Source: https://docs.agno.com/examples/teams/modes/coordinate/structured-output

Bash commands to clone the Agno repository, navigate to the coordinate mode example, set up a Python virtual environment, and execute the structured output demonstration script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/modes/coordinate

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 03_structured_output.py
```

--------------------------------

### Setup and Run Example Project

Source: https://docs.agno.com/examples/workflows/conditional-branching/router-basic

Provides shell commands to clone the Agno repository, navigate to the workflow example directory, create a virtual environment, and execute the router basic example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/05_conditional_branching

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python router_basic.py
```

--------------------------------

### Setup and Run DoclingReader Multi-Format Example

Source: https://docs.agno.com/examples/knowledge/readers/docling-multi-formats

Bash script commands to clone the Agno repository, set up a Python virtual environment, install dependencies including openai-whisper for audio processing, and run the DoclingReader multi-format example. Optionally starts a PgVector database using Docker.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/05_integrations/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Install additional dependencies for audio/video processing
uv pip install -U openai-whisper

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python docling_reader_multi_format.py
```

--------------------------------

### Setup and Execute Reasoning Example via CLI

Source: https://docs.agno.com/examples/reasoning/models/anthropic/async-reasoning-stream

Shell commands to clone the Agno repository, prepare the virtual environment using the provided setup script, and execute the async reasoning stream example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python async_reasoning_stream.py
```

--------------------------------

### Setup and Run Example - Bash

Source: https://docs.agno.com/examples/agent-os/interfaces/agui/agent-with-tools

Clones the Agno repository, navigates to the agent_os example directory, creates a virtual environment using the demo setup script, and runs the agent with tools application. The script handles environment activation and Python execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/agui

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_tools.py
```

--------------------------------

### Setup and Run Composio Example

Source: https://docs.agno.com/examples/tools/composio-tools

Bash script to clone the Agno repository, set up a Python virtual environment, and execute the Composio tools example. This script automates the setup process including dependency installation and environment activation for running the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python composio_tools.py
```

--------------------------------

### Setup and Run Llama Metrics Example

Source: https://docs.agno.com/examples/models/meta/llama/metrics

Bash script to clone the agno repository, set up a Python virtual environment, and execute the metrics.py cookbook example. Includes dependency installation via the demo setup script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python metrics.py
```

--------------------------------

### Setup and Run Session Summary Example - Bash

Source: https://docs.agno.com/examples/agents/state-and-session/session-summary

Shell script commands to clone the Agno repository, navigate to the session summary example directory, create a virtual environment, and execute the session summary demonstration. Includes all necessary setup steps for running the Python example.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/05_state_and_session
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python session_summary.py
```

--------------------------------

### Setup and Run Project - Bash

Source: https://docs.agno.com/examples/agents/state-and-session/session-state-manual-update

Clone the Agno repository, navigate to the session state example directory, create a virtual environment using the provided setup script, and execute the session state manual update example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/05_state_and_session

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python session_state_manual_update.py
```

--------------------------------

### Setup and run the Agno Streaming Agent example

Source: https://docs.agno.com/models/providers/gateways/fireworks/usage/basic-stream

These bash commands guide you through setting up the environment for the Agno Streaming Agent example. It includes exporting your Fireworks API key, installing necessary Python packages ('openai', 'agno') using 'uv pip', and finally executing the Python script.

```bash
export FIREWORKS_API_KEY=xxx
```

```bash
uv pip install -U openai agno
```

```bash
python cookbook/11_models/fireworks/basic_stream.py
```

--------------------------------

### Setup and Run Agno LiteLLM OpenAI Example

Source: https://docs.agno.com/examples/models/litellm-openai/basic

This bash script provides instructions to clone the Agno repository, navigate to the specific cookbook example directory, set up a virtual environment using a provided script, activate it, and finally execute the Python example script. It outlines the steps required to get the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run LiteLLM PDF Example

Source: https://docs.agno.com/examples/models/litellm/pdf-input-url

Shell script commands to clone the agno repository, set up a Python virtual environment, and execute the PDF input URL example. This includes installing dependencies via the demo setup script and activating the virtual environment before running the Python application.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_url.py
```

--------------------------------

### Setup and Run Agno Agent User Input Example (Bash)

Source: https://docs.agno.com/hitl/usage/user-input-required-async

These commands provide a complete guide to setting up the environment and executing the Agno agent example. It includes installing necessary Python packages, configuring the OpenAI API key for authentication across different operating systems, and finally running the Python script to observe the asynchronous user input flow.

```bash
uv pip install -U agno openai
```

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

```bash
$Env:OPENAI_API_KEY="your_openai_api_key_here"
```

```bash
python user_input_required_async.py
```

--------------------------------

### Setup and Run Example with Bash

Source: https://docs.agno.com/examples/evals/agent-as-judge/agent-as-judge-team-post-hook

Provides shell commands to clone the Agno repository, navigate to the agent-as-judge cookbook example, set up a Python virtual environment using the provided setup script, and execute the team post-hook evaluation example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/09_evals/agent_as_judge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_as_judge_team_post_hook.py
```

--------------------------------

### Setup and Run Example

Source: https://docs.agno.com/examples/agents/input-output/input-schema

Instructions for cloning the Agno repository, setting up the environment, and running the input schema example.

```APIDOC
## Setup Instructions

### Prerequisites
- Git installed
- Python 3.8 or higher
- Virtual environment support

### Setup Steps

#### 1. Clone Repository
```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/02_input_output
```

#### 2. Create Virtual Environment
```bash
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
```

#### 3. Run Example
```bash
python input_schema.py
```

### Expected Output
The script will execute the HackerNews agent twice:
1. First execution with dictionary input
2. Second execution with Pydantic model input

Both should produce identical results showing extracted insights from HackerNews posts related to AI and Machine Learning.
```

--------------------------------

### Setup and Run Support Agent Example

Source: https://docs.agno.com/cookbook/learning/support-agent

Bash commands to clone the agno repository, navigate to the learning cookbook, set up the Python environment, start PostgreSQL with PgVector support via Docker, and execute the support agent example.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning

# Setup (requires Docker for Postgres)
./setup_venv.sh
./cookbook/scripts/run_pgvector.sh

# Run
python 07_patterns/support_agent.py
```

--------------------------------

### Setup and Installation

Source: https://docs.agno.com/examples/tools/serpapi-tools

Instructions for cloning the Agno repository, setting up the development environment, and running SERP API integration examples.

```APIDOC
## Setup and Installation

### Description
Step-by-step instructions to clone the Agno repository, create a virtual environment, and run SERP API tool examples.

### Prerequisites
- Git installed
- Python 3.7 or higher
- Bash shell access

### Installation Steps

#### Step 1: Clone Repository
```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools
```

#### Step 2: Setup Virtual Environment
```bash
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
```

#### Step 3: Run Example
```bash
python serpapi_tools.py
```

### Configuration
- Virtual environment location: .venvs/demo/
- Example script: serpapi_tools.py
- Cookbook location: agno/cookbook/91_tools/

### Additional Resources
- Full cookbook example: https://github.com/agno-agi/agno/blob/main/cookbook/91_tools/serpapi_tools.py
- Documentation index: https://docs.agno.com/llms.txt
```

--------------------------------

### Configure Agno Agent with In-Memory Database (Python)

Source: https://docs.agno.com/examples/storage/in-memory/in-memory-storage-for-agent

This Python code demonstrates how to initialize an Agno `Agent` using an `InMemoryDb` for session storage. It includes setup, agent creation, and an example of running the agent to get a response. Ensure dependencies are installed using `uv pip install ddgs openai`.

```python
"""Run `uv pip install ddgs openai` to install dependencies."""

from agno.agent import Agent
from agno.db.in_memory import InMemoryDb

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
db = InMemoryDb()

# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------
agent = Agent(db=db)

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # The Agent sessions will now be stored in the in-memory database
    agent.print_response("Give me an easy and healthy dinner recipe")
```

--------------------------------

### Setup and Run Multi-Run Session Example - Bash

Source: https://docs.agno.com/examples/teams/task-mode/multi-run-session

Provides shell commands to clone the Agno repository, navigate to the task mode examples directory, set up a Python virtual environment using the provided demo setup script, and execute the multi-run session example. This ensures all dependencies are properly installed and the environment is correctly configured.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/task_mode

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 07_multi_run_session.py
```

--------------------------------

### Run LangDB Embedder Example (Bash)

Source: https://docs.agno.com/examples/knowledge/embedders/langdb-embedder

These bash commands provide a step-by-step guide to set up the project environment and execute the LangDB Embedder example. It covers cloning the repository, navigating to the example directory, creating and activating a Python virtual environment, optionally starting a PgVector Docker container, and finally running the Python script. This setup requires Git, Python, and Docker (for PgVector).

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python langdb_embedder.py
```

--------------------------------

### Setup and Run Agno Reasoning Example

Source: https://docs.agno.com/examples/reasoning/models/openai/reasoning-effort

Provides shell commands to clone the Agno repository, navigate to the reasoning cookbook example directory, set up a Python virtual environment, and execute the reasoning effort demonstration script. This setup ensures all dependencies are properly isolated and installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_effort.py
```

--------------------------------

### Setup and Run A2A Client Example

Source: https://docs.agno.com/examples/integrations/a2a/basic-agent/client

Bash script to clone the agno repository, navigate to the A2A basic agent example directory, create a Python virtual environment using the demo setup script, activate it, and run the client. Assumes git is installed and the repository is accessible.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/a2a/basic_agent

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python client.py
```

--------------------------------

### Setup and Run Example Script in Bash

Source: https://docs.agno.com/examples/models/clients/http-client-caching

Provides shell commands to clone the agno repository, navigate to the cookbook example directory, create a Python virtual environment using the demo setup script, and execute the HTTP client caching example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/clients

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python http_client_caching.py
```

--------------------------------

### Setup and Run Guardrails Example

Source: https://docs.agno.com/examples/agent-os/middleware/guardrails-demo

Bash script to clone the Agno repository, navigate to the guardrails example directory, create a Python virtual environment, and run the guardrails demonstration. Includes all necessary setup steps for a fresh installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/middleware

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python guardrails_demo.py
```

--------------------------------

### Setup and Run Structured I/O Example with Bash

Source: https://docs.agno.com/examples/workflows/advanced-concepts/structured-io/structured-io-function

This bash script provides a complete guide to set up the development environment and run the structured I/O example. It includes steps for cloning the repository, navigating to the specific example directory, creating and activating a virtual environment, and finally executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/structured_io

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_io_function.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/reasoning/tools/capture-reasoning-content-knowledge-tools

Bash commands to clone the Agno repository, navigate to the cookbook directory, create a virtual environment, and execute the reasoning content capture example script.

```Bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python capture_reasoning_content_knowledge_tools.py
```

--------------------------------

### Setup and Run Toolkit Example

Source: https://docs.agno.com/examples/tools/other/stop-after-tool-call-in-toolkit

Shell commands to clone the Agno repository, set up a virtual environment, and execute the demonstration script for stopping agent execution after a tool call.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/other

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python stop_after_tool_call_in_toolkit.py
```

--------------------------------

### Setup and Run Stock Analysis Agent Example

Source: https://docs.agno.com/examples/basics/agent-with-structured-output

Bash script commands to clone the agno repository, navigate to the quickstart cookbook example, set up a Python virtual environment, and execute the stock analysis agent script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_structured_output.py
```

--------------------------------

### Setup and Run Agno Agent Example from Repository (Bash)

Source: https://docs.agno.com/examples/basics/agent-with-tools

This bash script provides the necessary steps to set up and run the Agno agent example. It involves cloning the Agno GitHub repository, navigating to the specific example directory, creating and activating a Python virtual environment using a setup script, and finally executing the `agent_with_tools.py` script. This allows users to quickly get the example agent running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_tools.py
```

--------------------------------

### Setup and Run Agno Agent with Memory Example (Bash)

Source: https://docs.agno.com/examples/models/ollama/chat/memory

This bash script outlines the steps to clone the Agno repository, set up a Python virtual environment, install necessary dependencies, and execute the agent memory example. It also includes an optional command to start a PostgreSQL container with PgVector using Docker, which is essential for the agent's memory functionality.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/ollama/chat\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\n# Optiona: Run PgVector (needs docker)\n./cookbook/scripts/run_pgvector.sh\n\npython memory.py
```

--------------------------------

### Setup and Run Portkey Tool Use Example in Bash

Source: https://docs.agno.com/examples/models/portkey/tool-use

Provides shell commands to clone the Agno repository, navigate to the Portkey cookbook example directory, create a virtual environment, and execute the tool use demonstration script. Requires git and Python to be installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/portkey

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/teams/structured-input-output/pydantic-output

Bash script commands to clone the Agno repository, navigate to the structured input/output cookbook example, create a virtual environment using the demo setup script, activate it, and execute the pydantic_output.py example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/structured_input_output

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pydantic_output.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/teams/modes/tasks/dependencies

Bash commands to clone the Agno repository, navigate to the tasks example directory, set up a Python virtual environment, and execute the dependencies example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/modes/tasks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 03_dependencies.py
```

--------------------------------

### Setup and Run Cerebras Reasoning Tools Example

Source: https://docs.agno.com/examples/reasoning/tools/cerebras-llama-reasoning-tools

Provides bash commands to clone the Agno repository, navigate to the reasoning tools cookbook example, create a virtual environment, and execute the reasoning agent script. This setup ensures all dependencies are properly installed and the environment is configured for running the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cerebras_llama_reasoning_tools.py
```

--------------------------------

### Setup and Run Together Basic Example in Bash

Source: https://docs.agno.com/examples/models/together/basic

Shell script commands to clone the Agno repository, navigate to the Together cookbook example directory, set up a Python virtual environment, and execute the basic.py example. Requires git and Python to be installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/together

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run VoyageAI Embedder Example

Source: https://docs.agno.com/examples/knowledge/embedders/voyageai-embedder

Bash script for cloning the Agno repository, setting up a Python virtual environment, and running the VoyageAI embedder example. Includes optional PgVector Docker setup and dependency installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python voyageai_embedder.py
```

--------------------------------

### Setup and Run In-Memory Storage Example

Source: https://docs.agno.com/examples/storage/in-memory/in-memory-storage-for-team

Bash script to clone the Agno repository, set up a virtual environment, and execute the in-memory storage team example. This script automates the initial setup process including dependency installation and environment activation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/in_memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python in_memory_storage_for_team.py
```

--------------------------------

### Setup and Run Meta Basic Example

Source: https://docs.agno.com/examples/models/meta/llama-openai/basic

Clone the Agno repository, navigate to the Meta Llama OpenAI cookbook directory, set up a Python virtual environment, and execute the basic.py script. This provides a complete setup workflow for running the example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run WatsonX Structured Output Example

Source: https://docs.agno.com/examples/models/ibm/watsonx/structured-output

Bash script for cloning the Agno repository, navigating to the WatsonX cookbook example directory, setting up a Python virtual environment, and executing the structured_output.py script. This automates the environment setup and dependency installation required to run the IBM WatsonX example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ibm/watsonx

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run CEL Workflow Example

Source: https://docs.agno.com/examples/workflows/cel-expressions/condition/cel-previous-step

Bash script commands to clone the Agno repository, set up a virtual environment, and execute the CEL workflow example. This demonstrates the complete setup process for running the conditional workflow with proper dependencies installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/07_cel_expressions/condition

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cel_previous_step.py
```

--------------------------------

### Setup and Run Groq Knowledge Example via CLI

Source: https://docs.agno.com/examples/models/groq/knowledge

Shell commands to clone the Agno repository, set up a virtual environment, start a PgVector Docker container, and execute the knowledge base example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run Example with Bash

Source: https://docs.agno.com/examples/teams/structured-input-output/parser-model

Provides shell commands to clone the Agno repository, navigate to the example directory, create a Python virtual environment using the demo setup script, activate it, and execute the parser model example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/structured_input_output

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python parser_model.py
```

--------------------------------

### Setup and Run Image to Image Example

Source: https://docs.agno.com/examples/agents/multimodal/image-to-image

Provides shell commands to clone the Agno repository, navigate to the multimodal agents cookbook, create a Python virtual environment, and execute the Image to Image agent script. This setup ensures all dependencies are properly installed before running the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/12_multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_to_image.py
```

--------------------------------

### Setup and Run Agent Example with Bash

Source: https://docs.agno.com/examples/agents/context-management/system-message

Provides shell commands to clone the Agno repository, navigate to the context management cookbook example, set up a Python virtual environment using the provided setup script, and execute the system message customization example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/03_context_management

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python system_message.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/models/google/gemini/image-input-file-upload

Bash commands to clone the Agno repository, navigate to the Google Gemini cookbook directory, create a virtual environment, and execute the image upload example script. Includes repository setup and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the example
python image_input_file_upload.py
```

--------------------------------

### Setup and Run Docker Tool Example

Source: https://docs.agno.com/examples/tools/docker-tools

Commands to clone the repository, set up a virtual environment, and execute the Docker tool demonstration script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python docker_tools.py
```

--------------------------------

### Setup and Run Media Input Example

Source: https://docs.agno.com/examples/agents/multimodal/media-input-for-tool

Bash commands to clone the Agno repository, set up the required virtual environment, and execute the media input demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/12_multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python media_input_for_tool.py
```

--------------------------------

### Setup and Run Learning Examples via CLI

Source: https://docs.agno.com/cookbook/learning/overview

Commands to clone the Agno repository, set up the environment, and execute learning pattern examples such as user profiles and personal assistants.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning

# Setup
./setup_venv.sh

# Run examples
python 01_basics/1a_user_profile_always.py
python 07_patterns/personal_assistant.py
```

--------------------------------

### Setup and Execution Commands

Source: https://docs.agno.com/examples/knowledge/readers/pdf-reader-password

Provides the necessary shell commands to clone the repository, prepare the environment, start the vector database, and run the example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python pdf_reader_password.py
```

--------------------------------

### Setup and Run LiteLLM Knowledge Example

Source: https://docs.agno.com/examples/models/litellm/knowledge

Bash script for cloning the Agno repository, setting up a Python virtual environment, optionally running PgVector with Docker, and executing the knowledge.py example. Includes all necessary setup steps from repository initialization to agent execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run Example - Bash

Source: https://docs.agno.com/examples/teams/memory/team-with-memory-manager

Clones the Agno repository, sets up a Python virtual environment, and runs the team memory manager example script. Includes all necessary setup steps for demo execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the example
python 01_team_with_memory_manager.py
```

--------------------------------

### Setup and Run Local Reasoning Example

Source: https://docs.agno.com/examples/reasoning/models/ollama/local-reasoning

Bash script commands to clone the Agno repository, set up a Python virtual environment, and execute the local reasoning example. This setup ensures all dependencies are installed and the environment is properly configured before running the reasoning agents.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/ollama

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python local_reasoning.py
```

--------------------------------

### Setup and Run DynamoDB Team Example with Bash

Source: https://docs.agno.com/examples/storage/dynamodb/dynamo-for-team

Provides shell commands to clone the Agno repository, navigate to the DynamoDB example directory, create a virtual environment, and execute the team script. This setup ensures all dependencies are installed and the environment is properly configured.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/dynamodb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the example
python dynamo_for_team.py
```

--------------------------------

### Setup and Run Metrics Example via Bash

Source: https://docs.agno.com/examples/agents/advanced/metrics

Commands to clone the Agno repository, initialize the environment using the provided setup script, activate the virtual environment, and run the metrics demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python metrics.py
```

--------------------------------

### Setup and Initialize Environment

Source: https://docs.agno.com/production/applications/knowledge-agent

Commands to clone the Agno repository, create a virtual environment, install dependencies, and start the pgvector database.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r cookbook/01_showcase/01_agents/knowledge_agent/requirements.in
export OPENAI_API_KEY=your-openai-key
./cookbook/scripts/run_pgvector.sh
python cookbook/01_showcase/01_agents/knowledge_agent/scripts/load_knowledge.py
```

--------------------------------

### Setup and Run LiteLLM Example

Source: https://docs.agno.com/examples/models/litellm/basic

Provides shell commands to clone the Agno repository, navigate to the LiteLLM cookbook example directory, set up a virtual environment, and execute the basic.py script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Agno Example

Source: https://docs.agno.com/examples/agents/multimodal/image-to-structured-output

Provides shell commands to clone the Agno repository, navigate to the multimodal agents example directory, set up a virtual environment, and execute the image-to-structured-output script. This ensures all dependencies are installed and the example runs in an isolated environment.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/12_multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_to_structured_output.py
```

--------------------------------

### Setup and Installation for Supabase MCP Agent

Source: https://docs.agno.com/examples/tools/mcp/supabase

Commands to install the necessary Python dependencies and clone the Agno repository to run the Supabase MCP agent example locally.

```bash
uv pip install agno mcp
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp
```

--------------------------------

### Setup and Execute HITL Example via Bash

Source: https://docs.agno.com/examples/agents/human-in-the-loop/confirmation-required

Instructions for cloning the Agno repository, initializing the environment with a setup script, and running the confirmation required demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/10_human_in_the_loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python confirmation_required.py
```

--------------------------------

### Run the Local Server Example

Source: https://docs.agno.com/examples/tools/mcp/local-server/server

These bash commands guide the user through cloning the project repository, navigating to the example directory, setting up a virtual environment, activating it, and finally executing the `server.py` script to start the `FastMCP` server demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/local_server

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python server.py
```

--------------------------------

### Setup and Run Web Search Agent Example

Source: https://docs.agno.com/examples/models/vercel/tool-use

Provides shell commands to clone the Agno repository, navigate to the Vercel models cookbook directory, set up a Python virtual environment, and execute the web search agent example. This setup ensures all dependencies are properly installed before running the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vercel

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Example

Source: https://docs.agno.com/examples/teams/structured-input-output/pydantic-input

Provides shell commands to clone the Agno repository, navigate to the example directory, set up a virtual environment, and execute the Pydantic input example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/structured_input_output

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pydantic_input.py
```

--------------------------------

### Setup and Run GitHub Knowledge Example

Source: https://docs.agno.com/examples/knowledge/cloud/github

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the GitHub content source example. Includes all necessary setup steps for running the cookbook demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/cloud

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python github.py
```

--------------------------------

### Run Example Setup and Execution in Bash

Source: https://docs.agno.com/examples/teams/knowledge/team-with-knowledge-filters

Clones the Agno repository, navigates to the teams/knowledge cookbook example, creates a Python virtual environment using the provided setup script, and executes the knowledge filters example. This demonstrates the complete workflow from repository setup to running the team with knowledge filters.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_team_with_knowledge_filters.py
```

--------------------------------

### Setup and Run Workflow Example in Bash

Source: https://docs.agno.com/examples/agent-os/workflow/workflow-with-nested-steps

Provides shell commands to clone the Agno repository, navigate to the workflow example directory, create a virtual environment using the demo setup script, activate it, and run the workflow with nested steps example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/workflow

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_with_nested_steps.py
```

--------------------------------

### Setup and Run Xai Image Agent Example

Source: https://docs.agno.com/examples/models/xai/image-agent

Bash script commands to clone the Agno repository, navigate to the xAI cookbook example directory, create a Python virtual environment, and execute the image agent script. This setup ensures all dependencies are properly isolated and installed before running the agent.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/xai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent.py
```

--------------------------------

### Setup and Execution Commands for O3 Mini Example

Source: https://docs.agno.com/examples/reasoning/models/azure-openai/o3-mini-with-tools

Bash commands to clone the Agno repository, navigate to the reasoning model directory, initialize the virtual environment using a setup script, and execute the Python example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/azure_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python o3_mini_with_tools.py
```

--------------------------------

### Setup and Run Visualization Examples

Source: https://docs.agno.com/examples/tools/visualization-tools

Bash commands to clone the Agno repository, set up the required virtual environment using the provided demo script, and execute the visualization tools example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python visualization_tools.py
```

--------------------------------

### Setup and Run Agno Session Context Example

Source: https://docs.agno.com/examples/learning/basics/a-session-context-summary

Bash script for cloning the Agno repository, setting up a Python virtual environment, and executing the session context summary mode example. Includes repository initialization, dependency installation via demo setup script, and Python script execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/01_basics

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 3a_session_context_summary.py
```

--------------------------------

### Setup and Run Example in Bash

Source: https://docs.agno.com/examples/agents/human-in-the-loop/confirmation-advanced

Provides shell commands to clone the Agno repository, navigate to the example directory, set up a Python virtual environment, and execute the confirmation advanced example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/10_human_in_the_loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python confirmation_advanced.py
```

--------------------------------

### Setup and Run Resend Tools Example

Source: https://docs.agno.com/examples/tools/resend-tools

Bash script to clone the Agno repository, set up a virtual environment, and execute the Resend tools example. This automates the installation of dependencies and activation of the demo environment needed to run the resend_tools.py example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python resend_tools.py
```

--------------------------------

### Setup and Run Qdrant Agno Example

Source: https://docs.agno.com/examples/knowledge/vector-db/qdrant-db/qdrant-db

This bash script provides instructions to clone the `agno` repository, navigate to the Qdrant example directory, set up a virtual environment, and execute the Python script. It ensures all necessary dependencies are installed and the environment is ready to run the example.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/07_knowledge/vector_db/qdrant_db\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython qdrant_db.py
```

--------------------------------

### Setup and Run Bitbucket Tools Example

Source: https://docs.agno.com/examples/tools/bitbucket-tools

Bash script commands to clone the Agno repository, navigate to the tools cookbook directory, set up a Python virtual environment, and execute the Bitbucket tools example. This demonstrates the complete setup workflow for running Bitbucket integration examples.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python bitbucket_tools.py
```

--------------------------------

### Setup and Execute AIMLAPI Cookbook Example

Source: https://docs.agno.com/examples/models/aimlapi/basic

Bash commands to clone the Agno repository, configure the environment using a setup script, and run the AIMLAPI basic example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/aimlapi

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Example - Bash

Source: https://docs.agno.com/examples/agents/reasoning/reasoning-with-model

Provides shell commands to clone the Agno repository, navigate to the reasoning example directory, set up a Python virtual environment, and execute the reasoning model example. This demonstrates the complete workflow for running the reasoning agent locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/13_reasoning

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_with_model.py
```

--------------------------------

### Setup and Run YouTube Knowledge Example

Source: https://docs.agno.com/examples/knowledge/quickstart/from-youtube

Bash commands to clone the Agno repository, set up the environment, start the PgVector database via Docker, and execute the YouTube knowledge ingestion script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 05_from_youtube.py
```

--------------------------------

### Setup and Run AgentOS Example

Source: https://docs.agno.com/examples/agent-os/interfaces/slack/multiple-instances

Bash script to clone the agno repository, navigate to the slack interface example directory, create a Python virtual environment, and run the multiple instances example. Requires git and Python 3.x installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/slack

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python multiple_instances.py
```

--------------------------------

### Setup and Run GCS File Analysis Example

Source: https://docs.agno.com/examples/models/google/gemini/gcs-file-input

Bash script commands to clone the Agno repository, navigate to the Google Gemini cookbook example, create a Python virtual environment, and execute the GCS file analysis script. This setup ensures all dependencies are installed in an isolated environment.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python gcs_file_input.py
```

--------------------------------

### Setup and Run RBAC Example

Source: https://docs.agno.com/examples/agent-os/rbac/symmetric/basic

Provides setup instructions to clone the Agno repository, create a virtual environment, set the JWT verification key, and run the RBAC example. Uses a demo setup script to configure dependencies and activate the Python environment before executing the basic RBAC example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/rbac/symmetric

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export JWT_VERIFICATION_KEY="***"

python basic.py
```

--------------------------------

### Setup and Run Async Task Mode Example

Source: https://docs.agno.com/examples/teams/task-mode/async-task-mode

Shell commands to clone the Agno repository, set up the demo environment using a setup script, and execute the asynchronous task mode script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/task_mode

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 04_async_task_mode.py
```

--------------------------------

### Setup and Run Agentic Filtering Example

Source: https://docs.agno.com/examples/knowledge/filters/agentic-filtering

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the agentic filtering example. The setup script handles dependency installation and environment configuration for running the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python agentic_filtering.py
```

--------------------------------

### Clone and Setup Agno Repository with Virtual Environment

Source: https://docs.agno.com/examples/basics/multi-agent-team

Bash script to clone the Agno repository, navigate to the quickstart cookbook directory, create a virtual environment using the demo setup script, activate it, and prepare the environment for running multi-agent examples. This sets up all dependencies needed for the multi_agent_team.py example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python multi_agent_team.py
```

--------------------------------

### Setup and Run LiteLLM OpenAI Example

Source: https://docs.agno.com/examples/models/litellm-openai/tool-use

Bash script commands to clone the Agno repository, navigate to the LiteLLM OpenAI example directory, set up a Python virtual environment using the provided demo setup script, and execute the tool use example. This prepares the development environment and runs the agent demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run the Groq Finance Agent Example (Bash)

Source: https://docs.agno.com/examples/models/groq/reasoning/finance-agent

This bash script provides instructions to clone the `agno` repository, navigate to the example directory, set up a virtual environment using `demo_setup.sh`, activate it, and finally execute the `finance_agent.py` script. This allows users to run the Groq Finance Agent example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq/reasoning

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python finance_agent.py
```

--------------------------------

### Setup and Run OpenAI Basic Example

Source: https://docs.agno.com/examples/models/openai/chat/basic

This snippet provides instructions on how to clone the `agno` repository, navigate to the specific example directory, set up a virtual environment, and execute the `basic.py` script. It outlines the steps required to run the provided Python example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run LMStudio Structured Output Example

Source: https://docs.agno.com/examples/models/lmstudio/structured-output

Bash script commands to clone the Agno repository, navigate to the LMStudio cookbook example directory, create a virtual environment, and execute the structured output example. Requires git and Python 3.x installed.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/lmstudio
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python structured_output.py
```

--------------------------------

### Setup and Run Groq Browser Search Example in Bash

Source: https://docs.agno.com/examples/models/groq/browser-search

This bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a virtual environment, and execute the Python script for the Groq browser search agent. It covers the necessary steps to get the example running from scratch.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python browser_search.py
```

--------------------------------

### Setup and Run LMStudio Example via Bash

Source: https://docs.agno.com/examples/models/lmstudio/basic

Shell script commands to clone the Agno repository, navigate to the LMStudio cookbook example directory, set up a Python virtual environment, and execute the basic.py example script. Requires git and Python to be installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/lmstudio

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/knowledge/quickstart/include-exclude-files

Bash commands to clone the Agno repository, set up a virtual environment, optionally run PgVector with Docker, and execute the include/exclude files example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 08_include_exclude_files.py
```

--------------------------------

### Setup and Run Gemini PDF Processing Example

Source: https://docs.agno.com/examples/models/google/gemini/pdf-input-url

Bash script commands to clone the Agno repository, navigate to the Google Gemini cookbook directory, create a virtual environment, and execute the PDF processing example. This setup ensures all dependencies are installed and the environment is properly configured for running the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_url.py
```

--------------------------------

### Setup and Run Agno Self-Learning Agent Example (Bash)

Source: https://docs.agno.com/examples/basics/custom-tool-for-self-learning

This bash script provides instructions for cloning the Agno repository, navigating to the quickstart example, setting up a Python virtual environment, activating it, and finally running the custom_tool_for_self_learning.py script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python custom_tool_for_self_learning.py
```

--------------------------------

### Clone, Setup, and Run Agent OS Example with Bash

Source: https://docs.agno.com/examples/agent-os/schemas/team-schemas

Complete bash workflow for setting up the Agent OS cookbook example. Clones the repository, navigates to the schemas example directory, runs the demo setup script, activates the virtual environment, and executes the team_schemas application. Requires git and bash shell.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/schemas

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python team_schemas.py
```

--------------------------------

### Setup and Run LangDB Structured Output Example

Source: https://docs.agno.com/examples/models/langdb/structured-output

Shell commands to clone the Agno repository, set up the virtual environment, and execute the structured output cookbook example. This ensures all dependencies are installed and the environment is correctly configured.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/langdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run N1N Basic Example

Source: https://docs.agno.com/examples/models/n1n/basic

Shell commands to clone the Agno repository, navigate to the N1N cookbook example directory, create a virtual environment, and execute the basic.py script. This setup process prepares the environment and dependencies needed to run the N1N agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/n1n

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Execute SingleStore Example

Source: https://docs.agno.com/examples/agent-os/dbs/singlestore

Provides the shell commands necessary to clone the Agno repository, prepare the environment, and run the SingleStore integration example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/dbs

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python singlestore.py
```

--------------------------------

### Setup and Execute Dashscope Cookbook Example

Source: https://docs.agno.com/examples/models/dashscope/thinking-agent

Provides the shell commands required to clone the Agno repository, prepare the environment using a setup script, and run the thinking agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/dashscope

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python thinking_agent.py
```

--------------------------------

### Setup and Run Workflow Example

Source: https://docs.agno.com/examples/workflows/advanced-concepts/workflow-agent/workflow-agent-with-condition

Clone the Agno repository, set up a Python virtual environment, and execute the workflow example script. This demonstrates the complete setup process for running the workflow agent with condition example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/workflow_agent

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_agent_with_condition.py
```

--------------------------------

### Setup and Run AgentOS Scheduler Example

Source: https://docs.agno.com/examples/agent-os/scheduler/basic-schedule

Shell script commands to clone the agno repository, set up a Python virtual environment, optionally start PostgreSQL with Docker, and run the basic scheduler example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/scheduler

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python basic_schedule.py
```

--------------------------------

### Setup and Run SharePoint Example

Source: https://docs.agno.com/examples/knowledge/cloud/sharepoint

Bash commands to clone the Agno repository, set up a virtual environment, start the required PgVector database via Docker, and run the SharePoint integration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/cloud

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python sharepoint.py
```

--------------------------------

### Setup and Run Cerebras Example

Source: https://docs.agno.com/examples/models/cerebras/basic

Bash script commands to clone the Agno repository, navigate to the Cerebras cookbook example directory, set up a Python virtual environment, and execute the basic.py example. This ensures all dependencies are installed and the environment is properly configured.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cerebras

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Agno Gemini Example (Bash)

Source: https://docs.agno.com/examples/models/google/gemini/gemini-2-to-3

This bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a Python virtual environment, and execute the `gemini_2_to_3.py` script. It ensures all dependencies are correctly installed before running the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python gemini_2_to_3.py
```

--------------------------------

### Setup and Run Knowledge Filters Example in Bash

Source: https://docs.agno.com/examples/agents/knowledge/knowledge-filters

Clone the Agno repository, set up a Python virtual environment, and execute the knowledge filters example. Optionally runs PgVector in Docker for the vector database backend. This script automates the environment setup and dependency installation required to run the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/07_knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge_filters.py
```

--------------------------------

### Setup and Run MCP Server Example

Source: https://docs.agno.com/examples/tools/mcp/dynamic-headers/server

Shell commands to clone the Agno repository, navigate to the dynamic headers example, set up the virtual environment, and execute the server script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/dynamic_headers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python server.py
```

--------------------------------

### Setup Environment and Run Agno Audio Agent Example

Source: https://docs.agno.com/models/providers/native/openai/completion/usage/audio-output-agent

These bash commands guide the user through setting up the necessary environment for the Agno audio output agent. It includes exporting the OPENAI_API_KEY environment variable, installing required Python packages (openai, agno) using uv pip, and finally executing the Python script to run the agent.

```bash
export OPENAI_API_KEY=xxx
```

```bash
uv pip install -U openai agno
```

```bash
python cookbook/11_models/openai/chat/audio_output_agent.py
```

--------------------------------

### Setup and Run Webbrowser Example

Source: https://docs.agno.com/examples/tools/webbrowser-tools

Bash commands to clone the Agno repository, set up a virtual environment, and execute the webbrowser tools example script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python webbrowser_tools.py
```

--------------------------------

### Setup and Run Agno Web Search Example (Bash)

Source: https://docs.agno.com/examples/models/openai/responses/websearch-builtin-tool

This Bash snippet provides a step-by-step guide to set up the Agno repository, create and activate a Python virtual environment, and execute the `websearch_builtin_tool.py` example script. It's essential for running the provided Python agent demonstration.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/openai/responses\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython websearch_builtin_tool.py
```

--------------------------------

### Setup and Run Ollama Embedder Example

Source: https://docs.agno.com/examples/knowledge/embedders/ollama-embedder

Provides bash commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the Ollama embedder example script. This setup ensures all dependencies are installed and the environment is properly configured for running the embedding demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python ollama_embedder.py
```

--------------------------------

### Setup and Run OpenRouter Tools Example

Source: https://docs.agno.com/examples/models/openrouter/chat/tool-use

Bash script commands to clone the Agno repository, navigate to the OpenRouter chat example directory, create a virtual environment, and execute the tool_use.py script. Requires git and Python to be installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openrouter/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Agno Agent Example (Bash)

Source: https://docs.agno.com/examples/agents/input-output/input-formats

This bash script provides instructions to clone the Agno repository, navigate to the example directory, set up a virtual environment, and execute the Python script demonstrating agent input formats. It ensures all dependencies are correctly installed before running the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/02_input_output

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python input_formats.py
```

--------------------------------

### Setup and Run Team Pre-Hook Example - Bash

Source: https://docs.agno.com/examples/teams/hooks/pre-hook-input

Shell script commands to clone the Agno repository, navigate to the hooks example directory, create a Python virtual environment, and execute the pre-hook input validation example. Requires git and Python to be installed.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/hooks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pre_hook_input.py
```

--------------------------------

### Setup and Execute Cohere Cookbook Example

Source: https://docs.agno.com/examples/models/cohere/basic

Commands to clone the repository, prepare the environment, and run the basic Cohere script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cohere

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run AgentOS Example Project

Source: https://docs.agno.com/examples/agent-os/customize/pass-dependencies-to-agent

Provides shell commands to clone the agno repository, navigate to the example directory, create a virtual environment, and run the pass_dependencies_to_agent.py script with automatic setup.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/customize

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pass_dependencies_to_agent.py
```

--------------------------------

### Setup Environment and Run xAI Web Search Agent Example (Bash)

Source: https://docs.agno.com/examples/models/xai/tool-use

These bash commands guide you through cloning the Agno repository, navigating to the example directory, setting up a virtual environment, and executing the Python script for the xAI web search agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/xai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run FileSystemKnowledge Example in Bash

Source: https://docs.agno.com/examples/knowledge/protocol/file-system

Commands to clone the Agno repository, set up a virtual environment, and execute the FileSystemKnowledge example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/protocol

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python file_system.py
```

--------------------------------

### Setup and Run Structured Output Example (Bash)

Source: https://docs.agno.com/examples/models/ollama/responses/structured-output

This bash script provides a step-by-step guide to set up the development environment and execute the Python structured output example. It covers cloning the 'agno' repository, navigating to the specific example directory, creating and activating a virtual environment, and finally running the Python script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/ollama/responses\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython structured_output.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/reasoning/agents/capture-reasoning-content-default-cot

Bash commands to clone the Agno repository, navigate to the reasoning agents cookbook directory, set up a virtual environment, and execute the reasoning content capture example. Includes environment activation and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python capture_reasoning_content_default_COT.py
```

--------------------------------

### Setup and Run Session State Advanced Example in Bash

Source: https://docs.agno.com/examples/agents/state-and-session/session-state-advanced

Provides shell commands to clone the Agno repository, navigate to the session state example directory, set up a Python virtual environment using the provided demo setup script, and execute the shopping list manager example. This demonstrates the complete workflow for running the advanced session state example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/05_state_and_session

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python session_state_advanced.py
```

--------------------------------

### Setup and Run Agno Registry Example (Bash)

Source: https://docs.agno.com/examples/components/registry

This bash script provides a step-by-step guide to set up and execute the Agno Registry demonstration. It covers cloning the repository, navigating to the specific example directory, creating and activating a Python virtual environment, and finally running the `registry.py` script. Follow these commands to observe the registry in action locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/93_components

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python registry.py
```

--------------------------------

### Setup and Run Team Learning Example

Source: https://docs.agno.com/examples/teams/learning/team-learned-knowledge

Clone the Agno repository and execute the team learning demonstration script. The setup script creates a virtual environment and installs dependencies. Optionally run PgVector in Docker to provide the vector database backend for storing and searching team learnings.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/learning

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 05_team_learned_knowledge.py
```

--------------------------------

### Setup and Run Together Reasoning Agent Example in Bash

Source: https://docs.agno.com/examples/models/together/reasoning-agent

This bash script provides instructions to clone the agno repository, navigate to the example directory, set up a virtual environment using demo_setup.sh, activate it, and finally execute the Python reasoning agent script. It outlines the steps required to get the example running locally.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/together\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython reasoning_agent.py
```

--------------------------------

### Setup and Run Example Project

Source: https://docs.agno.com/examples/knowledge/quickstart/from-gcs

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the GCS knowledge example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 07_from_gcs.py
```

--------------------------------

### Setup and Run Agno Planning Example

Source: https://docs.agno.com/examples/learning/basics/b-session-context-planning

Bash script to clone the Agno repository, navigate to the learning examples directory, create a virtual environment, and execute the session context planning demo. Requires git and Python 3.x installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/01_basics

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 3b_session_context_planning.py
```

--------------------------------

### Setup and Run Background Hooks Example in Bash

Source: https://docs.agno.com/examples/agent-os/background-tasks/background-hooks-example

Shell script commands to clone the AgentOS repository, navigate to the background tasks example directory, create a virtual environment, and run the background hooks example. Requires git and Python 3.x installed.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/background_tasks

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python background_hooks_example.py
```

--------------------------------

### Setup and Run Agno Workflow Example

Source: https://docs.agno.com/examples/workflows/basic-workflows/sequence-of-steps/workflow-with-file-input

Bash commands to clone the Agno repository, navigate to the workflow example directory, set up a Python virtual environment, and execute the workflow script. Requires git and Python to be installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/01_basic_workflows/01_sequence_of_steps

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_with_file_input.py
```

--------------------------------

### Setup and Run Agno Example Project

Source: https://docs.agno.com/examples/teams/run-control/model-inheritance

Bash commands to clone the Agno repository, navigate to the teams example directory, set up a Python virtual environment using the provided setup script, and execute the model inheritance example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/run_control

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python model_inheritance.py
```

--------------------------------

### Setup and Run Example with Bash

Source: https://docs.agno.com/examples/workflows/advanced-concepts/structured-io/image-input

Clones the Agno repository, sets up a Python virtual environment using the demo setup script, and executes the image input workflow example. This provides a complete environment for running the image analysis and research workflow.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/structured_io

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_input.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/workflows/advanced-concepts/early-stopping/early-stop-condition

Bash commands to clone the Agno repository, navigate to the early stopping example directory, set up a Python virtual environment, and execute the early stop condition demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/early_stopping

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python early_stop_condition.py
```

--------------------------------

### Setup and Run AgentOSClient Example

Source: https://docs.agno.com/examples/agent-os/client/basic-client

Provides bash commands to clone the agno repository, set up a Python virtual environment, and execute the basic client example. Includes prerequisite setup script execution for demo environment configuration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/client

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_basic_client.py
```

--------------------------------

### Setup and Run File Analyst Example

Source: https://docs.agno.com/examples/agent-os/interfaces/slack/file-analyst

Provides bash commands to clone the Agno repository, navigate to the file analyst example, create a virtual environment, and run the application. Includes all necessary setup steps for a complete working environment.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/slack

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python file_analyst.py
```

--------------------------------

### Setup and Run Agent Example with Bash

Source: https://docs.agno.com/examples/agents/context-management/instructions

Shell script commands to clone the Agno repository, navigate to the context management example directory, set up a Python virtual environment, and execute the agent instructions example. Includes repository setup, environment activation, and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/03_context_management

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python instructions.py
```

--------------------------------

### Setup and Execution Commands

Source: https://docs.agno.com/examples/agents/approvals/audit-approval-async

Instructions for cloning the repository, setting up the virtual environment, and running the async audit approval demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/11_approvals

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audit_approval_async.py
```

--------------------------------

### Install Dependencies and Run Agno Input Transformation Example (Bash)

Source: https://docs.agno.com/hooks/usage/agent/input-transformation-pre-hook

These bash commands guide the user through the necessary steps to set up the environment and execute the Python example. It includes installing the required Python packages (`agno` and `openai`) using `uv pip` and then running the main Python script to see the input transformation in action.

```bash
uv pip install -U agno openai
```

```bash
python input_transformation_pre_hook.py
```

--------------------------------

### Setup and Run MCP Client Example

Source: https://docs.agno.com/examples/tools/mcp/sse-transport/client

Bash script commands to clone the Agno repository, set up a Python virtual environment, and execute the MCP client example. This prepares the development environment and runs the client.py script with all dependencies installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/sse_transport

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python client.py
```

--------------------------------

### Setup and Run WebsiteTools Example

Source: https://docs.agno.com/examples/tools/website-tools

Bash commands to clone the Agno repository, set up a virtual environment, and execute the website tools example script. These steps ensure the environment is correctly configured with the necessary dependencies.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python website_tools.py
```

--------------------------------

### Setup and Run Zoom Tools Example

Source: https://docs.agno.com/examples/tools/zoom-tools

Commands to clone the Agno repository, set up a virtual environment, export credentials, and execute the Zoom tools demonstration script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

export ZOOM_ACCOUNT_ID="***"
export ZOOM_CLIENT_ID="***"
export ZOOM_CLIENT_SECRET="***"

python zoom_tools.py
```

--------------------------------

### Clone, Setup, and Run Agno Example

Source: https://docs.agno.com/examples/models/groq/tool-use

Clone the Agno repository, navigate to the Groq model example directory, set up a virtual environment using the provided script, and execute the tool_use.py example. This prepares the environment and runs the agent demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Requesty Example in Bash

Source: https://docs.agno.com/examples/models/requesty/basic

Shell script commands to clone the Agno repository, navigate to the Requesty cookbook example directory, create a Python virtual environment using the provided setup script, and execute the basic example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/requesty

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run DashScope Tool Use Example

Source: https://docs.agno.com/examples/models/dashscope/tool-use

Bash commands to clone the Agno repository, navigate to the DashScope cookbook directory, initialize the virtual environment, and run the tool use demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/dashscope

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Clone and Run Gemini Vertex AI Example

Source: https://docs.agno.com/examples/models/google/gemini/vertexai

Complete setup and execution workflow for running the Gemini Vertex AI example. Includes repository cloning, virtual environment creation, dependency installation, and script execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python vertexai.py
```

--------------------------------

### Setup and Run AgentOS with MCP Dynamic Headers

Source: https://docs.agno.com/examples/agent-os/mcp-demo/dynamic-headers/client

Bash script demonstrating the setup and execution steps for running the AgentOS example with dynamic headers. Includes cloning the repository, creating a virtual environment, and starting the client application.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/mcp_demo/dynamic_headers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python client.py
```

--------------------------------

### Setup and Run the Agno Memory Tools Example (Bash)

Source: https://docs.agno.com/examples/memory/memory-tools

This bash script provides instructions to clone the `agno` repository, navigate to the example directory, set up a Python virtual environment, and execute the `08_memory_tools.py` script. It ensures all dependencies are installed and the environment is ready to run the agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/11_memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 08_memory_tools.py
```

--------------------------------

### Setup and Run Custom Chunking Strategy Example

Source: https://docs.agno.com/examples/knowledge/chunking/custom-strategy-example

Provides bash commands to clone the Agno repository, set up the development environment with a virtual environment, optionally run PgVector using Docker, and execute the custom chunking strategy example script. Includes steps for repository initialization, dependency installation, and optional database setup.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/chunking

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python custom_strategy_example.py
```

--------------------------------

### Setup and Run Tool Hooks Example

Source: https://docs.agno.com/examples/agents/hooks/tool-hooks

Bash script to clone the Agno repository, navigate to the tool hooks example directory, set up a virtual environment, and execute the tool_hooks.py script. This demonstrates the complete setup process for running the tool hooks example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/09_hooks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_hooks.py
```

--------------------------------

### Setup and Run Specialist Router Example

Source: https://docs.agno.com/examples/teams/modes/route/specialist-router

Bash script to clone the Agno repository, navigate to the specialist router example directory, create a virtual environment, and execute the specialist router demonstration. Requires git and Python to be installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/modes/route

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_specialist_router.py
```

--------------------------------

### Setup and Run Audio Processing Example

Source: https://docs.agno.com/examples/models/google/gemini/audio-input-local-file-upload

Bash script commands to clone the Agno repository, navigate to the Google Gemini cookbook directory, set up a Python virtual environment, and execute the audio input local file upload example. Requires git and Python to be installed.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_input_local_file_upload.py
```

--------------------------------

### Setup and Run LiteLLM PDF Example

Source: https://docs.agno.com/examples/models/litellm/pdf-input-local

Bash script commands to clone the Agno repository, navigate to the LiteLLM cookbook directory, create and activate a Python virtual environment, and execute the PDF input example. Uses the provided demo_setup.sh script for environment configuration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_local.py
```

--------------------------------

### Setup and Run Google Drive Example

Source: https://docs.agno.com/examples/tools/google-drive

Shell script commands to clone the Agno repository, set up a virtual environment, and execute the Google Drive integration example. This provides a complete setup workflow for running the Google Drive tools demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python google_drive.py
```

--------------------------------

### Setup and Run AgentOS Example

Source: https://docs.agno.com/examples/tools/mcp/mcp-toolbox-demo/agent-os

Provides shell commands to clone the agno repository, navigate to the MCP toolbox demo directory, create a virtual environment, and run the hotel assistant agent. The setup script automates environment configuration and dependency installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/mcp_toolbox_demo

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_os.py
```

--------------------------------

### Setup and Run Agno Anthropic Prompt Caching Example

Source: https://docs.agno.com/examples/models/anthropic/prompt-caching-extended

Provides shell commands to clone the Agno repository, navigate to the Anthropic cookbook directory, set up a Python virtual environment, and execute the prompt caching extended example script. This setup ensures all dependencies are properly installed and the demo runs in an isolated environment.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python prompt_caching_extended.py
```

--------------------------------

### Setup and Run Workflow Example

Source: https://docs.agno.com/examples/reasoning/tools/workflow-tools

Bash script commands to clone the agno repository, navigate to the workflow tools example, set up a Python virtual environment, and execute the blog post workflow demonstration.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_tools.py
```

--------------------------------

### Setup and Run Deepseek Example

Source: https://docs.agno.com/examples/models/deepseek/tool-use

Provides shell commands to clone the Agno repository, navigate to the Deepseek example directory, create a virtual environment, and execute the tool_use.py script. This setup uses the demo_setup.sh script to automate environment configuration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/deepseek

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Agno Planning Mode Example (Bash)

Source: https://docs.agno.com/examples/learning/session-context/planning-mode

This bash script provides a step-by-step guide to set up the Agno project environment and execute the planning mode example. It includes commands for cloning the repository, navigating to the specific example directory, creating and activating a Python virtual environment, and finally running the Python script that demonstrates the planning mode functionality.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/03_session_context

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_planning_mode.py
```

--------------------------------

### Setup and Run Agno Cookbook Example

Source: https://docs.agno.com/examples/agents/tools/tool-call-limit

Bash commands to clone the Agno repository, set up a virtual environment using the provided demo script, and execute the tool call limit example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/04_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_call_limit.py
```

--------------------------------

### Setup and Run Verbosity Control Example

Source: https://docs.agno.com/examples/models/openai/chat/verbosity-control

Bash script to clone the Agno repository, navigate to the OpenAI chat cookbook directory, create a Python virtual environment, and execute the verbosity control example. This ensures all dependencies are properly installed and the example runs in an isolated environment.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python verbosity_control.py
```

--------------------------------

### Install Dependencies and Run Agno Agent Memory Example in Bash

Source: https://docs.agno.com/models/providers/local/ollama/usage/memory

These bash commands guide the user through setting up the environment and executing the Agno agent memory example. It involves pulling the specified Ollama model, installing necessary Python packages like Agno, SQLAlchemy, and Psycopg, and finally running the main Python script.

```bash
ollama pull qwen2.5:latest
```

```bash
uv pip install -U ollama agno sqlalchemy psycopg pgvector
```

```bash
python cookbook/11_models/ollama/memory.py
```

--------------------------------

### Setup and Run Watsonx Knowledge Example

Source: https://docs.agno.com/examples/models/ibm/watsonx/knowledge

Bash commands to clone the Agno repository, set up the virtual environment, start the required PgVector database via Docker, and execute the knowledge base script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ibm/watsonx

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run Example with Bash

Source: https://docs.agno.com/examples/knowledge/quickstart/from-multiple

Provides shell commands to clone the Agno repository, set up a virtual environment, optionally run PgVector with Docker, and execute the knowledge loading example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 04_from_multiple.py
```

--------------------------------

### Run Ollama Basic Example Setup and Execution

Source: https://docs.agno.com/examples/models/ollama/chat/basic

This bash script provides instructions to clone the Agno repository, set up a virtual environment, and execute the `basic.py` example. It ensures all necessary dependencies are installed and the environment is ready to run the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Agno Future Life Story Example (Bash)

Source: https://docs.agno.com/examples/reasoning/agents/life-in-500000-years

This bash script provides instructions to clone the Agno repository, navigate to the example directory, set up a virtual environment, activate it, and then execute the Python script for the future life storytelling example. It covers the necessary steps to get the example running from scratch.

```bash
# Clone and setup repogit clone https://github.com/agno-agi/agno.gitcd agno/cookbook/10_reasoning/agents# Create and activate virtual environment./scripts/demo_setup.shsource .venvs/demo/bin/activatepython life_in_500000_years.py
```

--------------------------------

### Setup and Run Example in Bash

Source: https://docs.agno.com/examples/reasoning/agents/default-chain-of-thought

Provides shell commands to clone the Agno repository, navigate to the reasoning agents cookbook directory, set up a Python virtual environment, and execute the chain-of-thought example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python default_chain_of_thought.py
```

--------------------------------

### Setup and Execution

Source: https://docs.agno.com/examples/teams/session/share-session-with-agent

Instructions for cloning the repository, setting up the environment, and running the session sharing example.

```APIDOC
## Setup and Run Example

### Prerequisites
- Git installed
- Python 3.8 or higher
- OpenAI API credentials configured

### Installation Steps

#### Step 1: Clone Repository
```
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/session
```

#### Step 2: Setup Virtual Environment
```
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
```

#### Step 3: Run Example
```
python share_session_with_agent.py
```

### Expected Output
The script will execute three sequential interactions:
1. City Planner Agent responds to weather query for Tokyo
2. City Planner Team responds to activities query (using shared session)
3. City Planner Agent responds to follow-up question (with full context)

### Environment Configuration
- Ensure OPENAI_API_KEY is set in your environment
- Virtual environment activation required before running
- Demo setup script handles dependency installation

### Documentation Reference
- Complete documentation available at: https://docs.agno.com/llms.txt
- Use documentation index to discover all available pages
```

--------------------------------

### Setup and Run Vertex AI Claude Image Example

Source: https://docs.agno.com/examples/models/vertexai/claude/image-input-url

Bash script commands to clone the Agno repository, navigate to the Vertex AI Claude cookbook example directory, create a virtual environment, and execute the image input URL example. Requires git and Python installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_input_url.py
```

--------------------------------

### Setup and Run Anthropic Agent Example

Source: https://docs.agno.com/examples/models/anthropic/db

Bash script to clone the Agno repository, set up a Python virtual environment, and execute the Anthropic database agent example. This automates the installation and activation of dependencies required to run the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run Entity Memory Example

Source: https://docs.agno.com/examples/learning/entity-memory/entity-relationships

Provides shell commands to clone the Agno repository, set up a Python virtual environment, and execute the entity memory relationships example script. Includes dependency installation and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/04_entity_memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_entity_relationships.py
```

--------------------------------

### Setup and Run Slack Tools Example

Source: https://docs.agno.com/examples/tools/slack-tools

Bash script to clone the Agno repository, set up a virtual environment, and execute the Slack tools example. This script automates the environment configuration and dependency installation required to run the Slack integration demonstration.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python slack_tools.py
```

--------------------------------

### Setup and Run LlamaIndex Vector DB Example

Source: https://docs.agno.com/examples/knowledge/vector-db/llamaindex-db/llamaindex-db

Bash script for cloning the Agno repository, setting up a virtual environment, and executing the LlamaIndex vector database example. Uses the demo_setup.sh script to automate environment configuration and dependency installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/llamaindex_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python llamaindex_db.py
```

--------------------------------

### Setup Environment and Run Async Agent

Source: https://docs.agno.com/models/providers/gateways/nvidia/usage/async-tool-use

These commands guide the user through setting up the necessary environment variables, installing dependencies, and executing the Python script for the asynchronous agent. It includes setting the NVIDIA API key and installing the 'agno' library.

```bash
export NVIDIA_API_KEY=xxx
```

```bash
uv pip install -U agno
```

```bash
python cookbook/11_models/nvidia/async_tool_use.py
```

--------------------------------

### Run Ollama Retry Example with Bash

Source: https://docs.agno.com/examples/models/ollama/chat/retry

Provides shell commands to clone the Agno repository, navigate to the Ollama chat example directory, set up a Python virtual environment, and execute the retry example script. This setup ensures all dependencies are properly isolated and installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run Agno Channel Summarizer Example via Bash

Source: https://docs.agno.com/examples/agent-os/interfaces/slack/channel-summarizer

This bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a virtual environment, activate it, and then execute the `channel_summarizer.py` script. It outlines the necessary steps to get the Agno Channel Summarizer example running locally.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/05_agent_os/interfaces/slack\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython channel_summarizer.py
```

--------------------------------

### Setup and Run Vertexai Image Input Bytes Example

Source: https://docs.agno.com/examples/models/vertexai/claude/image-input-bytes

Bash script commands to clone the Agno repository, navigate to the Vertexai Claude cookbook example directory, create a Python virtual environment, and execute the image input bytes example. Requires git and Python 3.x installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_input_bytes.py
```

--------------------------------

### Setup and Run Agno Knowledge Tools Example (Bash)

Source: https://docs.agno.com/examples/reasoning/tools/knowledge-tools

This bash script provides a step-by-step guide to set up the development environment and execute the Agno Knowledge Tools example. It includes commands for cloning the Agno repository, navigating to the specific example directory, creating and activating a Python virtual environment, and finally running the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python knowledge_tools.py
```

--------------------------------

### Setup Agno Project and Run Dependencies Example

Source: https://docs.agno.com/examples/teams/dependencies/dependencies-to-members

Bash script to clone the Agno repository, navigate to the dependencies example directory, create a Python virtual environment, and execute the dependencies_to_members.py script. Requires git and Python 3.x installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/dependencies

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dependencies_to_members.py
```

--------------------------------

### Setup and Run Approval Example in Bash

Source: https://docs.agno.com/examples/agents/approvals/approval-list-and-resolve

Clones the Agno repository, navigates to the approvals cookbook example, sets up a Python virtual environment, and executes the approval resolution script. This demonstrates the complete setup workflow for running the approval management example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/11_approvals

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python approval_list_and_resolve.py
```

--------------------------------

### Setup Environment and Start vLLM Server

Source: https://docs.agno.com/models/providers/local/vllm/usage/tool-use

These bash commands handle the installation of necessary libraries and the execution of the vLLM server with auto-tool-choice enabled. This setup is required to allow the agent to parse tool calls using the Hermes parser.

```bash
uv pip install -U agno openai vllm

vllm serve NousResearch/Nous-Hermes-2-Mistral-7B-DPO \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --dtype float16 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.9

python cookbook/11_models/vllm/tool_use.py
```

--------------------------------

### Setup and Run Anthropic Web Fetch Example (Bash)

Source: https://docs.agno.com/examples/models/anthropic/web-fetch

These bash commands provide a step-by-step guide to set up and execute the Anthropic web fetch example. It involves cloning the `agno` repository, navigating to the specific example directory, creating and activating a Python virtual environment, and finally running the `web_fetch.py` script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/anthropic\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython web_fetch.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/integrations/observability/arize-phoenix-via-openinference-local

Provides shell commands to clone the Agno repository, set up a Python virtual environment, configure environment variables, and execute the Phoenix integration example. Includes steps for installing dependencies and exporting the Phoenix collector endpoint.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/observability

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export PHOENIX_COLLECTOR_ENDPOINT="***"

python arize_phoenix_via_openinference_local.py
```

--------------------------------

### Setup and Run Example - Bash Shell Commands

Source: https://docs.agno.com/examples/agents/dependencies/dependencies-in-tools

Shell script commands to clone the Agno repository, navigate to the dependencies example directory, create a virtual environment, and execute the dependencies_in_tools.py demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/15_dependencies

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dependencies_in_tools.py
```

--------------------------------

### Setup and Run Agentic RAG Example

Source: https://docs.agno.com/examples/agents/knowledge/agentic-rag-with-reranking

Commands to install necessary dependencies, clone the repository, set up a virtual environment, and execute the Agentic RAG script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/07_knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agentic_rag_with_reranking.py
```

--------------------------------

### Setup and Run Website Reader Example

Source: https://docs.agno.com/examples/knowledge/readers/website-reader

Shell commands to clone the Agno repository, set up a virtual environment, start a PgVector Docker container, and execute the website reader script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python website_reader.py
```

--------------------------------

### Run MySQL Agent Example with Setup Script

Source: https://docs.agno.com/examples/storage/mysql/mysql-for-agent

Bash commands to clone the Agno repository, navigate to the MySQL storage example directory, set up a Python virtual environment, and execute the agent script. The demo_setup.sh script automates environment configuration and dependency installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/mysql

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python mysql_for_agent.py
```

--------------------------------

### Setup and Run OpenAI Audio Input Agent Example (Bash)

Source: https://docs.agno.com/examples/models/openai/chat/audio-input-agent

These bash commands provide a step-by-step guide to set up the development environment and run the OpenAI audio input agent example. It includes cloning the Agno repository, navigating to the specific cookbook directory, creating and activating a virtual environment, and finally executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_input_agent.py
```

--------------------------------

### Setup and Run Redis Workflow Example

Source: https://docs.agno.com/examples/storage/redis/redis-for-workflow

Provides shell commands to clone the agno repository, navigate to the Redis storage example directory, set up a Python virtual environment, and execute the workflow script. Requires git and Python to be installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/redis

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python redis_for_workflow.py
```

--------------------------------

### Set Up and Run Zep Integration Example (Bash)

Source: https://docs.agno.com/examples/integrations/memory/zep-integration

This bash script outlines the steps to set up the development environment and run the Zep integration example. It includes commands for cloning the Agno repository, navigating to the specific example, creating and activating a Python virtual environment, and finally executing the Python script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/92_integrations/memory\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython zep_integration.py
```

--------------------------------

### Setup Environment and Install Dependencies

Source: https://docs.agno.com/integrations/discord/usage/agent-with-media

Commands to export required API keys, install the Agno and Discord libraries, and run the media agent script.

```bash
export GOOGLE_API_KEY=xxx
export DISCORD_BOT_TOKEN=xxx

uv pip install -U agno google-generativeai discord.py

python cookbook/13_integrations/discord/agent_with_media.py
```

--------------------------------

### Setup and Run the Typed Agent Example via Bash

Source: https://docs.agno.com/examples/basics/agent-with-typed-input-output

These bash commands provide a step-by-step guide to set up the development environment and execute the Python agent example. It includes cloning the repository, navigating to the specific example directory, creating and activating a Python virtual environment, and finally running the agent_with_typed_input_output.py script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_typed_input_output.py
```

--------------------------------

### Setup and Run SingleStore Team Example

Source: https://docs.agno.com/examples/storage/singlestore/singlestore-for-team

Commands to clone the repository, set up a virtual environment, and execute the SingleStore team storage example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/singlestore

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python singlestore_for_team.py
```

--------------------------------

### Setup and Run Reasoning Content Example

Source: https://docs.agno.com/examples/reasoning/tools/capture-reasoning-content-reasoning-tools

Bash commands to clone the Agno repository, navigate to the reasoning tools cookbook directory, set up a virtual environment, and execute the reasoning content capture example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python capture_reasoning_content_reasoning_tools.py
```

--------------------------------

### Setup and Run Agno References Format Example (Bash)

Source: https://docs.agno.com/examples/agents/knowledge/references-format

This bash script outlines the steps to set up and execute the Agno references format example. It includes cloning the Agno repository, navigating to the specific example directory, creating and activating a Python virtual environment, and optionally starting a PgVector Docker container. Finally, it runs the Python script to demonstrate the YAML reference formatting.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/07_knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python references_format.py
```

--------------------------------

### Setup and Run AgentOS Tracing Example

Source: https://docs.agno.com/examples/agent-os/tracing/basic-agent-tracing

Bash script to clone the agno repository, set up the virtual environment, and run the traced agent example. This automates the installation of dependencies and activation of the demo environment for executing the HackerNews agent with tracing.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/tracing

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_basic_agent_tracing.py
```

--------------------------------

### Setup and Run Traditional RAG Example (Bash)

Source: https://docs.agno.com/knowledge/agents/traditional-rag-pgvector

These bash commands provide the necessary steps to prepare the environment for the RAG example. This includes installing Python dependencies, setting up the OpenAI API key, and executing the main Python script.

```bash
uv pip install -U agno openai sqlalchemy psycopg pgvector
```

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

```bash
python traditional_rag_pgvector.py
```

--------------------------------

### Setup and Run MCP Toolbox Database Example

Source: https://docs.agno.com/examples/tools/mcp/mcp-toolbox-for-db

Bash script commands to clone the Agno repository, navigate to the MCP tools cookbook example, set up a Python virtual environment using the demo setup script, and execute the MCP toolbox database example. This provides the complete setup workflow for running the agent locally.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python mcp_toolbox_for_db.py
```

--------------------------------

### Setup and Run Google Gemini Basic Example (Bash)

Source: https://docs.agno.com/examples/models/google/gemini/basic

This bash script provides instructions to clone the `agno` repository, navigate to the Google Gemini cookbook example, set up a virtual environment using `demo_setup.sh`, activate it, and finally execute the `basic.py` Python script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/google/gemini\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython basic.py
```

--------------------------------

### Setup and Run Agno Tool Initialization Example

Source: https://docs.agno.com/examples/tools/other/add-tool-after-initialization

Shell commands to clone the Agno repository, prepare the environment using a setup script, and execute the Python script demonstrating dynamic tool addition.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/other

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python add_tool_after_initialization.py
```

--------------------------------

### Clone and Run Example with Setup Script

Source: https://docs.agno.com/examples/agents/advanced/custom-cancellation-manager

Provides bash commands to clone the agno repository, navigate to the example directory, set up a Python virtual environment using the provided setup script, and execute the custom cancellation manager demonstration.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python custom_cancellation_manager.py
```

--------------------------------

### Setup and Run Gemini Grounding Example

Source: https://docs.agno.com/examples/models/google/gemini/grounding

Bash script commands to clone the Agno repository, set up a virtual environment, and execute the grounding example. This demonstrates the complete workflow for installing dependencies and running the Gemini grounding agent locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python grounding.py
```

--------------------------------

### Setup and Run Calculator Tools Example - Bash

Source: https://docs.agno.com/examples/tools/calculator-tools

Shell script commands to clone the Agno repository, navigate to the calculator tools cookbook, set up a Python virtual environment, and execute the calculator tools example. Requires git and Python to be installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python calculator_tools.py
```

--------------------------------

### Setup and Run Agno Cookbook Example

Source: https://docs.agno.com/examples/models/meta/llama/image-input-bytes

Bash script commands to clone the Agno repository, navigate to the Meta Llama cookbook directory, create a virtual environment, and execute the image input bytes example. Requires git and Python to be installed.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_input_bytes.py
```

--------------------------------

### Setup and Run Async Tools Example in Bash

Source: https://docs.agno.com/examples/teams/tools/async-tools

Commands to clone the Agno repository, set up the virtual environment, and execute the async tools demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python async_tools.py
```

--------------------------------

### Setup and Run Image Generation Example

Source: https://docs.agno.com/examples/models/openai/chat/generate-images

Bash script commands to clone the Agno repository, navigate to the cookbook example directory, set up a Python virtual environment, and execute the image generation script. Requires git and Python to be installed on the system.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python generate_images.py
```

--------------------------------

### Setup and Run MCP Graphiti Example

Source: https://docs.agno.com/examples/tools/mcp/graphiti

Provides bash commands to clone the Agno repository, navigate to the MCP Graphiti example directory, set up a Python virtual environment using the demo setup script, and run the graphiti.py example. This assumes the Graphiti MCP server is already running on localhost:8000.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python graphiti.py
```

--------------------------------

### Setup and Run Moonshot Example

Source: https://docs.agno.com/examples/models/moonshot/basic

Bash script commands to clone the Agno repository, navigate to the Moonshot cookbook example directory, create a virtual environment using the provided setup script, activate it, and execute the basic.py example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/moonshot

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run OpenAI Retries Example

Source: https://docs.agno.com/examples/models/openai/chat/with-retries

Bash script commands to clone the Agno repository, navigate to the cookbook example directory, set up a Python virtual environment, and execute the with_retries.py script. Requires git and Python to be installed on the system.

```Bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python with_retries.py
```

--------------------------------

### Setup and Execution for Nebius Cookbook Example

Source: https://docs.agno.com/examples/models/nebius/structured-output

Commands to clone the Agno repository, navigate to the Nebius model directory, prepare the environment using a setup script, and run the structured output Python example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/nebius

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Execution Environment

Source: https://docs.agno.com/examples/storage/surrealdb/surrealdb-for-team

Bash commands to clone the Agno repository, set up a virtual environment, install necessary dependencies, and execute the SurrealDB team cookbook example.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/surrealdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Install dependencies
uv pip install anthropic ddgs newspaper4k lxml_html_clean surrealdb agno

python surrealdb_for_team.py
```

--------------------------------

### Setup and Run Cerebras COT Example

Source: https://docs.agno.com/examples/reasoning/agents/cerebras-llama-default-cot

Bash script to clone the Agno repository, navigate to the reasoning agents cookbook, set up a Python virtual environment, and execute the Cerebras chain-of-thought example. Requires git and Python 3.x installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cerebras_llama_default_COT.py
```

--------------------------------

### Setup and Run Doc Kb Async Example in Bash

Source: https://docs.agno.com/examples/knowledge/readers/doc-kb-async

Shell script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the async knowledge base example. Includes all necessary setup steps for running the documentation knowledge base demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python doc_kb_async.py
```

--------------------------------

### Setup and Run Agno Dependencies Example

Source: https://docs.agno.com/examples/teams/dependencies/dependencies-in-context

Commands to clone the Agno repository, set up a virtual environment, and execute the dependencies in context example script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/dependencies

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dependencies_in_context.py
```

--------------------------------

### Setup and Run Nexus Basic Example (Bash)

Source: https://docs.agno.com/examples/models/nexus/basic

This bash script provides instructions to clone the Agno repository, navigate to the Nexus example directory, set up a virtual environment, activate it, and finally execute the `basic.py` Python script. This allows users to run the provided Python example locally.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/nexus\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython basic.py
```

--------------------------------

### Setup and Run SurrealDB Memory Search Example

Source: https://docs.agno.com/examples/integrations/surrealdb/memory-search-surreal

Provides bash commands to clone the Agno repository, navigate to the SurrealDB integration cookbook example, set up a Python virtual environment, and execute the memory search script. This ensures all dependencies are installed and the environment is properly configured before running the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/surrealdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python memory_search_surreal.py
```

--------------------------------

### Setup and Run Workflow Example

Source: https://docs.agno.com/examples/components/get-workflow

Bash commands to clone the Agno repository, navigate to the components directory, set up the virtual environment, and execute the workflow retrieval script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/93_components

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python get_workflow.py
```

--------------------------------

### Setup and Execute Agno Team Knowledge Example via Bash

Source: https://docs.agno.com/examples/teams/knowledge/team-with-custom-retriever

This bash snippet provides the commands to prepare the environment for the Agno team example. It includes repository cloning, virtual environment activation, and starting the required PgVector database container.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 04_team_with_custom_retriever.py
```

--------------------------------

### Setup and Run Example with Bash

Source: https://docs.agno.com/examples/teams/multimodal/image-to-text

Provides shell commands to clone the Agno repository, navigate to the multimodal teams cookbook example, set up a Python virtual environment, and execute the image-to-text demonstration script. This includes repository cloning, environment activation, and running the Python example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_to_text.py
```

--------------------------------

### Setup and run Agno CSVReader example in Bash

Source: https://docs.agno.com/examples/knowledge/readers/csv-reader

This Bash script provides instructions to clone the Agno repository, navigate to the relevant example directory, set up a Python virtual environment, activate it, and finally execute the `csv_reader.py` script. It outlines the necessary steps to get the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python csv_reader.py
```

--------------------------------

### Setup and Run Agent-as-Judge Example

Source: https://docs.agno.com/examples/evals/agent-as-judge/agent-as-judge-binary

Bash script commands to clone the Agno repository, navigate to the evaluation cookbook example, set up a Python virtual environment, and execute the binary agent-as-judge evaluation. Requires git and Python 3.x installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/09_evals/agent_as_judge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_as_judge_binary.py
```

--------------------------------

### Setup and Run Agno Web Search Agent Example (Bash)

Source: https://docs.agno.com/examples/models/vllm/tool-use

This snippet provides instructions to set up the project environment and run the Python web search agent example. It includes commands for cloning the `agno` repository, navigating to the example directory, creating and activating a virtual environment, and executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vllm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run LMStudio Agent Example

Source: https://docs.agno.com/examples/models/lmstudio/db

Bash script to clone the Agno repository, set up a virtual environment, and execute the LMStudio database agent example. This automates the environment preparation and dependency installation required to run the Python agent code.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/lmstudio

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run Agno Memory Example with Bash

Source: https://docs.agno.com/examples/models/vertexai/claude/memory

Commands to clone the repository, set up a virtual environment, start a PgVector Docker container, and execute the memory persistence script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python memory.py
```

--------------------------------

### Setup and Run the Example

Source: https://docs.agno.com/examples/knowledge/custom-retriever/retriever-with-dependencies

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the custom retriever example. This provides a complete setup workflow for running the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/custom_retriever

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python retriever_with_dependencies.py
```

--------------------------------

### Setup and Run Memory Optimization Example

Source: https://docs.agno.com/examples/memory/optimize-memories/memory-summarize-strategy

Bash commands to clone the Agno repository, set up a virtual environment, and execute the memory summarization demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/11_memory/optimize_memories

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_memory_summarize_strategy.py
```

--------------------------------

### Install and Run Agno Gmail Cookbook

Source: https://docs.agno.com/examples/tools/gmail-tools

Commands to clone the Agno repository, initialize the environment using the provided setup script, and run the Gmail tools example.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python gmail_tools.py
```

--------------------------------

### Setup and Run LiteLLM Memory Example

Source: https://docs.agno.com/examples/models/litellm/memory

Commands to clone the Agno repository, set up the virtual environment, and execute the LiteLLM memory cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python memory.py
```

--------------------------------

### Setup and Run PDF Input Example

Source: https://docs.agno.com/examples/models/openai/chat/pdf-input-url

Bash script commands to clone the Agno repository, navigate to the OpenAI chat examples directory, create a virtual environment, and execute the PDF input URL example. Includes repository setup and environment activation steps.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_url.py
```

--------------------------------

### Clone, Setup, and Run Agent OS Quick Start

Source: https://docs.agno.com/examples/basics/run

Bash script commands to clone the Agno repository, set up a Python virtual environment using the provided demo setup script, and run the Agent OS server. This initializes all dependencies and starts the local Agent OS instance on port 7777 for web interface access.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python run.py
```

--------------------------------

### Setup and Run LiteLLM Metrics Example

Source: https://docs.agno.com/examples/models/litellm/metrics

Bash script to clone the Agno repository, set up a virtual environment, and execute the metrics.py cookbook example. Includes all necessary setup steps for running the LiteLLM metrics demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python metrics.py
```

--------------------------------

### Setup and Run AgentOSClient Workflow Example

Source: https://docs.agno.com/examples/agent-os/client/run-workflows

Provides bash commands to clone the Agno repository, set up a Python virtual environment, and execute the workflow example script. This setup script initializes the demo environment and activates the virtual environment before running the workflow demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/client

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 07_run_workflows.py
```

--------------------------------

### Setup and Execute OpenRouter Cookbook Example

Source: https://docs.agno.com/examples/models/openrouter/chat/basic

Shell commands to clone the Agno repository, configure the environment using a setup script, and run the basic OpenRouter chat script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openrouter/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Schedule History Example in Bash

Source: https://docs.agno.com/examples/agent-os/scheduler/run-history

Provides shell commands to clone the Agno repository, navigate to the scheduler cookbook example, create a virtual environment, and execute the run history demonstration script. This is the complete setup workflow for running the schedule history analysis example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/scheduler

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python run_history.py
```

--------------------------------

### Setup and Execute Agno Input Schema Example

Source: https://docs.agno.com/examples/agents/input-output/input-schema

This Bash snippet provides a step-by-step guide to set up the agno project, navigate to the specific example directory, create and activate a Python virtual environment, and finally run the input_schema.py script. These steps are essential to reproduce and test the input schema functionality locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/02_input_output

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python input_schema.py
```

--------------------------------

### Setup and Run Workflow Example

Source: https://docs.agno.com/examples/agent-os/dbs/surreal-db/workflows

Bash script to clone the Agno repository, set up the development environment, activate a virtual environment, and execute the workflows module. This demonstrates the complete setup process for running the multi-agent workflow example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/dbs/surreal_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflows.py
```

--------------------------------

### Setup and Run Custom Tools Example in Bash

Source: https://docs.agno.com/examples/teams/tools/custom-tools

Provides shell commands to clone the Agno repository, navigate to the custom tools example directory, create a virtual environment, and execute the custom tools demonstration script. Includes setup automation via shell script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python custom_tools.py
```

--------------------------------

### Setup Environment and Run Memory Agent Example

Source: https://docs.agno.com/examples/models/anthropic/memory

Shell commands to clone the repository, set up a virtual environment, start a pgvector Docker container, and execute the memory agent script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python memory.py
```

--------------------------------

### Setup and Run VLLM Structured Output Example

Source: https://docs.agno.com/examples/models/vllm/structured-output

These bash commands provide instructions to clone the `agno` repository, navigate to the example directory, set up a virtual environment using `demo_setup.sh`, activate it, and finally execute the `structured_output.py` script. This allows users to run the VLLM structured output example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vllm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Agno Memory Example

Source: https://docs.agno.com/examples/models/mistral/memory

Bash commands to clone the repository, set up a virtual environment, start a pgvector container via Docker, and execute the memory-enabled agent script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/mistral

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python memory.py
```

--------------------------------

### Setup and Run Dashscope Knowledge Tools Example

Source: https://docs.agno.com/examples/models/dashscope/knowledge-tools

Bash script to clone the agno repository, set up a virtual environment, configure API keys, and execute the knowledge tools example. This demonstrates the complete setup workflow for running the Dashscope agent with knowledge base integration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/dashscope

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export OPENAI_API_KEY="***"

python knowledge_tools.py
```

--------------------------------

### Run Schedule Validation Example with Bash

Source: https://docs.agno.com/examples/agent-os/scheduler/schedule-validation

Shell script commands to clone the Agno repository, set up the project environment, create a virtual environment, and execute the schedule validation example. Includes steps for repository setup and dependency installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/scheduler

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python schedule_validation.py
```

--------------------------------

### Setup and Run Cerebras OpenAI Knowledge Example

Source: https://docs.agno.com/examples/models/cerebras-openai/knowledge

Shell commands to clone the Agno repository, set up the demo environment, and run the knowledge base example script. It includes steps for virtual environment activation and starting a PgVector instance via Docker.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cerebras_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run Agno Structured Output Example via Bash

Source: https://docs.agno.com/examples/models/together/structured-output

These bash commands provide instructions to clone the Agno repository, navigate to the specific cookbook example directory, set up a Python virtual environment using `demo_setup.sh`, activate it, and finally execute the `structured_output.py` script. This sequence allows users to quickly get the example running locally.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/together\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython structured_output.py
```

--------------------------------

### WorkflowTools Multi-Agent Blog Post Workflow Setup

Source: https://docs.agno.com/tools/reasoning_tools/workflow-tools

Demonstrates a complete multi-agent workflow setup using WorkflowTools with three specialized agents (Web Agent, HackerNews Agent, Writer Agent) for creating blog posts. The example includes agent initialization with OpenAI models, tool integration, and few-shot examples for guiding agent behavior.

```Python
import asyncio
from textwrap import dedent

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIResponses
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.workflow import WorkflowTools
from agno.workflow.types import StepInput, StepOutput
from agno.workflow.workflow import Workflow

FEW_SHOT_EXAMPLES = dedent("""\
    You can refer to the examples below as guidance for how to use each tool.
    ### Examples
    #### Example: Blog Post Workflow
    User: Please create a blog post on the topic: AI Trends in 2024
    Run: input_data="AI trends in 2024", additional_data={"topic": "AI, AI agents, AI workflows", "style": "The blog post should be written in a style that is easy to understand and follow."}
    Final Answer: I've created a blog post on the topic: AI trends in 2024 through the workflow. The blog post shows...
    
    You HAVE TO USE additional_data to pass the topic and style to the workflow.
""")

# Define agents
web_agent = Agent(
    name="Web Agent",
    model=OpenAIResponses(id="gpt-5.2"),
    tools=[DuckDuckGoTools()],
    role="Search the web for the latest news and trends",
)
hackernews_agent = Agent(
    name="Hackernews Agent",
    model=OpenAIResponses(id="gpt-5.2"),
    tools=[HackerNewsTools()],
    role="Extract key insights and content from Hackernews posts",
)

writer_agent = Agent(
    name="Writer Agent",
    model=OpenAIResponses(id="gpt-5.2"),
    instructions="Write a blog post on the topic",
)
```

--------------------------------

### Setup and Execute Requesty Example

Source: https://docs.agno.com/examples/models/requesty/tool-use

Provides the shell commands necessary to clone the Agno repository, set up a virtual environment using the provided demo script, and execute the Requesty tool use demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/requesty

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Discord Bot Example

Source: https://docs.agno.com/examples/integrations/discord/agent-with-media

Shell script commands to clone the Agno repository, navigate to the Discord integration example, set up a Python virtual environment, and run the Discord bot agent. Requires git and Python to be installed on the system.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/discord

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_media.py
```

--------------------------------

### Setup Environment and LiteLLM Proxy

Source: https://docs.agno.com/models/providers/gateways/litellm-openai/usage/basic

Shell commands to set the API key, install required packages (litellm, openai, agno), and start the LiteLLM proxy server.

```bash
export LITELLM_API_KEY=xxx
uv pip install -U litellm[proxy] openai agno
litellm --model gpt-5-mini --host 127.0.0.1 --port 4000
```

--------------------------------

### Setup and Run Reasoning Model Example

Source: https://docs.agno.com/examples/reasoning/models/azure-openai/reasoning-model-gpt-4-1

Bash script commands to clone the Agno repository, navigate to the reasoning model example directory, set up a Python virtual environment, and execute the reasoning model demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/azure_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_model_gpt_4_1.py
```

--------------------------------

### Setup and Run SingleStore Agno Example with Bash

Source: https://docs.agno.com/examples/knowledge/vector-db/singlestore-db/singlestore-db

This bash script provides instructions to clone the Agno repository, navigate to the SingleStore example directory, set up a Python virtual environment, and execute the provided Python script. It ensures all necessary dependencies are installed and the environment is ready to run the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/singlestore_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python singlestore_db.py
```

--------------------------------

### Setup and Run Agno Memory Example

Source: https://docs.agno.com/examples/models/lmstudio/memory

Shell commands to clone the repository, set up a virtual environment, start a pgvector container via Docker, and execute the memory agent script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/lmstudio

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python memory.py
```

--------------------------------

### Run Entity Memory Example with Bash

Source: https://docs.agno.com/examples/teams/learning/team-entity-memory

Setup and execution script for the entity memory demonstration. Clones the Agno repository, creates a Python virtual environment, and runs the team entity memory example. Requires git and Python 3.x installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/learning

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 03_team_entity_memory.py
```

--------------------------------

### Setup and Run Agno MCP Client Example

Source: https://docs.agno.com/examples/tools/mcp/local-server/client

Shell commands to clone the Agno repository, set up the virtual environment using the provided demo setup script, and execute the client script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/local_server

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python client.py
```

--------------------------------

### Setup and Run Memory Search Example

Source: https://docs.agno.com/examples/memory/memory-manager/memory-search

Commands to clone the Agno repository, set up the virtual environment, and execute the memory search demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/11_memory/memory_manager

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 04_memory_search.py
```

--------------------------------

### Setup and Run DeepKnowledge Agent Example with Bash

Source: https://docs.agno.com/examples/models/groq/deep-knowledge

This bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a Python virtual environment, activate it, and finally execute the `deep_knowledge.py` script to run the DeepKnowledge agent. This allows users to quickly get the example running.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python deep_knowledge.py
```

--------------------------------

### Setup and Run AgentOps Integration Example

Source: https://docs.agno.com/examples/integrations/observability/agent-ops

Provides bash commands to clone the Agno repository, navigate to the AgentOps integration example, set up a Python virtual environment, and execute the agent script. This workflow ensures all dependencies are properly installed in an isolated environment.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/observability

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_ops.py
```

--------------------------------

### Setup and Run Reasoning Agent Example

Source: https://docs.agno.com/examples/agents/advanced/reasoning-agent-events

Shell commands to clone the Agno repository, set up the necessary virtual environment using the provided demo script, and execute the reasoning agent events example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_agent_events.py
```

--------------------------------

### Setup and Run Agno Crawl4aiTools Examples

Source: https://docs.agno.com/examples/tools/crawl4ai-tools

This bash script provides instructions to clone the Agno repository, navigate to the specific examples directory, set up a virtual environment, and execute the Python script demonstrating Crawl4aiTools usage. It ensures all necessary dependencies are correctly installed and the environment is activated before running the examples.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python crawl4ai_tools.py
```

--------------------------------

### Setup and Execute DALL-E Examples via CLI

Source: https://docs.agno.com/examples/tools/dalle-tools

Shell commands to clone the Agno repository, prepare the environment using the provided setup script, and run the DALL-E tools demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dalle_tools.py
```

--------------------------------

### Setup and Execute Agno Session Options Example (Bash)

Source: https://docs.agno.com/examples/teams/session/session-options

This bash script provides a step-by-step guide to set up and run the Agno session options example. It covers cloning the Agno repository, navigating to the specific example directory, creating and activating a Python virtual environment using a helper script, and finally executing the session_options.py script. This is crucial for reproducing the demonstrated session behaviors.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/session

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python session_options.py
```

--------------------------------

### Setup and Run Cohere Agent Example

Source: https://docs.agno.com/examples/models/cohere/db

Bash script to clone the Agno repository, navigate to the Cohere cookbook example directory, create a virtual environment using the demo setup script, and execute the agent application. This sets up all necessary dependencies and runs the Python agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cohere

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run Agno Accuracy Evaluation Example with Bash

Source: https://docs.agno.com/examples/evals/accuracy/accuracy-with-tools

This Bash script provides instructions to clone the 'agno' repository, navigate to the specific example directory, set up a virtual environment, activate it, and then execute the Python accuracy evaluation script. It outlines the steps required to get the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/09_evals/accuracy

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python accuracy_with_tools.py
```

--------------------------------

### Setup and Run Agent Example in Bash

Source: https://docs.agno.com/examples/agent-os/interfaces/whatsapp/agent-with-user-memory

Clones the Agno repository, sets up a Python virtual environment, and runs the agent with user memory example. This script automates the initial setup process and activates the development environment.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/whatsapp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_user_memory.py
```

--------------------------------

### Setup and Run Azure Retries Example

Source: https://docs.agno.com/examples/models/azure/retry

Bash commands to clone the Agno repository, navigate to the Azure models cookbook directory, set up a Python virtual environment, and execute the retry example script. Requires git and Python to be installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run Financial Dataset Tools Example

Source: https://docs.agno.com/examples/tools/financial-datasets-tools

Bash commands to clone the Agno repository, initialize the environment using a setup script, and run the financial datasets tools demonstration.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python financial_datasets_tools.py
```

--------------------------------

### Setup and Run AgentOS Redis Example

Source: https://docs.agno.com/examples/agent-os/dbs/redis-db

Provides bash commands to clone the agno repository, navigate to the Redis database example directory, create a Python virtual environment using the demo setup script, activate it, and run the redis_db.py example with hot reload enabled.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/dbs

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python redis_db.py
```

--------------------------------

### Setup and Run Agno Knowledge Path Example (Bash)

Source: https://docs.agno.com/examples/knowledge/quickstart/from-path

This Bash script provides the necessary steps to set up the Agno project, create a virtual environment, and execute the Python example that loads knowledge from a local file path. It includes commands for cloning the repository, installing dependencies, and optionally running a Dockerized PgVector instance.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 01_from_path.py
```

--------------------------------

### Setup and Run Agno Postgres Example

Source: https://docs.agno.com/examples/tools/postgres-tools

This Bash script provides instructions for setting up the Agno repository and running the Postgres integration example. It includes commands to clone the repository, navigate to the specific example directory, create and activate a Python virtual environment, and execute the `postgres_tools.py` script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python postgres_tools.py
```

--------------------------------

### Setup and Execute Valyu Tools Example in Bash

Source: https://docs.agno.com/examples/tools/valyu-tools

Commands to clone the Agno repository, set up a virtual environment using the provided demo script, and execute the Valyu tools cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python valyu_tools.py
```

--------------------------------

### Setup and Run CEL Workflow Example

Source: https://docs.agno.com/examples/workflows/cel-expressions/condition/cel-previous-step-outputs

Bash script to clone the agno repository, set up a Python virtual environment, and execute the CEL previous step outputs workflow example. Automates the environment configuration and dependency installation required to run the workflow demonstration.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/07_cel_expressions/condition

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cel_previous_step_outputs.py
```

--------------------------------

### Setup and Run Finance Team Example

Source: https://docs.agno.com/examples/reasoning/teams/finance-team-chain-of-thought

Provides bash commands to clone the Agno repository, navigate to the reasoning teams cookbook directory, create a virtual environment using the demo setup script, and execute the finance team chain of thought example. This demonstrates the complete workflow from environment setup to running the multi-agent financial analysis.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/teams

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python finance_team_chain_of_thought.py
```

--------------------------------

### Setup and Run SurrealDB Memory Example in Bash

Source: https://docs.agno.com/examples/integrations/surrealdb/memory-creation

Provides shell commands to clone the Agno repository, navigate to the SurrealDB cookbook example, set up a Python virtual environment, and execute the memory creation script. Requires git and Python installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/surrealdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python memory_creation.py
```

--------------------------------

### Setup and Run Agno Knowledge URL Example

Source: https://docs.agno.com/examples/knowledge/quickstart/from-url

Shell commands to clone the Agno repository, set up the virtual environment, start a PgVector Docker container, and execute the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 02_from_url.py
```

--------------------------------

### Setup and Run S3 Knowledge Example via Bash

Source: https://docs.agno.com/examples/knowledge/quickstart/from-s3

Commands to clone the Agno repository, set up the virtual environment, start a PgVector instance using Docker, and execute the S3 knowledge loading script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 06_from_s3.py
```

--------------------------------

### Setup and Run Ollama Cloud Example

Source: https://docs.agno.com/examples/models/ollama/chat/ollama-cloud

Bash commands to clone the Agno repository, navigate to the Ollama chat cookbook, and initialize a virtual environment before running the example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python ollama_cloud.py
```

--------------------------------

### Setup and Run Browserbase Tools Example

Source: https://docs.agno.com/examples/tools/browserbase-tools

Clone the Agno repository, set up a Python virtual environment, and execute the Browserbase tools example script. This provides a complete setup workflow for testing Browserbase integration with Agno Agents.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python browserbase_tools.py
```

--------------------------------

### Setup and Run Agno Workflow Example in Bash

Source: https://docs.agno.com/examples/workflows/advanced-concepts/session-state/rename-session

Shell script commands to clone the Agno repository, navigate to the session state example directory, set up a Python virtual environment, and execute the rename_session.py script. Requires git and Python 3.x installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/session_state

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python rename_session.py
```

--------------------------------

### Setup and Run Agno Multi-user Example

Source: https://docs.agno.com/memory/agent/multi-user-multi-session-chat

Commands to configure the environment by setting the OpenAI API key, installing dependencies via uv, and executing the multi-user chat script.

```bash
export OPENAI_API_KEY=xxx
uv pip install -U agno openai
python multi_user_multi_session_chat.py
```

--------------------------------

### Setup and Run State Sharing Example

Source: https://docs.agno.com/examples/teams/state/state-sharing

Commands to clone the Agno repository, set up the virtual environment, and execute the state sharing demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/state

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python state_sharing.py
```

--------------------------------

### Setup and Run Airbnb Agent Example

Source: https://docs.agno.com/examples/agent-os/interfaces/a2a/multi-agent-a2a/airbnb-agent

Commands to clone the Agno repository, initialize the environment, and run the Airbnb agent server.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/a2a/multi_agent_a2a

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python airbnb_agent.py
```

--------------------------------

### Setup and Execution Commands for Portkey Example

Source: https://docs.agno.com/examples/models/portkey/basic

Bash commands to clone the Agno repository, prepare the virtual environment, and execute the basic Portkey integration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/portkey

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup Environment and Start vLLM Server

Source: https://docs.agno.com/models/providers/local/vllm/usage/async-basic-stream

These bash commands cover the installation of required libraries, the configuration and launch of the vLLM server with specific model parameters, and the execution of the agent script.

```bash
uv pip install -U agno openai vllm

vllm serve Qwen/Qwen2.5-7B-Instruct \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --dtype float16 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.9

python cookbook/11_models/vllm/async_basic_stream.py
```

--------------------------------

### Setup and Run Workflow Example

Source: https://docs.agno.com/examples/workflows/conditional-execution/condition-basic

Provides shell commands to clone the agno repository, navigate to the conditional execution example directory, set up a Python virtual environment, and execute the workflow script. This demonstrates the complete setup process for running the conditional workflow example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/02_conditional_execution

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python condition_basic.py
```

--------------------------------

### Setup and Run Agno Human-in-the-Loop Example (Bash)

Source: https://docs.agno.com/examples/agents/human-in-the-loop/agentic-user-input

This Bash script provides the necessary steps to set up the Agno repository, navigate to the specific human-in-the-loop example directory, create and activate a Python virtual environment, and then execute the Python agent script. This allows users to quickly get the example running and interact with the agent.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/10_human_in_the_loop

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agentic_user_input.py
```

--------------------------------

### Setup and Run Together Tool Use Example

Source: https://docs.agno.com/examples/models/together/tool-use

Shell commands to clone the Agno repository, navigate to the Together model cookbook, set up a virtual environment, and execute the tool use script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/together

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Agno Workflow Example with Bash

Source: https://docs.agno.com/examples/components/workflows/save-router-steps

This Bash script provides instructions to clone the Agno repository, navigate to a specific example directory, set up a Python virtual environment using a provided script, activate it, and then execute a Python script that demonstrates workflow operations. It outlines the necessary steps to get the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/93_components/workflows

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python save_router_steps.py
```

--------------------------------

### Setup and Run Aimlapi Image Agent Example

Source: https://docs.agno.com/examples/models/aimlapi/image-agent-bytes

Bash script commands to clone the Agno repository, navigate to the Aimlapi cookbook example directory, create a virtual environment, and execute the image agent script. This provides a complete setup workflow for running the image analysis example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/aimlapi

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent_bytes.py
```

--------------------------------

### Setup and Run Llama Async Knowledge Example

Source: https://docs.agno.com/examples/models/meta/llama/async-knowledge

Shell commands to clone the Agno repository, set up the virtual environment, start a PgVector instance via Docker, and execute the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python async_knowledge.py
```

--------------------------------

### Setup and Run Azure OpenAI Database Example

Source: https://docs.agno.com/examples/models/azure/openai/db

Commands to clone the Agno repository, set up a virtual environment using a helper script, and execute the database example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure/openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run PPTX Reader Example

Source: https://docs.agno.com/examples/knowledge/readers/pptx-reader-async

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the PPTX reader async example. Includes all necessary setup steps for a complete working environment.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python pptx_reader_async.py
```

--------------------------------

### Setup and Run Agno File Search Example

Source: https://docs.agno.com/examples/models/google/gemini/file-search-advanced

Bash script commands to clone the Agno repository, navigate to the file search example directory, create a virtual environment, and execute the file search advanced example. Includes repository setup and environment activation steps.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python file_search_advanced.py
```

--------------------------------

### Setup and Run Learning Machine Example with Bash

Source: https://docs.agno.com/examples/teams/memory/learning-machine

Provides shell commands to clone the Agno repository, navigate to the learning machine example directory, set up a Python virtual environment, and execute the learning machine demonstration script. Includes repository setup and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python learning_machine.py
```

--------------------------------

### Setup Environment and Run Image Agent Script

Source: https://docs.agno.com/models/providers/native/openai/responses/usage/image-agent-with-memory

These bash commands guide the user through setting up the necessary environment variables, installing dependencies, and executing the Python script for the image agent. It ensures the OPENAI_API_KEY is configured and required libraries are installed before running the agent.

```bash
export OPENAI_API_KEY=xxx
```

```bash
uv pip install -U openai agno
```

```bash
python cookbook/11_models/openai/responses/image_agent_with_memory.py
```

--------------------------------

### Setup and Run Mistral OCR Example - Bash

Source: https://docs.agno.com/examples/models/mistral/image-ocr-with-structured-output

Shell script commands to clone the Agno repository, navigate to the Mistral cookbook directory, set up a Python virtual environment, and execute the image OCR example. Requires git and Python to be installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/mistral

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the example
python image_ocr_with_structured_output.py
```

--------------------------------

### Setup and Run SingleStore Agent Example

Source: https://docs.agno.com/examples/storage/singlestore/singlestore-for-agent

Bash script commands to clone the Agno repository, navigate to the SingleStore example directory, create a virtual environment, and execute the agent script. This demonstrates the complete workflow for running the SingleStore-backed agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/singlestore

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python singlestore_for_agent.py
```

--------------------------------

### Setup and Run Agno Document Chunking Example (Bash)

Source: https://docs.agno.com/examples/knowledge/chunking/document-chunking

This bash script provides the necessary commands to set up and run the Agno document chunking example. It includes steps for cloning the repository, navigating to the example directory, creating and activating a virtual environment, optionally starting PgVector with Docker, and executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/chunking

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python document_chunking.py
```

--------------------------------

### Setup and Run AgentOS RBAC Example

Source: https://docs.agno.com/examples/agent-os/rbac/asymmetric/basic

Bash script commands to clone the AgentOS repository, set up a Python virtual environment, configure JWT signing and verification keys, and run the RBAC example on port 7777. Requires git and Python to be installed.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/rbac/asymmetric

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export JWT_SIGNING_KEY="***"
export JWT_VERIFICATION_KEY="***"

python basic.py
```

--------------------------------

### Setup and Run OpenAI Audio Agent Example

Source: https://docs.agno.com/examples/models/openai/chat/audio-output-agent

Bash script to clone the Agno repository, set up a Python virtual environment, and execute the audio output agent example. Includes all necessary setup steps for running the cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the example
python audio_output_agent.py
```

--------------------------------

### Environment Setup and Execution for Async Agent Example

Source: https://docs.agno.com/models/providers/native/mistral/usage/async-tool-use

These bash commands provide the necessary steps to prepare your environment and run the asynchronous agent example. This includes setting your Mistral API key, installing required Python packages, and executing the main Python script.

```bash
export MISTRAL_API_KEY=xxx
```

```bash
uv pip install -U mistralai agno
```

```bash
python cookbook/11_models/mistral/async_tool_use.py
```

--------------------------------

### Setup and Run Structured Output Example

Source: https://docs.agno.com/models/providers/native/openai/responses/usage/structured-output

These bash commands provide the necessary steps to prepare your environment and execute the Python example. It includes setting your OpenAI API key, installing required Python packages (openai, agno), and running the script to observe the structured output capabilities.

```bash
export OPENAI_API_KEY=xxx
```

```bash
uv pip install -U openai agno
```

```bash
python cookbook/11_models/openai/responses/structured_output.py
```

--------------------------------

### Setup and Run Audio Input Agent Example (Bash)

Source: https://docs.agno.com/examples/models/litellm-openai/audio-input-agent

These bash commands outline the steps to set up the development environment and execute the Python audio input agent example. It involves cloning the 'agno' repository, navigating to the specific example, creating and activating a virtual environment, and running the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_input_agent.py
```

--------------------------------

### Setup and Run MCP Client Example

Source: https://docs.agno.com/examples/tools/mcp/streamable-http-transport/client

Bash script commands to clone the Agno repository, set up a Python virtual environment, and execute the MCP client example. This demonstrates the complete setup process required to run the MCP client code locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/streamable_http_transport

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python client.py
```

--------------------------------

### Setup and Run Example Script

Source: https://docs.agno.com/examples/tools/tool-decorator/async-tool-decorator

Bash commands to clone the Agno repository, navigate to the async tool decorator example directory, set up a Python virtual environment, and execute the async tool decorator script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/tool_decorator

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python async_tool_decorator.py
```

--------------------------------

### Setup and Execution for vLLM Code Generation

Source: https://docs.agno.com/models/providers/local/vllm/usage/code-generation

Commands to install necessary libraries, start the vLLM inference server with specific model parameters, and execute the code generation script.

```bash
uv pip install -U agno openai vllm

vllm serve deepseek-ai/deepseek-coder-6.7b-instruct \
    --dtype float32 \
    --tool-call-parser pythonic

python cookbook/11_models/vllm/code_generation.py
```

--------------------------------

### Setup and Execute Agno GPT-4.1 Reasoning Example in Bash

Source: https://docs.agno.com/examples/reasoning/models/openai/reasoning-model-gpt-4-1

This bash script provides a step-by-step guide to prepare the environment and run the Agno example. It covers cloning the repository, navigating to the specific cookbook directory, setting up a virtual environment, activating it, and finally executing the Python script that demonstrates the GPT-4.1 reasoning model.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/10_reasoning/models/openai\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython reasoning_model_gpt_4_1.py
```

--------------------------------

### Setup and Run Agno PDF Example

Source: https://docs.agno.com/examples/models/openai/chat/pdf-input-local

Clone the Agno repository, navigate to the OpenAI chat cookbook directory, create a Python virtual environment, and execute the PDF input example script. This bash script automates the setup process using provided demo setup scripts.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_local.py
```

--------------------------------

### Setup and Run the RAG Custom Embeddings Example

Source: https://docs.agno.com/examples/agents/knowledge/rag-custom-embeddings

Commands to clone the repository, set up the virtual environment, start the PgVector database via Docker, and execute the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/07_knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python rag_custom_embeddings.py
```

--------------------------------

### Setup Environment and Dependencies for Agno Persistent Sessions

Source: https://docs.agno.com/history/agent/persistent-session-history

Bash commands to install the required Agno and PostgreSQL libraries, set the OpenAI API key, and start the database container.

```bash
uv pip install agno psycopg2-binary
export OPENAI_API_KEY=****
cookbook/run_pgvector.sh
python persistent_session_history.py
```

--------------------------------

### Setup and Run Async Reasoning Example

Source: https://docs.agno.com/examples/reasoning/models/gemini/async-reasoning-stream

Bash script commands to clone the Agno repository, navigate to the reasoning cookbook example, set up a Python virtual environment, and execute the async reasoning stream example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python async_reasoning_stream.py
```

--------------------------------

### Setup and Run Agentic Chunking Example

Source: https://docs.agno.com/examples/knowledge/chunking/agentic-chunking

Instructions to clone the Agno repository, configure the environment, start the PgVector database via Docker, and run the agentic chunking script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/chunking

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python agentic_chunking.py
```

--------------------------------

### Setup and Execution Commands for Sambanova Example

Source: https://docs.agno.com/examples/models/sambanova/basic

Shell commands to clone the Agno repository, initialize the environment using the provided setup script, and execute the Sambanova basic cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/sambanova

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run OpenAI Metrics Example

Source: https://docs.agno.com/examples/models/openai/chat/metrics

Bash script commands to clone the Agno repository, navigate to the cookbook example directory, create a virtual environment, and execute the metrics.py script. Provides the complete setup workflow for running the OpenAI metrics example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python metrics.py
```

--------------------------------

### Setup and Run Perplexity Web Search Example

Source: https://docs.agno.com/examples/models/perplexity/web-search

Bash commands to clone the Agno repository, navigate to the specific cookbook directory, set up a virtual environment, and execute the web search script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/perplexity

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python web_search.py
```

--------------------------------

### Setup and Run the MCP Parallel Agent Example (Bash)

Source: https://docs.agno.com/examples/tools/mcp/parallel

These bash commands provide a step-by-step guide to setting up the project environment and executing the `agno` Parallel MCP agent example. It includes cloning the repository, creating and activating a virtual environment, exporting the necessary `PARALLEL_API_KEY`, and finally running the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export PARALLEL_API_KEY="***"

python parallel.py
```

--------------------------------

### Setup and Run Agno Agent Example

Source: https://docs.agno.com/examples/agent-os/agno-agent

This bash script provides instructions to clone the Agno repository, navigate to the example directory, set up a Python virtual environment, and execute the Agno Agent Python script. It ensures all dependencies are installed and the environment is ready to run the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agno_agent.py
```

--------------------------------

### Setup and Execution for Agno Agent

Source: https://docs.agno.com/examples/models/meta/llama-openai/memory

Bash commands to clone the Agno repository, set up a virtual environment, start the pgvector database container, and run the memory example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python memory.py
```

--------------------------------

### Setup and Run Tavily Example in Bash

Source: https://docs.agno.com/examples/tools/tavily-tools

Clone the Agno repository, set up a virtual environment, and execute the Tavily tools example. This script automates the setup process for running the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tavily_tools.py
```

--------------------------------

### Setup and Run Agno Websearch Example

Source: https://docs.agno.com/examples/tools/websearch-tools

Provides shell commands to clone the Agno repository, navigate to the websearch tools cookbook directory, create a virtual environment, and execute the websearch_tools.py example script. This setup enables users to quickly test websearch functionality locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python websearch_tools.py
```

--------------------------------

### Run Agno SQL Tools Example (Bash)

Source: https://docs.agno.com/examples/tools/sql-tools

This bash script provides instructions to set up the Agno repository, create and activate a virtual environment, and then execute the Python script that demonstrates the SQL tools integration. It's a complete guide to get the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python sql_tools.py
```

--------------------------------

### Setup and Run MCP Toolbox Example

Source: https://docs.agno.com/examples/tools/mcp/mcp-toolbox-demo/agent

Bash script for cloning the Agno repository, setting up a virtual environment, and running the MCP toolbox demo. This provides the complete setup workflow needed to execute the hotel management agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp/mcp_toolbox_demo

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent.py
```

--------------------------------

### Setup and Run Keyword Search Example in Bash

Source: https://docs.agno.com/examples/knowledge/search-type/keyword-search

Provides shell commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector using Docker, and execute the keyword search example script. This setup script automates the environment configuration needed to run the keyword search demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/search_type

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python keyword_search.py
```

--------------------------------

### Setup and Run Redis Example with Docker

Source: https://docs.agno.com/examples/storage/redis/redis-for-team

Bash script commands to clone the repository, set up a Python virtual environment, and run the Redis-backed team example. Includes Docker commands to start a Redis container locally and verify it is running before executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/redis

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Start Redis container
docker run --name my-redis -p 6379:6379 -d redis

# Verify container is running
docker ps

# Run the example
python redis_for_team.py
```

--------------------------------

### Setup and Run Agno Image Transformation Example (Bash)

Source: https://docs.agno.com/multimodal/team/usage/image-to-image-transformation

These bash commands provide the necessary steps to set up the environment and execute the Agno image transformation example. This includes installing the `agno` library, configuring API keys for OpenAI and Fal, and running the Python script.

```bash
uv pip install agno
```

```bash
export OPENAI_API_KEY=****
export FAL_KEY=****
```

```bash
python cookbook/02_examples/teams/multimodal/image_to_image_transformation.py
```

--------------------------------

### Setup and Run OpenAI Audio Input Example

Source: https://docs.agno.com/examples/models/openai/chat/audio-input-local-file-upload

Bash commands to clone the Agno repository, set up the necessary virtual environment, and execute the audio processing cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_input_local_file_upload.py
```

--------------------------------

### Setup and Run Agno OpenAI Chat Example via Bash

Source: https://docs.agno.com/examples/models/openai/chat/db

This Bash script provides a step-by-step guide to run the Agno OpenAI chat example. It includes commands to clone the Agno repository, navigate to the specific example directory, create and activate a Python virtual environment using `scripts/demo_setup.sh`, and finally execute the `db.py` Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run Aimlapi Structured Output Example

Source: https://docs.agno.com/examples/models/aimlapi/structured-output

Bash script commands to clone the Agno repository, navigate to the Aimlapi cookbook example directory, create a virtual environment using the demo setup script, and execute the structured output example. This sets up all dependencies required to run the movie script generation agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/aimlapi

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Agno Scientific Research Example

Source: https://docs.agno.com/examples/reasoning/agents/scientific-research

Bash script commands to clone the Agno repository, navigate to the reasoning agents cookbook, set up a Python virtual environment, and execute the scientific abstract critique example. Requires git and Python 3.x installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python scientific_research.py
```

--------------------------------

### Setup and Run Cohere Tool Use Example in Bash

Source: https://docs.agno.com/examples/models/cohere/tool-use

Provides shell commands to clone the Agno repository, navigate to the Cohere example directory, set up a virtual environment, and execute the tool use example script. This establishes the development environment needed to run the Cohere agent demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cohere

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Anthropic PDF Example

Source: https://docs.agno.com/examples/models/anthropic/pdf-input-url

Bash script commands to clone the Agno repository, navigate to the Anthropic cookbook directory, create a Python virtual environment, and execute the PDF input URL example. Requires git and Python 3.x installed on the system.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_url.py
```

--------------------------------

### Setup and Run AI Agent Research Example (Bash)

Source: https://docs.agno.com/examples/teams/context-compression/tool-call-compression-with-manager

This Bash script provides the necessary steps to clone the Agno repository, navigate to the example directory, set up a virtual environment, and execute the Python script for AI agent research. It ensures all dependencies are correctly installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/context_compression

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_call_compression_with_manager.py
```

--------------------------------

### Setup and Run Agno OpenAI O3 Mini Example

Source: https://docs.agno.com/examples/models/openai/responses/reasoning-o3-mini

This bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a virtual environment, activate it, and finally execute the Python script for the OpenAI O3 Mini example. It covers the necessary steps to run the provided cookbook example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_o3_mini.py
```

--------------------------------

### Setup and Run Multiple Knowledge Instances Example

Source: https://docs.agno.com/examples/knowledge/os/multiple-knowledge-instances

Bash script commands to clone the AgentOS repository, set up a Python virtual environment, optionally run PgVector using Docker, and execute the multiple knowledge instances example. This provides the complete setup workflow for running the cookbook example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/os

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python multiple_knowledge_instances.py
```

--------------------------------

### Setup and Run Agno Website Tools Example

Source: https://docs.agno.com/examples/tools/website-tools-knowledge

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the website tools knowledge example. Includes all necessary setup steps for running the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python website_tools_knowledge.py
```

--------------------------------

### Setup and Run Agno ClickUp Example with Bash

Source: https://docs.agno.com/examples/tools/clickup-tools

This bash script provides instructions to clone the Agno repository, navigate to the ClickUp tools example, set up a virtual environment, and execute the Python script. It ensures all necessary dependencies are installed and the environment is ready to run the Agno agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python clickup_tools.py
```

--------------------------------

### Setup and Run Agno Session Example - Bash

Source: https://docs.agno.com/examples/teams/session/share-session-with-agent

Shell script commands to clone the Agno repository, navigate to the session example directory, create a virtual environment, and execute the session sharing demonstration. Includes all necessary setup steps for running the Python example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/session

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python share_session_with_agent.py
```

--------------------------------

### Setup and Run Jira Integration Example

Source: https://docs.agno.com/examples/tools/jira-tools

Bash script commands to clone the Agno repository, set up a virtual environment, and execute the Jira tools example. This provides a complete setup workflow for running the Jira integration demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python jira_tools.py
```

--------------------------------

### Setup and Run Aimlapi Example in Bash

Source: https://docs.agno.com/examples/models/aimlapi/tool-use

Shell script commands to clone the Agno repository, navigate to the Aimlapi example directory, set up a Python virtual environment, and execute the tool use example. Includes repository setup and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/aimlapi

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Agno Markdown Reader Example (Bash)

Source: https://docs.agno.com/examples/knowledge/readers/markdown-reader-async

This bash script provides a complete guide to set up the development environment and run the Agno Markdown Reader example. It includes commands for cloning the repository, navigating to the example directory, creating and activating a Python virtual environment, optionally running PgVector using Docker, and executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python markdown_reader_async.py
```

--------------------------------

### Setup and Execution for Knowledge Filters

Source: https://docs.agno.com/examples/knowledge/filters/filtering-with-conditions-on-agent

Bash commands to clone the Agno repository, set up the virtual environment, start the PgVector database via Docker, and run the filtering example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python filtering_with_conditions_on_agent.py
```

--------------------------------

### Setup and Run Nvidia Example via Bash

Source: https://docs.agno.com/examples/models/nvidia/basic

Commands to clone the Agno repository, navigate to the Nvidia cookbook directory, set up the virtual environment, and execute the basic model script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/nvidia

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Run Qdrant Hybrid Search Example

Source: https://docs.agno.com/examples/knowledge/vector-db/qdrant-db/qdrant-db-hybrid-search

These bash commands provide step-by-step instructions to set up and run the Qdrant hybrid search demonstration. It guides users through cloning the Agno repository, navigating to the specific example directory, creating and activating a virtual environment, and finally executing the Python script to start the interactive agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/qdrant_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python qdrant_db_hybrid_search.py
```

--------------------------------

### Setup and Run GibsonAI MCP Server Example (Bash)

Source: https://docs.agno.com/examples/tools/mcp/gibsonai

This set of bash commands outlines the complete process for setting up and running the GibsonAI MCP server example. It covers cloning the Agno repository, creating and activating a Python virtual environment, exporting the OPENAI_API_KEY, and finally executing the Python agent script. This allows users to quickly get the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export OPENAI_API_KEY="***"

python gibsonai.py
```

--------------------------------

### Setup and Run Huggingface Llama Essay Writer Example

Source: https://docs.agno.com/examples/models/huggingface/llama-essay-writer

Shell script commands to clone the Agno repository, navigate to the Huggingface cookbook example directory, create a virtual environment, and execute the essay writer script. Requires git and Python to be installed on the system.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/huggingface
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python llama_essay_writer.py
```

--------------------------------

### Setup and Run Brave Agent Example via Bash

Source: https://docs.agno.com/examples/tools/mcp/brave

This bash script provides instructions to clone the 'agno' repository, navigate to the example directory, set up a Python virtual environment, export the 'BRAVE_API_KEY', and execute the 'brave.py' script. It ensures all dependencies are installed and the environment is correctly configured for running the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export BRAVE_API_KEY="***"

python brave.py
```

--------------------------------

### Setup and Run Reasoning Stream Example

Source: https://docs.agno.com/examples/reasoning/models/azure-openai/basic-reasoning-stream

Bash script to clone the Agno repository, navigate to the Azure OpenAI reasoning cookbook example, set up a Python virtual environment, and execute the basic reasoning stream demonstration. This automates the environment setup and runs the Python example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/azure_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_reasoning_stream.py
```

--------------------------------

### Setup and Run Zep Tools Example

Source: https://docs.agno.com/examples/tools/zep-tools

Bash commands to clone the Agno repository, configure the environment, and execute the Zep tools cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python zep_tools.py
```

--------------------------------

### Setup and Run LiteLLM PDF Example

Source: https://docs.agno.com/examples/models/litellm/pdf-input-bytes

Bash script commands to clone the Agno repository, navigate to the LiteLLM cookbook directory, set up a Python virtual environment, and execute the PDF input bytes example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_bytes.py
```

--------------------------------

### Setup and Run Jina Reader Example

Source: https://docs.agno.com/examples/tools/jinareader-tools

Bash commands to clone the Agno repository, set up the required virtual environment using the provided demo script, and execute the Jina Reader tool example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python jinareader_tools.py
```

--------------------------------

### Setup and Run Agno Agent for Streaming

Source: https://docs.agno.com/models/providers/native/openai/responses/usage/basic-stream

These shell commands guide the user through setting the OpenAI API key, installing the necessary dependencies (openai and agno), and executing the Python script.

```bash
export OPENAI_API_KEY=xxx
uv pip install -U openai agno
python cookbook/11_models/openai/responses/basic_stream.py
```

--------------------------------

### Setup and Run Agno Agent with Memory Example

Source: https://docs.agno.com/examples/basics/agent-with-memory

This bash script provides the necessary commands to clone the Agno repository, navigate to the quickstart example, set up a Python virtual environment, activate it, and execute the `agent_with_memory.py` script. This demonstrates how to run an Agno agent configured with memory capabilities.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_memory.py
```

--------------------------------

### Complete Async Main Function with MCP Setup

Source: https://docs.agno.com/examples/tools/mcp/dynamic-headers/client

Full example showing the complete workflow: importing required modules, defining a header_provider, creating MCPTools with the provider, connecting to MCP server, creating agents, running agents with different user contexts, and cleaning up resources. Demonstrates multi-user and multi-tenant scenarios with dynamic header injection.

```python
import asyncio
from typing import TYPE_CHECKING, Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.run import RunContext
from agno.tools.mcp import MCPTools

if TYPE_CHECKING:
    from agno.agent import Agent
    from agno.team import Team

async def main():
    """Example showing dynamic headers with different users."""

    # Define header provider
    def header_provider(
        run_context: RunContext,
        agent: Optional["Agent"] = None,
        team: Optional["Team"] = None,
    ) -> dict:
        headers = {
            "X-User-ID": run_context.user_id or "unknown",
            "X-Session-ID": run_context.session_id or "unknown",
            "X-Run-ID": run_context.run_id,
            "X-Tenant-ID": run_context.metadata.get("tenant_id", "no-tenant")
            if run_context.metadata
            else "no-tenant",
            "X-Agent-Name": agent.name
            if agent
            else team.name
            if team
            else "unnamed-agno-entity",
        }
        return headers

    # Create MCPTools with header_provider
    mcp_tools = MCPTools(
        url="http://localhost:8000/mcp",
        transport="streamable-http",
        header_provider=header_provider,
    )

    await mcp_tools.connect()
    print("Connected to MCP server")

    try:
        # Create and run agents
        agent_1 = Agent(
            name="agent-1",
            model=OpenAIChat(id="gpt-5.2"),
            tools=[mcp_tools],
            markdown=False,
        )

        response1 = await agent_1.arun(
            "Please use the greet tool to greet me. My name is neel.",
            user_id="neel",
            session_id="session-1",
            metadata={"tenant_id": "tenant-1"},
        )
        print(f"Response: {response1.content}\n")

    finally:
        await mcp_tools.close()
        print("Connection closed")

if __name__ == "__main__":
    asyncio.run(main())
```

--------------------------------

### Setup and Run Seltz Example

Source: https://docs.agno.com/examples/tools/seltz-tools

This bash script outlines the steps to clone the Agno repository, navigate to the Seltz example directory, set up a virtual environment, activate it, and then execute the Python script demonstrating SeltzTools. It's a common setup for running Agno cookbook examples.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python seltz_tools.py
```

--------------------------------

### Setup and Run Distributed Search Example in Bash

Source: https://docs.agno.com/examples/teams/search-coordination/distributed-infinity-search

Commands to clone the Agno repository, navigate to the search coordination cookbook, set up the virtual environment, and execute the demonstration script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/search_coordination
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python 03_distributed_infinity_search.py
```

--------------------------------

### Setup and Run the Personalized Memory Agent

Source: https://docs.agno.com/examples/models/perplexity/memory

Bash commands to clone the Agno repository, configure the environment, start the required pgvector Docker container, and execute the memory agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/perplexity

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python memory.py
```

--------------------------------

### Setup and Run Agno Team Memory Example with Bash

Source: https://docs.agno.com/memory/team/team-with-memory-manager

These bash commands provide the necessary steps to set up the environment and execute the Agno team memory example. It covers installing Python dependencies, configuring the OpenAI API key, and running the main Python script.

```bash
uv pip install -U agno openai psycopg sqlalchemy
```

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

```bash
python team_with_memory_manager.py
```

--------------------------------

### Setup and Run Together Embedder Example

Source: https://docs.agno.com/examples/knowledge/embedders/together-embedder

Commands to clone the Agno repository, set up a virtual environment, start a PgVector instance via Docker, and execute the Together Embedder demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python together_embedder.py
```

--------------------------------

### Setup and Run Image Generation Agent Example

Source: https://docs.agno.com/examples/models/openai/responses/image-generation-agent

Bash script commands to clone the Agno repository, set up a virtual environment, and execute the image generation agent example. This demonstrates the complete setup process from repository cloning through agent execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_generation_agent.py
```

--------------------------------

### Setup and Execute Agno Knowledge Filtering Example

Source: https://docs.agno.com/examples/knowledge/filters/filtering-on-load

Commands to prepare the environment, including cloning the repository, setting up a virtual environment, and running the necessary infrastructure via Docker.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python filtering_on_load.py
```

--------------------------------

### Setup Environment and Run Agno PowerPoint Agent Example (Bash)

Source: https://docs.agno.com/examples/models/anthropic/skills/agent-with-powerpoint

This Bash script provides instructions for setting up the development environment, including cloning the Agno repository, navigating to the example directory, creating a virtual environment, and installing dependencies. It then shows how to export the ANTHROPIC_API_KEY and execute the Python script that creates a PowerPoint presentation using the Agno agent.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/anthropic/skills\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\n# Export relevant API keys\nexport ANTHROPIC_API_KEY=\"***\"\n\npython agent_with_powerpoint.py
```

--------------------------------

### Setup and Run Nebius Cookbook Example via Bash

Source: https://docs.agno.com/examples/models/nebius/basic

Commands to clone the Agno repository, navigate to the specific Nebius model directory, and initialize the environment using the provided setup scripts before running the Python example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/nebius

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Reasoning Example with Bash

Source: https://docs.agno.com/examples/reasoning/models/gemini/basic-reasoning

Provides shell commands to clone the Agno repository, navigate to the reasoning cookbook example, set up a Python virtual environment, and execute the basic reasoning demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_reasoning.py
```

--------------------------------

### Setup and Run Recursive Chunking Example

Source: https://docs.agno.com/examples/knowledge/chunking/recursive-chunking

Shell commands to clone the Agno repository, set up the environment, start the PgVector database via Docker, and execute the recursive chunking script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/chunking

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python recursive_chunking.py
```

--------------------------------

### Setup and Run Audio Agent Example

Source: https://docs.agno.com/examples/models/litellm/audio-input-agent

Bash script commands to clone the Agno repository, navigate to the litellm cookbook directory, set up a Python virtual environment, and execute the audio input agent example. Includes repository cloning, environment activation, and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_input_agent.py
```

--------------------------------

### Setup and Run Claude Tool Use Example

Source: https://docs.agno.com/examples/models/aws/claude/tool-use

Bash script commands to clone the Agno repository, navigate to the Claude AWS example directory, create a virtual environment, and execute the tool use demonstration. Requires git and Python with uv package manager installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/aws/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Chroma DB Hybrid Search Example

Source: https://docs.agno.com/examples/knowledge/vector-db/chroma-db/chroma-db-hybrid-search

Bash script sequence for cloning the Agno repository, navigating to the Chroma DB hybrid search example, setting up a Python virtual environment, and executing the hybrid search demonstration. Requires git and Python to be installed.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/chroma_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python chroma_db_hybrid_search.py
```

--------------------------------

### Setup and Run Dual Inheritance Example

Source: https://docs.agno.com/examples/tools/other/stop-after-tool-call-dual-inheritance

Bash script commands to clone the agno repository, set up a virtual environment, and execute the dual inheritance toolkit example. This demonstrates the complete workflow from repository setup through running the demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/other

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python stop_after_tool_call_dual_inheritance.py
```

--------------------------------

### Setup and Run Groq Reasoning Agent Example

Source: https://docs.agno.com/examples/models/groq/reasoning-agent

Bash script to clone the Agno repository, set up a Python virtual environment, and execute the reasoning agent cookbook example. This demonstrates the complete workflow from environment setup to running the agent.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_agent.py
```

--------------------------------

### Setup and Run Output Model Example in Bash

Source: https://docs.agno.com/examples/agents/input-output/output-model

Commands to clone the Agno repository, configure the environment, and execute the output model demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/02_input_output

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python output_model.py
```

--------------------------------

### Setup and Run LiteLLM Image Agent Example

Source: https://docs.agno.com/examples/models/litellm/image-agent-bytes

Provides the shell commands necessary to clone the repository, prepare the environment, and run the image agent bytes example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent_bytes.py
```

--------------------------------

### Setup and Run Azure Basic Agno Example (Bash)

Source: https://docs.agno.com/examples/models/azure/ai-foundry/basic

This Bash snippet provides the necessary commands to set up the development environment and run the Azure Basic Agno example. It includes steps for cloning the repository, navigating to the example directory, creating and activating a Python virtual environment, and executing the Python script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/azure/ai_foundry\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython basic.py
```

--------------------------------

### Setup and Run vLLM Server Environment

Source: https://docs.agno.com/models/providers/local/vllm/usage/basic-stream

Bash commands to install the necessary Agno and vLLM libraries, start the vLLM inference server with specific hardware optimizations, and run the agent script.

```bash
uv pip install -U agno openai vllm
```

```bash
vllm serve Qwen/Qwen2.5-7B-Instruct \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --dtype float16 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.9
```

```bash
python cookbook/11_models/vllm/basic_stream.py
```

--------------------------------

### Setup and Run DynamoDB Agent Example in Bash

Source: https://docs.agno.com/examples/storage/dynamodb/dynamo-for-agent

Provides shell commands to clone the Agno repository, navigate to the DynamoDB example directory, create a virtual environment, and execute the agent script. This setup script automates the environment configuration needed to run the DynamoDB agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/dynamodb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dynamo_for_agent.py
```

--------------------------------

### Setup and Run Agno Task Mode Example - Bash

Source: https://docs.agno.com/examples/teams/task-mode/basic-task-mode

Provides shell commands to clone the Agno repository, navigate to the task mode example directory, set up a Python virtual environment using the demo setup script, activate the environment, and execute the basic task mode example. This is the complete setup workflow for running the multi-agent team demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/task_mode

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_basic_task_mode.py
```

--------------------------------

### Setup and Run Structured Input Example

Source: https://docs.agno.com/examples/workflows/advanced-concepts/structured-io/input-schema

Bash commands to clone the Agno repository, set up the virtual environment, and run the input schema demonstration script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/structured_io

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python input_schema.py
```

--------------------------------

### Setup and Run Exa Tools Example - Bash

Source: https://docs.agno.com/examples/tools/exa-tools

Shell script commands to clone the Agno repository, navigate to the tools cookbook directory, create a Python virtual environment, and execute the Exa tools example. This provides a complete setup workflow for running the Exa integration demonstration.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python exa_tools.py
```

--------------------------------

### Execute Vertex AI Credentials Cookbook Example

Source: https://docs.agno.com/examples/models/google/gemini/vertexai-with-credentials

Bash commands to clone the Agno repository, initialize the virtual environment using the provided setup script, and run the credentials example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python vertexai_with_credentials.py
```

--------------------------------

### Setup and Run Ollama Qwen Demo

Source: https://docs.agno.com/examples/models/ollama/chat/demo-qwen

Shell commands to clone the Agno repository, navigate to the cookbook directory, prepare the environment using a setup script, and execute the Python demo.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python demo_qwen.py
```

--------------------------------

### Setup and Execute Agno Discord Agent Example

Source: https://docs.agno.com/examples/integrations/discord/basic

These bash commands guide users through cloning the Agno repository, navigating to the specific Discord integration example, and setting up a Python virtual environment. Finally, it demonstrates how to activate the environment and run the basic.py script to launch the Discord bot.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/92_integrations/discord\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython basic.py
```

--------------------------------

### Setup and Run Fireworks Embedder Example

Source: https://docs.agno.com/examples/knowledge/embedders/fireworks-embedder

Bash commands to clone the repository, set up the virtual environment, start a PgVector instance using Docker, and execute the Fireworks embedder script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python fireworks_embedder.py
```

--------------------------------

### Setup and Run Gemini Image Generation Example

Source: https://docs.agno.com/examples/tools/models/gemini-image-generation

Shell commands to clone the Agno repository, initialize the environment using a setup script, and execute the Gemini image generation example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/models

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python gemini_image_generation.py
```

--------------------------------

### Setup and Run Agno Tavily Reader Async Example with Bash

Source: https://docs.agno.com/examples/knowledge/readers/tavily-reader-async

This Bash script provides the necessary commands to set up the development environment for the Agno Tavily Reader example. It includes cloning the repository, navigating to the example directory, creating and activating a Python virtual environment, and optionally starting a PgVector instance using Docker before executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python tavily_reader_async.py
```

--------------------------------

### Environment Setup and Execution for File Generation Tools

Source: https://docs.agno.com/examples/tools/file-generation-tools

Step-by-step CLI instructions to clone the Agno repository, initialize the virtual environment, and run the file generation cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python file_generation_tools.py
```

--------------------------------

### Setup and Run Agno Claude Tool Use Example

Source: https://docs.agno.com/examples/models/vertexai/claude/tool-use

This bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a virtual environment, and execute the Python tool use script. It ensures all dependencies are installed and the environment is correctly configured.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Async HITL Example

Source: https://docs.agno.com/examples/teams/human-in-the-loop/confirmation-required-async-stream

Shell commands to clone the Agno repository, set up the necessary virtual environment, and execute the async streaming confirmation script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/03_teams/human_in_the_loop\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython confirmation_required_async_stream.py
```

--------------------------------

### Setup and Run Vercel Basic Cookbook Example

Source: https://docs.agno.com/examples/models/vercel/basic

Shell commands to clone the Agno repository, set up the virtual environment, and execute the Vercel basic example script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vercel

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Knowledge Tool Team Example

Source: https://docs.agno.com/examples/reasoning/teams/knowledge-tool-team

Bash script to clone the Agno repository, navigate to the reasoning teams cookbook directory, create a virtual environment, and execute the knowledge tool team example. This demonstrates the complete setup workflow for running the multi-agent team demonstration.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/teams

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python knowledge_tool_team.py
```

--------------------------------

### Setup and Execution Commands for SQLite Team Example

Source: https://docs.agno.com/examples/storage/sqlite/sqlite-for-team

Bash commands to clone the Agno repository, prepare the environment using the provided setup script, and run the SQLite team storage example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/sqlite

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the example
python sqlite_for_team.py
```

--------------------------------

### Setup and Run Agno vLLM Memory Example

Source: https://docs.agno.com/examples/models/vllm/memory

This bash script provides a step-by-step guide to set up the Agno repository, create and activate a Python virtual environment, and execute the memory example. It also includes an optional command to run a PgVector container using Docker, which is a prerequisite for the Python script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/vllm\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\n# Optiona: Run PgVector (needs docker)\n./cookbook/scripts/run_pgvector.sh\n\npython memory.py
```

--------------------------------

### Set up and Run Agno BrightData Example in Bash

Source: https://docs.agno.com/examples/tools/brightdata-tools

This bash snippet provides a step-by-step guide to set up and run the Agno BrightData example. It covers cloning the Agno repository, navigating to the relevant cookbook directory, creating and activating a Python virtual environment, and finally executing the `brightdata_tools.py` script to demonstrate the agent's capabilities.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python brightdata_tools.py
```

--------------------------------

### Setup and Run Knowledge Filter Example

Source: https://docs.agno.com/examples/knowledge/filters/filtering-with-conditions-on-team

Bash commands to clone the Agno repository, set up the environment, start a local PgVector instance using Docker, and execute the knowledge filtering script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python filtering_with_conditions_on_team.py
```

--------------------------------

### Setup and Run CEL Workflow Example

Source: https://docs.agno.com/examples/workflows/cel-expressions/loop/cel-content-keyword

Bash script commands to clone the Agno repository, set up a Python virtual environment, and execute the CEL content keyword loop example. This demonstrates the complete setup process for running the workflow demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/07_cel_expressions/loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cel_content_keyword.py
```

--------------------------------

### Setup and Run Traditional RAG Example

Source: https://docs.agno.com/examples/agents/knowledge/traditional-rag

Shell commands to clone the Agno repository, configure the virtual environment, start the required PgVector Docker container, and execute the RAG implementation script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/07_knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python traditional_rag.py
```

--------------------------------

### Setup and Run Callable Tools Example in Bash

Source: https://docs.agno.com/examples/agents/tools/callable-tools

Commands to clone the Agno repository, set up the environment using a demo script, and execute the callable tools example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/04_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_callable_tools.py
```

--------------------------------

### Clone and Setup Agno Repository

Source: https://docs.agno.com/examples/basics/sequential-workflow

Shell script commands to clone the Agno repository, navigate to the quickstart cookbook directory, and set up a Python virtual environment for running examples. This prepares the environment for executing workflow demonstrations.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python sequential_workflow.py
```

--------------------------------

### Setup and Execution Commands for Tool Hooks Example

Source: https://docs.agno.com/examples/tools/tool-hooks/pre-and-post-hooks

Bash commands to clone the Agno repository, configure the environment using the provided setup script, and run the hooks demonstration.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/tool_hooks
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python pre_and_post_hooks.py
```

--------------------------------

### Setup and Run Agno Research Team Example

Source: https://docs.agno.com/examples/teams/context-compression/tool-call-compression

Commands to clone the repository, set up the virtual environment, and execute the tool call compression example script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/context_compression
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python tool_call_compression.py
```

--------------------------------

### Setup and Run Neosantara Tool Use Example

Source: https://docs.agno.com/examples/models/neosantara/tool-use

Bash script commands to clone the Agno repository, navigate to the Neosantara cookbook example directory, set up a Python virtual environment, and execute the tool_use.py script. This provides a complete setup workflow for running the example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/neosantara

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Linkup Example via CLI

Source: https://docs.agno.com/examples/tools/linkup-tools

Commands to clone the Agno repository, set up a virtual environment, and execute the Linkup tools example script. This ensures all dependencies are correctly configured before running the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python linkup_tools.py
```

--------------------------------

### Setup and Run Gemini Example via Bash

Source: https://docs.agno.com/examples/models/google/gemini/gemini-3-pro-thinking-level

Provides the shell commands necessary to clone the Agno repository, configure the virtual environment using a setup script, and run the Gemini thinking level demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python gemini_3_pro_thinking_level.py
```

--------------------------------

### Setup and Run Agno Azure OpenAI Example

Source: https://docs.agno.com/examples/models/azure/openai/tool-use

Bash script commands to clone the Agno repository, navigate to the Azure OpenAI example directory, create a virtual environment, and execute the tool use example. Includes repository setup and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure/openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Cohere Embedder Example (Bash)

Source: https://docs.agno.com/examples/knowledge/embedders/cohere-embedder

This bash script provides the necessary steps to set up the development environment, clone the Agno repository, install dependencies, and execute the Python `cohere_embedder.py` example. It includes an optional step to run `PgVector` using Docker for the database backend.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/07_knowledge/embedders\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\n# Optiona: Run PgVector (needs docker)\n./cookbook/scripts/run_pgvector.sh\n\npython cohere_embedder.py
```

--------------------------------

### Setup and Run OpenAI Embedder Example

Source: https://docs.agno.com/examples/knowledge/embedders/openai-embedder

Bash commands to clone the Agno repository, configure the virtual environment, start a local PgVector instance via Docker, and execute the embedder script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python openai_embedder.py
```

--------------------------------

### Setup and Run Agno Agent Example with Bash

Source: https://docs.agno.com/examples/agents/basics/basic-agent

This snippet provides the necessary bash commands to clone the 'agno' repository, navigate to the example directory, set up a virtual environment, and execute the Python agent script. It covers the environment setup and execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_agent.py
```

--------------------------------

### Setup and Run Stop Agent Example

Source: https://docs.agno.com/examples/tools/exceptions/stop-agent-exception

Bash commands to clone the Agno repository, configure the environment using a setup script, and execute the Stop Agent exception demonstration.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/exceptions

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python stop_agent_exception.py
```

--------------------------------

### Environment Setup and Execution for Agno Knowledge Example

Source: https://docs.agno.com/examples/models/ollama/chat/knowledge

Shell commands to clone the Agno repository, set up the required virtual environment, start a PgVector instance via Docker, and execute the knowledge script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Installation and Setup

Source: https://docs.agno.com/compression/token-counting

Installation instructions for optional tokenizer dependencies to improve local token count accuracy. Includes setup for tiktoken and tokenizers packages.

```APIDOC
## Installation and Setup

### Description
Optional dependencies improve local token count accuracy by using provider-specific tokenizers instead of heuristic estimates.

### Installation Command
```bash
uv pip install -U tiktoken tokenizers
```

### Optional Dependencies

#### tiktoken
- **Purpose**: OpenAI-style tokenization
- **Used When**: Available and model is OpenAI-compatible
- **Accuracy**: Exact tokenization for OpenAI models
- **Installation**: `pip install tiktoken`

#### tokenizers
- **Purpose**: Open-source model tokenization
- **Used When**: Available for the specific model
- **Accuracy**: Exact tokenization for supported open-source models
- **Installation**: `pip install tokenizers`

### Fallback Behavior

If neither tokenizer is available for the given model:
- System falls back to **heuristic estimates**
- Estimates are less accurate but still functional
- Recommended to install tokenizers for better accuracy

### Verification
```python
from agno.models.openai import OpenAI

model = OpenAI(id="gpt-4")

# Check which tokenizer is being used
print(f"Tokenizer: {model.tokenizer_name}")
print(f"Tokenizer available: {model.has_tokenizer}")
```
```

--------------------------------

### Run AgentOS MCP Example Application using Bash

Source: https://docs.agno.com/examples/agent-os/mcp-demo/enable-mcp-example

These bash commands provide a step-by-step guide to clone the agno repository, navigate to the specific mcp_demo example, set up a virtual environment using a provided script, activate it, and finally execute the Python application that enables the MCP server. This allows users to quickly get the example running locally.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/05_agent_os/mcp_demo\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython enable_mcp_example.py
```

--------------------------------

### Setup and Run Audio Multimodal Example

Source: https://docs.agno.com/examples/agents/multimodal/audio-input-output

Bash commands to clone the Agno repository, configure the environment, and execute the audio processing demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/12_multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_input_output.py
```

--------------------------------

### Setup and Run SurrealDB Example Project with Bash

Source: https://docs.agno.com/examples/agent-os/dbs/surreal-db/db

This bash script outlines the steps to set up and run the SurrealDB example. It involves cloning the `agno` repository, navigating to the specific example directory, creating and activating a Python virtual environment, and finally executing the `db.py` script to demonstrate the SurrealDB integration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/dbs/surreal_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run LangDB Web Search Example

Source: https://docs.agno.com/examples/models/langdb/web-search

Provides the shell commands necessary to clone the Agno repository, navigate to the LangDB cookbook directory, set up the virtual environment, and execute the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/langdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python web_search.py
```

--------------------------------

### Setup and Run Async Approval Example

Source: https://docs.agno.com/examples/agents/approvals/approval-async

Commands to clone the Agno repository, configure the environment, and execute the async approval demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/11_approvals

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python approval_async.py
```

--------------------------------

### Setup and Run Schedule Management Example - Bash

Source: https://docs.agno.com/examples/agent-os/scheduler/schedule-management

Shell script commands to clone the Agno repository, set up a virtual environment, and execute the schedule management example. Includes repository cloning, directory navigation, environment setup, and script execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/scheduler

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python schedule_management.py
```

--------------------------------

### Setup and Run Agno Team Example

Source: https://docs.agno.com/examples/agents/tools/team-callable-members

Bash commands to clone the Agno repository, navigate to the cookbook examples, set up a virtual environment, and execute the team callable members example script. This provides a complete setup workflow for running the dynamic team composition demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/04_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 03_team_callable_members.py
```

--------------------------------

### Setup and Run Gemini Thinking Budget Example

Source: https://docs.agno.com/examples/models/google/gemini/agent-with-thinking-budget

Bash script commands to clone the Agno repository, navigate to the Gemini cookbook example directory, set up a Python virtual environment, and execute the thinking budget demonstration script. This automates the environment setup and runs the agent_with_thinking_budget.py example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_thinking_budget.py
```

--------------------------------

### Setup and Execution Environment for Arxiv Reader

Source: https://docs.agno.com/examples/knowledge/readers/arxiv-reader-async

Bash commands to clone the Agno repository, configure the virtual environment, start the PgVector Docker container, and run the asynchronous Arxiv reader example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python arxiv_reader_async.py
```

--------------------------------

### Setup Agno Repository and Run Knowledge Example with PgVector

Source: https://docs.agno.com/examples/models/openai/chat/knowledge

This bash script outlines the steps to prepare the Agno development environment. It includes cloning the repository, navigating to the example directory, creating and activating a Python virtual environment, and optionally starting a PgVector Docker container. Finally, it executes the knowledge.py script to run the Agno agent example, demonstrating the knowledge base integration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run Performance Evaluation Example

Source: https://docs.agno.com/examples/evals/performance/simple-response

Bash script commands to clone the Agno repository, navigate to the performance evaluation cookbook example, create a Python virtual environment, and execute the simple response performance evaluation script. Includes repository setup and environment activation steps.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/09_evals/performance

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python simple_response.py
```

--------------------------------

### Setup and Run Meta Metrics Example

Source: https://docs.agno.com/examples/models/meta/llama-openai/metrics

Bash script for cloning the Agno repository, setting up the development environment, and executing the metrics example. Creates a virtual environment and runs the metrics collection demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python metrics.py
```

--------------------------------

### Setup and Execute SearXNG Example Script

Source: https://docs.agno.com/examples/tools/searxng-tools

Commands to clone the Agno repository, set up the environment, and run the SearXNG tools demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python searxng_tools.py
```

--------------------------------

### Setup and Run MCP Tools Example

Source: https://docs.agno.com/examples/tools/mcp-tools

Bash script to clone the Agno repository, navigate to the tools cookbook directory, create a Python virtual environment, activate it, and execute the MCP tools example. This provides a complete setup workflow for running the MCP integration demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python mcp_tools.py
```

--------------------------------

### Setup and Run Agno Ollama Example

Source: https://docs.agno.com/examples/models/ollama/chat/db

Bash script commands to clone the Agno repository, navigate to the Ollama chat example directory, create a Python virtual environment using the demo setup script, activate it, and execute the agent application.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Run the Team with Custom Tools Script

Source: https://docs.agno.com/tools/usage/team-with-custom-tools

After setting up the environment and installing dependencies, execute this command to run the Python script. This will start the Agno team, which will then process the example question and demonstrate its capabilities.

```bash
python team_with_custom_tools.py
```

--------------------------------

### Bash Commands for AgentOS Example Setup

Source: https://docs.agno.com/examples/agent-os/tracing/tracing-with-multi-db-and-tracing-flag

This bash script outlines the steps to set up and run the AgentOS tracing example. It includes cloning the repository, navigating to the example directory, setting up a virtual environment, and executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/tracing

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 07_tracing_with_multi_db_and_tracing_flag.py

```

--------------------------------

### Setup and Run Early Stop Loop Example in Bash

Source: https://docs.agno.com/examples/workflows/advanced-concepts/early-stopping/early-stop-loop

Provides shell commands to clone the agno repository, navigate to the early_stopping example directory, create and activate a Python virtual environment using the demo setup script, and execute the early_stop_loop.py example to test the workflow's early termination functionality.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/early_stopping

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python early_stop_loop.py
```

--------------------------------

### Setup and Run CSV Row Chunking Example

Source: https://docs.agno.com/examples/knowledge/chunking/csv-row-chunking

Bash script demonstrating the complete setup process for running the CSV row chunking example. Includes repository cloning, virtual environment creation, optional PgVector Docker setup, and script execution for the Agno cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/chunking

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python csv_row_chunking.py
```

--------------------------------

### Setup and Run Fireworks Tool Use Example

Source: https://docs.agno.com/examples/models/fireworks/tool-use

Bash commands to clone the Agno repository, navigate to the relevant cookbook directory, set up the environment, and run the example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/fireworks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Media Pipeline Example

Source: https://docs.agno.com/examples/workflows/conditional-branching/selector-media-pipeline

Commands to clone the Agno repository, set up the necessary virtual environment, and run the conditional branching media pipeline script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/05_conditional_branching

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python selector_media_pipeline.py
```

--------------------------------

### Setup and Run Agno PDF Reader Example (Bash)

Source: https://docs.agno.com/examples/knowledge/readers/pdf-reader-async

These bash commands guide you through cloning the Agno repository, setting up a virtual environment, and optionally running a PgVector database using Docker. Finally, it executes the Python script to demonstrate the asynchronous PDF reader functionality. This is essential for reproducing the example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python pdf_reader_async.py

```

--------------------------------

### Setup and Run Code Generation Example

Source: https://docs.agno.com/examples/models/vllm/code-generation

Provides bash commands to clone the Agno repository, navigate to the vLLM cookbook example, create a Python virtual environment, and execute the code generation script. This setup is required before running the Python agent code.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vllm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python code_generation.py
```

--------------------------------

### Setup and Installation

Source: https://docs.agno.com/tools/toolkits/others/dalle

Prerequisites and setup instructions for using the DALL-E toolkit with Agno. Includes installation of required dependencies and environment configuration.

```APIDOC
## Setup and Installation

### Description
Install required dependencies and configure environment variables to use the DALL-E toolkit with Agno agents.

### Prerequisites

#### Install OpenAI Library
Install the openai library using uv pip:
```bash
uv pip install openai
```

#### Set Environment Variable
Set the OPENAI_API_KEY environment variable with your OpenAI API key:
```bash
export OPENAI_API_KEY=****
```

### Configuration

After installation and environment setup, you can import and use the DALL-E toolkit:

```python
from agno.agent import Agent
from agno.tools.dalle import DalleTools

# Create an Agent with the DALL-E tool
agent = Agent(tools=[DalleTools()], name="DALL-E Image Generator")
```

### Verification

Test your setup by generating a simple image:

```python
agent.print_response(
    "Generate a simple test image",
    markdown=True
)
```
```

--------------------------------

### Setup Environment and Run Excel Reader Demo

Source: https://docs.agno.com/examples/knowledge/readers/excel-reader

Bash commands to clone the Agno repository, set up the required virtual environment, start the PgVector database via Docker, and execute the Excel reader example script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python excel_reader.py
```

--------------------------------

### Setup and Run Agno Hackernews Example (Bash)

Source: https://docs.agno.com/examples/tools/hackernews-tools

This bash script outlines the steps required to set up and run the Agno Hackernews example. It covers cloning the Agno repository, navigating to the specific cookbook directory, creating and activating a Python virtual environment, and finally executing the Python script that utilizes the Hackernews tools. This provides a complete guide for local execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python hackernews_tools.py
```

--------------------------------

### Setup and Run Dynamic Session State Example

Source: https://docs.agno.com/examples/agents/state-and-session/dynamic-session-state

Bash script to clone the Agno repository, navigate to the example directory, set up a Python virtual environment, and execute the dynamic session state demonstration. This script automates the environment setup and runs the Python example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/05_state_and_session

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dynamic_session_state.py
```

--------------------------------

### Setup and Run Entity Memory Example

Source: https://docs.agno.com/examples/learning/entity-memory/facts-and-events

Provides shell commands to clone the Agno repository, navigate to the entity memory example directory, set up a Python virtual environment, and execute the entity memory demonstration script. This is the complete setup workflow for running the facts and events example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/04_entity_memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_facts_and_events.py
```

--------------------------------

### Setup and Run Reasoning Example via CLI

Source: https://docs.agno.com/examples/reasoning/models/vertex-ai/basic-reasoning-stream

Commands to clone the Agno repository, navigate to the specific reasoning model directory, set up the virtual environment, and execute the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/vertex_ai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_reasoning_stream.py
```

--------------------------------

### Setup and Run Image to Audio Example

Source: https://docs.agno.com/examples/agents/multimodal/image-to-audio

Bash commands to clone the Agno repository, set up the required virtual environment, and execute the image-to-audio conversion script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/12_multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_to_audio.py
```

--------------------------------

### Setup and Run DashScope Basic Example (Bash)

Source: https://docs.agno.com/examples/models/dashscope/basic

This bash script provides step-by-step instructions to clone the Agno repository, navigate to the specific DashScope example directory, set up a Python virtual environment, and execute the basic.py script. This allows users to run the demonstrated DashScope integration locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/dashscope

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py

```

--------------------------------

### Setup and Run PgVector Hybrid Search Example

Source: https://docs.agno.com/examples/knowledge/vector-db/pgvector/pgvector-hybrid-search

Shell commands to clone the Agno repository, set up the virtual environment, start a PgVector instance via Docker, and execute the hybrid search script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/pgvector

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python pgvector_hybrid_search.py
```

--------------------------------

### Setup and Run Pipedream MCP Example

Source: https://docs.agno.com/examples/tools/mcp/pipedream-auth

Bash script commands to clone the Agno repository, navigate to the MCP cookbook example, set up a Python virtual environment, and execute the Pipedream authentication example. This demonstrates the complete setup workflow for running the authenticated MCP server example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pipedream_auth.py
```

--------------------------------

### Setup and Execution Commands for O3 Mini Example

Source: https://docs.agno.com/examples/reasoning/models/openai/o3-mini

Bash commands to clone the repository, prepare the environment, and run the O3 Mini reasoning script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python o3_mini.py
```

--------------------------------

### Setup and Run Session State Example via Bash

Source: https://docs.agno.com/examples/tools/other/session-state-tool

Commands to clone the Agno repository, navigate to the relevant cookbook directory, set up the virtual environment, and execute the session state tool demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/other

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python session_state_tool.py
```

--------------------------------

### Setup and Run Reddit Tools Example

Source: https://docs.agno.com/examples/tools/reddit-tools

Bash script to clone the Agno repository, set up a virtual environment, and execute the Reddit tools example. This demonstrates the complete workflow from environment setup to running the agent query.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reddit_tools.py
```

--------------------------------

### Setup and Run Team Learning Example in Bash

Source: https://docs.agno.com/examples/teams/learning/team-always-learn

Clone the agno repository, set up a Python virtual environment, and execute the team learning example. This script automates the environment setup process and runs the demonstration of automatic team learning functionality.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/learning

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_team_always_learn.py
```

--------------------------------

### Setup and Execution Commands for Nebius Embedder

Source: https://docs.agno.com/examples/knowledge/embedders/nebius-embedder

Shell commands to clone the Agno repository, set up the virtual environment, start a local PgVector instance via Docker, and run the embedder example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python nebius_embedder.py
```

--------------------------------

### Setup and Run Agno LangDB Example via Bash

Source: https://docs.agno.com/examples/models/langdb/basic

This bash script provides instructions to clone the `agno` repository, navigate to the `langdb` cookbook directory, set up a virtual environment using `demo_setup.sh`, activate it, and then execute the `basic.py` Python example.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/langdb\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython basic.py
```

--------------------------------

### Setup and Run Gemini Reasoning Tools Example (Bash)

Source: https://docs.agno.com/examples/reasoning/tools/gemini-reasoning-tools

This bash script provides instructions to clone the 'agno-agi/agno' repository, navigate to the example directory, set up a Python virtual environment using 'demo_setup.sh', activate it, and finally execute the 'gemini_reasoning_tools.py' script to run the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python gemini_reasoning_tools.py
```

--------------------------------

### Setup and Run Semantic Chunking Example via Bash

Source: https://docs.agno.com/examples/knowledge/chunking/semantic-chunking

Commands to clone the Agno repository, configure the environment, start the required PgVector database using Docker, and execute the semantic chunking script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/chunking

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python semantic_chunking.py
```

--------------------------------

### Setup and Run Replicate Tools Example

Source: https://docs.agno.com/examples/tools/replicate-tools

Bash script to clone the Agno repository, navigate to the tools cookbook directory, set up a Python virtual environment, and execute the Replicate tools example. This provides a complete setup workflow for running the Replicate integration locally.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python replicate_tools.py
```

--------------------------------

### Setup and Run Agno Function Workflow Example (Bash)

Source: https://docs.agno.com/examples/workflows/basic-workflows/function-workflows/function-workflow

This snippet provides shell commands to set up the Agno repository, navigate to the specific example directory, create and activate a Python virtual environment, and finally execute the 'function_workflow.py' script. This allows users to run the demonstrated workflows locally. Ensure you have Git and Python installed before running these commands.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/01_basic_workflows/03_function_workflows

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python function_workflow.py
```

--------------------------------

### Setup and Run Agentic Session State Example

Source: https://docs.agno.com/examples/agents/state-and-session/agentic-session-state

Bash script commands to clone the Agno repository, navigate to the session state example directory, create a Python virtual environment, and execute the agentic session state demonstration. This setup process initializes the development environment with all necessary dependencies for running the agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/05_state_and_session

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agentic_session_state.py
```

--------------------------------

### Setup and Execution Commands

Source: https://docs.agno.com/examples/teams/knowledge/team-with-knowledge

Shell commands to clone the Agno repository, prepare the environment using the provided setup script, and run the knowledge-based team example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_team_with_knowledge.py
```

--------------------------------

### Setup and Run Groq Reasoning Demo (Bash)

Source: https://docs.agno.com/examples/models/groq/reasoning/demo-deepseek-qwen

This bash script outlines the steps required to set up and execute the Groq reasoning demonstration. It covers cloning the `agno` repository, navigating to the relevant example, creating and activating a Python virtual environment, and finally running the `demo_deepseek_qwen.py` script. An optional command for running PgVector with Docker is also included.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq/reasoning

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python demo_deepseek_qwen.py
```

--------------------------------

### Setup and Run Agentic Learning Example

Source: https://docs.agno.com/examples/learning/quickstart/agentic-learn

Bash commands to clone the Agno repository, set up the environment, and execute the agentic learning demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_agentic_learn.py
```

--------------------------------

### Setup and Run Fireworks Example

Source: https://docs.agno.com/examples/models/fireworks/basic

Bash script commands to clone the Agno repository, navigate to the Fireworks cookbook example directory, create a Python virtual environment, and execute the basic.py example. This provides a complete setup workflow for running the Fireworks agent locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/fireworks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run AgentOS MCP Tools Example in Bash

Source: https://docs.agno.com/examples/agent-os/mcp-demo/mcp-tools-advanced-example

Provides shell commands to clone the Agno repository, set up a Python virtual environment using the demo setup script, configure required API keys as environment variables, and execute the AgentOS application with MCPTools. This script automates the complete setup process for running the example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/mcp_demo

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export BRAVE_API_KEY="***"

python mcp_tools_advanced_example.py
```

--------------------------------

### Setup and Run Xai Basic Example

Source: https://docs.agno.com/examples/models/xai/basic

Bash script to clone the Agno repository, set up a Python virtual environment, and execute the xAI basic example. Includes repository cloning, environment activation, and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/xai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Run InternLM Retry Example Setup

Source: https://docs.agno.com/examples/models/internlm/retry

Bash script commands to clone the Agno repository, navigate to the InternLM example directory, set up a Python virtual environment, and execute the retry example. This demonstrates the complete setup process for running the retry configuration example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/internlm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup Environment and Install Dependencies

Source: https://docs.agno.com/models/providers/native/google/usage/storage

Commands to set the Google API key and install necessary Python packages including google-genai, sqlalchemy, and agno using uv.

```bash
export GOOGLE_API_KEY=xxx
uv pip install -U google-genai sqlalchemy psycopg agno
```

--------------------------------

### Setup and Run Agno Memory Manager Example

Source: https://docs.agno.com/examples/memory/memory-manager/db-tools-control

Shell commands to clone the Agno repository, navigate to the memory manager cookbook, set up the virtual environment, and execute the database tools control demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/11_memory/memory_manager

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 05_db_tools_control.py
```

--------------------------------

### Setup and Run Agno Coordination Example

Source: https://docs.agno.com/examples/teams/basics/basic-coordination

Shell commands to clone the Agno repository, set up the demonstration environment using a setup script, and execute the basic coordination Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_basic_coordination.py
```

--------------------------------

### Setup and Execute CometAPI Cookbook Example

Source: https://docs.agno.com/examples/models/cometapi/tool-use

Bash commands to clone the Agno repository, navigate to the CometAPI cookbook directory, set up the environment, and run the tool use example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cometapi

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Audio Analysis Example

Source: https://docs.agno.com/examples/teams/multimodal/audio-to-text

Shell commands to clone the Agno repository, navigate to the multimodal cookbook directory, initialize the environment, and execute the audio-to-text script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_to_text.py
```

--------------------------------

### Setup and Execute Azure Blob Storage Example

Source: https://docs.agno.com/examples/knowledge/cloud/azure-blob

Bash commands to clone the Agno repository, set up the virtual environment, start a local PgVector instance via Docker, and run the Azure Blob Storage integration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/cloud

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python azure_blob.py
```

--------------------------------

### Setup and Run Cerebras OpenAI Example

Source: https://docs.agno.com/examples/models/cerebras-openai/basic

Bash script commands to clone the Agno repository, navigate to the Cerebras OpenAI cookbook example directory, set up a virtual environment using the demo setup script, and execute the basic.py example. This provides the complete workflow for running the Cerebras OpenAI agent example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cerebras_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Siliconflow Tool Use Example (Bash)

Source: https://docs.agno.com/examples/models/siliconflow/tool-use

This bash script provides instructions to clone the Agno repository, navigate to the Siliconflow example directory, set up a virtual environment using a provided script, activate it, and then execute the Python script demonstrating Siliconflow tool use.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/siliconflow

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Agno Vector Removal Example (Bash)

Source: https://docs.agno.com/examples/knowledge/quickstart/remove-vectors

This bash script outlines the steps to clone the Agno repository, navigate to the example directory, and set up a Python virtual environment. It then provides the command to execute the vector removal Python script, with an optional step to start a PgVector instance via Docker.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 10_remove_vectors.py
```

--------------------------------

### Setup and Run Agno WatsonX Chain-of-Thought Example via Bash

Source: https://docs.agno.com/examples/reasoning/agents/ibm-watsonx-default-cot

These bash commands guide users through cloning the Agno repository, navigating to the specific example directory, and setting up a Python virtual environment. Finally, it executes the ibm_watsonx_default_COT.py script to run the WatsonX chain-of-thought demonstration locally. This ensures all dependencies are met for execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python ibm_watsonx_default_COT.py
```

--------------------------------

### Setup and Run Workflow Example

Source: https://docs.agno.com/examples/agent-os/workflow/workflow-with-custom-function-updating-session-state

Bash script commands to clone the AgentOS repository, navigate to the workflow cookbook example, create a virtual environment, and run the content creation workflow with hot reload enabled.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/workflow

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_with_custom_function_updating_session_state.py
```

--------------------------------

### Setup and Execute Video Input Example

Source: https://docs.agno.com/examples/models/google/gemini/video-input-youtube

Bash commands to clone the Agno repository, set up the virtual environment, and execute the video analysis script for Google Gemini.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python video_input_youtube.py
```

--------------------------------

### Setup and Run Ollama Image Agent Example

Source: https://docs.agno.com/examples/models/ollama/chat/image-agent

Bash script commands to clone the Agno repository, navigate to the Ollama chat cookbook directory, set up a Python virtual environment, and execute the image agent example. This provides the complete setup workflow for running the cookbook example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent.py
```

--------------------------------

### Setup and Run Dynamic Model Router Example in Bash

Source: https://docs.agno.com/examples/models/openrouter/chat/dynamic-model-router

Provides shell commands to clone the Agno repository, navigate to the OpenRouter example directory, set up a Python virtual environment, and execute the dynamic model router example script. This setup ensures all dependencies are properly isolated and the example runs in a clean environment.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openrouter/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dynamic_model_router.py
```

--------------------------------

### Setup and Run SurrealDB Example

Source: https://docs.agno.com/examples/knowledge/vector-db/surrealdb/surreal-db

Bash script for cloning the Agno repository, setting up a Python virtual environment, and executing the SurrealDB vector database example. Includes all necessary setup steps for running the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/surrealdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python surreal_db.py
```

--------------------------------

### Setup and Execute Database Agent Example

Source: https://docs.agno.com/examples/components/get-agent

Bash commands to clone the Agno repository, set up the necessary virtual environment, and run the agent retrieval script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/93_components

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python get_agent.py
```

--------------------------------

### Setup and Run AgentOS Example

Source: https://docs.agno.com/examples/agent-os/customize/custom-health-endpoint

Bash script to clone the agno repository, set up a Python virtual environment, and run the custom health endpoint example. This demonstrates the complete setup process from repository cloning through environment activation to running the application.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/customize

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python custom_health_endpoint.py
```

--------------------------------

### Setup and Execute Agno Custom Workflow Example (Bash)

Source: https://docs.agno.com/examples/components/workflows/save-custom-steps

This bash script provides a step-by-step guide to run the Agno custom workflow example. It includes commands for cloning the Agno repository, navigating to the specific example directory, setting up and activating a Python virtual environment, and finally executing the save_custom_steps.py script. This allows users to quickly replicate the demonstration of saving and loading custom workflow steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/93_components/workflows

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python save_custom_steps.py
```

--------------------------------

### Setup and Run Agno MySQL Team Example

Source: https://docs.agno.com/examples/storage/mysql/mysql-for-team

Shell commands to clone the Agno repository, initialize the environment, and execute the MySQL storage example script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/06_storage/mysql\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython mysql_for_team.py
```

--------------------------------

### Setup and Run Workflow Agent Example

Source: https://docs.agno.com/examples/workflows/advanced-concepts/workflow-agent/basic-workflow-agent

Shell script commands to clone the agno repository, navigate to the workflow example directory, set up a Python virtual environment, and execute the basic workflow agent demonstration. This setup ensures all dependencies are isolated and the example runs in a clean environment.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/workflow_agent

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_workflow_agent.py
```

--------------------------------

### Run Example: Analyze AWS S3 Files with Gemini (Bash)

Source: https://docs.agno.com/examples/models/google/gemini/s3-url-file-input

This Bash snippet provides instructions to set up the Agno repository, create a virtual environment, and execute the Python script for analyzing S3 files with Gemini. It guides users through cloning the repository, navigating to the example directory, and running the necessary setup and Python scripts.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python s3_url_file_input.py
```

--------------------------------

### Setup and Run Agno Approval Example

Source: https://docs.agno.com/examples/agents/approvals/approval-external-execution

Commands to clone the Agno repository and navigate to the directory containing the approval and external execution cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/11_approvals
```

--------------------------------

### AgentOSClient Main Execution and Setup

Source: https://docs.agno.com/examples/agent-os/client/run-agents

Provides the main entry point for running both non-streaming and streaming agent examples. Includes async initialization and orchestration of agent runs. Also includes bash setup commands for cloning the repository, creating a virtual environment, and executing the demonstration script.

```python
async def main():
    await run_agent_non_streaming()
    await run_agent_streaming()


if __name__ == "__main__":
    asyncio.run(main())
```

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/client

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_run_agents.py
```

--------------------------------

### Setup and Run Agno Knowledge Example with Bash

Source: https://docs.agno.com/examples/models/azure/openai/knowledge

This bash script provides instructions to clone the Agno repository, set up a virtual environment, optionally run PgVector using Docker, and then execute the Python knowledge script. It outlines the necessary steps for a complete local setup of the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure/openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run the Xai Structured Output Example

Source: https://docs.agno.com/examples/models/xai/structured-output

These bash commands provide instructions to clone the Agno repository, navigate to the example directory, set up a virtual environment using a provided script, activate it, and then execute the `structured_output.py` Python script to run the structured output agent example.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/xai\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython structured_output.py
```

--------------------------------

### Setup and Run Agno Tools Example

Source: https://docs.agno.com/examples/tools/python-function-as-tool

Bash commands to clone the Agno repository, initialize the demo environment using a setup script, and execute the Python function tool script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python python_function_as_tool.py
```

--------------------------------

### Clone and Setup Agno Cookbook Example

Source: https://docs.agno.com/examples/teams/context-management/few-shot-learning

Commands to clone the Agno repository and navigate to the directory containing the few-shot learning and context management examples.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/context_management
```

--------------------------------

### Setup and Execute OpenWeather Example

Source: https://docs.agno.com/examples/tools/openweather-tools

Shell commands to clone the Agno repository, set up the required virtual environment, and execute the OpenWeather tools demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python openweather_tools.py
```

--------------------------------

### Setup and Run Nvidia Tool Use Example

Source: https://docs.agno.com/examples/models/nvidia/tool-use

Bash commands to clone the Agno repository, set up the environment using a shell script, and execute the Nvidia tool use script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/nvidia

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Agno Llama Basic Example (Bash)

Source: https://docs.agno.com/examples/models/meta/llama/basic

This bash snippet provides instructions for setting up the Agno repository, navigating to the specific example directory, creating and activating a virtual environment, and finally executing the Python script to run the Llama agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Transcription Example via Bash

Source: https://docs.agno.com/examples/models/mistral/image-transcribe-document-agent

Commands to clone the Agno repository, initialize the environment using a setup script, and execute the transcription agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/mistral

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_transcribe_document_agent.py
```

--------------------------------

### Setup and Run Remote ADK Agent Example

Source: https://docs.agno.com/examples/agent-os/remote/remote-adk-agent

Provides bash commands to clone the Agno repository, set up a virtual environment, configure API keys, and execute the remote ADK agent example. This is the complete setup workflow needed to run the Python examples.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/remote

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export GOOGLE_API_KEY="***"

python 04_remote_adk_agent.py
```

--------------------------------

### Setup and Run Agno Groq Streaming Agent (Bash)

Source: https://docs.agno.com/models/providers/gateways/groq/usage/basic-stream

These bash commands guide you through the necessary steps to set up your environment, including exporting your Groq API key, installing required Python dependencies, and finally running the streaming agent script.

```bash
export GROQ_API_KEY=xxx
```

```bash
uv pip install -U groq agno
```

```bash
python cookbook/11_models/groq/basic_stream.py
```

--------------------------------

### Setup and Run Workflow Example

Source: https://docs.agno.com/examples/workflows/advanced-concepts/run-control/metrics

Bash script commands to clone the Agno repository, navigate to the workflow metrics example directory, create a Python virtual environment, and execute the metrics.py script to demonstrate workflow metric collection.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/run_control

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python metrics.py
```

--------------------------------

### Setup and Run OpenCV Tools Demo

Source: https://docs.agno.com/examples/tools/opencv-tools

Bash commands to clone the Agno repository, configure the environment using a setup script, and execute the OpenCV tools example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python opencv_tools.py
```

--------------------------------

### Setup and Run Agno ChromaDB Asynchronous Example

Source: https://docs.agno.com/knowledge/vector-stores/chroma/usage/async-chroma-db

These bash commands provide the necessary steps to set up the environment and execute the Agno ChromaDB asynchronous example. It includes installing required Python packages using "uv pip", setting the "OPENAI_API_KEY" environment variable for API access, and running the main Python script.

```bash
uv pip install -U chromadb pypdf openai agno
```

```bash
export OPENAI_API_KEY=xxx
```

```bash
python cookbook/08_knowledge/vector_db/chroma_db/async_chroma_db.py
```

--------------------------------

### Setup and Run Agno OpenAI Example

Source: https://docs.agno.com/examples/models/openai/chat/basic-stream-metrics

Bash script commands to clone the Agno repository, navigate to the OpenAI chat cookbook directory, create a Python virtual environment using the demo setup script, and execute the basic_stream_metrics.py example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_stream_metrics.py
```

--------------------------------

### Setup and Run CometAPI Basic Example (Bash)

Source: https://docs.agno.com/examples/models/cometapi/basic

This Bash snippet provides a sequence of commands to set up and run the `cometapi/basic.py` example. It covers cloning the `agno` repository, navigating to the correct directory, creating and activating a virtual environment, and executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cometapi

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Agno Agent with CerebrasOpenAI

Source: https://docs.agno.com/models/providers/gateways/cerebras-openai/usage/storage

These commands guide the user through setting up the environment and running the Agno agent. It involves setting an API key, installing necessary Python dependencies, and executing the agent script.

```bash
export CEREBRAS_API_KEY=xxx
```

```bash
uv pip install -U openai sqlalchemy agno
```

```bash
python cookbook/11_models/cerebras_openai/db.py
```

--------------------------------

### Setup and Run AgentOS Example with Bash

Source: https://docs.agno.com/examples/agent-os/background-tasks/background-evals-example

Provides shell commands to clone the agno repository, set up a Python virtual environment, and run the background evaluation example. The demo_setup.sh script automates environment configuration, and the example runs on port 7777 with hot-reload enabled.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/background_tasks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python background_evals_example.py
```

--------------------------------

### Run Agno Learning Shorthand Example (Bash)

Source: https://docs.agno.com/examples/learning/quick-tests/learning-true-shorthand

This snippet provides the necessary bash commands to set up the Agno repository, create and activate a virtual environment, and then execute the Python script that demonstrates the `learning=True` shorthand. It includes commands for cloning the repository, navigating to the example directory, and running a setup script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/06_quick_tests

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_learning_true_shorthand.py
```

--------------------------------

### Setup and Run Vertex AI PDF Bytes Example

Source: https://docs.agno.com/examples/models/vertexai/claude/pdf-input-bytes

Shell commands to clone the Agno repository, configure the virtual environment, and execute the PDF input bytes cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_bytes.py
```

--------------------------------

### Setup and Execute Agno A2A Server Example

Source: https://docs.agno.com/examples/integrations/a2a/basic-agent/--main--

Shell commands to clone the Agno repository, prepare the virtual environment using a setup script, and launch the A2A server.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/a2a/basic_agent

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python __main__.py
```

--------------------------------

### Running the Agent-as-Judge Example

Source: https://docs.agno.com/examples/evals/agent-as-judge/agent-as-judge-with-tools

Provides setup and execution instructions for running the tool-using agent-as-judge evaluation example. Includes repository cloning, environment setup, and script execution commands.

```APIDOC
## Setup and Execution

### Description
Instructions for cloning the Agno repository, setting up the development environment, and executing the agent-as-judge evaluation example.

### Prerequisites
- Git installed
- Python 3.8 or higher
- Virtual environment support

### Setup Steps

#### Step 1: Clone Repository
```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/09_evals/agent_as_judge
```

#### Step 2: Create Virtual Environment
```bash
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
```

#### Step 3: Run Evaluation
```bash
python agent_as_judge_with_tools.py
```

### Expected Output
- Agent processes the input query using available tools
- Judge model evaluates the agent's response
- Evaluation results printed to console including score and reasoning
- Assertion validates that evaluation returned a result

### Configuration
- **Repository**: https://github.com/agno-agi/agno.git
- **Example Path**: cookbook/09_evals/agent_as_judge
- **Script Name**: agent_as_judge_with_tools.py
- **Virtual Environment**: .venvs/demo
```

--------------------------------

### Setup and Run Audio Input Agent

Source: https://docs.agno.com/models/providers/native/openai/completion/usage/audio-input-agent

These bash commands guide the user through setting up the environment and running the Python script. It includes setting the OpenAI API key, installing necessary Python dependencies, and executing the main agent script.

```bash
export OPENAI_API_KEY=xxx
```

```bash
uv pip install -U openai requests agno
```

```bash
python cookbook/11_models/openai/chat/audio_input_agent.py
```

--------------------------------

### Setup and Run Coordinate Mode Example in Bash

Source: https://docs.agno.com/examples/teams/modes/coordinate/with-tools

Commands to clone the Agno repository, set up the virtual environment, and execute the coordinate mode example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/modes/coordinate

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_with_tools.py
```

--------------------------------

### Setup and Run Context Management Example

Source: https://docs.agno.com/examples/models/anthropic/context-management

Bash commands to clone the Agno repository, set up the environment, export the necessary Anthropic API key, and execute the context management cookbook script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export ANTHROPIC_API_KEY="***"

python context_management.py
```

--------------------------------

### Setup and Run ModelsLabTools Example

Source: https://docs.agno.com/examples/tools/models-lab-tools

Bash commands to clone the Agno repository, set up the required virtual environment using a demo script, and execute the ModelsLab tools example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python models_lab_tools.py
```

--------------------------------

### Setup and Run Finance Agent Example

Source: https://docs.agno.com/examples/reasoning/agents/finance-agent

Provides shell commands to clone the Agno repository, navigate to the reasoning agents cookbook, set up a Python virtual environment, and execute the finance agent example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python finance_agent.py
```

--------------------------------

### Setup and Run Human-in-the-Loop Example

Source: https://docs.agno.com/examples/agents/human-in-the-loop/user-input-required

This bash script outlines the steps to set up and run the Agno human-in-the-loop example. It includes cloning the Agno repository, navigating to the specific example directory, creating and activating a Python virtual environment using a setup script, and finally executing the 'user_input_required.py' script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/10_human_in_the_loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python user_input_required.py
```

--------------------------------

### Setup and Run OpenAI PDF Input Example

Source: https://docs.agno.com/examples/models/openai/responses/pdf-input-url

Bash commands to clone the Agno repository, set up the virtual environment, and execute the PDF input URL cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_url.py
```

--------------------------------

### Setup and Run Workflow Serialization Example

Source: https://docs.agno.com/examples/workflows/advanced-concepts/run-control/workflow-serialization

Bash script to clone the Agno repository, set up a Python virtual environment, and execute the workflow serialization example. Includes repository setup and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/run_control

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_serialization.py
```

--------------------------------

### Setup and Run Agno GeminiTools Example

Source: https://docs.agno.com/examples/models/google/gemini/imagen-tool-advanced

Bash script commands to clone the Agno repository, navigate to the GeminiTools example directory, set up a Python virtual environment, and execute the image generation example. This automates the environment setup and activates the demo virtual environment before running the Python script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python imagen_tool_advanced.py
```

--------------------------------

### Setup and Run Llama Agent Example

Source: https://docs.agno.com/examples/models/meta/llama/db

Bash script to clone the agno repository, set up a Python virtual environment, and run the Llama DB example. Executes the demo setup script and activates the virtual environment before running the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Execute Background Hooks Workflow

Source: https://docs.agno.com/examples/agent-os/background-tasks/background-hooks-workflow

Command line instructions to clone the repository, set up the virtual environment using the provided setup script, and run the background hooks workflow example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/background_tasks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python background_hooks_workflow.py
```

--------------------------------

### Setup and Run Agno PPTX Reader Example (Bash)

Source: https://docs.agno.com/examples/knowledge/readers/pptx-reader

These bash commands provide instructions for setting up the development environment and running the Agno PPTX reader example. It covers cloning the Agno repository, navigating to the relevant example directory, creating and activating a Python virtual environment, and optionally running a PgVector database using Docker before executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python pptx_reader.py
```

--------------------------------

### Setup and Execution Commands

Source: https://docs.agno.com/examples/tools/mcp/filesystem

Bash commands for cloning the Agno repository, setting up the environment, and running the filesystem agent example.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/91_tools/mcp\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython filesystem.py
```

--------------------------------

### Setup and Run Maxim Integration Example

Source: https://docs.agno.com/examples/integrations/observability/maxim-ops

Bash script to clone the Agno repository, navigate to the observability integration example, set up a Python virtual environment, and execute the Maxim integration demo. This prepares the environment with all necessary dependencies.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/observability

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python maxim_ops.py
```

--------------------------------

### Run LiteLLM Tool Use Cookbook Example

Source: https://docs.agno.com/examples/models/litellm/tool-use

Bash commands to clone the repository, set up the environment using a demo script, and execute the tool use example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Siliconflow Example with Bash

Source: https://docs.agno.com/examples/models/siliconflow/basic

Shell script commands to clone the Agno repository, navigate to the Siliconflow cookbook example directory, create a virtual environment, and execute the basic.py example script. This sets up all dependencies required to run the Siliconflow agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/siliconflow

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run PDF Reader Example with Bash

Source: https://docs.agno.com/examples/knowledge/readers/pdf-reader-url-password

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector using Docker, and execute the PDF reader example. This demonstrates the complete setup process for running the password-protected PDF reader example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python pdf_reader_url_password.py
```

--------------------------------

### Setup and Run AgentOSClient Example in Bash

Source: https://docs.agno.com/examples/agent-os/client/run-teams

Shell commands to clone the Agno repository, navigate to the client cookbook directory, set up the demo environment, and execute the team run script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/client

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 06_run_teams.py
```

--------------------------------

### Setup and Run OpenBB Tools Example - Bash

Source: https://docs.agno.com/examples/tools/openbb-tools

Shell script commands to clone the Agno repository, set up a virtual environment, and execute the OpenBB tools example. Includes repository cloning, directory navigation, environment setup, and Python script execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python openbb_tools.py
```

--------------------------------

### Setup and Run AGNO Learned Knowledge Example

Source: https://docs.agno.com/examples/learning/quickstart/learned-knowledge

This bash script provides instructions to clone the AGNO repository, navigate to the specific cookbook example, set up a virtual environment using a provided script, activate it, and then execute the Python demonstration script for learned knowledge.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 03_learned_knowledge.py

```

--------------------------------

### Setup and Run Agno Team Example

Source: https://docs.agno.com/examples/teams/basics/respond-directly-with-history

Commands to clone the Agno repository, set up a virtual environment, and execute the direct response history example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 04_respond_directly_with_history.py
```

--------------------------------

### Setup and Run Llama Cpp Tool Use Example

Source: https://docs.agno.com/examples/models/llama-cpp/tool-use

Provides the shell commands necessary to clone the repository, set up the environment, and execute the tool use script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/llama_cpp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Agno Agent with Perplexity

Source: https://docs.agno.com/models/providers/native/perplexity/usage/knowledge

These commands guide you through the necessary steps to prepare your environment and execute the Agno agent script. It includes setting your Perplexity API key, installing required Python packages, and running the main agent script.

```bash
export PERPLEXITY_API_KEY=xxx
```

```bash
uv pip install -U agno openai sqlalchemy pgvector pypdf
```

```bash
python cookbook/11_models/perplexity/knowledge.py
```

--------------------------------

### Install Dependencies for Milvus Agno Example (Bash)

Source: https://docs.agno.com/knowledge/vector-stores/milvus/usage/async-milvus-db-hybrid-search

This command installs the necessary Python packages, including pymilvus, pypdf, openai, and agno, required to run the asynchronous Milvus hybrid search example. It uses 'uv pip install -U' for efficient installation and upgrades.

```bash
uv pip install -U pymilvus pypdf openai agno
```

--------------------------------

### Run Agno Anthropic Timeout Example (Bash)

Source: https://docs.agno.com/examples/models/anthropic/basic-with-timeout

This bash script provides instructions to set up the development environment and execute the Python example. It involves cloning the Agno repository, navigating to the specific cookbook directory, setting up a Python virtual environment using 'demo_setup.sh', activating it, and finally running the 'basic_with_timeout.py' script. This setup ensures all necessary dependencies are installed.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_with_timeout.py
```

--------------------------------

### Setup and Run Agno OpenAI Responses Example

Source: https://docs.agno.com/examples/models/openai/responses/db

Bash commands to clone the Agno repository, navigate to the OpenAI responses cookbook, set up the virtual environment, and execute the database example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run Dynamic Tools Example

Source: https://docs.agno.com/examples/agents/dependencies/dynamic-tools

Bash script to clone the Agno repository, navigate to the dynamic tools example directory, create a virtual environment, and execute the dynamic_tools.py script. This demonstrates the complete workflow for setting up and running the dynamic tools example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/15_dependencies

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dynamic_tools.py
```

--------------------------------

### Setup and Run Routing Example via Bash

Source: https://docs.agno.com/examples/teams/modes/route/with-fallback

Commands to clone the Agno repository, set up the environment, and execute the fallback routing script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/modes/route

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 03_with_fallback.py
```

--------------------------------

### Setup and Run Trello Agent Example

Source: https://docs.agno.com/examples/tools/trello-tools

Bash commands to clone the Agno repository, navigate to the tools cookbook directory, set up a Python virtual environment, and execute the Trello tools example script. This provides a complete setup workflow for running the Trello integration locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python trello_tools.py
```

--------------------------------

### Setup and Run Web Reader Example via Bash

Source: https://docs.agno.com/examples/knowledge/readers/web-reader

Commands to clone the Agno repository, navigate to the knowledge readers directory, and set up a virtual environment to execute the web reader script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python web_reader.py
```

--------------------------------

### Setup and Execute Qdrant MCP Example

Source: https://docs.agno.com/examples/tools/mcp/qdrant

Shell commands to clone the Agno repository, set up the virtual environment, configure the required Qdrant API key, and run the Python agent script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export QDRANT_API_KEY="***"

python qdrant.py
```

--------------------------------

### Setup and Run MCP GitHub Agent

Source: https://docs.agno.com/examples/tools/mcp/github

Bash script to clone the Agno repository, set up a virtual environment, and execute the GitHub agent example. This script automates the installation of dependencies and environment configuration needed to run the MCP GitHub agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python github.py
```

--------------------------------

### Setup and Installation

Source: https://docs.agno.com/tools/toolkits/web-scrape/browserbase

Install required dependencies and configure Browserbase API credentials. This includes setting up the Browserbase account and obtaining necessary API keys.

```APIDOC
## Setup and Installation

### Description
Install BrowserbaseTools dependencies and configure API credentials for Browserbase authentication.

### Prerequisites
1. Sign up for Browserbase account at https://www.browserbase.com/
2. Obtain API credentials from your Browserbase dashboard
3. Install required Python packages

### Installation Steps

#### Step 1: Install Dependencies
```shell
uv pip install browserbase playwright
```

#### Step 2: Configure Environment Variables
```shell
export BROWSERBASE_API_KEY=your-api-key-here
export BROWSERBASE_PROJECT_ID=your-project-id-here
```

#### Step 3: Verify Installation
```python
from agno.tools.browserbase import BrowserbaseTools

# Test initialization
tools = BrowserbaseTools()
print("BrowserbaseTools initialized successfully")
```

### Required Packages
- **browserbase** - Browserbase Python SDK
- **playwright** - Headless browser automation library

### Documentation
For complete documentation, visit: https://docs.agno.com/llms.txt
```

--------------------------------

### Setup and Run Multilingual Router Example

Source: https://docs.agno.com/examples/teams/basics/respond-directly-router-team

Provides bash commands to clone the Agno repository, navigate to the example directory, create a virtual environment, and execute the multilingual router team demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_respond_directly_router_team.py
```

--------------------------------

### Setup and Execute Agno Dependency Example

Source: https://docs.agno.com/examples/agents/dependencies/dependencies-in-context

Shell commands to clone the Agno repository, set up a virtual environment, and execute the dependencies example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/15_dependencies

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dependencies_in_context.py
```

--------------------------------

### Setup and Execute Loop Basic Example in Bash

Source: https://docs.agno.com/examples/workflows/loop-execution/loop-basic

Commands to clone the Agno repository, set up the environment using a helper script, and execute the loop-based workflow script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/03_loop_execution

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python loop_basic.py
```

--------------------------------

### Setup and Run DuckDB Tools Example

Source: https://docs.agno.com/examples/tools/duckdb-tools

Bash script to clone the Agno repository, set up a virtual environment, and execute the DuckDB tools example. This script automates the environment setup and runs the duckdb_tools.py demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python duckdb_tools.py
```

--------------------------------

### Setup and Run Web Search Reader Example

Source: https://docs.agno.com/examples/knowledge/readers/web-search-reader

Bash script to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the web search reader example. This provides a complete setup workflow for running the web search reader demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python web_search_reader.py
```

--------------------------------

### Setup and Run FastEmbed Embedder Example (Bash)

Source: https://docs.agno.com/examples/knowledge/embedders/qdrant-fastembed

These bash commands provide a step-by-step guide to set up the Agno repository, create and activate a Python virtual environment, optionally run a PgVector database using Docker, and finally execute the Python script demonstrating FastEmbed embeddings.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python qdrant_fastembed.py
```

--------------------------------

### Setup and Run Agno Cookbook Example - Bash

Source: https://docs.agno.com/examples/models/google/gemini/audio-input-bytes-content

Shell script commands to clone the Agno repository, navigate to the Google Gemini cookbook directory, create a Python virtual environment, and execute the audio input bytes content example. Includes repository setup and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the example
python audio_input_bytes_content.py
```

--------------------------------

### Setup and Run Image Generation Team Example in Bash

Source: https://docs.agno.com/examples/teams/multimodal/generate-image-with-team

Provides shell commands to clone the Agno repository, navigate to the multimodal teams example directory, set up a Python virtual environment using the demo setup script, and execute the image generation team example. Requires git and bash shell.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python generate_image_with_team.py
```

--------------------------------

### Set up and Run the IBM WatsonX Reasoning Tools Example

Source: https://docs.agno.com/examples/reasoning/tools/ibm-watsonx-reasoning-tools

This Bash script provides the necessary commands to set up the development environment and execute the Python example for IBM WatsonX Reasoning Tools. It includes steps for cloning the Agno repository, navigating to the specific cookbook example, creating and activating a virtual environment, and running the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python ibm_watsonx_reasoning_tools.py
```

--------------------------------

### Setup and Run Custom Logging Example

Source: https://docs.agno.com/examples/agents/advanced/custom-logging

Bash commands to clone the Agno repository, set up a virtual environment, and execute the custom logging example. Includes repository cloning, environment activation, and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python custom_logging.py
```

--------------------------------

### Run Nested Teams Example with Bash

Source: https://docs.agno.com/examples/teams/basics/nested-teams

Setup and execution script for running the nested teams example. Clones the Agno repository, sets up a Python virtual environment using the provided demo setup script, and runs the nested teams example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python nested_teams.py
```

--------------------------------

### Setup and Run Tool Decorator Example

Source: https://docs.agno.com/examples/tools/tool-decorator/tool-decorator-with-instructions

Bash commands to clone the Agno repository, configure the virtual environment, and execute the tool decorator demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/tool_decorator

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_decorator_with_instructions.py
```

--------------------------------

### Execute Sentence Transformer Embedder Example with Bash Commands

Source: https://docs.agno.com/examples/knowledge/embedders/sentence-transformer-embedder

This bash script provides a step-by-step guide to set up the Agno project, activate a virtual environment, and run the Python example for sentence transformer embeddings. It includes an optional command to start a PgVector database using Docker.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python sentence_transformer_embedder.py
```

--------------------------------

### Setup and Run Agno Task Mode Example

Source: https://docs.agno.com/examples/teams/basics/task-mode

Shell commands to clone the Agno repository, set up the necessary virtual environment using the provided demo script, and execute the task mode demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python task_mode.py
```

--------------------------------

### Setup and Run Agno Loop Routing Example

Source: https://docs.agno.com/examples/workflows/conditional-branching/loop-in-choices

Bash commands to clone the Agno repository, configure the environment, and execute the loop-in-choices example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/05_conditional_branching

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python loop_in_choices.py
```

--------------------------------

### Setup and Run MCP CLI Example in Bash

Source: https://docs.agno.com/examples/tools/mcp/cli

Shell script commands to clone the Agno repository, navigate to the MCP CLI cookbook example, create a virtual environment using the demo setup script, and execute the Python CLI application.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python cli.py
```

--------------------------------

### Setup and Run Agno Filtering Example

Source: https://docs.agno.com/examples/knowledge/filters/filtering

Provides shell commands to clone the Agno repository, set up the development environment, and run the filtering example. Includes optional Docker setup for PgVector and virtual environment activation for dependency isolation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python filtering.py
```

--------------------------------

### Setup and Run OpenAI O3 Example

Source: https://docs.agno.com/examples/models/openai/responses/tool-use-o3

Shell script commands to clone the agno repository, navigate to the cookbook example directory, set up a Python virtual environment, and execute the tool use O3 example. Includes repository cloning, environment activation, and script execution steps.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use_o3.py
```

--------------------------------

### Setup and Run Huggingface Example with Bash

Source: https://docs.agno.com/examples/models/huggingface/basic

Provides shell commands to clone the Agno repository, navigate to the Huggingface cookbook example directory, create and activate a Python virtual environment, and execute the basic.py script. This setup ensures all dependencies are properly isolated.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/huggingface

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Agno Reasoning Example

Source: https://docs.agno.com/examples/reasoning/agents/python-101-curriculum

Bash commands to clone the Agno repository, set up the necessary virtual environment using a helper script, and execute the curriculum planning Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python python_101_curriculum.py
```

--------------------------------

### Setup and Run A2A Messaging Example

Source: https://docs.agno.com/examples/agent-os/client-a2a/basic-messaging

Provides bash commands to clone the Agno repository, set up a Python virtual environment, and run the basic A2A messaging example. This setup script prepares the development environment and activates the necessary dependencies for running the A2A client example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/client_a2a

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_basic_messaging.py
```

--------------------------------

### Setup Environment and Run Script

Source: https://docs.agno.com/examples/teams/context-management/few-shot-learning

Executes a setup script to create a virtual environment, activates it, and then runs the few_shot_learning.py script. This is the standard procedure for starting the demo.

```bash
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python few_shot_learning.py
```

--------------------------------

### Setup and Run OpenRouter Streaming Example

Source: https://docs.agno.com/examples/models/openrouter/responses/stream

Provides bash commands to clone the Agno repository, set up a Python virtual environment, configure API keys, and execute the streaming example. This script automates the environment setup process and ensures the OPENROUTER_API_KEY is properly exported before running the streaming agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openrouter/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export OPENROUTER_API_KEY="***"

python stream.py
```

--------------------------------

### Setup and Run CEL Ternary Router Example

Source: https://docs.agno.com/examples/workflows/cel-expressions/router/cel-ternary

Bash script to clone the Agno repository, set up a virtual environment, and execute the CEL ternary router example. This demonstrates the complete workflow from repository setup through running the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/07_cel_expressions/router

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cel_ternary.py
```

--------------------------------

### Setup and Run Background Hooks Example

Source: https://docs.agno.com/examples/agent-os/background-tasks/background-hooks-decorator

Commands to clone the Agno repository, set up a virtual environment, and execute the background hooks demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/background_tasks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python background_hooks_decorator.py
```

--------------------------------

### Setup and Run Azure Image Agent Bytes Example

Source: https://docs.agno.com/examples/models/azure/ai-foundry/image-agent-bytes

This bash snippet provides instructions for setting up and running the Azure Image Agent Bytes example. It covers cloning the 'agno' repository, navigating to the specific cookbook directory, creating and activating a virtual environment, and executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure/ai_foundry

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent_bytes.py
```

--------------------------------

### Clone Repository and Setup Environment

Source: https://docs.agno.com/examples/agent-os/interfaces/a2a/basic

Provides bash commands to clone the Agno repository, navigate to the example directory, create a virtual environment using the provided setup script, and activate it for running the basic agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/a2a

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Airflow Tools Example

Source: https://docs.agno.com/examples/tools/airflow-tools

Bash commands to clone the Agno repository, initialize a virtual environment, and run the Airflow tools cookbook example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python airflow_tools.py
```

--------------------------------

### Setup and Run Azure OpenAI Example

Source: https://docs.agno.com/examples/models/azure/openai/basic

Bash script commands to clone the Agno repository, navigate to the Azure OpenAI cookbook example directory, set up a Python virtual environment, and execute the basic.py example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure/openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Multi-Skill Agent Example via Bash

Source: https://docs.agno.com/examples/models/anthropic/skills/multi-skill-agent

This bash script provides instructions to set up the project repository, create and activate a virtual environment, export the necessary API key, and finally execute the Python script for the multi-skill agent example. It outlines the steps required to run the demonstration locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic/skills

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export ANTHROPIC_API_KEY="***"

python multi_skill_agent.py
```

--------------------------------

### Setup and Run Research Team Example

Source: https://docs.agno.com/examples/agent-os/interfaces/agui/research-team

Bash script to clone the Agno repository, navigate to the research team example, create a virtual environment, and run the research team application. Includes all necessary setup steps for demo execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/agui

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the application
python research_team.py
```

--------------------------------

### Setup and Run Discord Agent - Bash

Source: https://docs.agno.com/examples/integrations/discord/agent-with-user-memory

Shell script commands to clone the Agno repository, navigate to the Discord integration cookbook example, create a Python virtual environment, and execute the Discord agent. Requires git and Python 3.8+ installed on the system.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/discord

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_user_memory.py
```

--------------------------------

### Setup and Run Agentic Learning Example

Source: https://docs.agno.com/examples/learning/learned-knowledge/agentic-mode

Provides shell commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the agentic learning example. This setup includes all necessary dependencies and configuration for running the learned knowledge demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/05_learned_knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 01_agentic_mode.py
```

--------------------------------

### Setup and Run Ollama Responses Example

Source: https://docs.agno.com/examples/models/ollama/responses/basic

Shell commands to clone the Agno repository, navigate to the Ollama responses cookbook, set up a virtual environment, and execute the basic example script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/ollama/responses\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython basic.py
```

--------------------------------

### Setup and Run Reasoning Tools Example

Source: https://docs.agno.com/examples/reasoning/tools/reasoning-tools

Bash script to clone the Agno repository, set up a virtual environment, and execute the reasoning tools example. This includes repository cloning, environment activation, and running the Python script with proper dependencies.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_tools.py
```

--------------------------------

### Setup and Run E2B Tools Example (Bash)

Source: https://docs.agno.com/examples/tools/e2b-tools

This Bash script provides the necessary commands to set up the development environment and execute the E2B tools demonstration. It involves cloning the Agno repository, navigating to the specific example directory, creating and activating a Python virtual environment, and finally running the `e2b_tools.py` script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python e2b_tools.py
```

--------------------------------

### Setup and Run Agno OpenRouter Retry Example

Source: https://docs.agno.com/examples/models/openrouter/chat/retry

Bash script commands to clone the Agno repository, navigate to the OpenRouter example directory, set up a Python virtual environment, and execute the retry demonstration script. This provides the complete setup workflow for running the retry example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openrouter/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run N1N Tool Use Example via Bash

Source: https://docs.agno.com/examples/models/n1n/tool-use

This snippet provides a sequence of bash commands to clone the `agno` repository, navigate to the example directory, set up a virtual environment, and execute the Python script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/n1n\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython tool_use.py
```

--------------------------------

### Vector Search Setup and Execution in Bash

Source: https://docs.agno.com/examples/knowledge/search-type/vector-search

Provides shell commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the vector search example. This script automates the environment preparation and dependency installation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/search_type

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python vector_search.py
```

--------------------------------

### Setup and Run Media Agent Example via Bash

Source: https://docs.agno.com/examples/agent-os/interfaces/whatsapp/agent-with-media

These shell commands facilitate the setup of the Agno environment. They include cloning the repository, setting up a virtual environment, and launching the media agent application.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/whatsapp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_media.py
```

--------------------------------

### Setup and Run Agno Image Generation Agent

Source: https://docs.agno.com/models/providers/native/openai/completion/usage/generate-images

These bash commands guide you through setting up your environment and running the Agno image generation agent. It includes steps for setting your OpenAI API key, installing required Python dependencies, and executing the Python script.

```bash
export OPENAI_API_KEY=xxx
```

```bash
uv pip install -U openai agno
```

```bash
python cookbook/11_models/openai/chat/generate_images.py
```

--------------------------------

### Setup and Run Groq Metrics Example

Source: https://docs.agno.com/examples/models/groq/metrics

Bash script commands to clone the Agno repository, set up a Python virtual environment, and execute the metrics.py example. Includes repository cloning, environment activation, and script execution steps for running the Groq metrics cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python metrics.py
```

--------------------------------

### Setup and Run Agno FileTools Example

Source: https://docs.agno.com/examples/tools/file-tools

This Bash script provides instructions to set up the Agno repository, navigate to the specific cookbook example, create and activate a Python virtual environment, and finally execute the file_tools.py script. This allows users to run the demonstrated Agno agent file management examples locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python file_tools.py
```

--------------------------------

### Setup and Run Memori Integration Example

Source: https://docs.agno.com/examples/integrations/memory/memori-integration

Bash script for cloning the Agno repository, setting up a Python virtual environment, and running the Memori integration example. Includes steps for environment activation and API key configuration via DATABASE_PATH environment variable.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export DATABASE_PATH="***"

python memori_integration.py
```

--------------------------------

### Setup and Execute DeepSeek Retry Example

Source: https://docs.agno.com/examples/models/deepseek/retry

Bash script commands to clone the Agno repository, navigate to the DeepSeek cookbook example, set up a Python virtual environment, and run the retry demonstration script. This provides the complete environment setup needed to execute the retry example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/deepseek

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run Gemini Agent Example in Bash

Source: https://docs.agno.com/examples/models/google/gemini/storage-and-memory

Provides shell commands to clone the agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the storage and memory example script. Includes demo setup script and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python storage_and_memory.py
```

--------------------------------

### Setup and Run Claude Agent Example

Source: https://docs.agno.com/examples/models/vertexai/claude/db

Bash script commands to clone the agno repository, set up a Python virtual environment, and execute the Claude database agent example. This demonstrates the complete workflow from repository setup to running the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Run DeepInfra Retry Example with Setup Script

Source: https://docs.agno.com/examples/models/deepinfra/retry

Bash commands to clone the Agno repository, navigate to the DeepInfra example directory, set up a Python virtual environment, and execute the retry example script. Uses a demo setup script to automate environment configuration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/deepinfra

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run Learning Machine Example

Source: https://docs.agno.com/examples/agents/memory-and-learning/learning-machine

Bash script commands to clone the Agno repository, set up a Python virtual environment, and execute the learning machine example. Includes repository cloning, environment activation, and script execution for the learning agent demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/06_memory_and_learning

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python learning_machine.py
```

--------------------------------

### Setup and Installation for Document Summarizer

Source: https://docs.agno.com/production/applications/document-summarizer

Commands to clone the repository, set up a Python 3.12 virtual environment, install required dependencies, and configure the OpenAI API key.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r cookbook/01_showcase/01_agents/document_summarizer/requirements.in
export OPENAI_API_KEY=your-openai-key
```

--------------------------------

### Setup and Execution Commands

Source: https://docs.agno.com/examples/agents/advanced/background-execution-structured

Bash commands for cloning the repository, setting up the virtual environment, and running the background execution example. Includes optional PgVector setup and API key configuration.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

# Export relevant API keys
export OPENAI_API_KEY="***"

python background_execution_structured.py
```

--------------------------------

### Setup and Run Tool Call Compression Example

Source: https://docs.agno.com/examples/agents/advanced/tool-call-compression

Bash script to clone the Agno repository, navigate to the example directory, set up a Python virtual environment, and execute the tool call compression example. Includes activation of the virtual environment before running the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_call_compression.py
```

--------------------------------

### Setup and Run Groq Structured Output Example

Source: https://docs.agno.com/examples/models/groq/structured-output

Bash script commands to clone the Agno repository, navigate to the Groq cookbook directory, set up a Python virtual environment, and execute the structured output example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Fireworks Structured Output Example (Bash)

Source: https://docs.agno.com/examples/models/fireworks/structured-output

This bash script provides a sequence of commands to set up and execute the Fireworks structured output example. It involves cloning the `agno` repository, navigating to the specific cookbook directory, creating and activating a virtual environment using a provided setup script, and finally running the Python example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/fireworks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Workflow Examples

Source: https://docs.agno.com/examples/workflows/advanced-concepts/session-state/state-in-router

Bash script commands to clone the Agno repository, set up a Python virtual environment, and execute the workflow examples. Includes repository cloning, directory navigation, environment activation, and Python script execution.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/session_state

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python state_in_router.py
```

--------------------------------

### Setup and Run Docling Reader Example

Source: https://docs.agno.com/examples/knowledge/readers/docling-reader-url

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector using Docker, and execute the Docling Reader URL example. This provides a complete development environment setup.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/05_integrations/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python docling_reader_url.py
```

--------------------------------

### Setup and Run Cerebras Tool Use Example

Source: https://docs.agno.com/examples/models/cerebras/tool-use

Bash script commands to clone the Agno repository, navigate to the Cerebras cookbook example directory, set up a Python virtual environment, and execute the tool_use.py script. This provides a complete setup workflow for running the Cerebras tool use example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cerebras

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Team Dependencies Example via Bash

Source: https://docs.agno.com/examples/teams/dependencies/dependencies-in-tools

Commands to clone the Agno repository, set up a virtual environment, and execute the team dependency demonstration script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/dependencies

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python dependencies_in_tools.py
```

--------------------------------

### Setup and Run Azure AI Foundry Example

Source: https://docs.agno.com/examples/models/azure/ai-foundry/tool-use

Bash script to clone the Agno repository, navigate to the Azure AI Foundry example directory, create a virtual environment, and execute the tool use example. Sets up all dependencies required for running the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure/ai_foundry

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Team HITL Example

Source: https://docs.agno.com/examples/teams/human-in-the-loop/team-tool-confirmation-stream

Bash script commands to clone the Agno repository, navigate to the team HITL example directory, set up a Python virtual environment, and execute the team tool confirmation streaming example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/human_in_the_loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python team_tool_confirmation_stream.py
```

--------------------------------

### Setup and Execute Neosantara Cookbook Example

Source: https://docs.agno.com/examples/models/neosantara/basic

Bash commands to clone the Agno repository, navigate to the Neosantara model directory, configure the virtual environment, and execute the basic script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/neosantara

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup Environment and Run Groq Agent Team Example

Source: https://docs.agno.com/examples/models/groq/agent-team

These bash commands provide instructions to clone the 'agno' repository, navigate to the example directory, set up a virtual environment, and execute the 'agent_team.py' script. This allows users to run the Groq Agent Team example locally.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/groq\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython agent_team.py
```

--------------------------------

### Setup and Run Agent State Management Example

Source: https://docs.agno.com/examples/basics/agent-with-state-management

Bash script to clone the Agno repository, set up a Python virtual environment, and run the agent state management example. This provides a complete setup workflow for testing the state management functionality in the Agno framework.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_with_state_management.py
```

--------------------------------

### Run Agno Agent Example with Setup

Source: https://docs.agno.com/examples/agent-os/dbs/surreal-db/agents

Bash script commands to clone the Agno repository, set up a virtual environment, and execute the agents.py module. This demonstrates the complete setup workflow for running Agno agent examples in a development environment with proper dependency isolation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/dbs/surreal_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agents.py
```

--------------------------------

### Clone Repository and Setup Environment

Source: https://docs.agno.com/examples/agents/knowledge/agentic-rag-with-reasoning

Bash commands to clone the Agno repository, navigate to the cookbook example directory, create a virtual environment using the provided setup script, and activate it for running the agentic RAG example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/07_knowledge

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agentic_rag_with_reasoning.py
```

--------------------------------

### Setup and Run Markdown Reader Async Example

Source: https://docs.agno.com/examples/knowledge/readers/md-reader-async

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the markdown reader async example. This provides a complete setup workflow for running the demonstration locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python md_reader_async.py
```

--------------------------------

### Setup and Run Agno Example

Source: https://docs.agno.com/examples/teams/basics/concurrent-member-agents

Bash script commands to clone the Agno repository, navigate to the concurrent member agents example, set up a Python virtual environment, and execute the example. This demonstrates the complete workflow for running the concurrent agent demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/01_quickstart

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 08_concurrent_member_agents.py
```

--------------------------------

### Setup and Run YFinance Tools Example in Bash

Source: https://docs.agno.com/examples/tools/yfinance-tools

Provides the shell commands necessary to clone the Agno repository, initialize the environment, and run the YFinance tools demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python yfinance_tools.py
```

--------------------------------

### Setup and Run Filtering Example via Bash

Source: https://docs.agno.com/examples/knowledge/filters/filtering-with-invalid-keys

Commands to clone the Agno repository, configure the environment, and execute the filtering example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python filtering_with_invalid_keys.py
```

--------------------------------

### Setup and Run Cohere Structured Output Example

Source: https://docs.agno.com/examples/models/cohere/structured-output

Bash script commands to clone the Agno repository, navigate to the Cohere cookbook example directory, set up a Python virtual environment, and execute the structured output example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cohere

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Agno Workflow Example

Source: https://docs.agno.com/examples/components/workflows/save-loop-steps

Bash script to clone the Agno repository, navigate to the workflows cookbook directory, set up a virtual environment, and execute the save loop steps example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/93_components/workflows

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python save_loop_steps.py
```

--------------------------------

### Setup and Run Agno Image Agent (Bash)

Source: https://docs.agno.com/models/providers/gateways/together/usage/image-agent

These bash commands guide the user through setting up the environment for the Agno Image Agent. It includes setting the Together AI API key, installing necessary Python dependencies, and executing the main Python script to run the agent.

```bash
export TOGETHER_API_KEY=xxx
```

```bash
uv pip install -U openai agno
```

```bash
python cookbook/11_models/together/image_agent.py
```

--------------------------------

### Setup and Run Audio Transcription Example

Source: https://docs.agno.com/examples/agents/multimodal/audio-to-text

Bash script commands to clone the Agno repository, navigate to the multimodal agents cookbook, set up a Python virtual environment, and execute the audio-to-text transcription example. This provides a complete setup workflow for running the audio transcription demo.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/12_multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_to_text.py
```

--------------------------------

### Clone, Setup, and Run Agno Anthropic Beta Example

Source: https://docs.agno.com/examples/models/anthropic/betas

Bash script commands to clone the Agno repository, navigate to the Anthropic cookbook example directory, create a virtual environment using the provided setup script, activate it, and execute the beta features demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python betas.py
```

--------------------------------

### Setup and Run Together Retry Example

Source: https://docs.agno.com/examples/models/together/retry

Commands to clone the Agno repository, set up the environment, and execute the retry demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/together

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run Team Persistence Example

Source: https://docs.agno.com/examples/components/save-team

Bash commands to clone the Agno repository, set up the required virtual environment, and execute the team saving demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/93_components

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python save_team.py
```

--------------------------------

### Setup and Run Agno Excel Agent Example (Bash)

Source: https://docs.agno.com/examples/models/anthropic/skills/agent-with-excel

These bash commands guide the user through setting up the Agno project repository, creating and activating a Python virtual environment, and configuring the ANTHROPIC_API_KEY. Finally, it demonstrates how to execute the Python script that showcases the Agno agent's Excel generation capabilities.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic/skills

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export ANTHROPIC_API_KEY="***"

python agent_with_excel.py
```

--------------------------------

### Setup and Run SurrealDB Example

Source: https://docs.agno.com/examples/knowledge/filters/vector-dbs/filtering-surrealdb

Bash commands to clone the Agno repository, set up the environment using a demo script, and execute the SurrealDB filtering example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters/vector_dbs

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python filtering_surrealdb.py
```

--------------------------------

### Setup and Run Cerebras Knowledge Example

Source: https://docs.agno.com/examples/models/cerebras/knowledge

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the knowledge.py example. Includes steps for environment activation and optional vector database setup.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cerebras

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run Personal Assistant Example

Source: https://docs.agno.com/cookbook/learning/personal-assistant

Shell commands to clone the Agno repository, set up the Python virtual environment, configure PostgreSQL via Docker, and execute the personal assistant example. Requires Docker for the PostgreSQL database container.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning

# Setup (requires Docker for Postgres)
./setup_venv.sh
./cookbook/scripts/run_pgvector.sh

# Run
python 07_patterns/personal_assistant.py
```

--------------------------------

### Setup and Run Weave Integration Example

Source: https://docs.agno.com/examples/integrations/observability/weave-op

Bash commands to clone the Agno repository, set up a virtual environment using the provided scripts, and execute the Weave integration demo.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/observability

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python weave_op.py
```

--------------------------------

### Slack Tools Setup and Execution

Source: https://docs.agno.com/examples/tools/slack-tools

Instructions for setting up the development environment and running Slack tools examples with Agno agents. Includes repository cloning, virtual environment setup, and execution commands.

```APIDOC
## Slack Tools - Setup and Execution

### Description
Provides step-by-step instructions for setting up the Agno repository, configuring the development environment, and running Slack tools examples.

### Prerequisites
- Python 3.7 or higher
- Git
- pip package manager

### Required Dependencies
```bash
pip install openai slack-sdk
```

### Setup Instructions
```bash
# Clone the Agno repository
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
```

### Execution
```bash
# Run the Slack tools example
python slack_tools.py
```

### Example Output
The script will execute three agent examples:
1. Send a message to #general channel
2. List all channels in the workspace
3. Retrieve the last 5 messages from #general

### Additional Resources
- [Slack Tools Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/91_tools/slack_tools.py)
- [Agno Documentation](https://docs.agno.com/llms.txt)
```

--------------------------------

### Setup and Run VertexAI Structured Output Example

Source: https://docs.agno.com/examples/models/vertexai/claude/structured-output

This bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a virtual environment using a provided script, activate it, and finally execute the Python structured output example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Execution for Video Bytes Cookbook

Source: https://docs.agno.com/examples/models/google/gemini/video-input-bytes-content

Shell commands to clone the Agno repository, set up the required virtual environment using the provided demo script, and execute the video bytes content example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python video_input_bytes_content.py
```

--------------------------------

### Setup and Run SQLite Agent Example

Source: https://docs.agno.com/examples/storage/sqlite/sqlite-for-agent

Bash script commands to clone the Agno repository, navigate to the SQLite storage example directory, create a Python virtual environment, and execute the agent script. This demonstrates the complete workflow for running the SQLite-backed agent example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/sqlite

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python sqlite_for_agent.py
```

--------------------------------

### Setup and Run Agno Guardrail Example

Source: https://docs.agno.com/examples/basics/agent-with-guardrails

Bash commands to clone the Agno repository, initialize the environment using a setup script, and execute the guardrail demonstration agent.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/00_quickstart
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python agent_with_guardrails.py
```

--------------------------------

### Setup and run Agno streaming agent example (Bash)

Source: https://docs.agno.com/models/providers/native/anthropic/usage/basic-stream

These bash commands provide the necessary steps to set up your environment and execute the Python streaming agent example. It includes setting the "ANTHROPIC_API_KEY" environment variable, installing required Python packages ("anthropic", "agno") using "uv pip", and finally running the Python script.

```bash
export ANTHROPIC_API_KEY=xxx
```

```bash
uv pip install -U anthropic agno
```

```bash
python cookbook/11_models/anthropic/basic_stream.py
```

--------------------------------

### Setup and Execute Nebius Tool Use Example (Bash)

Source: https://docs.agno.com/examples/models/nebius/tool-use

This Bash script provides instructions to clone the `agno` repository, navigate to the Nebius cookbook example, set up a virtual environment using `demo_setup.sh`, activate it, and then execute the `tool_use.py` Python script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/nebius\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython tool_use.py
```

--------------------------------

### Setup and Run Nebius Knowledge Example

Source: https://docs.agno.com/examples/models/nebius/knowledge

Bash commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the knowledge example. This provides a complete setup workflow for running the Nebius agent with knowledge base integration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/nebius

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run WatsonX Agno Agent Example (Bash)

Source: https://docs.agno.com/examples/models/ibm/watsonx/tool-use

This script provides instructions to clone the `agno` repository, navigate to the example directory, set up a virtual environment, and execute the Python script demonstrating the WatsonX agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ibm/watsonx

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Install Dependencies and Run Agno Team Example

Source: https://docs.agno.com/knowledge/teams/team-with-knowledge

These bash commands provide the necessary steps to set up the environment and execute the Python example. This includes installing required libraries using `uv pip`, configuring the `OPENAI_API_KEY` environment variable, and running the main Python script.

```bash
uv pip install -U agno lancedb
```

```bash
export OPENAI_API_KEY=****
```

```bash
python cookbook/02_examples/teams/knowledge/01_team_with_knowledge.py
```

--------------------------------

### Setup and Run Async Scheduler Example

Source: https://docs.agno.com/examples/agent-os/scheduler/async-schedule

Bash script to clone the agno repository, set up a Python virtual environment, and execute the async schedule management example. Includes repository cloning, environment activation, and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/scheduler

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python async_schedule.py
```

--------------------------------

### Setup and Run CEL Compound Exit Example

Source: https://docs.agno.com/examples/workflows/cel-expressions/loop/cel-compound-exit

Bash script to clone the Agno repository, set up a virtual environment, and execute the CEL compound exit workflow example. This demonstrates the complete setup process for running the workflow locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/07_cel_expressions/loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cel_compound_exit.py
```

--------------------------------

### Setup and Run Agno Example Script in Bash

Source: https://docs.agno.com/examples/agents/advanced/automatic-cultural-management

Provides shell commands to clone the Agno repository, navigate to the cookbook directory, create a Python virtual environment, and execute the automatic cultural management example script. This setup ensures all dependencies are isolated and the demo runs in a controlled environment.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 03_automatic_cultural_management.py
```

--------------------------------

### Setup and Run Vercel Reasoning Tools Example

Source: https://docs.agno.com/examples/reasoning/tools/vercel-reasoning-tools

Bash script commands to clone the Agno repository, navigate to the reasoning tools cookbook example, set up a Python virtual environment, and execute the Vercel reasoning tools demonstration. This prepares the environment and runs the agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python vercel_reasoning_tools.py
```

--------------------------------

### Setup and Run OpenAI Flex Tier Example via Bash

Source: https://docs.agno.com/examples/models/openai/chat/agent-flex-tier

Provides the shell commands necessary to clone the repository, prepare the environment, and execute the agent script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_flex_tier.py
```

--------------------------------

### Setup and Run Requesty Structured Output Example

Source: https://docs.agno.com/examples/models/requesty/structured-output

These bash commands provide instructions to clone the `agno` repository, navigate to the specific cookbook example directory, set up a virtual environment using a provided script, activate it, and finally execute the Python script demonstrating structured output with `requesty`.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/requesty

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### SQLTools Prerequisites and Installation

Source: https://docs.agno.com/tools/toolkits/database/sql

Setup requirements and installation instructions for SQLTools, including database adapters for PostgreSQL and MySQL.

```APIDOC
## SQLTools Prerequisites and Installation

### Description
Required dependencies and installation steps for using SQLTools with various database systems.

### Core Requirements

#### SQLAlchemy Installation
```bash
uv pip install -U sqlalchemy
```

### Database Adapters

#### PostgreSQL Setup
Install the psycopg2-binary adapter:
```bash
uv pip install -U psycopg2-binary
```

#### MySQL Setup
Install the mysqlclient adapter:
```bash
uv pip install -U mysqlclient
```

**Note**: The mysqlclient adapter may have additional system-level dependencies. Consult the [official installation guide](https://github.com/PyMySQL/mysqlclient/blob/main/README.md#install) for more details.

### Database Setup

#### PostgreSQL Docker Container
The following example creates a PostgreSQL database running in Docker:
```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agno/pgvector:16
```
```

--------------------------------

### Setup Environment and Run Agno Agent

Source: https://docs.agno.com/models/providers/native/openai/completion/usage/storage

These bash commands provide the necessary steps to set up the environment and run the 'agno' agent. This includes setting the OpenAI API key, installing required Python dependencies, starting a PgVector Docker container for the database, and executing the Python agent script.

```bash
export OPENAI_API_KEY=xxx
```

```bash
uv pip install -U sqlalchemy psycopg openai agno
```

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agnohq/pgvector:16
```

```bash
python cookbook/11_models/openai/chat/db.py
```

--------------------------------

### Setup and Run Agno Gemini Example (Bash)

Source: https://docs.agno.com/examples/models/google/gemini/gemini-3-pro

These bash commands provide instructions to clone the Agno repository, navigate to the specific example directory, set up a Python virtual environment using a provided script, activate it, and finally execute the Python example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python gemini_3_pro.py
```

--------------------------------

### Setup and Run Shopify Tools Example

Source: https://docs.agno.com/examples/tools/shopify-tools

Bash script commands to clone the Agno repository, navigate to the tools cookbook directory, create a Python virtual environment, and execute the Shopify tools example. Includes environment activation and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python shopify_tools.py
```

--------------------------------

### Setup and Run Concurrent Execution Example via Bash

Source: https://docs.agno.com/examples/agents/advanced/concurrent-execution

Commands to clone the Agno repository, configure the virtual environment using the provided setup script, and execute the concurrent execution Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python concurrent_execution.py
```

--------------------------------

### Setup and Run Agno Workflow Example

Source: https://docs.agno.com/examples/agent-os/workflow/workflow-with-input-schema

Commands to clone the Agno repository, set up a virtual environment, and execute the workflow script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/workflow

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_with_input_schema.py
```

--------------------------------

### Setup and Run Agno Team Example in Bash

Source: https://docs.agno.com/examples/components/get-team

This bash script provides instructions to clone the Agno repository, navigate to the relevant example directory, set up a Python virtual environment using `demo_setup.sh`, activate it, and then execute the Python script `get_team.py` to demonstrate loading a team from the database.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/93_components

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python get_team.py
```

--------------------------------

### Setup and Run OpenRouter Tool Example via Bash

Source: https://docs.agno.com/examples/models/openrouter/responses/tool-use

Commands to clone the Agno repository, set up a virtual environment, export the necessary API keys, and execute the tool-use script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openrouter/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export OPENROUTER_API_KEY="***"

python tool_use.py
```

--------------------------------

### Install Dependencies and Run Script

Source: https://docs.agno.com/models/providers/gateways/langdb/usage/structured-output

Bash commands to install required Python packages (openai and agno) and execute the structured output example script. Uses uv pip for package management and runs the cookbook example file.

```bash
uv pip install -U openai agno
python cookbook/11_models/langdb/structured_output.py
```

--------------------------------

### Setup and Run Agno YouTube Example with Bash

Source: https://docs.agno.com/examples/tools/youtube-tools

This bash script provides instructions to clone the Agno repository, navigate to the cookbook directory, set up a virtual environment, activate it, and then execute the Python example for YouTube tools. It's essential for running the provided Python agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python youtube_tools.py
```

--------------------------------

### Setup and Execution Commands

Source: https://docs.agno.com/examples/models/openai/chat/image-agent-with-memory

Bash commands to clone the Agno repository, set up a virtual environment using the provided demo script, and execute the image agent cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent_with_memory.py
```

--------------------------------

### Setup and Run DynamoDB Example via CLI

Source: https://docs.agno.com/examples/agent-os/dbs/dynamo

Commands to clone the Agno repository, set up the necessary virtual environment, and execute the DynamoDB integration script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/05_agent_os/dbs\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython dynamo.py
```

--------------------------------

### Clone and Setup AgentOS Repository

Source: https://docs.agno.com/examples/agent-os/rbac/symmetric/agent-permissions

Sets up the development environment for running the per-agent permissions example. Clones the AgentOS repository, navigates to the RBAC example directory, creates a virtual environment, and activates it for running the example code.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/rbac/symmetric

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
```

--------------------------------

### Setup and Run Google Maps Agent Example

Source: https://docs.agno.com/examples/tools/google-maps-tools

Bash script commands for cloning the Agno repository, setting up a Python virtual environment, and executing the Google Maps agent example. Uses the demo_setup.sh script to automate environment configuration and then runs the google_maps_tools.py example file.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python google_maps_tools.py
```

--------------------------------

### Setup Environment and Run Custom Store Demo

Source: https://docs.agno.com/examples/learning/custom-stores/custom-store-with-db

Provides the necessary shell commands to clone the repository, initialize the virtual environment, and run the custom store database example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/08_custom_stores

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_custom_store_with_db.py
```

--------------------------------

### Setup and Run Async Filtering Example

Source: https://docs.agno.com/examples/knowledge/filters/async-filtering

Bash script to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the async filtering example. Includes steps for repository setup, environment activation, and running the demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python async_filtering.py
```

--------------------------------

### Configure Environment and Run Streaming Agent (Bash)

Source: https://docs.agno.com/models/providers/gateways/cerebras/usage/basic-stream

These bash commands guide you through the necessary steps to prepare your environment and execute the streaming agent example. It includes setting the Cerebras API key, installing required Python packages using 'uv pip', and running the Python script.

```bash
export CEREBRAS_API_KEY=xxx
```

```bash
uv pip install -U cerebras-cloud-sdk agno
```

```bash
python cookbook/11_models/cerebras/basic_stream.py
```

--------------------------------

### Setup and Run AgentOS Background Hooks Example

Source: https://docs.agno.com/examples/agent-os/background-tasks/background-hooks-team

Commands to clone the Agno repository, set up the environment, and run the background hooks example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/background_tasks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python background_hooks_team.py
```

--------------------------------

### Setup and Run OpenAI Basic Example via Bash

Source: https://docs.agno.com/examples/models/openai/responses/basic

Shell commands to clone the Agno repository, navigate to the OpenAI cookbook directory, set up the virtual environment, and execute the basic response script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Lumalabs Example

Source: https://docs.agno.com/examples/tools/lumalabs-tools

Bash script to clone the Agno repository, set up a Python virtual environment, and execute the Lumalabs video generation example. This demonstrates the complete workflow from environment preparation to running the agent with video generation requests.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python lumalabs_tools.py
```

--------------------------------

### Setup and Run Agno Agent Instantiation Performance Example

Source: https://docs.agno.com/examples/evals/performance/instantiate-agent

These bash commands provide instructions to clone the `agno` repository, navigate to the performance evaluation example directory, set up a virtual environment, and execute the Python script to run the agent instantiation performance evaluation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/09_evals/performance

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python instantiate_agent.py
```

--------------------------------

### Setup and Run Ethical Dilemma Example (Bash)

Source: https://docs.agno.com/examples/reasoning/models/deepseek/ethical-dilemma

This bash script provides the necessary commands to set up and run the ethical dilemma example. It includes steps for cloning the Agno repository, navigating to the specific example directory, creating and activating a virtual environment using a setup script, and finally executing the Python script to run the simulation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/models/deepseek

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python ethical_dilemma.py
```

--------------------------------

### Setup and Run Agno Workflow Example in Bash

Source: https://docs.agno.com/examples/workflows/advanced-concepts/session-state/state-with-team

These shell commands facilitate the setup of the Agno repository and the execution of the session state management example. The process includes cloning the source code, initializing a virtual environment, and running the specific Python script to observe workflow behavior.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/session_state

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python state_with_team.py
```

--------------------------------

### Setup and Run Agno Tool Decorator Example

Source: https://docs.agno.com/examples/tools/tool-decorator/tool-decorator

Bash commands to clone the Agno repository, set up the demonstration environment using a setup script, and execute the tool decorator Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/tool_decorator

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_decorator.py
```

--------------------------------

### Clone Repository and Setup Development Environment

Source: https://docs.agno.com/examples/agent-os/background-tasks/background-output-evaluation

Clones the agno repository from GitHub, navigates to the background_tasks example directory, and sets up a Python virtual environment using the provided demo setup script. This prepares the development environment for running the Agent OS background task example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/background_tasks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python background_output_evaluation.py
```

--------------------------------

### Bash: Setup and Run Agno Example

Source: https://docs.agno.com/examples/agent-os/workflow/basic-workflow-team

This bash script outlines the steps to clone the Agno repository, navigate to the example directory, set up a virtual environment, activate it, and run the basic workflow team Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/workflow

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic_workflow_team.py
```

--------------------------------

### Setup and Run Confluence Example

Source: https://docs.agno.com/examples/tools/confluence-tools

Provides shell commands to clone the Agno repository, set up a Python virtual environment, and execute the Confluence tools example. This includes repository cloning, environment activation, and running the confluence_tools.py script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python confluence_tools.py
```

--------------------------------

### Set Up and Run Agno Workflow Example

Source: https://docs.agno.com/examples/agent-os/workflow/workflow-with-router

This bash script provides instructions to clone the Agno repository, navigate to the specific workflow example directory, set up a Python virtual environment, activate it, and then execute the Python workflow script. It outlines the necessary steps to get the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/workflow

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_with_router.py
```

--------------------------------

### Setup and Run Mistral Image Agent Example in Bash

Source: https://docs.agno.com/examples/models/mistral/image-file-input-agent

Commands to clone the Agno repository, prepare the environment, and execute the Mistral image agent cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/mistral

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_file_input_agent.py
```

--------------------------------

### Setup and Run LanceDB Example via CLI

Source: https://docs.agno.com/examples/knowledge/vector-db/lance-db/lance-db

Provides the shell commands necessary to clone the repository, set up the environment using a demo script, and execute the LanceDB demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/lance_db

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python lance_db.py
```

--------------------------------

### Setup and Run AutoGen Performance Example

Source: https://docs.agno.com/examples/evals/performance/comparison

Shell commands to clone the Agno repository, navigate to the performance comparison directory, set up the environment, and execute the benchmark script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/09_evals/performance/comparison

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python autogen_instantiation.py
```

--------------------------------

### Setup and Run Parallel Workflow Example

Source: https://docs.agno.com/examples/workflows/parallel-execution/parallel-basic

Bash script to clone the Agno repository, navigate to the parallel execution example directory, create a Python virtual environment, and execute the parallel workflow demonstration. This sets up all dependencies and runs the parallel_basic.py example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/04_parallel_execution

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python parallel_basic.py
```

--------------------------------

### Setup and Run Vertex AI Claude Example (Shell)

Source: https://docs.agno.com/examples/models/vertexai/claude

This snippet provides shell commands to clone the Agno repository, set up a virtual environment, and execute the Python example demonstrating Vertex AI Claude integration. Follow these steps to run the example locally.

```shell
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run AWS Bedrock Structured Output Example

Source: https://docs.agno.com/examples/models/aws/bedrock/structured-output

Bash script commands to clone the Agno repository, set up a Python virtual environment, and execute the structured output example. This demonstrates the complete workflow from environment setup to running the movie script generation agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/aws/bedrock

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Cohere Image Agent Example

Source: https://docs.agno.com/examples/models/cohere/image-agent-bytes

Shell script commands to clone the agno repository, set up a Python virtual environment, and execute the image agent bytes example. This includes repository cloning, directory navigation, environment setup, and running the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cohere

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent_bytes.py
```

--------------------------------

### Setup and Run Ollama Demo Phi4 Example

Source: https://docs.agno.com/examples/models/ollama/chat/demo-phi4

Provides bash commands to clone the Agno repository, navigate to the Ollama chat demo directory, set up a Python virtual environment, and execute the Phi4 demo script. This setup ensures all dependencies are isolated and the example runs in a controlled environment.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python demo_phi4.py
```

--------------------------------

### Setup and Run Agent Pre-Hook Example

Source: https://docs.agno.com/examples/agents/hooks/pre-hook-input

Bash script commands to clone the Agno repository, navigate to the hooks example directory, create a virtual environment, and execute the pre-hook input validation test script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/09_hooks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pre_hook_input.py
```

--------------------------------

### Setup and Run Agno Middleware Demo

Source: https://docs.agno.com/examples/agent-os/middleware/agent-os-with-custom-middleware

Provides the shell commands necessary to clone the Agno repository, initialize the environment via a setup script, and run the middleware example.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/middleware

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python agent_os_with_custom_middleware.py
```

--------------------------------

### Setup and Run Agno Advanced Scopes Demo

Source: https://docs.agno.com/examples/agent-os/rbac/symmetric/advanced-scopes

This sequence of bash commands guides users through setting up and running the Agno advanced scopes demo. It involves cloning the repository, navigating to the example directory, creating and activating a virtual environment, exporting a JWT verification key, and finally executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/rbac/symmetric

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export JWT_VERIFICATION_KEY="***"

python advanced_scopes.py
```

--------------------------------

### Setup and Run LanceDB Filtering Example

Source: https://docs.agno.com/examples/knowledge/filters/vector-dbs/filtering-lance-db

Bash script commands to clone the Agno repository, navigate to the filtering example directory, create a virtual environment, and execute the filtering_lance_db.py script. Provides a complete setup workflow for running the LanceDB filtering demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters/vector_dbs

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python filtering_lance_db.py
```

--------------------------------

### Setup and Run Notion Tools Example via Bash

Source: https://docs.agno.com/examples/tools/notion-tools

Commands to clone the Agno repository, set up the environment, and execute the Notion tools script. It includes steps for virtual environment activation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python notion_tools.py
```

--------------------------------

### Setup and Run AWS Bedrock Embedder Example

Source: https://docs.agno.com/examples/knowledge/embedders/aws-bedrock-embedder

Bash script for cloning the agno repository, setting up a Python virtual environment, and running the AWS Bedrock embedder example. Includes optional PgVector Docker setup for vector database operations.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python aws_bedrock_embedder.py
```

--------------------------------

### Environment Setup and Execution for Agno Examples

Source: https://docs.agno.com/examples/teams/structured-input-output/json-schema-output

Shell commands to clone the Agno repository, initialize a virtual environment, and run the structured output example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/structured_input_output

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python json_schema_output.py
```

--------------------------------

### Environment Setup and Execution for Mistral Agent

Source: https://docs.agno.com/models/providers/native/mistral/usage/structured-output-with-tool-use

These bash commands provide the necessary steps to prepare the environment and run the Mistral agent example. It covers setting the 'MISTRAL_API_KEY' environment variable, installing required Python packages ('mistralai', 'agno'), and executing the Python script that defines and runs the agent.

```bash
export MISTRAL_API_KEY=xxx
```

```bash
uv pip install -U mistralai agno
```

```bash
python cookbook/11_models/mistral/structured_output_with_tool_use.py
```

--------------------------------

### Setup and Run Llama OpenAI Agent Example

Source: https://docs.agno.com/examples/models/meta/llama-openai/storage

Bash script to clone the Agno repository, navigate to the Llama OpenAI example directory, set up a virtual environment, and execute the agent script. Uses the demo_setup.sh script for environment configuration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python storage.py
```

--------------------------------

### Setup and Run Fibonacci Reasoning Script

Source: https://docs.agno.com/examples/reasoning/agents/fibonacci

Bash commands to clone the Agno repository, set up the demo environment using a setup script, and execute the Fibonacci planning example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python fibonacci.py
```

--------------------------------

### Setup and Run Agno Image Transformation Example

Source: https://docs.agno.com/examples/teams/multimodal/image-to-image-transformation

This bash script provides instructions to set up and run the Agno image-to-image transformation example. It involves cloning the Agno repository, navigating to the specific example directory, setting up a virtual environment using a provided script, activating the environment, and finally executing the Python script for image transformation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/multimodal

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_to_image_transformation.py
```

--------------------------------

### Setup and Run Nebius Database Example

Source: https://docs.agno.com/examples/models/nebius/db

Commands to clone the Agno repository, navigate to the Nebius model cookbook, set up a virtual environment, and execute the database integration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/nebius

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run Langtrace Integration Example

Source: https://docs.agno.com/examples/integrations/observability/langtrace-op

Shell commands to clone the Agno repository, set up a virtual environment, and execute the Langtrace integration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/observability

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python langtrace_op.py
```

--------------------------------

### Setup and Run Logfire Integration Example

Source: https://docs.agno.com/examples/integrations/observability/logfire-via-openinference

Provides shell commands to clone the Agno repository, set up a Python virtual environment using the demo setup script, export required API keys and configuration endpoints, and execute the Logfire integration example. Supports multiple Logfire regions (US, EU) and local deployments.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/observability

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export LOGFIRE_WRITE_TOKEN="***"
export OTEL_EXPORTER_OTLP_ENDPOINT="***"
export OTEL_EXPORTER_OTLP_HEADERS="***"

python logfire_via_openinference.py
```

--------------------------------

### Setup and Execute Spider Tools Cookbook Example

Source: https://docs.agno.com/examples/tools/spider-tools

Bash commands to clone the Agno repository, navigate to the tools cookbook, initialize the environment, and run the spider_tools.py script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python spider_tools.py
```

--------------------------------

### Setup and Run Gemini Agent Example with Bash

Source: https://docs.agno.com/examples/models/google/gemini/db

Provides shell commands to clone the Agno repository, set up a Python virtual environment, and execute the Gemini database example. Uses the demo_setup.sh script to automate environment configuration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run VLLM Example Script

Source: https://docs.agno.com/examples/models/vllm/db

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the VLLM database example. Includes repository cloning, environment activation, and optional PostgreSQL vector database setup.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vllm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python db.py
```

--------------------------------

### Setup Environment and Run Agno Agent (Bash)

Source: https://docs.agno.com/models/providers/cloud/aws-bedrock/usage/knowledge

These bash commands guide through setting up the environment for the Agno agent. It includes exporting AWS credentials, installing necessary Python dependencies using 'uv pip', running a PgVector-enabled PostgreSQL container with Docker, and finally executing the Python agent script.

```bash
export AWS_ACCESS_KEY_ID=***
export AWS_SECRET_ACCESS_KEY=***
export AWS_REGION=***
```

```bash
uv pip install -U boto3 sqlalchemy pgvector pypdf openai psycopg agno
```

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agnohq/pgvector:16
```

```bash
python knowledge.py
```

--------------------------------

### Setup and Run Remote Team Example

Source: https://docs.agno.com/examples/teams/run-control/remote-team

Commands to clone the Agno repository, set up the virtual environment, and execute the remote team demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/run_control

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python remote_team.py
```

--------------------------------

### Installation and Configuration

Source: https://docs.agno.com/tools/toolkits/web-scrape/scrapegraph

Setup instructions for installing the scrapegraph-py library and configuring API authentication. Required before using any ScrapeGraphTools methods.

```APIDOC
## Installation and Configuration

### Prerequisites
The scrapegraph-py library is required to use ScrapeGraphTools.

### Installation
```shell
uv pip install -U scrapegraph-py
```

### API Key Configuration
If your ScrapeGraph configuration or specific models require an API key, set the `SGAI_API_KEY` environment variable:

```shell
export SGAI_API_KEY="YOUR_SGAI_API_KEY"
```

### Environment Variables
- **SGAI_API_KEY** (string) - Optional - Your ScrapeGraph API key for authentication

### Supported Features
- Heavy JavaScript rendering for dynamic content
- Multiple scraping methods (smartscraper, markdownify, searchscraper, crawl, scrape)
- Structured data extraction using natural language prompts
- Raw HTML content retrieval
- Website crawling with data extraction
```

--------------------------------

### Setup and Run GitHub Tools Demo

Source: https://docs.agno.com/examples/tools/github-tools

Bash script commands to clone the agno repository, set up a virtual environment, and execute the GitHub tools demonstration. This provides the complete setup workflow for running the examples locally.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python github_tools.py
```

--------------------------------

### Install Agno and Run Memory Manager Example

Source: https://docs.agno.com/memory/agent/custom-memory-manager

Commands to install the Agno library using uv and execute the custom memory manager script.

```bash
uv pip install -U agno
python custom_memory_manager.py
```

--------------------------------

### Setup and Run Ollama Reasoning Tools Example

Source: https://docs.agno.com/examples/reasoning/tools/ollama-reasoning-tools

Provides shell commands to clone the Agno repository, set up a Python virtual environment, and execute the Ollama reasoning tools example. This script automates the environment configuration and activates the demo virtual environment for running the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python ollama_reasoning_tools.py
```

--------------------------------

### Setup and Run Agno Workflow Example

Source: https://docs.agno.com/examples/workflows/conditional-execution/condition-with-else

Commands to clone the Agno repository, set up the virtual environment, and execute the conditional execution script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/02_conditional_execution

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python condition_with_else.py
```

--------------------------------

### Setup and Run Agno Workflow Examples using Bash

Source: https://docs.agno.com/examples/workflows/conditional-branching/selector-types

These bash commands provide comprehensive instructions to set up the Agno repository, navigate to the specific workflow example directory, and execute the Python script. The process involves cloning the repository, changing directories, setting up a virtual environment using a provided script, activating it, and finally running the `selector_types.py` file to observe the workflow examples in action.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/05_conditional_branching

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python selector_types.py
```

--------------------------------

### Setup and Run Brandfetch Example

Source: https://docs.agno.com/examples/tools/brandfetch-tools

Shell script commands to clone the Agno repository, set up a Python virtual environment, and execute the Brandfetch tools example. Includes repository cloning, environment activation, and script execution steps.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python brandfetch_tools.py
```

--------------------------------

### Setup and Run Mem0 Integration Example

Source: https://docs.agno.com/examples/integrations/memory/mem0-integration

Bash commands to clone the Agno repository, navigate to the memory integration directory, set up the environment, and execute the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/92_integrations/memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python mem0_integration.py
```

--------------------------------

### Setup and Installation for Translation Agent

Source: https://docs.agno.com/production/applications/translation-agent

Commands to clone the repository, create a virtual environment using uv, and install the necessary dependencies for the translation agent showcase.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r cookbook/01_showcase/01_agents/translation_agent/requirements.in
```

--------------------------------

### Setup and Run Stream Hook Example - Bash

Source: https://docs.agno.com/examples/teams/hooks/stream-hook

Provides shell commands to clone the Agno repository, navigate to the hooks example directory, set up a Python virtual environment, and execute the stream hook example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/hooks

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python stream_hook.py
```

--------------------------------

### Install AWS Lambda Dependencies and Setup

Source: https://docs.agno.com/examples/tools/aws-lambda-tools

Commands to install the required boto3 library and clone the Agno repository to access the tools cookbook.

```bash
uv pip install boto3
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools
```

--------------------------------

### Setup and Execution Commands for Dashscope Example

Source: https://docs.agno.com/examples/models/dashscope/image-agent

Bash commands to clone the Agno repository, navigate to the Dashscope cookbook directory, set up the virtual environment, and execute the image agent script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/dashscope

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent.py
```

--------------------------------

### Setup and Execute Agno Team Streaming Example

Source: https://docs.agno.com/examples/teams/streaming/team-streaming

Shell commands to clone the Agno repository, prepare the environment using a setup script, and run the team streaming demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/streaming

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python team_streaming.py
```

--------------------------------

### Setup and Run Agentic User Profile Example

Source: https://docs.agno.com/examples/learning/basics/b-user-profile-agentic

Bash script commands to clone the Agno repository, navigate to the learning examples directory, set up a Python virtual environment, and execute the agentic user profile demonstration script. This prepares the environment and runs the complete example workflow.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/01_basics

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 1b_user_profile_agentic.py
```

--------------------------------

### Clone and Setup Agno Repository with Virtual Environment

Source: https://docs.agno.com/examples/models/vertexai/claude/knowledge

Bash script to clone the Agno repository, navigate to the Claude VertexAI cookbook example, create a Python virtual environment using the demo setup script, and activate it for running the knowledge example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run Team Memory Example via Bash

Source: https://docs.agno.com/examples/teams/memory/team-with-agentic-memory

Instructions for cloning the Agno repository, preparing the environment, and executing the team memory demo script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/memory

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_team_with_agentic_memory.py
```

--------------------------------

### Setup and Run Agno Workflow Demo Environment

Source: https://docs.agno.com/examples/workflows/basic-workflows/sequence-of-steps/workflow-using-steps-nested

Bash script commands to clone the Agno repository, navigate to the workflow example directory, set up a Python virtual environment, and execute the workflow script. This provides a complete setup workflow for running the basic sequence of steps example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/01_basic_workflows/01_sequence_of_steps

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_using_steps_nested.py
```

--------------------------------

### Setup and Run Vertexai Claude Thinking Example

Source: https://docs.agno.com/examples/models/vertexai/claude/thinking

Shell script commands to clone the agno repository, navigate to the cookbook example directory, create a virtual environment, and execute the thinking.py script. The demo_setup.sh script handles environment configuration automatically.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vertexai/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python thinking.py
```

--------------------------------

### Setup and Run Agno Workflow Example

Source: https://docs.agno.com/examples/workflows/advanced-concepts/run-control/event-storage

Bash script commands to clone the Agno repository, navigate to the workflow example directory, create a Python virtual environment, and execute the event storage demonstration script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/run_control

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python event_storage.py
```

--------------------------------

### Setup and Run Vllm Example

Source: https://docs.agno.com/examples/models/vllm/basic

Bash script commands for cloning the Agno repository, setting up a Python virtual environment, and executing the Vllm basic example. This includes repository cloning, environment activation, and running the Python script with all dependencies properly configured.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vllm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run Cerebras Example

Source: https://docs.agno.com/examples/models/cerebras/structured-output

Bash script commands to clone the Agno repository, navigate to the Cerebras cookbook example directory, set up a Python virtual environment, and execute the structured output example script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cerebras

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Agno Agent for PDF Processing (Bash)

Source: https://docs.agno.com/models/providers/native/openai/responses/usage/pdf-input-local

These bash commands guide you through setting up your environment and executing the Python script. It includes steps to set your OpenAI API key, install necessary Python dependencies using 'uv pip', and run the main Python script to process the PDF.

```bash
export OPENAI_API_KEY=xxx
```

```bash
uv pip install -U openai agno
```

```bash
python cookbook/11_models/openai/responses/pdf_input_local.py
```

--------------------------------

### Setup and Execute Groq Image Agent Example

Source: https://docs.agno.com/examples/models/groq/image-agent

Shell commands to clone the Agno repository, navigate to the Groq cookbook directory, configure the virtual environment, and run the image agent script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent.py
```

--------------------------------

### Setup and Run External Tool Example

Source: https://docs.agno.com/examples/agents/human-in-the-loop/external-tool-execution

Shell commands to clone the Agno repository, set up the environment, and execute the external tool execution script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/10_human_in_the_loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python external_tool_execution.py
```

--------------------------------

### Setup and Run Telegram Tool Example

Source: https://docs.agno.com/examples/tools/telegram-tools

Bash commands to clone the Agno repository, set up the virtual environment, and execute the Telegram tools cookbook example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python telegram_tools.py
```

--------------------------------

### Setup and Run Cache Example with Bash

Source: https://docs.agno.com/examples/agents/advanced/cache-model-response

Shell script commands to clone the Agno repository, navigate to the cache example directory, set up a Python virtual environment, and execute the cache model response demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/14_advanced

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cache_model_response.py
```

--------------------------------

### Setup and Run LangDB Finance Agent

Source: https://docs.agno.com/examples/models/langdb/finance-agent

Provides the shell commands necessary to clone the repository, prepare the environment using a setup script, and run the finance agent example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/langdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python finance_agent.py
```

--------------------------------

### Setup and Run Include Exclude Tools Example

Source: https://docs.agno.com/examples/tools/other/include-exclude-tools

Bash commands to clone the Agno repository, navigate to the specific cookbook directory, set up the virtual environment, and execute the include/exclude tools demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/other

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python include_exclude_tools.py
```

--------------------------------

### Setup and Run Google Image Generation Example

Source: https://docs.agno.com/examples/models/google/gemini/image-generation

Bash commands to clone the Agno repository, navigate to the Gemini cookbook directory, set up the virtual environment, and execute the image generation script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_generation.py
```

--------------------------------

### Setup and Run Agno Project Environment

Source: https://docs.agno.com/examples/agent-os/interfaces/slack/basic

Clones the Agno repository, sets up a Python virtual environment using the provided demo setup script, and runs the basic agent example. This prepares all dependencies and launches the application.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/interfaces/slack

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run the basic agent
python basic.py
```

--------------------------------

### Clone, Setup, and Run Approval Audit Example in Bash

Source: https://docs.agno.com/examples/agents/approvals/audit-approval-overview

Bash commands to clone the Agno repository, navigate to the approvals cookbook example, create a virtual environment, and execute the audit approval overview script. This setup process prepares the environment for running the approval audit demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/11_approvals

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audit_approval_overview.py
```

--------------------------------

### Setup and Execute DuckDuckGo Tools Example

Source: https://docs.agno.com/examples/tools/duckduckgo-tools

Bash commands to clone the Agno repository, set up the required virtual environment using the provided demo script, and execute the DuckDuckGo tools demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python duckduckgo_tools.py
```

--------------------------------

### Install Dependencies and Run Script

Source: https://docs.agno.com/models/providers/native/openai/completion/usage/structured-output

Install required packages (openai and agno) and execute the structured output example script. Set the OpenAI API key environment variable before running the script.

```bash
export OPENAI_API_KEY=xxx
uv pip install -U openai agno
python cookbook/11_models/openai/chat/structured_output.py
```

--------------------------------

### Setup and Execute Ollama Reasoning Agent Example

Source: https://docs.agno.com/examples/models/ollama/chat/reasoning-agent

Bash commands to clone the Agno repository, configure the environment using a setup script, and run the reasoning agent Python file.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_agent.py
```

--------------------------------

### Setup and Run Team HITL Streaming Example

Source: https://docs.agno.com/examples/teams/human-in-the-loop/external-tool-execution-stream

Bash script to clone the Agno repository, navigate to the team HITL example directory, set up a Python virtual environment, and execute the external tool execution streaming example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/human_in_the_loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python external_tool_execution_stream.py
```

--------------------------------

### Setup and Run Ollama Temperature Example

Source: https://docs.agno.com/examples/models/ollama/chat/set-temperature

Commands to clone the Agno repository, navigate to the Ollama cookbook directory, set up a virtual environment, and execute the temperature configuration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ollama/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python set_temperature.py
```

--------------------------------

### Setup and Run Cached Tool Example

Source: https://docs.agno.com/examples/tools/tool-decorator/cache-tool-calls

Bash script to clone the Agno repository, navigate to the tool decorator example directory, create a virtual environment, and execute the cache_tool_calls.py script. This sets up all dependencies required to run the cached tool example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/tool_decorator

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cache_tool_calls.py
```

--------------------------------

### Setup and Run Deepseek R1 Demo Environment

Source: https://docs.agno.com/models/providers/local/ollama/usage/demo-deepseek-r1

These bash commands provide a step-by-step guide to prepare the environment for running the Deepseek R1 demo. It includes pulling the Deepseek R1 model using Ollama, installing required Python packages (ollama, agno), and finally executing the Python script that interacts with the model.

```bash
ollama pull deepseek-r1:14b
```

```bash
uv pip install -U ollama agno
```

```bash
python cookbook/11_models/ollama/demo_deepseek_r1.py
```

--------------------------------

### Setup and Run Email Tools Example

Source: https://docs.agno.com/examples/tools/email-tools

Bash script to clone the Agno repository, set up a virtual environment, and execute the email tools example. Includes repository cloning, environment activation, and running the email_tools.py script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python email_tools.py
```

--------------------------------

### Execute WatsonX Database Example via CLI

Source: https://docs.agno.com/examples/models/ibm/watsonx/db

Provides the necessary shell commands to clone the repository, prepare the environment using a setup script, and run the WatsonX database example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/ibm/watsonx

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Run Multi-Agent Scheduler Example in Bash

Source: https://docs.agno.com/examples/agent-os/scheduler/multi-agent-schedules

Provides shell commands to clone the Agno repository, navigate to the scheduler cookbook example, create a virtual environment, and execute the multi-agent scheduling demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/scheduler

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python multi_agent_schedules.py
```

--------------------------------

### Setup and Run Agno Knowledge Example

Source: https://docs.agno.com/examples/knowledge/cloud/cloud-agentos

Shell commands to clone the Agno repository, set up the virtual environment, run the PgVector database via Docker, and execute the knowledge base script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/cloud

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

# Export relevant API keys
export SHAREPOINT_TENANT_ID="***"

# Run the application
python cloud_agentos.py
```

--------------------------------

### Setup and Run Cerebras OpenAI Example

Source: https://docs.agno.com/examples/models/cerebras-openai/structured-output

Bash script commands to clone the Agno repository, navigate to the Cerebras OpenAI cookbook example directory, create a virtual environment, and execute the structured output example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cerebras_openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Execution Commands for Anthropic PDF Example

Source: https://docs.agno.com/examples/models/anthropic/pdf-input-file-upload

Shell commands to clone the Agno repository, navigate to the specific cookbook example, set up the virtual environment, and run the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/anthropic

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_file_upload.py
```

--------------------------------

### Setup and Run Jina Embedder Example

Source: https://docs.agno.com/examples/knowledge/embedders/jina-embedder

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector using Docker, and execute the Jina embedder example. Includes setup script execution and environment activation steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/embedders

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optional: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python jina_embedder.py
```

--------------------------------

### Setup and Run LiteLLM Reasoning Agent Example in Bash

Source: https://docs.agno.com/examples/models/litellm/reasoning-agent

These bash commands provide instructions to clone the Agno repository, navigate to the example directory, set up a virtual environment, and execute the Python reasoning agent script. This allows users to run the LiteLLM reasoning agent example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/litellm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python reasoning_agent.py
```

--------------------------------

### Setup and Run AgentOS SQLite Example via CLI

Source: https://docs.agno.com/examples/agent-os/dbs/sqlite

Shell commands to clone the Agno repository, prepare the environment, and run the SQLite agent example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/dbs

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python sqlite.py
```

--------------------------------

### Setup and Run Agno Image Agent Example (Bash)

Source: https://docs.agno.com/examples/models/openai/responses/image-agent

These bash commands provide instructions for cloning the Agno repository, navigating to the example directory, setting up a virtual environment, and executing the `image_agent.py` script. This allows users to run the OpenAI Image Agent example locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent.py
```

--------------------------------

### Setup and Run OpenAI Moderation Example

Source: https://docs.agno.com/examples/teams/guardrails/openai-moderation

Bash commands to clone the Agno repository, configure the environment, and run the moderation guardrail example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/guardrails

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python openai_moderation.py
```

--------------------------------

### Setup and Run Financial Advisory Example

Source: https://docs.agno.com/examples/teams/task-mode/custom-tools

Bash script commands to clone the Agno repository, navigate to the financial advisory example directory, set up a Python virtual environment, and execute the multi-agent financial advisory system.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/task_mode

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 06_custom_tools.py
```

--------------------------------

### Install Dependencies and Run Agno LanceDB Example

Source: https://docs.agno.com/knowledge/vector-stores/lancedb/usage/lance-db

These bash commands provide the necessary steps to prepare your environment for running the Agno LanceDB example. It includes installing required Python packages using 'uv pip', setting the 'OPENAI_API_KEY' environment variable, and executing the Python script.

```bash
uv pip install -U lancedb pypdf openai agno
```

```bash
export OPENAI_API_KEY=xxx
```

```bash
python cookbook/08_knowledge/vector_db/lance_db/lance_db.py
```

--------------------------------

### Clone and Run AsyncMongoDb Workflow Example

Source: https://docs.agno.com/examples/storage/mongo/async-mongo/async-mongodb-for-workflow

Setup and execute the complete AsyncMongoDb workflow example. Clones the Agno repository, creates a virtual environment, and runs the async MongoDB workflow demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/mongo/async_mongo

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python async_mongodb_for_workflow.py
```

--------------------------------

### Set Up and Run ArxivTools Example (Bash)

Source: https://docs.agno.com/examples/tools/arxiv-tools

This bash script provides instructions to set up the Agno repository and run the `arxiv_tools.py` example. It covers cloning the repository, navigating to the correct directory, creating and activating a Python virtual environment, and finally executing the Python script to demonstrate the ArxivTools agent functionalities.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python arxiv_tools.py

```

--------------------------------

### Setup and Execution Commands for Azure Image Agent

Source: https://docs.agno.com/examples/models/azure/ai-foundry/image-agent

Provides the necessary CLI commands to clone the repository, prepare the environment using a setup script, and execute the image agent cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure/ai_foundry

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent.py
```

--------------------------------

### Setup Environment and Execute LMStudio Agent Example (Bash)

Source: https://docs.agno.com/examples/models/lmstudio/tool-use

This bash script provides instructions to clone the Agno repository, navigate to the specific example directory, set up a virtual environment, and run the Python script demonstrating LMStudio tool use. It ensures all necessary dependencies and environment configurations are in place for execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/lmstudio

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Environment Setup and Dependency Installation

Source: https://docs.agno.com/models/providers/gateways/litellm-openai/usage/tool-use

Commands to set the LiteLLM API key and install necessary packages including litellm, openai, and agno using the uv package manager.

```bash
export LITELLM_API_KEY=xxx
uv pip install -U litellm[proxy] openai agno
```

--------------------------------

### Setup and Run Parallel Tools Example

Source: https://docs.agno.com/examples/tools/parallel-tools

Bash script for cloning the Agno repository, setting up a Python virtual environment, and executing the parallel tools example. This script automates the environment configuration and runs the demonstration with streaming output.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python parallel_tools.py
```

--------------------------------

### Setup and Run SingleStore for Agno Agent

Source: https://docs.agno.com/knowledge/vector-stores/singlestore/usage/singlestore-db

These bash commands provide a step-by-step guide for setting up the environment and running the Agno agent with SingleStore. It includes installing required Python packages, deploying a SingleStore instance via Docker, configuring environment variables for database connection and API keys, and finally executing the Python integration script.

```bash
uv pip install -U PyMySQL sqlalchemy pypdf openai agno
```

```bash
docker run -d --name singlestoredb \
--platform linux/amd64 \
-p 3306:3306 \
-p 8080:8080 \
-v /tmp:/var/lib/memsql \
-e ROOT_PASSWORD=admin \
-e SINGLESTORE_DB=AGNO \
-e SINGLESTORE_USER=root \
-e SINGLESTORE_PASSWORD=admin \
-e LICENSE_KEY=accept \
ghcr.io/singlestore-labs/singlestoredb-dev:latest

docker start singlestoredb

docker exec singlestoredb memsql -u root -padmin -e "CREATE DATABASE IF NOT EXISTS AGNO;"
```

```bash
export SINGLESTORE_HOST="localhost"
export SINGLESTORE_PORT="3306"
export SINGLESTORE_USERNAME="root"
export SINGLESTORE_PASSWORD="admin"
export SINGLESTORE_DATABASE="AGNO"
export SINGLESTORE_SSL_CA=".certs/singlestore_bundle.pem"
export OPENAI_API_KEY=xxx
```

```bash
python cookbook/08_knowledge/vector_db/singlestore_db/singlestore_db.py
```

--------------------------------

### Setup and Run Couchbase Example

Source: https://docs.agno.com/examples/knowledge/vector-db/couchbase-db/couchbase-db

Bash commands to clone the repository, set up the virtual environment, and export required environment variables for Couchbase and OpenAI.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/couchbase_db

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

export COUCHBASE_CONNECTION_STRING="***"
export COUCHBASE_PASSWORD="***"
export COUCHBASE_USER="***"
export OPENAI_API_KEY="***"

python couchbase_db.py
```

--------------------------------

### Install Required Python Dependencies

Source: https://docs.agno.com/models/providers/native/google/usage/audio-input-file-upload

Bash command to install the necessary Python packages for the audio input example. Uses uv pip to install google-genai and agno packages with their latest versions.

```bash
uv pip install -U google-genai agno
```

--------------------------------

### Setup and Run Reliability Evaluation Example (Bash)

Source: https://docs.agno.com/examples/evals/reliability/db-logging

This Bash script provides instructions to clone the Agno repository, navigate to the example directory, set up a Python virtual environment, and execute the db_logging.py script. This allows users to run the reliability evaluation example locally.

```bash
# Clone and setup repogit clone https://github.com/agno-agi/agno.gitcd agno/cookbook/09_evals/reliability# Create and activate virtual environment./scripts/demo_setup.shsource .venvs/demo/bin/activatepython db_logging.py
```

--------------------------------

### Clone Repository and Run Example

Source: https://docs.agno.com/examples/storage/surrealdb/surrealdb-for-agent

Sets up the development environment by cloning the Agno repository, creating a virtual environment, and executing the SurrealDB agent example script. This provides a complete setup workflow from repository initialization to script execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/06_storage/surrealdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python surrealdb_for_agent.py
```

--------------------------------

### Setup and Run Azure Structured Output Example

Source: https://docs.agno.com/examples/models/azure/openai/structured-output

Shell commands to clone the Agno repository, navigate to the Azure OpenAI cookbook directory, set up the virtual environment, and execute the structured output demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/azure/openai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Complete Agent with Skills Initialization Example

Source: https://docs.agno.com/skills/loading-skills

This comprehensive example demonstrates the full setup of an `Agent` with `LocalSkills` loading, custom instructions, and an invocation to review code. It includes path resolution for skills and showcases how to integrate an agent with its loaded capabilities.

```python
from pathlib import Path
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.skills import Skills, LocalSkills

# Get skills directory relative to this file
skills_dir = Path(__file__).parent / "skills"

# Create agent with skills
agent = Agent(
    name="Code Assistant",
    model=OpenAIResponses(id="gpt-5.2"),
    skills=Skills(loaders=[LocalSkills(str(skills_dir))]),
    instructions=[
        "You are a helpful coding assistant with access to specialized skills."
    ],
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response(
        "Review this Python function:\n\n"
        "def calc(x,y): return x+y"
    )
```

--------------------------------

### Setup and Installation for Pinecone Integration

Source: https://docs.agno.com/knowledge/vector-stores/pinecone/usage/pinecone-db

Commands to install the necessary dependencies using uv and configure the environment variables required for Pinecone and OpenAI authentication.

```bash
uv pip install -U pinecone-client pypdf openai agno

export PINECONE_API_KEY="your-pinecone-api-key"
export OPENAI_API_KEY=xxx

python cookbook/08_knowledge/vector_db/pinecone_db/pinecone_db.py
```

--------------------------------

### Generate Visual Recipe Guide with Images

Source: https://docs.agno.com/production/applications/recipe-agent

Run the visual guide example to generate step-by-step cooking images using DALL-E. This demonstrates the complete multi-modal workflow including image generation and file persistence.

```bash
python cookbook/01_showcase/01_agents/recipe_agent/examples/visual_guide.py
```

--------------------------------

### Setup and Run OpenAI Audio Stream Example

Source: https://docs.agno.com/examples/models/openai/chat/audio-output-stream

Shell commands to clone the Agno repository, set up the demo environment using a virtual environment, and execute the audio output stream script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openai/chat

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python audio_output_stream.py
```

--------------------------------

### Setup and Run Agno Workflow Example

Source: https://docs.agno.com/examples/workflows/basic-workflows/sequence-of-steps/sequence-with-functions

Bash commands to clone the Agno repository, initialize the demo environment, and run the workflow sequence script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/01_basic_workflows/01_sequence_of_steps

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python sequence_with_functions.py
```

--------------------------------

### Setup and Execute Agno Session State Example (Bash)

Source: https://docs.agno.com/examples/workflows/advanced-concepts/session-state/state-in-function

This Bash script provides the necessary steps to set up the Agno repository, navigate to the specific example, create and activate a Python virtual environment, and finally run the Python script demonstrating workflow session state management.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/session_state

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python state_in_function.py
```

--------------------------------

### Environment Setup and Execution for Agno Agent

Source: https://docs.agno.com/models/providers/native/vercel/usage/knowledge

These bash commands guide through the essential steps to prepare the environment for running the Agno agent. This includes setting the Vercel V0 API key, installing required Python packages, launching a PgVector database instance via Docker, and finally executing the Python agent script.

```bash
export V0_API_KEY=xxx
```

```bash
uv pip install -U sqlalchemy pgvector pypdf openai agno
```

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agnohq/pgvector:16
```

```bash
python cookbook/11_models/vercel/knowledge.py
```

--------------------------------

### Setup and Run Gemini PDF Example

Source: https://docs.agno.com/examples/models/google/gemini/pdf-input-file-upload

Bash script to clone the Agno repository, set up a virtual environment, and run the PDF file upload example. Includes repository cloning, environment activation, and script execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pdf_input_file_upload.py
```

--------------------------------

### Setup and Run Session History Example

Source: https://docs.agno.com/examples/agents/state-and-session/last-n-session-messages

Shell commands to clone the Agno repository, set up the demonstration environment, and execute the session history management script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/05_state_and_session

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python last_n_session_messages.py
```

--------------------------------

### Setup and Run OpenRouter Agent Example with Bash

Source: https://docs.agno.com/examples/models/openrouter/responses/basic

This bash script provides instructions to clone the `agno` repository, navigate to the example directory, set up a virtual environment, and export the `OPENROUTER_API_KEY`. Finally, it shows how to execute the Python script demonstrating OpenRouter agent usage.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/openrouter/responses

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export OPENROUTER_API_KEY="***"

python basic.py
```

--------------------------------

### Set Up and Run Nexus Tool Use Example in Bash

Source: https://docs.agno.com/examples/models/nexus/tool-use

This bash script provides step-by-step instructions to clone the Agno repository, navigate to the Nexus example directory, set up a Python virtual environment, and execute the Python script demonstrating Nexus tool use. It ensures all necessary dependencies and environment are configured for running the example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/nexus

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python tool_use.py
```

--------------------------------

### Setup and Run Audit Approval Example

Source: https://docs.agno.com/examples/agents/approvals/audit-approval-external

Commands to clone the Agno repository and navigate to the audit approval cookbook directory.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/11_approvals
```

--------------------------------

### Run Agno IBM Image Agent Bytes Example

Source: https://docs.agno.com/examples/models/ibm/watsonx/image-agent-bytes

These bash commands provide instructions to set up the Agno repository, create and activate a virtual environment, and then execute the Python example script. It covers cloning the repository, navigating to the example directory, and running a setup script to prepare the environment.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/ibm/watsonx\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython image_agent_bytes.py
```

--------------------------------

### Setup and Run DashScope Image Agent Example

Source: https://docs.agno.com/examples/models/dashscope/image-agent-bytes

Bash commands to clone the Agno repository, navigate to the DashScope cookbook directory, set up the environment, and execute the image analysis script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/dashscope

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python image_agent_bytes.py
```

--------------------------------

### Setup and Execute Workflow Cancellation Example

Source: https://docs.agno.com/examples/workflows/advanced-concepts/run-control/cancel-run

Bash script commands for cloning the agno repository, setting up a Python virtual environment, and running the workflow cancellation example. Includes repository cloning, directory navigation, environment setup using a demo script, and execution of the cancel_run.py Python script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/run_control

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cancel_run.py
```

--------------------------------

### Setup and Run AgentOS Cookbook Example via CLI

Source: https://docs.agno.com/examples/agent-os/client/server

Commands to clone the Agno repository and navigate to the specific AgentOS client cookbook directory to prepare the environment for running the server.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/client
```

--------------------------------

### Setup and Execute Agno Learning Demo

Source: https://docs.agno.com/examples/learning/basics/learned-knowledge

Bash commands to initialize the environment, start the required PgVector database via Docker, and run the Python learning demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/01_basics

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python 4_learned_knowledge.py
```

--------------------------------

### Setup and Run Perplexity Structured Output Example

Source: https://docs.agno.com/examples/models/perplexity/structured-output

Bash script commands to clone the Agno repository, navigate to the Perplexity cookbook example directory, create a virtual environment, and execute the structured output example. This sets up all dependencies required to run the movie script generation agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/perplexity

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Agno Workflow Example

Source: https://docs.agno.com/examples/agent-os/workflow/workflow-with-loop

Bash script to clone the Agno repository, set up a virtual environment, and run the workflow with loop example. Includes repository cloning, virtual environment activation, and Python script execution.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/workflow

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python workflow_with_loop.py
```

--------------------------------

### Run BigQuery Example from Cookbook

Source: https://docs.agno.com/examples/tools/google-bigquery-tools

Clone the Agno repository, set up a virtual environment, and execute the Google BigQuery tools example. This script automates the setup process and runs the demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python google_bigquery_tools.py
```

--------------------------------

### Setup and Run CometAPI Multi-Model Example

Source: https://docs.agno.com/examples/models/cometapi/multi-model

Commands to clone the Agno repository, navigate to the CometAPI cookbook directory, set up a virtual environment, and execute the multi-model showcase script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/cometapi

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python multi_model.py
```

--------------------------------

### Setup and Run Agno with Upstash Vector DB (Bash)

Source: https://docs.agno.com/knowledge/vector-stores/upstash/usage/upstash-db

These bash commands guide you through setting up the development environment for Agno's Upstash integration. It covers installing necessary Python packages, configuring environment variables for Upstash credentials and OpenAI API key, and executing the main Python script to demonstrate the functionality.

```bash
uv pip install -U upstash-vector pypdf openai agno
export UPSTASH_VECTOR_REST_URL="your-upstash-vector-rest-url"
export UPSTASH_VECTOR_REST_TOKEN="your-upstash-vector-rest-token"
export OPENAI_API_KEY=xxx
python cookbook/08_knowledge/vector_db/upstash_db/upstash_db.py
```

--------------------------------

### Setup and Run Siliconflow Structured Output Example

Source: https://docs.agno.com/examples/models/siliconflow/structured-output

These bash commands provide the necessary steps to clone the `agno` repository, navigate to the example directory, set up a virtual environment, activate it, and finally execute the Python script demonstrating Siliconflow structured output.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/siliconflow

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Mistral Small Agent Example (Bash)

Source: https://docs.agno.com/examples/models/mistral/mistral-small

This bash script outlines the steps to prepare your environment for running the Mistral Small agent example. It involves cloning the `agno` repository, navigating to the specific example directory, setting up a virtual environment, activating it, and executing the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/mistral

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python mistral_small.py
```

--------------------------------

### Setup and Execute Agno Cookbook Demo

Source: https://docs.agno.com/examples/teams/tools/member-tool-hooks

Bash commands to clone the Agno repository, navigate to the tools directory, initialize the virtual environment, and run the member tool hooks example script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python member_tool_hooks.py
```

--------------------------------

### Setup and Run LightRAG Example

Source: https://docs.agno.com/examples/knowledge/vector-db/lightrag/lightrag

Bash script for cloning the Agno repository, setting up a Python virtual environment, configuring API keys, and executing the LightRAG example. Requires LIGHTRAG_API_KEY environment variable to be set before running.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/vector_db/lightrag

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export LIGHTRAG_API_KEY="***"

python lightrag.py
```

--------------------------------

### Setup and Run Decision Logging Example

Source: https://docs.agno.com/examples/learning/decision-logs/decision-log-always

Bash script commands to clone the Agno repository, navigate to the decision logs example directory, create a Python virtual environment, and execute the automatic decision logging demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/09_decision_logs

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_decision_log_always.py
```

--------------------------------

### Setup and Execute Anthropic Thinking Example (Bash)

Source: https://docs.agno.com/examples/models/anthropic/thinking

This bash script outlines the steps to clone the agno repository, navigate to the Anthropic cookbook example, set up a virtual environment, and execute the thinking.py script to run the agent example.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/anthropic\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython thinking.py
```

--------------------------------

### Install Ollama Model

Source: https://docs.agno.com/models/providers/local/ollama/usage/knowledge

Bash command to pull the llama3.2 model from Ollama. This must be executed after installing Ollama following the official installation guide.

```bash
ollama pull llama3.2
```

--------------------------------

### Setup and Run Azure OpenAI Reasoning Tools Example

Source: https://docs.agno.com/examples/reasoning/tools/azure-openai-reasoning-tools

Bash script commands to clone the Agno repository, navigate to the reasoning tools cookbook example, set up a Python virtual environment, and execute the Azure OpenAI reasoning tools demonstration.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python azure_openai_reasoning_tools.py
```

--------------------------------

### Setup and Run MCP Server Example in Bash

Source: https://docs.agno.com/examples/tools/mcp/multiple-servers-allow-partial-failure

Shell script commands to clone the Agno repository, set up a Python virtual environment, configure API keys, and execute the MCP server example with partial failure handling.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools/mcp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Export relevant API keys
export ACCUWEATHER_API_KEY="***"
export BRAVE_API_KEY="***"

python multiple_servers_allow_partial_failure.py
```

--------------------------------

### Setup and Run vLLM Retry Example

Source: https://docs.agno.com/examples/models/vllm/retry

Shell script commands to clone the Agno repository, navigate to the vLLM example directory, create a Python virtual environment, and execute the retry demonstration script. This sets up the necessary dependencies and runs the retry.py example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/vllm

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run Vertex AI Search Example

Source: https://docs.agno.com/examples/models/google/gemini/vertex-ai-search

Bash script to clone the Agno repository, set up a virtual environment, and execute the Vertex AI Search example. Includes repository cloning, environment activation, and Python script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python vertex_ai_search.py
```

--------------------------------

### Clone and Run Twilio Tools Example

Source: https://docs.agno.com/examples/tools/twilio-tools

Set up the Agno repository, create a virtual environment, and execute the Twilio tools example script. This demonstrates the complete workflow from environment setup to running the agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python twilio_tools.py
```

--------------------------------

### Setup and Execute ScrapeGraph Tools Example

Source: https://docs.agno.com/examples/tools/scrapegraph-tools

Shell commands to clone the Agno repository, set up the environment using the provided demo script, and execute the ScrapeGraph tools cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python scrapegraph_tools.py
```

--------------------------------

### Setup and Run Remote Agent Examples

Source: https://docs.agno.com/examples/agent-os/remote/remote-agent

Bash commands to clone the Agno repository, set up the required virtual environment, and execute the remote agent script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/remote

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_remote_agent.py
```

--------------------------------

### Setup and Run OpenAI Reasoning Tools Example

Source: https://docs.agno.com/examples/reasoning/tools/openai-reasoning-tools

Bash script for cloning the agno repository, setting up a Python virtual environment, and executing the OpenAI reasoning tools example. Includes repository navigation, environment activation, and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python openai_reasoning_tools.py
```

--------------------------------

### Run Agno AgentOS Basic Example in Bash

Source: https://docs.agno.com/examples/agent-os/os-config/basic

Shell commands to clone the repository, prepare the environment using a setup script, and run the Python application.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/os_config

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python basic.py
```

--------------------------------

### Setup and Run PubMed Example via CLI

Source: https://docs.agno.com/examples/tools/pubmed-tools

Bash commands to clone the Agno repository, set up the required virtual environment using the provided demo script, and execute the PubMed tools example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python pubmed_tools.py
```

--------------------------------

### Setup and Run Agno Workflow Examples

Source: https://docs.agno.com/examples/workflows/advanced-concepts/history/step-history

Bash commands to clone the Agno repository, set up a virtual environment, and execute the workflow history demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/06_advanced_concepts/history

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python step_history.py
```

--------------------------------

### Setup and Execution Commands for Agno Team Demo

Source: https://docs.agno.com/examples/teams/human-in-the-loop/external-tool-execution

Bash commands to clone the Agno repository, initialize the environment using the provided setup script, and run the external tool execution example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/human_in_the_loop

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python external_tool_execution.py
```

--------------------------------

### Setup and Run Groq Retry Example

Source: https://docs.agno.com/examples/models/groq/retry

Shell commands to clone the Agno repository, set up the virtual environment, and execute the retry demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/groq

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run Broadcast Debate Example

Source: https://docs.agno.com/examples/teams/modes/broadcast/debate

Provides shell commands to clone the Agno repository, navigate to the broadcast debate example directory, set up a virtual environment, and execute the debate script. This demonstrates the complete workflow for running the structured debate example.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/03_teams/modes/broadcast

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 02_debate.py
```

--------------------------------

### Setup and Run Agno Agent with Cerebras OpenAI

Source: https://docs.agno.com/models/providers/gateways/cerebras-openai/usage/knowledge

These bash commands guide the user through setting up the environment for the Agno agent. It includes setting the Cerebras API key, installing necessary Python dependencies using 'uv pip', and finally executing the Python script that runs the agent.

```bash
export CEREBRAS_API_KEY=xxx
```

```bash
uv pip install -U openai sqlalchemy pgvector pypdf agno
```

```bash
python cookbook/11_models/cerebras_openai/knowledge.py
```

--------------------------------

### Setup and Run LlamaCpp Structured Output Example

Source: https://docs.agno.com/examples/models/llama-cpp/structured-output

Commands to clone the Agno repository, set up the environment, and execute the structured output script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/llama_cpp

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output.py
```

--------------------------------

### Setup and Run Gemini External URL Example

Source: https://docs.agno.com/examples/models/google/gemini/external-url-input

Bash commands to clone the Agno repository, navigate to the Gemini examples directory, set up the virtual environment, and execute the Python script for analyzing external URLs.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python external_url_input.py
```

--------------------------------

### Setup and Run Agno Claude Example

Source: https://docs.agno.com/examples/models/aws/claude/db

Bash script for cloning the Agno repository, setting up a Python virtual environment, and executing the Claude DB example. Creates an isolated development environment using the demo_setup.sh script.

```Bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/aws/claude

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python db.py
```

--------------------------------

### Setup and Execution Environment for Qdrant Filtering

Source: https://docs.agno.com/examples/knowledge/filters/vector-dbs/filtering-qdrant-db

Shell commands to clone the Agno repository, configure the local environment using the provided setup scripts, and run the Qdrant filtering example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/filters/vector_dbs

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python filtering_qdrant_db.py
```

--------------------------------

### Setup and Execute the CEL Routing Workflow Example (Bash)

Source: https://docs.agno.com/examples/workflows/cel-expressions/router/cel-previous-step-route

This Bash script provides the necessary commands to set up the development environment and run the Python example demonstrating CEL-based workflow routing. It covers cloning the `agno` repository, navigating to the specific example directory, creating and activating a virtual environment, and finally executing the `cel_previous_step_route.py` script. This allows users to quickly replicate and test the workflow locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/04_workflows/07_cel_expressions/router

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python cel_previous_step_route.py
```

--------------------------------

### Setup and Run Agno CSV Reader Example

Source: https://docs.agno.com/examples/knowledge/readers/csv-reader-custom-encodings

This bash script provides instructions to set up the Agno project, create a virtual environment, and run the Python example for custom CSV encodings. It includes steps for cloning the repository, navigating to the example directory, setting up the environment, and optionally running a PgVector database using Docker.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/07_knowledge/readers

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python csv_reader_custom_encodings.py
```

--------------------------------

### Setup and Run Web Tools Example

Source: https://docs.agno.com/examples/tools/web-tools

Shell script commands to clone the Agno repository, navigate to the tools cookbook directory, set up a Python virtual environment, and execute the web tools example. This demonstrates the complete workflow for testing WebTools functionality with an Agno agent.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python web_tools.py
```

--------------------------------

### Setup and Run Thinking Agent Example

Source: https://docs.agno.com/examples/models/google/gemini/thinking-agent

Bash commands to clone the Agno repository, navigate to the Google Gemini cookbook directory, initialize the environment, and execute the thinking agent script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/google/gemini

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python thinking_agent.py
```

--------------------------------

### Setup and Run Session State Hooks Example in Bash

Source: https://docs.agno.com/examples/agents/hooks/session-state-hooks

Provides shell commands to clone the Agno repository, navigate to the hooks example directory, set up a Python virtual environment, and execute the session state hooks demonstration script.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/02_agents/09_hooks
./scripts/demo_setup.sh
source .venvs/demo/bin/activate
python session_state_hooks.py
```

--------------------------------

### Setup and Run Unsplash Tools Example in Bash

Source: https://docs.agno.com/examples/tools/unsplash-tools

This snippet provides bash commands to clone the Agno repository, navigate to the relevant example directory, set up a Python virtual environment, and execute the `unsplash_tools.py` script. This is a common workflow for running Agno cookbook examples locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python unsplash_tools.py
```

--------------------------------

### Setup and Run Llama Knowledge Example

Source: https://docs.agno.com/examples/models/meta/llama/knowledge

Bash script commands to clone the Agno repository, set up a Python virtual environment, optionally run PgVector with Docker, and execute the Llama knowledge example. Includes steps for environment activation and optional vector database initialization.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/meta/llama

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

# Optiona: Run PgVector (needs docker)
./cookbook/scripts/run_pgvector.sh

python knowledge.py
```

--------------------------------

### Setup and Run LangDB Data Analyst Example

Source: https://docs.agno.com/examples/models/langdb/data-analyst

Bash script for cloning the Agno repository, setting up a virtual environment, and running the data analyst example. Includes repository cloning, environment activation, and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/langdb

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python data_analyst.py
```

--------------------------------

### Setup and Run xAI Retry Example

Source: https://docs.agno.com/examples/models/xai/retry

Bash commands to clone the Agno repository, navigate to the xAI cookbook directory, set up the virtual environment, and execute the retry demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/xai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Setup and Run Agno Reasoning Example with Bash

Source: https://docs.agno.com/examples/reasoning/agents/is-9-11-bigger-than-9-9

Provides shell commands to clone the Agno repository, navigate to the reasoning agents cookbook, set up a Python virtual environment, and execute the decimal comparison reasoning example. Includes repository cloning, environment activation, and script execution steps.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/10_reasoning/agents

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python is_9_11_bigger_than_9_9.py
```

--------------------------------

### Setup and Run Agno PythonTools Example

Source: https://docs.agno.com/examples/tools/python-tools

Bash commands to clone the Agno repository, set up the environment, and execute the Python tools cookbook example. It includes steps for repository cloning, directory navigation, and virtual environment activation.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/91_tools

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python python_tools.py
```

--------------------------------

### Setup and Run Xai Live Search Agent Example

Source: https://docs.agno.com/examples/models/xai/live-search-agent

Bash script commands to clone the agno repository, set up a Python virtual environment, and execute the live search agent example. This includes repository cloning, environment activation, and running the Python script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/xai

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python live_search_agent.py
```

--------------------------------

### Run Llama Cpp Basic Example Script in Bash

Source: https://docs.agno.com/examples/models/llama-cpp/basic

This bash snippet provides step-by-step instructions to set up and run the `basic.py` example. It covers cloning the Agno repository, navigating to the example directory, creating and activating a Python virtual environment, and finally executing the Python script.

```bash
# Clone and setup repo\ngit clone https://github.com/agno-agi/agno.git\ncd agno/cookbook/90_models/llama_cpp\n\n# Create and activate virtual environment\n./scripts/demo_setup.sh\nsource .venvs/demo/bin/activate\n\npython basic.py
```

--------------------------------

### Run Agno Session Context Summary Mode Example

Source: https://docs.agno.com/examples/learning/session-context/summary-mode

This snippet provides instructions to clone the Agno repository, navigate to the example directory, set up a virtual environment, and execute the Python script demonstrating the session context summary mode. It outlines the necessary steps to get the example running.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/03_session_context

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_summary_mode.py
```

--------------------------------

### Setup and Execute Mistral Cookbook Example

Source: https://docs.agno.com/examples/models/mistral/structured-output-with-tool-use

Shell commands to clone the Agno repository, navigate to the Mistral cookbook directory, set up a virtual environment, and execute the structured output script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/mistral

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python structured_output_with_tool_use.py
```

--------------------------------

### Setup and Execute A2A Error Handling Example

Source: https://docs.agno.com/examples/agent-os/client-a2a/error-handling

Commands for cloning the Agno repository, setting up the environment using a shell script, and running the error handling cookbook example.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/client_a2a

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 04_error_handling.py
```

--------------------------------

### Run Custom Store Example from Command Line

Source: https://docs.agno.com/examples/learning/custom-stores/minimal-custom-store

This snippet provides shell commands for setting up and running the custom store example. It includes steps to clone the repository, navigate to the specific example, create and activate a virtual environment, and execute the Python script to see the custom store functionality in action.

```bash
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/08_learning/08_custom_stores

./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python 01_minimal_custom_store.py
```

--------------------------------

### Setup and Run NVIDIA Retry Example

Source: https://docs.agno.com/examples/models/nvidia/retry

Commands to clone the Agno repository, set up a virtual environment, and execute the retry demonstration script.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/90_models/nvidia

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python retry.py
```

--------------------------------

### Run AgentOS Scheduler Example

Source: https://docs.agno.com/examples/agent-os/scheduler/scheduler-with-agentos

This Bash script provides instructions to set up and run the AgentOS scheduler example. It covers cloning the Agno repository, navigating to the example directory, creating and activating a Python virtual environment, and finally executing the `scheduler_with_agentos.py` script. This allows users to quickly get the example running locally.

```bash
# Clone and setup repo
git clone https://github.com/agno-agi/agno.git
cd agno/cookbook/05_agent_os/scheduler

# Create and activate virtual environment
./scripts/demo_setup.sh
source .venvs/demo/bin/activate

python scheduler_with_agentos.py
```

--------------------------------

### Setup and Run Cohere Image Agent Example (Bash)

Source: https://docs.agno.com/examples/models/cohere/image-agent

These bash commands provide instructions to clone the Agno repository, navigate to the specific cookbook example directory, set up a virtual environment for dependencies, and execute the Python script for the Cohere Image Agent.

```bash
# Clone and setup repogit clone https://github.com/agno-agi/agno.gitcd agno/cookbook/90_models/cohere# Create and activate virtual environment./scripts/demo_setup.shsource .venvs/demo/bin/activatepython image_agent.py
```