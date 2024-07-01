"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai
from ..models import Thumbnail, Comment

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0.75,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 100,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat()


def get_summary(th:Thumbnail):
    msg = f'I will provide you with a youtube video link. I want you to respond with the summary less than 100 words of the video if possible or return an empty response, indicating a complication. here is the video link: {th.video.yt_link}'
    response = chat_session.send_message(msg)
    print(response.text)

    if response.text:
        th.summary = response.text

def get_sentiment(comment:Comment):
    msg = f'indicate the sentiment of the text that will be provided, there are 3 possible values, positive, neutral, and negative. you must return one of these 3 words, nothing more. incase of complications, return neutral. the text to be analyzed is "{comment.text}"'
    response = chat_session.send_message(msg)
    print(response.text)
    comment.sentiment = response.text
    return response.text
