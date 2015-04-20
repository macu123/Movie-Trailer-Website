import media
import fresh_tomatoes

transformers = media.Movie("Transformers: Age of Extinction",
                           "The fourth installment of the live-action Transformers film series",
                           "Images/transformers.jpeg",
                           "https://www.youtube.com/watch?v=hfGODpB3vCc",
                           "Mark Wahlberg, Stanley Tucci, Kelsey Grammer",
                           "English",
                           "Action & Adventure, Science Fiction & Fantasy",
                           "June 19, 2014")

furious7 = media.Movie("Furious 7",
                       "The seventh installment in The Fast and the Furious franchise",
                       "Images/furious7.jpg",
                       "https://www.youtube.com/watch?v=Skpu5HaVkOc",
                       "Vin Diesel, Paul Walker, Dwayne Johnson",
                       "English",
                       "Mystery & Suspense, Action & Adventure",
                       "March 16, 2015")

kingsman = media.Movie("Kingsman: The Secret Service",
                       "A spy action comedy film based on the comic book The Secret Service",
                       "Images/kingsman.jpg",
                       "https://www.youtube.com/watch?v=m4NCribDx4U",
                       "Colin Firth, Samuel L. Jackson, Mark Strong",
                       "English",
                       "Mystery & Suspense",
                       "13 December, 2014")

letsbecops = media.Movie("Let's Be Cops",
                         "It's the ultimate buddy cop movie except that they're not cops",
                         "Images/letsbecops.jpg",
                         "https://www.youtube.com/watch?v=UKIAZjs__Xc",
                         "Jake Johnson, Damon Wayans, Nina Dobrev",
                         "English",
                         "Action & Adventure, Comedy",
                         "August 13, 2014")



internship = media.Movie("THE INTERNSHIP",
                         "Two salesmen went to a coveted internship at Google",
                         "Images/internship.jpeg",
                         "https://www.youtube.com/watch?v=cdnoqCViqUo",
                         "Vince Vaughn, Owen Wilson",
                         "English",
                         "Drama, Comedy",
                         "June 7, 2013")

captain = media.Movie("Captain America: The Winter Soldier",
                      "It's the sequel to 2011's Captain America: The First Avenger",
                      "Images/captain.jpg",
                      "https://www.youtube.com/watch?v=tbayiPxkUMM",
                      "Chris Evans, Scarlett Johansson, Sebastian Stan",
                      "English",
                      "Action & Adventure, Science Fiction & Fantasy",
                      "March 13, 2014")

movies = [transformers, furious7, kingsman, letsbecops, internship, captain]
fresh_tomatoes.open_movies_page(movies)
