from pytube import YouTube

# Create a YouTube object for the video you want to download
yt = YouTube("https://www.youtube.com/watch?v=g8e3-bxIty0&list=PLLMmbOLFy25Eohpgb_V3GWKdf8sL0Upvt&index=70&ab_channel=%CE%94%CE%B7%CE%BC%CE%AE%CF%84%CF%81%CE%B7%CF%82%CE%A8%CE%BF%CF%8D%CE%BD%CE%B7%CF%82")

# Select the highest quality stream
stream = yt.streams.get_highest_resolution()

#Download the video to your current working directory
stream.download()