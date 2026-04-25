 
if st.button("Analyze"):
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        st.write("Analyzing contract...")
        st.write("### Contract Content:")
        st.write(content)