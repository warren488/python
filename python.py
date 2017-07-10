print("gaza")

class Movie:
    def __init__(self, title, year, date, genre, director):
        self.title = title
        self.year = year
        self.date = date
        self.genre = genre
        self.director = director

class Person:
    def __init__(self):
        print('hello')
        self.name = 'warren'
movie1 = Movie("My Movie", 2017, "01-31", "Comedy", "Warren")
movie2 = Movie("Our Movie", 2016, "04-21", "Horror", "Someone")

movies = [movie1, movie2]

x=0
while(x < 2):
    print(movies[x].title)
    x += 1

