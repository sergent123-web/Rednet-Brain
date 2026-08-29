import streamlit as st

st.set_page_config(page_title="REDNET AI", page_icon="🤖")

st.title("🤖 REDNET AI")
st.write("Welcome to REDNET! Voice + Images + PDFs coming soon 🚀")

user_input = st.text_input("Ask REDNET anything:")
if st.button("Send"):
    st.write(f"**REDNET:** Hello! I’m running in web app mode now")
