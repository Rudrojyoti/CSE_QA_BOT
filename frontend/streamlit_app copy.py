import streamlit as st
import requests

st.set_page_config(page_title="CSE Subject Chatbot", page_icon="🎓")

st.title("🎓 CSE Subject Expert Chatbot")

# Subject Selection
subject = st.selectbox(
    "Choose Subject",
    ["General", "OS", "CN", "DBMS"]
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask your CSE doubt...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = requests.post(
        "http://localhost:5000/chat",
        json={"message": user_input, "subject": subject}
    )

    if response.status_code == 200:
        bot_reply = response.json()["response"]
    else:
        bot_reply = "Server error."

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)