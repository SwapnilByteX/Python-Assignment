class circle:
    Pi = 3.14

    def __init__(self):
        self.radius = 0.0
        self.circumference = 0.0
        self.area = 0.0

    def accept(self):

        self.radius = float(input("enter the radius : "))

    def calculate_area(self):

        self.area = circle.Pi *self.radius **2

    def calculate_circumference(self):

        self.circumference = 2 * circle.Pi * self.radius

    def Display(self):
        print("Radius of circle is : ",self.radius)
        print("Area of cirle is : ",self.area)
        print("Circumference of circle is : ",self.circumference)



def main():

    obj1 = circle()
    obj1.accept()
    obj1.calculate_area()
    obj1.calculate_circumference()
    obj1.Display()

if __name__ == "__main__":
    main()