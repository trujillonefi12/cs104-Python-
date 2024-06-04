import turtle
import random

# Initialize the turtle
t = turtle.Turtle()
s = turtle.getscreen()


def correctFloatingNumber(prompt, error_message):
    while True:
        try:
            userInput = float(input(prompt))
            return userInput
        except ValueError:
            print(error_message)


def displayColorChoices():
    print("What color would you like your polygon to be?")
    print(
        """
        1 - Red          6 - Blue
        2 - Orange       7 - Purple 
        3 - Black        8 - Violet 
        4 - Green        9 - Gold
        5 - Indigo       10 - Cyan
        11 - Rainbow (Random)
        """
    )


# Function to draw the polygon
def drawPolygon(sides, sideLength, color_choice):
    # Set the color based on user choice
    colors = [
        "red",
        "orange",
        "black",
        "green",
        "indigo",
        "blue",
        "purple",
        "violet",
        "gold",
        "cyan",
    ]

    if color_choice == 11:
        t.color(random.choice(colors))
    else:
        if 1 <= color_choice <= 10:
            t.color(colors[int(color_choice) - 1])
        else:
            print("Invalid color choice, using default color (black).")
            t.color("black")

    extAngle = 360 / sides

    for _ in range(int(sides)):
        t.forward(sideLength)
        t.left(extAngle)


def main():
    while True:
        displayColorChoices()
        choice = correctFloatingNumber("Choice?: ", "Please enter a number!")
        sides = correctFloatingNumber(
            "How many sides for your polygon?: ", "Please enter a number!"
        )
        sideLength = correctFloatingNumber(
            "What side length will your polygon have?: ", "Please enter a number!"
        )
        drawPolygon(sides, sideLength, choice)

        # wANT TO CONTINEUS?
        repeat = input("Would you like to draw another polygon? (y/n): ").lower()
        if repeat != "y":
            break

    s.mainloop()


if __name__ == "__main__":
    main()
