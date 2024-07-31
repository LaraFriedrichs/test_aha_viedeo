import streamlit as st

st.header("Schau dir dieses Viedeo an!")
st.subheader("Watch this viedeo!")

#url_viedeo='https://github.com/LaraFriedrichs/test_aha_viedeo/blob/main/data/viedeo_test.mp4'
#url_viedeo='https://raw.githubusercontent.com/LaraFriedrichs/test_aha_viedeo/main/data/viedeo_test.mp4'
url_viedeo="https://github.com/Larafriedrichs/test_aha_viedeo/raw/main/data/viedeo_test.mp4"
st.video(url_viedeo,format="video/mp4",)
