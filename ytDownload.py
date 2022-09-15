from pytube import YouTube

link1 = "https://www.youtube.com/watch?v=vEQ8CXFWLZU&t=10s"


def download(link, folder):
    yt = YouTube(link)
    print("Title", yt.title)
    print("View: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    yd.download(folder)
