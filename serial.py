"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """takes in a number to generate""" 
        self.start = self.current = start
        

    def reset(self):
        """resets the starting number to the input value"""
        self.current = self.start
       

    def generate(self):
        """increments starting number eachtime function is called"""
        res = self.current
        if self.current == self.start:
            res = self.start
        self.current = self.current + 1
        return res

