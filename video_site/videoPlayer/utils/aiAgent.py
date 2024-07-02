import requests
import os
from youtube_transcript_api import YouTubeTranscriptApi

class SentimentAnalyzer:
    def __init__(self):
        self.api_token = os.environ["HUGGING_FACE_API"]
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
        self.model = "nlptown/bert-base-multilingual-uncased-sentiment"
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model}"

    def send_request(self, text: str):
        payload = {
            "inputs": text
        }
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        if response.status_code == 200:
            result = response.json()[0]  # get the first result
            print("Sentiment analysis result:", result)
            return result
        else:
            print("Failed to get a response:", response.status_code, response.text)
            return None

    def analyze(self, text: str):
        label_map = {
            '1 star': 'negative',
            '2 stars': 'negative',
            '3 stars': 'neutral',
            '4 stars': 'positive',
            '5 stars': 'positive'
        }
        result = self.send_request(text)
        if result:
            print(result)
            sentiment = label_map[result[0]['label']]
            # print(f"Text: {text}\nSentiment: {sentiment}, Score: {result[0]['score']:.4f}\n")
            return sentiment

            # return result
        else:
            return None


class SummaryGenerator:
    def __init__(self):
        self.api_token = os.environ["HUGGING_FACE_API"]
        self.api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }
        self.max_length = 100
        self.min_length = 10

    def get_transcript(self, video_id:str):
        if '=' in video_id:
            video_id = video_id.split('=')[-1]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_transcript = " ".join([entry['text'] for entry in transcript])
        except:
            full_transcript = ''
        return full_transcript

    def summarize_text(self, text):
        if not text:
            return "Not enough information in this video for a summary!"
        data = {
            "inputs": text,
            "parameters": {"max_length": self.max_length, "min_length": self.min_length, "do_sample": False}
        }

        response = requests.post(self.api_url, headers=self.headers, json=data)

        if response.status_code == 200:
            return response.json()[0]['summary_text']
        else:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    def summarize_youtube_video(self, video_id):
        transcript = self.get_transcript(video_id)
        summary = self.summarize_text(transcript)
        return summary


summary_generator = SummaryGenerator()
comment_analyzer = SentimentAnalyzer()

if __name__ == '__main__':
    # Example usage:
    # Ensure you have set the HUGGING_FACE_API environment variable before running this code
    video_id = "https://www.youtube.com/watch?v=QbL0X3B4mjg"

    summary_generator_test = SummaryGenerator()
    summary = summary_generator_test.summarize_youtube_video(video_id)
    print("Summary:", summary)

    # For sentiment analysis, create an instance of SentimentAnalyzer and call the analyze method
    sentiment_analyzer_test = SentimentAnalyzer()
    text = "This is a sample text for sentiment analysis."
    sentiment = sentiment_analyzer_test.analyze(text)
    print("Sentiment:", sentiment)
