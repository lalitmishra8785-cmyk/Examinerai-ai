import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="UPSC Mains AI Evaluator")

st.title("🧠 UPSC Mains Answer Evaluation (AI Powered)")

paper = st.selectbox("Select Paper", ["GS-1","GS-2","GS-3","GS-4","Essay"])
question = st.text_area("Paste Question")
answer = st.text_area("Paste Your Answer", height=300)
word_limit = st.radio("Word Limit", ["150","250","Essay"])

if st.button("Evaluate My Answer"):
    prompt = f"""
    You are a UPSC Mains examiner.

    Paper: {paper}
    Word Limit: {word_limit}

    Question:
    {question}

    Answer:
    {answer}

    Evaluate strictly on:
    - Relevance
    - Structure
    - Content depth
    - Language & presentation
    - Value addition

    Give marks out of 40.
    Provide examiner-style feedback.
    Suggest 3–4 precise improvements.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )

    st.subheader("📊 Evaluation Result")
    st.write(response["choices"][0]["message"]["content"])
