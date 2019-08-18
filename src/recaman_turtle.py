"""Recaman turtle"""
import turtle


class RecamanTurtle(turtle.Turtle):
    """Extention of turtle.Turtle adapted to Recamán's sequence"""

    def __init__(self, margin: int = 0):
        """Initialize RecamanTurtle

        :param margin: space between turtle's starting position and edge of the
        screen (default is 0)
        :type margin: int
        """
        super(RecamanTurtle, self).__init__()

        # Start with bottom semi-circle
        self.alignment = -1
        self.start_offset = -self.getscreen().window_width() / 2 + margin

        # Move turtle to left edge of window and leave 20px margin
        self.penup()
        self.setx(self.start_offset)
        self.left(90)
        self.pendown()

    def draw(self, pos: int):
        """Draw a step of Recamán's sequence

        :param pos: term / value of Recamán's sequence to move the turtle to
        :type pos: int
        """
        # Calculate steps to desired position
        step = self.xcor() + -self.start_offset - pos

        self.circle(step / 2, 180 * self.alignment)
        self.left(180)
        self.alignment *= -1
