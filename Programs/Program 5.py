class Cuboid:
    def __init__(self,l,w,h):
        self.length=l
        self.width=w
        self.height=h
    def get_area(self):
        return 2*self.length*self.width+2*self.width*self.height+2*self.height*self.length
    def get_volume(self):
        return self.length*self.width*self.height 
data = Cuboid(20,5,16)
print(data.get_area())
print(data.get_volume())