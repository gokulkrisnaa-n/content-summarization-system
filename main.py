__author__ = 'gokulkrisnaa-n'

# Importing necessary libraries
import openai
import streamlit as st
import os
from dotenv import load_dotenv

# Loading API keys from .env file
load_dotenv()
gpt_api_key = os.getenv("GPT_API_KEY")


# Content summarization using GPT API
def summarize_text(prompt, max_tokens=200, temperature=0.3, top_p=0.2):
    try:
        openai.api_key = gpt_api_key
        response = openai.ChatCompletion.create(
            model='gpt-4o-mini',
            stop=None,
            messages=[
                # Instructs how the model should behave
                {'role': 'developer', 'content': 'Consider yourself as the BEST content summarization system. You have to be perfect in text summarization.'},
                # Sends the user text to summarize as prompt to the GPT model
                {'role': 'user', 'content': f'Summarize this text: {prompt}'}
            ],
            max_tokens=max_tokens,
            top_p=top_p,
            temperature=temperature
        )

        # Response from the model is stored
        generated_summary = response.choices[0].message.content
        return generated_summary

    except Exception as e:
        return f'Error: {str(e)}'


# Creating UI for chatbot using streamlit
def run_ui():
    st.title('Content Summarization System')
    st.write('Type text below to summarize the content')

    user_input = st.text_area("Enter text here:")
    user_max_tokens = st.slider("Select max tokens:", min_value=50, max_value=300, value=200, step=10)
    user_temperature = st.slider("Select temperature:", min_value=0.0, max_value=1.0, value=0.3, step=0.05)
    user_top_p = st.slider("Select top-p:", min_value=0.0, max_value=1.0, value=0.2, step=0.05)

    if st.button("Summarize"):
        if user_input.strip():
            with st.spinner("Generating summary..."):
                summary = summarize_text(user_input, user_max_tokens, user_temperature, user_top_p)
                st.subheader("Summary:")
                st.write(summary)
        else:
            st.warning("Please enter text to summarize.")


if __name__ == '__main__':
    run_ui()
