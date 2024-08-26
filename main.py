from pytube import YouTube
from sys import argv

link = str(input("Enter the Video Link: "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Downloading Completed")
