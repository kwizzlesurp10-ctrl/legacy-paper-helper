import streamlit as st

st.set_page_config(page_title="LegacyPaperHelper", page_icon="📄")

st.title("LegacyPaperHelper")
st.subheader("Turn old scanned papers into useful data")

st.write("This is a simple demo interface. The full version will use code from dormant GitHub repositories to extract graphs, text, and data from uploaded documents.")

uploaded_file = st.file_uploader("Upload a scanned PDF or image", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    st.success("File uploaded successfully!")
    st.info("In the full version, this would process the document and extract data.")
    
    if st.button("Process Document (Demo)"):
        st.balloons()
        st.success("Demo processing complete! In the real version you would get an Excel/CSV file here.")

st.markdown("---")
st.caption("Built by reviving 4 dormant open source tools")