class Fan:
    def __init__(self):
        self.brand="xyz"
        self.cost=1200
        self.color="red"
        self.wings=3
    def on(self):
        print("FAN IS ON")
    def rotate(self):
        print("FAN IS ROTATING")
    def off(self):
        print("FAN IS OFF")
f1=Fan()
print(f1.brand)
print(f1.cost)
print(f1.wings)
print(f1.color)
f1.on()
f1.rotate()
f1.off()