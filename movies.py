#module that includes functions to open url in browser window
import webbrowser

# create a class to hold functions
# init holds a place in memory for function values
# self creates an instance of the object title, ect. 
class = Movie():
	def __init__(self, movie_title, movie_about, poster_img, trailer_youtube):
		self.title = movie_title
		self.about = movie_about
		self.poster.img_url = poster_img
		self.trailer_youtube_url = trailer_youtube

	# plays youtube movie trailer in browser
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)
