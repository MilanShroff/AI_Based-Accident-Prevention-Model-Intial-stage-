import streamlit as st
from PIL import Image
from ultralytics import YOLO


model = YOLO('best.pt')


st.title("AI-Based Accident Prevention in MMS")
st.write(
    """
    This smart vision tool helps prevent workplace accidents in MMS operations by ensuring proper use of:
    - 👷 Person detection
    - 🪖 Helmet detection
    - 🦺 Safety vest detection
    """
)


st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    color: #FF6F00;
}
.stApp {
    background-image: url("https://images.unsplash.com/photo-1579547621706-1a9c79d5ffa5");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<p class="big-font">Upload an image below 👇</p>', unsafe_allow_html=True)


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
 
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)


    if st.button("Run Detection"):
        with st.spinner("Running YOLO detection..."):
            results = model.predict(image, device="cpu")

        st.success("✅ Detection complete! See below 👇")


        st.success("✅ Detection complete! See below 👇")

        for r in results:
           im_array = results[0].plot()
           im = Image.fromarray(im_array)
           st.image(im, caption='Detection Result', use_column_width=True)
