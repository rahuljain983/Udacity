# import is used for Getting the python Built-in or user-defined functionality that will be needed in the code.
import media
import fresh_tomatoes
import os

#to get the current directory and retrieve the images stored at the imnaes folder
currentDirectory = os.getcwd()

#instance of media class to store the information about Movie.
toy_story = media.Movie("Toy Story","A story of boy and his toys having life", currentDirectory + "\Images\Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar","A story of hybrid human-alien called an Avatar" ,currentDirectory + "\Images\Avatar.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
andaz_apna_apna = media.Movie("Andaz Apna Apna","Two young boys of middle-class falls in love with high class girls.",currentDirectory +"\Images\Andaz_apna_apna.jpg","https://www.youtube.com/watch?v=fd_w7Qw8biU")
bahubali = media.Movie("Bahubali","A story of a king born to lead Mahismati",currentDirectory +"\Images\Bahubali.jpg","https://www.youtube.com/watch?v=4zVgyKZZx3o")
movies = [toy_story,avatar,andaz_apna_apna,bahubali]

#calling the open movie page function of fresh_tomatoes to show the movie Url.
fresh_tomatoes.open_movies_page(movies)
