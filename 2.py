class Hero:
    def __init__(self):
        self.name="yash"
        self.age=45
        self.numOfMovies=25
    def act(self):
        print("yash is toxic")
h1= Hero()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
h1.Movie="kgf" #adding
print(h1.Movie)
h1.age=47 #modifying
print(h1.age)
del h1.numOfMovies #deleting
print(h1.numOfMovies) # here it will throw an error as it got deleted from the memrory