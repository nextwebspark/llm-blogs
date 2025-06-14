from langchain.chains.llm import LLMChain
from langchain.chat_models import ChatOpenAI
import streamlit as st
import os

from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate

_ = load_dotenv(find_dotenv())

llm_model=os.environ['OPENAI_API_MODEL']

langChanllm = ChatOpenAI(temperature=0.0, model=llm_model)

template_string = """Translate the text \
that is delimited by triple backticks \
into {language} in style {style}. \
text: ```{text}```
"""
prompt = PromptTemplate(input_variables=["text", "language", "style"], template=template_string)
translator_chain = LLMChain(llm=langChanllm, prompt=prompt)
st.title("Text Translator App 🖥️")
text = st.text_area("Enter text to translate")
language = st.text_area("Enter language to translate (e.g., French, Spanish, Japanese)")
style = st.text_input("Enter style (polite ton, formal ton, funny ton)")

if st.button("Translate"):
    if text and language and style:
        result = translator_chain.run(language=language, text=text, style=style)
        st.success(result)
    else:
        st.warning("Please enter both the text and target language.")


