import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
API_KEY = "Your Api key here"
genai.configure(api_key=API_KEY)

def review_code(code_snippet):
    """Send the code snippet to Gemini API for review."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""
    Review the following code for best practices, optimizations, and potential issues:
    ```
    {code_snippet}
    ```
    Provide a detailed analysis and suggestions for improvement.
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("AI-Powered Code Review with Gemini")
st.write("Enter your code below to get a review from Gemini AI.")

code = st.text_area("Paste your code here:", height=200)

if st.button("Review Code"):
    if code.strip():
        with st.spinner("Reviewing your code..."):
            review = review_code(code)
        st.subheader("Code Review Feedback:")
        st.write(review)
    else:
        st.warning("Please enter some code before submitting.")
