class dog:
    def __init__(self):
        self.breed="husky"
    def __bark(self):
        print("dog is barking")
    def helper(self):
        self .__bark()

d1=dog()
d1.helper()