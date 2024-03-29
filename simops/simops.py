class SimOps:
    """Simple operations for math class"""

    def __init__(self, x, y):
        """Init function"""
        self.x = x
        self.y = y

    @property
    def add(self):
        """Add function"""
        return self.x + self.y

    @property
    def subtract(self):
        """Subtract function"""
        return self.x - self.y

    @property
    def multiply(self):
        """"Multiply function"""
        return self.x * self.y

    @property
    def divide(self):
        """Divide function"""
        if self.y == 0:
            raise ValueError('Can not divide by zero!!')
        return self.x / self.y