 import streamlit as st

st.title("Contract Analyzer")

uploaded_file = st.file_uploader("Upload your contract", type=["txt"])

if st.button("Analyze"):
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")

        st.write("Analyzing contract...")
        st.write("### Contract Content:")
        st.write(content)
    else:
        st.write("Please upload a file first.")
