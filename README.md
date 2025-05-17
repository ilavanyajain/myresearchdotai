# MyResearchDotAI

MyResearchDotAI is an AI-powered research assistant that helps you generate research papers and summaries using advanced language models and academic search tools.

## Features
- Uses Anthropic Claude and OpenAI models for research queries
- Integrates with Google Scholar for academic article search
- Supports Wikipedia and web search tools
- Outputs structured research summaries (topic, summary, sources, tools used)
- Keeps your API keys secure (do not commit `.env`)

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ilavanyajain/myresearchdotai.git
   cd myresearchdotai
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv myvenv
   source myvenv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your `.env` file:**
   - Create a `.env` file in the project root with your API keys:
     ```env
     OPENAI_API_KEY=your_openai_key
     ANTHROPIC_API_KEY=your_anthropic_key
     ```
   - **Do not commit your `.env` file!**

## Usage
Run the main script and follow the prompt:
```bash
python main.py
```
You will be asked: `What can I help you research?` Enter your research topic or question, and the assistant will provide a structured summary with sources.

## Project Structure
- `main.py` — Main entry point, orchestrates the research workflow
- `tools.py` — Custom tools for search, Wikipedia, Google Scholar, and saving results
- `.env` — (Not committed) Store your API keys here

## Security
- API keys are never committed to the repository
- If you accidentally commit secrets, follow GitHub's guide to remove them from history

## License
MIT License 