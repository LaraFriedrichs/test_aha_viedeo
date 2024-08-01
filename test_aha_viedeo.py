import streamlit as st

st.header("Schau dir dieses Viedeo an!")
st.subheader("Watch this viedeo!")

#viedeo_file=open('C:/Users/49176/OneDrive/Desktop/test_aha_viedeo/viedeo_test.mp4')
#viedeo_bytes=viedeo_file.read()

#st.viedeo(viedeo_bytes)

#url_viedeo='https://github.com/LaraFriedrichs/test_aha_viedeo/blob/main/data/viedeo_test.mp4'
#url_viedeo='https://raw.githubusercontent.com/LaraFriedrichs/test_aha_viedeo/main/data/viedeo_test.mp4'
url_video="https://github.com/Larafriedrichs/test_aha_viedeo/raw/main/viedeo_test.mp4"
#st.video(url_viedeo)

video_file=open(url_video)
video_bytes=video_file.read()

st.video(viedeo_bytes)