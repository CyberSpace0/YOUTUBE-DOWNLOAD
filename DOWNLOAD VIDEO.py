from pytube import YouTube
link = input('enter the link: ')
video = YouTube(link)
stream = video.streams
stream[1].download(R'D:\videos\Download')
for i in stream:
    print(i)