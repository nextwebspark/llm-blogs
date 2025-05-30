from openai import OpenAI
import streamlit as st
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'])
llm_model=os.environ['OPENAI_API_MODEL']

def get_completion(prompt, model=llm_model):
    messages = [
        {"role": "system", "content": "Act like a text summarizing tool, give response in json which key 'summary' "},
        {"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content


# Initialize Streamlit UI
st.title("Chatbot Prototype")

# Display a text input box for user query
user_input = st.text_input("Ask me anything:")

if user_input:
    # Pass the user input to the llm_chain for processing
    response = get_completion(user_input)

    # Display the chatbot's response
    st.write("Assistant:", response)


