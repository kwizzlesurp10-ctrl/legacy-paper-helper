import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pandas as pd
import io

st.set_page_config(page_title="LegacyPaperHelper", page_icon="📄", layout="wide")

st.title("LegacyPaperHelper")
st.markdown("### Turn old scanned papers into useful data — simply.")

st.info("This is an early working version. More features coming soon!")

# Sidebar
with st.sidebar:
    st.header("Settings")
    confidence = st.slider("Detection Sensitivity", 0.3, 0.9, 0.6, 0.05)
    st.caption("Higher = more sensitive to text and lines")

uploaded_file = st.file_uploader(
    "Upload a scanned document or photo of a paper", 
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    # Read image
    if uploaded_file.type == "application/pdf":
        # Simple PDF handling (first page)
        from pdf2image import convert_from_bytes
        images = convert_from_bytes(uploaded_file.read(), first_page=1, last_page=1)
        image = np.array(images[0])
    else:
        image = np.array(Image.open(uploaded_file))
    
    st.subheader("Original Document")
    st.image(image, caption="Uploaded document", use_container_width=True)
    
    # Basic processing
    if st.button("Process Document", type="primary"):
        with st.spinner("Analyzing document..."):
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Simple thresholding
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
            
            # Find contours (basic region detection)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Draw rectangles on a copy
            result_img = image.copy()
            regions = []
            
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w > 50 and h > 20:  # Filter small noise
                    cv2.rectangle(result_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    regions.append({"x": x, "y": y, "width": w, "height": h})
            
            st.subheader("Detected Regions")
            st.image(result_img, caption="Green boxes = detected text/figure areas", use_container_width=True)
            
            # Show detected regions as table
            if regions:
                df = pd.DataFrame(regions)
                st.write("**Detected Regions Table**")
                st.dataframe(df)
                
                # Offer CSV download
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download Regions as CSV",
                    data=csv,
                    file_name="detected_regions.csv",
                    mime="text/csv"
                )
            else:
                st.warning("No clear regions detected. Try adjusting the sensitivity slider.")
            
            st.success("Basic analysis complete! Full graph digitization coming in next update.")
