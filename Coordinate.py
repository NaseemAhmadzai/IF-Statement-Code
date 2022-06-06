# Coordinate OOP Example

# Defining a class:
# starts with class [name of class]([Parent Class/SuperClass])
# Beacause we are making a "brand new object", its parent is "object".

from calendar import c


class coordinate(object):
    # Represents the X-Y coordinates in a 2D space.
    # data attributes - this is the data representation of our object.
    # X and Y coordinates.
    
    # The coordinates class will have its own methods 
    # These methods only work with this class. its a how we interact with it.
    
    # The __init__ method - Yes there are two underscores before and after.
    # in other programming languages. this is called constructor. its purpose is to initialize (or construct) and 
    # setup the data in the newly defined instance.
    #it must have self as its first parameter. Any other parameters are optional.
    # in our case, we will need an x and y integer parameters.
    
    def __init__(self, x, y):
        '''
        Initializor for the coordinate class. Sets the X and Y attributes of the coordinate which are the values in a cartesian
        coordinate system.
        param: x and y are integers
        
        '''
        
        self.x = x
        self.y = y
        # self refers to "this current instance" of the object.
        # self.x and self.y refer to the current instance x and y coordinate values.
        # the other x and y are the values from the "outside word" - the parameters
        # that are being passed in.
        
        
        
        # Accessor Methods - it is best to use these two types of "Accessor methods" to protect the properties and data inside
        # the object. They are sometimes known as "getter" and "setter" methods. 
        # Getter methods:
        
        def get_x(self):
            """
            Returns the x_Coordinate of this current instance.
            """
            return self.x
        
        def get_y(self):
            """
            Returns the y_Coordinate of this current instance.
            """
            return self.x
        
        def getCoords(self):
            """
            Returns the x-y coordinates as a tuple.
            """
            return(self.x,self.y)
        
        def set_x(self,x):
            """
            Sets the x-coordinate to the value passed in.
            params: x is an integer.
            returns nothing
            """
            self.x = x
        
        def set_x(self,y):
            """
            Sets the y-coordinate to the value passed in.
            params: y is an integer.
            returns nothing
            """
            self.y = y
        
        def distance(self,other):
           '''
           calculates the distance between self and other object.
           params: other is another coordinate object.
           returns a float whihc is the disance between these two points.
           ''' 
           
           a_sq = (self.x - other.get_x()) ** 2
           b_sq = (self.y - other.get_y()) ** 2
           
           c = (a_sq + b_sq) ** 0.5 # square root of (a^2 + b^2) is the distance.
           return c 
        
        # special methods we can overload.
        def __str__(self): # Yes, two underscores and str for "string".
            '''
            Returns the strings object verson of the coordinate object.
            '''

            # if we dont "overload" and write our own version the __str__ inherited from the parent class object
            # will print out that "memory" adress stuff
            
            return "<" + str(self.x) + ", "+ str(self.y) + ">"
        
        
        # Special operator "=="
        
        def __eq__(self, other): # Overload the equivalance operator.
            '''
            Comparison opereator.
            returns True if both coordinates are the same, otherwise false..
    
            '''
            return (self.x == other.get_x() and (self.y == other.get_y()))
        
        # TOSHOW
        def __add__(self,other):
            '''
            adds two coordinates together by adding relative x's and y's together. 
            '''
            assert isinstance(other,coordinate), "Both oprands must be coordinate object"
            
            c_x = self.get_x() + other.get_x()
            c_y = self.get_y() + other.get_y()
            
            return coordinate(c_x,c_y)
   
   
        #TODO SUBSTRACTION
        
        def __sub__(self,other):
            
            '''
            substracts two coordinates together by asubtracting relative x's and y's together. 
            '''
            assert isinstance(other,coordinate), "Both oprands must be coordinate object"
            # assert <boolean expression to check>, "Error message to show."
            
            c_x = self.get_x() - other.get_x()
            c_y = self.get_y() - other.get_y()
            
            return coordinate(c_x,c_y)
        
        def __mul__(self, other):
            '''
            multiply two coordinates together by multiplying relative x's and y's together.
            param: integer
            returns: A new coordinate object.
            '''
            
            
            assert isinstance(other,int), "Both oprands must be an integer"
            # assert <boolean expression to check>, "Error message to show."
            c1 = coordinate(3,7)
            return coordinate(self.x * other, self.y * other)
            