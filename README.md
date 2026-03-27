A Streamlit web application that uses Google Gemini to generate tailored explanations of landmark AI research papers. Users can select a paper, choose an explanation style, set the depth, and optionally ask a specific question — all processed through a LangChain prompt pipeline.

---

## Features

- Explains 4 foundational AI papers: Transformers, BERT, GPT-3, and Diffusion Models
- Four explanation styles: Beginner-Friendly, Technical, Code-Oriented, Mathematical
- Three depth levels: Short, Medium, Long
- Optional custom question field for targeted answers
- Download explanation as a `.txt` file
- Latency tracking per generation
- Clean two-column Streamlit layout with custom CSS

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| LLM | Google Gemini 2.0 Flash |
| Orchestration | LangChain |
| Prompt management | LangChain `load_prompt` (JSON template) |
| Environment | python-dotenv |

---

## Project Structure

```
arxplainer/
├── app.py               # Main Streamlit application
├── template.json        # LangChain prompt template
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed)
└── README.md
```

---

## Setup

### 1. Clone the repository

```bash
https://github.com/Poorabb/Research-Paper-generator.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_api_key_here
```

You can get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## How It Works

1. The user selects a paper, style, depth, and optional question via the Streamlit UI.
2. The inputs are injected into a structured prompt loaded from `template.json`.
3. LangChain chains the prompt with the Gemini model and invokes it.
4. The response is displayed with generation time and a download option.

```
User Input → LangChain Prompt Template → Gemini 2.0 Flash → Streamlit Output
```

---

## Prompt Template

The prompt instructs the model to cover four points for every paper:

1. The core problem the paper solves
2. The key innovation or method introduced
3. Real-world impact and significance
4. Limitations or open questions

If the user provides a custom question, the model answers it directly after the summary.

---

## Supported Papers

| Paper | Year |
|---|---|
| Attention Is All You Need | 2017 |
| BERT: Pre-training of Deep Bidirectional Transformers | 2018 |
| GPT-3: Language Models are Few-Shot Learners | 2020 |
| Diffusion Models Beat GANs on Image Synthesis | 2021 |

---

## Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Your Google Gemini API key |

---

## Requirements

```
streamlit
langchain
langchain-google-genai
langchain-core
python-dotenv
google-generativeai
```

---

## Future Improvements

- Add support for more papers via a search or upload interface
- Stream the model response token-by-token for faster perceived latency
- Add a history panel to compare multiple explanations side by side
- Support PDF upload so users can explain any paper, not just presets
- Add a feedback/rating mechanism per explanation

---

## License

MIT License. See `LICENSE` for details.
