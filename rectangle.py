class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def __lt__(self, other):
        return self.area() < other.area()


# Getting input for first rectangle
print("Enter details of First Rectangle:")
l1 = float(input("Enter length: "))
b1 = float(input("Enter breadth: "))

# Getting input for second rectangle
print("\nEnter details of Second Rectangle:")
l2 = float(input("Enter length: "))
b2 = float(input("Enter breadth: "))

# Creating objects
r1 = Rectangle(l1, b1)
r2 = Rectangle(l2, b2)

# Comparing areas
print("\nArea of First Rectangle:", r1.area())
print("Area of Second Rectangle:", r2.area())

if r1 < r2:
    print("Second Rectangle has greater area.")
elif r2 < r1:
    print("First Rectangle has greater area.")
else:
    print("Both rectangles have equal area.")
