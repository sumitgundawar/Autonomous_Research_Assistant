# Autonomous Research Assistant 🤖📚

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered system that automates research, analysis, and report generation using multi-agent collaboration.

## 🌟 Features

- **Multi-Agent Architecture**:
  - Researcher Agent (arXiv/web scraping)
  - Analyst Agent (data processing/visualization)
  - Writer Agent (RAG-enhanced report generation)
  - Reviewer Agent (quality control)

- **Tech Stack**:
  - Google Gemini Pro (LLM)
  - LangChain (agent orchestration)
  - ChromaDB (vector storage)
  - Streamlit (UI)

## 🛠️ How It Works

```mermaid
graph TD
    A[User Query] --> B(Researcher Agent)
    B --> C[Raw Data]
    C --> D(Analyst Agent)
    D --> E[Insights + Charts]
    E --> F(Writer Agent)
    F --> G[Structured Report]
    G --> H(Reviewer Agent)
    H --> I[Final Output]

🚀 Installation
1. Clone the repository:

git clone https://github.com/yourusername/autonomous-research-assistant.git
cd autonomous-research-assistant

2. Set up environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Configure API keys:
Create .env file:

GOOGLE_API_KEY="your_api_key"
# Optional:
SERPAPI_API_KEY="your_key"  # For web searches

🖥️ Usage
1. Run locally:

streamlit run app/main.py

2. Docker deployment:

docker build -t research-assistant .
docker run -p 8501:8501 --env-file .env research-assistant

🧪 Testing
pytest tests/ -v

🤝 Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/your-feature)
3. Commit changes (git commit -m 'Add some feature')
4. Push to branch (git push origin feature/your-feature)
5. Open a Pull Request

📜 License
MIT License - See LICENSE for details.

📊 Project Structure
Copy
autonomous-research-assistant/
├── agents/
│   ├── researcher.py
│   ├── analyst.py
│   ├── writer.py
│   └── reviewer.py
├── app/
│   ├── main.py          # Streamlit UI
│   └── orchestration.py # Agent workflow
├── tests/
├── vector_db/           # ChromaDB storage
├── .env.example         # API key template
├── Dockerfile
└── requirements.txt

📈 Future Enhancements

Add live web search integration
Implement agent debate system
Support PDF report generation
Add user feedback mechanism


Made with ❤️ by Sumit