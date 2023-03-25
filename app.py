import streamlit as st
import instaloader

st.set_page_config(page_title="Download Instagram Videos", page_icon=":movie_camera:", layout="wide")

# Create a function to download the video
def download_video(post_url):
    L = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(L.context, post_url)
    video_url = post.video_url
    st.write("Downloading...")
    with open(post.owner_username + "_" + post.shortcode + ".mp4", "wb") as f:
        f.write(L.context.get(video_url).read())
    st.write("Download complete!")

# Define the Streamlit app
def app():
    st.title("Download Instagram Videos")
    st.markdown("Enter the Instagram post URL below to download the video.")
    st.markdown("Note: You can download videos from public Instagram accounts only.")

    post_url = st.text_input("Post URL")
    if st.button("Download"):
        if post_url:
            try:
                download_video(post_url)
            except:
                st.write("Invalid URL. Please enter a valid URL.")
        else:
            st.write("Please enter a post URL.")
