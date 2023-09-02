class Car:

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def show_info(self):
        print("model", self.model)
        print("color", self.color)
        print("year", self.year)

    def set_color(self, newcolor):
        self.color = newcolor

    def set_model(self, newmodel):
        self.model = newmodel

    def set_year(self, newyear):
        self.year = newyear

    def show_info(self):
        print("color", self.color)
        print("year", self.year)
        print("model", self.model)


myCar = Car("audi", "red", 2000)
myCar.color = "blue"
myCar.show_info()

myCar2 = Car("tesla", "grey", 2020)

myCar2.show_info()
