from dotenv import load_dotenv
load_dotenv() ## Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini pro model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_response(question):
    ans=model.generate_content(question)
    return ans.text

## initialize our streamlit app

st.set_page_config(page_title='Q&A Demo')
st.title("GeminiChat♊: Your AI Assistant 🤖")
st.write("Welcome to GeminiChat! Ask any question and get answers.")
input=st.text_input("Input: ", key="input")
submit=st.button("Submit", key="submit")

## when submit button is clicked
if submit:
    response=get_response(input)
    st.subheader("The Response is")
    st.write(response)

# Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #000000; /* Black background color */
    color: #ffffff; /* White text color */
    text-align: center;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="footer">Unlock the power of curiosity with GeminiChat♊, your trusted question-answer generator fueled by Gemini.ai 🤖.</p>', unsafe_allow_html=True)