# gives favMovies access to fresh_tomatoes.py
import fresh_tomatoes
# gives favMovies access to movies.py
import movies

# create variable and call class movie found in file Movies. Movie holds data for each individual movie.
white_chicks = movies.Movie("White Chicks",
							"Two FBI agents go undercover to solve a case",
							"https://s-media-cache-ak0.pinimg.com/236x/5a/7e/85/5a7e8544569be952fd62c3d72bd8d24c.jpg",
							"https://www.youtube.com/watch?v=lY2rSYjpFS4")



finding_nemo = movies.Movie("Finding Nemo",
							"While on a quest to find his lost son, an unfunny clown fish finds himself.",
							"http://www.impawards.com/2003/posters/finding_nemo.jpg",
							"https://www.youtube.com/watch?v=wZdpNglLbt8")

v_for_vendetta = movies.Movie("V for Vendetta",
							  "V, a vigilante uses terrorist tactics to fight the oppressors of London's fascist government.",
							  "http://posterwire.com/wp-content/uploads/v_for_vendetta_b.jpg",
							  "https://www.youtube.com/watch?v=k_13fFIrhPk")

dope = movies.Movie("Dope",
					"A Harvard set student confinded to the ghettos of LA finds himself hustling a local Drug Lord",
					"http://t3.gstatic.com/images?q=tbn:ANd9GcRUL9rAXn-DFquwdK8xP3vxFX1oynxjHoyttQoSOaCMwy3I7TI6",
					"https://www.youtube.com/watch?v=JCh1Ude3KSc")

the_internship = movies.Movie("The Internship",
							  "A couple uneducated old guys score competitive internships at Google",
							  "https://cdn.amctheatres.com/Media/Default/BlogPost/movie-news/Autographedposter_internship_AMC2.jpg"
							  "https://www.youtube.com/watch?v=cdnoqCViqUo")

the_joneses = movies.Movie("The Joneses",
							"A group of undercover marketers pose as a family to encourage their new neighbors to purchase loads of stuff.",
							"https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Joneses_poster.jpg/220px-Joneses_poster.jpg",
							"https://www.youtube.com/watch?v=n2Y3GoN2PGw")

movies = [white_chicks, finding_nemo, v_for_vendetta, dope, the_internship, the_joneses]
fresh_tomatoes.open_movies_page(movies)