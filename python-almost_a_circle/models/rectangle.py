
#!/usr/bin/python3
"""Define a Rectangle class that inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """Represent a rectangle with validated dimensions and position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle with dimensions and coordinates."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after validating its type and value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after validating its type and value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the rectangle's horizontal position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal position after validation."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the rectangle's vertical position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical position after validation."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using # and its coordinates."""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the rectangle's formatted string representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update the rectangle using positional or keyword arguments."""
        attributes = ("id", "width", "height", "x", "y")

        if args:
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in attributes:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return a dictionary containing the rectangle's attributes."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
