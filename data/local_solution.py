mport streamlit as st

st.header("Schau dir dieses Video an!")
st.subheader("Watch this video!")

#Saved local
with open('C:/Users/49176/OneDrive/Desktop/test_aha_viedeo/viedeo_test.mp4', 'rb') as video_file:
    video_bytes = video_file.read()

st.video(video_bytes)