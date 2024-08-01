from pytube import YouTube

def test_youtube(url):
    try:
        yt = YouTube(url)
        print("Title:", yt.title)
        print("Views:", yt.views)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    test_youtube("https://www.youtube.com/watch?v=_-2ZUciZgls")