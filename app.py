import streamlit as st

st.set_page_config(page_title="REDNET AI", page_icon="🤖")

st.title("🤖 REDNET AI")
st.write("Ask me anything!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Message REDNET..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # THIS IS WHERE REDNET BRAIN GOES
    # Right now it just echoes. Replace with your AI logic
    response = f"REDNET: I heard you say '{prompt}'. How can I help you?" 
    
    # Save AI message
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
