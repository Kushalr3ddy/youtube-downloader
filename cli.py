from pytube import YouTube
link = input("enter link:")
YouTube(link).streams.first().download