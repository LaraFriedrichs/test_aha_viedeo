import streamlit as st

st.header("Schau dir dieses Viedeo an!")
st.subheader("Watch this viedeo!")

viedeo_file= open('https://github.com/LaraFriedrichs/test_aha_viedeo/blob/main/viedeo_test.mp4','rb')
video_bytes=video-file.read()
st.video(video_bytes)
st.divider