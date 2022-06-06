from Coordinate import *
#From the coordinate python library file import EVERYTHING - that's the *
class Shape(object):
    #base class for our Shape object.
    
    def __init__(self, x = 0, y = 0):
        '''Basic initializer of our Shape class. Only one "property"
which is the location of the origin of the shape.
params: x and y are integers that represent the coordinates of this
shape. They are optional.'''
        
        self.origin = coordinate(x, y)
        
    def __str__(self):
        '''Return a string representation of this object.'''
        return "Generic shape located at: " + str(self.origin)
    
    def get_origin(self):
        '''Returns the origin of this shape.'''
        
        return self.origin
    
    def set_origin(self, other):
        '''Changes the origin of this object to another location.
parameter: other is a coordinate object.
returns Nothing.'''
        
        assert isinstance(other, coordinate), "Parameter must be a coordinate object."
        
        self.origin.set_x(other.get_x())
        self.origin.set_y(other.get_y())
        
    def same_origin(self, other):
        '''returns True if these two shapes are located at the same origin.'''
        
        assert isinstance(other, Shape), "Param must be an instance of a shape."
        
        return self.get_origin() == other.get_origin()
    
    #How far apart are two shapes?????
    def distance(self, other):
        '''Computes the "straight line" distance between two shapes.
param: an instance of any shape.
returns: the distance between them as a float.'''
        assert isinstance(other, Shape), "Param must be an instance of a shape."
        
        selfLoc = self.get_origin()
        otherLoc = other.get_origin()
        d = selfLoc.distance(otherLoc)
        
        return d
        #Same as the four lines of code above.
        #return self.get_origin().distance(other.get_origin())
    
    def move_by(self, coord):
        '''Moves by the x and y amounts in the coordinate parameter.
param: coord is a coordinate object.
returns nothing.'''
        
        assert isinstance(coord, coordinate), "Parameter must be a Coordinate"
        
        newCoord = self.get_origin() + coord
        
        self.set_origin(newCoord)
        
        
    def same_type(self, other):
        '''returns True if they're the same data type.
param: other is some other thing.
returns: T or F.'''
        
        return type(self) == type(other)
    
    def compatible_type(self, other):
        '''Returns True if object is a descendent of Shape as well.'''
        
        return isinstance(other, Shape)
    
    def get_area(self):
        '''This is a placeholder method.'''
        print("This is a generic Shape instance.")
        print("It has no properties other than its origin")
        print("It has no area")
        return None
class Rectangle(Shape):
    
    def __init__(self, x = 0, y = 0, height = 1, width = 2):
        '''initializer for Rectangle object.
x, y are the coordinate of the object. height and with are of the rectangle.'''
        super().__init__(x, y)
        (self.height, self.width) = (height, width)
        
    def get_height(self):
        '''returns the height of the rectangle.'''
        return self.height
    
    def get_width(self):
        '''returns the width of the rectangle.'''
        return self.width
    
    def set_height(self, h):
        '''Sets the new height of the rectangle. Returns nothing.'''
        self.height = h
        
    def set_width(self, w):
        '''Sets the new height of the rectangle. Returns nothing.'''
        self.width = w
        
    def get_area(self):
        '''returns the area of the rectangle.'''
        return self.height * self.width
    
    
    def __str__(self):
        '''Returns a formatted string of the rectangle shape.'''
        if self.height == self.width:
            shape = "Square at "
            sides = " with side length " + str(self.width)
        else:
            shape = "Rectangle at "
            sides = " with height " + str(self.height) + \
            " and width " + str(self.width)
        return shape + str(self.origin) + sides
class Square(Rectangle): #Making a "Square" class based off of our Rectangle class.
    
    def __init__(self, x = 0, y = 0, side = 1):
        '''initializer for Square object.
x, y and side are integers. x and y are its origin, side is side length.'''
        
        #Need to call the parent class initializer.
        super().__init__(x, y, side, side) #call the superclass initializer/parent class initializer-
        
        
    def get_side(self):
        '''Returns the side length of the square as an int.'''
        return self.height
    
    def set_side(self, s):
        '''Sets the new side length for the square.
param: s is an integer.
Returns nothing.'''
        #Square is based off of rectangle. Make sure you
        #set height and width to the new side length.
        self.height = s #Set the new side length.
        self.width = s
        
    def set_width(self, s):
        '''Override the Rectangle's set_width so that both
height and width are changed.
s is an integer.
Returns nothing.'''
        self.set_side(s)
        
    def set_height(self, s):
        '''Override the Rectangle's set_height so that both
height and width are changed.
s is an integer.
Returns nothing.'''
        self.set_side(s)
       
    #the get_area() and __str__() methods was removed from the Square class
    #b/c we inherit them from the Rectangle class.
    


class Triangle(Shape):
    
    def __init__(self, x = 0, y = 0, s1 = 1, s2 = 2, s3 = 3):
        '''initializer for Triangle object.
x, y are the coordinate of the object. s1, 2 and 3 are the different sidelengths'''
        super().__init__(x, y)
        
        #Side lengths are a tuple of three integers.
        #why? Because I can, and it makes sense to hold them together.
        self.threeSides = (s1, s2, s3)
        
    def get_side(self, sideNum):
        '''Gets one of the three sides.
params: sideNum is an integer from 1-3.
returns: That particular side length.'''
        
        return self.threeSides[sideNum - 1]
        
    def set_side(self, sideNum, sideVal):
        '''sets one of the three sides.
params: sideNum is an integer from 1-3, sideVal is a new side value.
returns: Nothing'''
        (s1, s2, s3) = self.threeSides #unpack the tuple representing the sides.
        
        #Change the side as requested.
        if sideNum == 1:
            s1 = sideVal
        elif sideNum == 2:
            s2 = sideVal
        elif sideNum == 3:
            s3 = sideVal
            
        self.threeSides = (s1, s2, s3) #pack it back up.
        
    def get_area(self):
        '''Calculates and returns the area of the triangle.'''
        #use Heron's formula:
        #https://www.mathopenref.com/heronsformula.html
        (a, b, c) = self.threeSides #unpack the three sides.
        p = (a + b + c)/2
        area = (p * (p - a) * (p - b) * (p - c))**0.5
        
        return area
        
    def __str__(self):
        '''returns a nicely formatted string version of the triangle.'''
        (a, b, c) = self.threeSides #unpack the sides!
        
        if a == b and b == c:
            sideType = "An equilateral "
        elif a == b or b == c or a == c:
            sideType = "An isoceles "
        else:
            sideType = "A scalene "
        
        sides = list(self.threeSides)
        #get the longest sidelength
        c = max(sides)
        cSquared = c*c
        
        #remove it b/c we don't need it anymore.
        sides.remove(c)
        legsSquared = sides[0] * sides[0] + sides[1] * sides[1]
        
        if cSquared == legsSquared:
            angleType = "right "
        elif cSquared > legsSquared:
            angleType = "obtuse "
        else:
            angleType = "acute "
            
        return sideType + angleType + "triangle located at " + str(self.get_origin())

