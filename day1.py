class Fan:
    def __init__(self):
        self.brand="usha"
        self.cost=1500
        self.color="white"
        self.wings=3
    def on(self):
        print("Fan is on")
    def rotate(self):
        print("Fan is rotate")
    def off(self):
        print("Fan is off")
f1=Fan()
print(f1.brand)
print(f1.cost)
print(f1.wings)
print(f1.color)
f1.on()
f1.rotate()
f1.off()
