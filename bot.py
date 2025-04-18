import streamlit as st

st.title("Hello Custom Chatbot")

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")
credit_card_placeholder = st.empty()

with prompt_placeholder:
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat", 
        value="Hello bot",
    )
    cols[1].form_submit_button(
        "Submit",
    )