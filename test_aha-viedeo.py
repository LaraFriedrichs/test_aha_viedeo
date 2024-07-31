import streamlit as st

st.header("Schau dir dieses Viedeo an!")
st.subheader("Watch this viedeo!")

url_viedeo='https://github.com/LaraFriedrichs/test_aha_viedeo/raw/main/viedeo_test.mp4'
st.video(url_viedeo)
st.divider