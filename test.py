# test glimpse
import os
from glimpse import Glimpse

def test():
    api_key = os.environ.get('OPENAI_API_KEY') # Read the API key from the environment variable
    glimpse = Glimpse(api_key)

    with open("sample_transcript.txt", "w") as f:
        f.write(glimpse.get_transcript("https://youtu.be/hac-cD44HzI"))
    
    with open("transcript.txt", "w") as f:
        f.write(glimpse.get_transcript("https://www.youtube.com/watch?v=eD9ry2Lgglw"))
    
    with open("sample_transcript.txt", "r") as f:
        with open("blog.md", "w") as g:
            g.write(glimpse.get_blog(f.read()))

    with open("glimpse.md", "w") as f:
        f.write(glimpse.get_glimpse("https://www.youtube.com/watch?v=5q87K1WaoFI"))

if __name__ == "__main__":
    test()
