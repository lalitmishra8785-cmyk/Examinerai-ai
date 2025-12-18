import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="ExaminerAI – UPSC Mains Evaluator")

st.title("🧠 ExaminerAI – UPSC Mains Answer Evaluation")
st.caption("Think like an examiner. Write like a topper.")

paper = st.selectbox("Select Paper", ["GS-1","GS-2","GS-3","GS-4","Essay"])
question = st.text_area("Paste UPSC Question")
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
1. Relevance
2. Structure
3. Content depth
4. Language & presentation
5. Value addition

Give marks out of 40.
Provide examiner-style feedback.
Suggest precise improvements.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    st.subheader("📊 Evaluation Result")
    st.write(response["choices"][0]["message"]["content"])

st.markdown(
    "*Disclaimer: This is an AI-based evaluation aligned with UPSC trends. Final marks depend on examiner discretion.*"
)
