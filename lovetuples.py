romantic_movie1 = ("The Princess Bride", 1987, 98, "The story of a man and a woman who lived happily ever after.", ["Buttercup", "Westley", "Fezzik", "Inigo Montoya", "Vizzini"])
romantic_movie2 = ("Groundhog Day", 1993, 101, "He's having the day of his life… over and over again.", ["Phil Connors"])
romantic_movie3 = ("Amélie", 2001, 122, "One person can change your life forever.", ["Amélie Poulain", "Nino Quincampoix", "The Garden Gnome"])

List_of_romantic_movies = [romantic_movie1, romantic_movie2, romantic_movie3]
for movie in List_of_romantic_movies:
    print (movie[0] + " " + str(movie[1]) + ": " + (movie[3]))
# The next one is uneccessarily complicated. I didn't need a whole other list to make this work. Just a basic print statement like the one I wrote at the bottom. But after working through this, I didn't want to give it up so here it is. It still gives the same output.
def search(romantic_movie1):
    indexed = []
    for index, item in enumerate(romantic_movie1):
        if index == 0 or index == 1 or index == 3:
            indexed.append(item)
    print (str(indexed[0]) + ", " + str(indexed[1]) + ", " + str(indexed[2]))
search(romantic_movie1)
search(romantic_movie2)
search(romantic_movie3)
# print (romantic_movie1[0]+ " " + str(romantic_movie1[1]) + " " + romantic_movie1 [3])
