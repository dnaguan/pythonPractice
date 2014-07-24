import turtle

def draw_figures():
	window = turtle.Screen()
	window.bgcolor("red")

	square = turtle.Turtle()
	square.shape("turtle")
	square.color("yellow")
	square.speed(2)

	square.forward(100)
	square.right(90)
	square.forward(100)
	square.right(90)
	square.forward(100)
	square.right(90)
	square.forward(100)
	square.right(90)

	circle = turtle.Turtle()
	circle.shape("classic")
	circle.color("blue")
	circle.circle(100)

	triangle = turtle.Turtle()
	triangle.shape("triangle")
	triangle.color("green")
	triangle.seth(60)
	triangle.forward(200)
	triangle.left(120)
	triangle.forward(200)
	triangle.left(120)
	triangle.forward(200)

	window.exitonclick()

draw_figures()