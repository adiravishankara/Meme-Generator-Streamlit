import streamlit as st
import json
import requests
from PIL import Image

class meme_generator:
    def __init__(self):
        st.title("Meme Generator")
        st.button("Get Meme", on_click=lambda: self.refresh_meme)
        self.text = st.text_input("Subreddit", value="wholesomememes")
        self.refresh_meme()

    def get_meme(self, sr='wholesomememes'):
        sr = sr
        url = 'https://meme-api.herokuapp.com/gimme/' + sr
        response = json.loads(requests.request("GET", url).text)
        my_meme = response["url"]
        title = response["title"]
        author = response["author"]
        subreddit = response["subreddit"]
        return my_meme, title, sr, author

    def refresh_meme(self):
        my_meme, title, subreddit, author = self.get_meme(self.text)
        st.image(my_meme, caption='{} by {} on r/{}'.format(title, author, subreddit), width=400)


if __name__ == '__main__':
    meme_generator()