
class Movie:
    def __init__(self, title, stars,length):
        self.title = title
        self.stars = stars
        self.lenght=length

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_stars(self):
        return self.stars
    
    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self,movies):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
       self.movies.sort(key=lambda movie: movie.get_stars(), reverse=True)

    def get_movies_by_rating(self):
        return self.movies

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':
    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    # TODO 2) Use the Movie class to get the ticket price of one of your movies.
    # TODO 3) Instantiate a NetflixQueue object.
    # TODO 4) Add your movies to the Netflix queue.
    # TODO 5) Print all the movies in your queue.
    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."

    dic={'parasite':[4,132],
    'demon slayer':[4.5,117],
    'joker':[4.05,122],
    'mean girls':[3,97],
    'clueless':[3,97],
    'twilight':[2,122]}
    lst=[]
    mylst=[]
    best=[]
    mynetflix=NetflixQueue(lst)
    for i in dic:
        movie=Movie(i,dic[i[0],dic[i[1]]])
        mynetflix.add_movie(movie)
        lst.append(movie)
    print(lst[-1].get_ticket_price())
    mynetflix.print_movies()
    mynetflix.sort_movies_by_rating()
    best=mynetflix.get_movies_by_rating()

    print('the best movie is',mynetflix.get_best_movie().to_string())
    print('the second best movie is',best[1].to_string())


    



