import os
import streamlit as st
from groq import Groq

# -------------------------
# Configuration
# -------------------------
st.set_page_config(page_title="LLM Calculator", page_icon="🧮")

st.title("🧮 LLM Calculator")
st.write("Powered by **Groq LLM** + **Streamlit**")

# Groq API Key (set as HF Space Secret or env variable)
GROQ_API_KEY ="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"

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found. Please set it as an environment variable.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# -------------------------
# UI
# -------------------------
user_input = st.text_input(
    "Enter a calculation (math expression or natural language):",
    placeholder="e.g. 25 * (4 + 6) or what is 20% of 150"
)

# -------------------------
# LLM Calculator Logic
# -------------------------
def calculate_with_llm(query: str) -> str:
    prompt = f"""
You are a calculator.
- Solve the user's math problem accurately.
- Return ONLY the final numeric answer.
- No explanations, no text.

Problem: {query}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()

# -------------------------
# Action
# -------------------------
if st.button("Calculate"):
    if user_input.strip():
        with st.spinner("Calculating..."):
            try:
                result = calculate_with_llm(user_input)
                st.success(f"✅ Result: **{result}**")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a calculation.")
