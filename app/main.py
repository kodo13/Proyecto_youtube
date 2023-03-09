from pytube import YouTube


yt = YouTube("https://www.youtube.com/watch?v=awK0OUOAIUM")
#introudcimos link a video de youtube

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)