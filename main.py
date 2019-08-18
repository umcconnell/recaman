"""Main module"""
import tkinter

from src.recaman import recaman
from src.recaman_turtle import RecamanTurtle

from src.cli import collect
from src.helpers import can_convert


ARGS = collect({
    "steps": {
        "text": "Iterations (>= 1) of Recamán's sequence (default is 100):",
        "required": False,
        "check": lambda x: can_convert(x, int) and int(x) > 0,
        "transform": lambda x: int(x) if x else 100
    },
    "scale": {
        "text": "Scaling of the drawing: negative float flips drawing (default is 1):",
        "required": False,
        "check": lambda x: can_convert(x, float),
        "transform": lambda x: float(x) if x else 1
    },
    "speed": {
        "text": """Speed of the turtle (default is 6)
    "no animation": 0
    "fast": 10
    "normal": 6
    "slow": 3
    "slowest": 1\n""",
        "required": False,
        "check": lambda x: can_convert(x, int) and int(x) > -1,
        "transform": lambda x: int(x) if x else 6
    },
    "margin": {
        "text": "Space between turtle and left edge of the screen (default is 0):",
        "required": False,
        "check": lambda x: can_convert(x, int),
        "transform": lambda x: int(x) if x else 0
    }
})

TURTLE = RecamanTurtle(ARGS["margin"])
TURTLE.speed(ARGS["speed"])

for step in recaman(ARGS["steps"]):
    TURTLE.draw(step * ARGS["scale"])

# Keep window open until user closes it
tkinter.mainloop()
