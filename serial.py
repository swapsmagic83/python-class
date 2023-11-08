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

    def __init__(self,start):
        self.start = self.next = start

    def generate(self):
        self.next = self.next + 1
        return self.next
    def reset(self):
        self.next = self.start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start+1}>"

