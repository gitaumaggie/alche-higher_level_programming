#!/usr/bin/python3
"""Define the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square with size, position and ID."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set both the width and height of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the square's formatted string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """Update square attributes using positional or keyword values."""
        attributes = ("id", "size", "x", "y")

        if args:
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in attributes:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return a dictionary of the square's attributes."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
