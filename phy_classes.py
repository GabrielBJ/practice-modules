#!/usr/bin/env python3

# Creating a class named Physics_Courses

class Physics_Courses:

    # Properties/Atributes
    x1 = "computational physics"
    x2 = "quantum mechanics II"
    x3 = "solid state physics"
    x4 = "electodynamics II"

# Create a class names Physics_Courses2

class Physics_Courses2:
    """
    J.G.B.B
    """

    # define an __init__ method 
    def __init__(self, course, grade):
        """
        Description: This method will initialize the properties of the class.
        """
        self.course = course
        self.grade = grade

# Now let's practice inheritance!!!
# Create a base class named Physics_Courses3

class Physics_Courses3:

    # define an __init__ method 
    def __init__(self, course, grade):
        """
        Description: This method will initialize the properties of the class.
        """
        self.course = course
        self.grade = grade

    # define a method named print_info
    def print_info(self):
        print(self.course, self.grade)

# Creating derived classes

class all_courses(Physics_Courses3):
    pass

# Create a derived class named all_courses_customised with a new 
# __init__ method

class all_courses_customised(Physics_Courses3):
    def __init__(self, course, grade, average):
        self.course = course
        self.grade = grade
        self.average = average
       
# Adding new methods to the derived class

class all_courses_customised2(Physics_Courses3):
    
    # define a __init__ method 
    def __init__(self,course, grade, average, field_of_study):
        
        # Use super() function to inherit the properties of the base class
        super().__init__(course, grade)

        # Add new properties to the derived class
        self.average = average
        self.field_of_study = field_of_study

    # adding new methods to the derived class
    def print_all_values(self):
        print(self.course, self.grade, self.average, self.field_of_study)


########################################################################

# Magic methods and encapsulation 

class Sensor():

    def __init__(self, name, location):
        self.name = name
        self._location = location
        self.__version = "1.0"

    # a getter function 
    def get_version(self):
        print(f"The sensor version is {self.__version}")

    # a setter function 
    def set_version(self, version):
        self.__version = version

########################################################################
# Exercise 1: iterator class

class sequence():

    def __iter__(self):
        # Define attribute to start from 1
        self.x = 1
        # Return it
        return self

    def __next__(self):
        y = self.x
        # Build iterator adding 1 to the previous value
        self.x += 1
        # Return the iterator
        return y 


