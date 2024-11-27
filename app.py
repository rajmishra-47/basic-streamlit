from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate 
import requests
import json

model=OllamaLLM(model="llama3.2")

prompt=""" 

Keep a check on this {context} and and give a simple recipe based on these ingridients {ingridients}

Answer:

"""


prompt_2=""" I am not interested in these {context} show me some thing else"""


text=ChatPromptTemplate.from_template(prompt)

text2=ChatPromptTemplate.from_template(prompt_2)

chain=text | model

chain2=text2 | model



if 'context' not in st.session_state:
    st.session_state.context="Basic Coking"

if 'result' not in st.session_state:
    st.session_state.result=""

if 'userInput' not in st.session_state:
    st.session_state.userInput=""
  

st.session_state.userInput=st.text_input("Enter the ingridients")

if st.session_state.userInput:

    if st.session_state.userInput.lower()=="exit":
        st.write("Good Bye")


    elif st.session_state.userInput!="exit":
            with st.spinner("Loading....."):
                st.session_state.result=chain.invoke({"context":st.session_state.context,"ingridients":st.session_state.userInput})
                st.write(st.session_state.result)
                st.session_state.context+=st.session_state.result


if st.button(" Want some thing else... Type in any ingrident to get or click the button for next",type="primary"):
          st.session_state.result=chain2.invoke({"context":st.session_state.context})
