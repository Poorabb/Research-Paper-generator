import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import time

load_dotenv()

st.set_page_config(
    page_title="Research Paper generator — AI Research Paper Decoder",
    page_icon="📄",
    layout="centered"
)

st.markdown("""
<style>
    .stApp { max-width: 780px; margin: auto; }
    .header-badge {
        display: inline-block;
        background: #e6f4ea; color: #1e7e34;
        padding: 4px 12px; border-radius: 20px;
        font-size: 12px; font-weight: 600;
    }
    .result-card {
        background: #f9f9f9; border-left: 3px solid #4f8ef7;
        padding: 1.2rem 1.4rem; border-radius: 8px;
        margin-top: 1rem; line-height: 1.7;
    }
    .meta-row { font-size: 12px; color: #888; margin-top: 8px; }
</style>
""", unsafe_allow_html=True)

st.markdown("# Research Paper generator")
st.markdown('<span class="header-badge">Gemini-powered</span>', unsafe_allow_html=True)
st.caption("Decode landmark AI research papers — tailored to your level and style.")
st.divider()

PAPERS = {
    "Attention Is All You Need (Transformers)": "Attention Is All You Need",
    "BERT: Deep Bidirectional Transformers": "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners": "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis": "Diffusion Models Beat GANs on Image Synthesis",
}

STYLES = ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
LENGTHS = {
    "Short (1-2 paragraphs)": "Short",
    "Medium (3-5 paragraphs)": "Medium",
    "Long (detailed explanation)": "Long",
}

col1, col2 = st.columns(2)

with col1:
    paper_label = st.selectbox("Research Paper", list(PAPERS.keys()))
    paper_input = PAPERS[paper_label]

with col2:
    style_input = st.selectbox("Explanation Style", STYLES)

length_label = st.selectbox("Explanation Depth", list(LENGTHS.keys()))
length_input = LENGTHS[length_label]

custom_question = st.text_input(
    "Specific question? (optional)",
    placeholder="e.g. How does multi-head attention differ from single-head?"
)

st.divider()

if st.button("Generate Explanation", use_container_width=True, type="primary"):
    try:
        template = load_prompt("template.json")
        model = GoogleGenerativeAI(model="gemini-3-flash-preview")

        chain = template | model

        with st.spinner("Reading the paper..."):
            start = time.time()
            result = chain.invoke({
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input,
                "custom_question": custom_question or "No specific question — give a general summary.",
            })
            elapsed = round(time.time() - start, 1)

        st.markdown("### Explanation")
        st.markdown(
            f'<div class="result-card">{result}</div>'
            f'<div class="meta-row">Model: gemini-2.0-flash &nbsp;·&nbsp; {elapsed}s &nbsp;·&nbsp; {style_input} · {LENGTHS[length_label]}</div>',
            unsafe_allow_html=True
        )

        st.download_button(
            "Download as .txt",
            data=result,
            file_name=f"{paper_input[:30].replace(' ', '_')}_explanation.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Something went wrong: {e}")