import fresh_tomatoes
import media

"""Creates six Movie objects, initialising these
objects with title, storyline, link of
poster image and link of video trailer """

aven = media.Movie("Avengers Infinity War",
                   "Avengers: Infinity War is a 2018 American"
                   "superhero film based on the Marvel Comics",
                   "https://upload.wikimedia.org/wikipedia/"
                   "en/4/4d/Avengers_Infinity_War_poster.jpg",
                   "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

padma = media.Movie("Padmaavat",
                    "Padmaavat is a 2018 Indian epic period drama film",
                    "https://upload.wikimedia.org/wikipedia/"
                    "en/7/73/Padmaavat_poster.jpg",
                    "https://www.youtube.com/watch?v=X_5_BLt76c0")

msd = media.Movie("M.S. Dhoni: The Untold Story",
                  "M.S. Dhoni: The Untold Story is a 2016 Indian"
                  "bollywood biographical sports film",
                  "https://upload.wikimedia.org/wikipedia/"
                  "en/thumb/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg/"
                  "220px-M.S._Dhoni_-_"
                  "The_Untold_Story_poster.jpg",
                  "https://www.youtube.com/watch?v=6L6XqWoS8tw")

im3 = media.Movie("Iron Man 3",
                  "Iron Man 3 (stylized onscreen as Iron Man Three)"
                  "is a 2013 American[4] superhero film ",
                  "https://upload.wikimedia.org/wikipedia/"
                  "en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                  "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")

d2 = media.Movie("Chak De! India",
                 "Chak De! India (English: Go For it! India[2]"
                 "or Go! India[3])"
                 "is a 2007 Indian sports film",
                 "https://upload.wikimedia.org/wikipedia/"
                 "en/thumb/0/0c/Chak_De%21_India.jpg/"
                 "220px-Chak_De%21_India.jpg",
                 "https://www.youtube.com/watch?v=6a0-dSMWm5g")

sm = media.Movie("Spider-Man: Homecoming",
                 "Peter Parker tries to balance high school life"
                 "with being Spider-Man, while facing the Vulture.",
                 "https://upload.wikimedia.org/wikipedia/"
                 "en/f/f9/Spider-Man_Homecoming_poster.jpg",
                 "https://www.youtube.com/watch?v=rk-dF1lIbIg")

# Store the Movie objects in a list
movies = [aven,
          padma,
          msd,
          im3,
          d2,
          sm]
# open the browser with the page that have the above mentioned movies
fresh_tomatoes.open_movies_page(movies)
