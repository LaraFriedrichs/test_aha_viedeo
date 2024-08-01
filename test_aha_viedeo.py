# import streamlit as st

# st.header("Schau dir dieses Video an!")
# st.subheader("Watch this video!")


# #url_viedeo='https://github.com/LaraFriedrichs/test_aha_viedeo/blob/main/data/viedeo_test.mp4'
# url_video='https://raw.githubusercontent.com/LaraFriedrichs/test_aha_viedeo/main/data/viedeo_test.mp4'
# #url_video="https://github.com/Larafriedrichs/test_aha_viedeo/raw/main/viedeo_test.mp4"
# st.video(url_video)

# #video_file=open(url_video)
# #video_bytes=video_file.read()

# #st.video(video_bytes)

# st.markdown("info")

import streamlit as st

st.header("Schau dir dieses Video an!")
st.subheader("Watch this video!")

#url_video = 'https://raw.githubusercontent.com/LaraFriedrichs/test_aha_viedeo/main/data/viedeo_test.mp4'
url_video='https://github.com/LaraFriedrichs/test_aha_viedeo/raw/main/viedeo_test.mp4'
st.video(url_video)

st.markdown("info")
