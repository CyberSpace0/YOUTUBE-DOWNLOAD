from pytube import YouTube
link = input('enter the link: ')
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()