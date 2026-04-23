import streamlit as st

st.title("Contract Analysis App")

uploaded_file = st.file_uploader("Upload your contract", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.write("Contract Content:")
    st.write(text)

    if st.button("Analyze"):
        st.write("Analyzing contract...")
