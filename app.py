import os
import requests
import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")
st.title("🧮 Calculator App")

GROQ_API_KEY = "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"

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not set")
    st.stop()

query = st.text_input(
    "Enter your calculation",
    placeholder="Example: 25 * (4 + 6) or what is 10% of 200"
)

def calculate_with_groq(question):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": f"Calculate and return ONLY the final number: {question}"
            }
        ],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"].strip()

if st.button("Calculate"):
    if query:
        with st.spinner("Calculating..."):
            try:
                result = calculate_with_groq(query)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error("Calculation failed")
    else:
        st.warning("Please enter a calculation")
