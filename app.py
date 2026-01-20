import streamlit as st
import re

st.set_page_config(page_title="Calculator App", page_icon="🧮")
st.title("🧮 Calculator App")

expression = st.text_input("Enter your calculation", placeholder="Example: 25*(4+6)")

def safe_eval(expr):
    # Allow only numbers and math operators
    if not re.fullmatch(r"[0-9+\-*/(). ]+", expr):
        raise ValueError("Invalid characters")
    return eval(expr)

if st.button("Calculate"):
    try:
        result = safe_eval(expression)
        st.success(f"Result: {result}")
    except:
        st.error("Calculation failed")
