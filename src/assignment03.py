from turtle import *

def init():
    # initializes the screen and the turtle

    setup(1000, 1000)
    hideturtle()
    speed('fastest')

def smooth(data, smoothing_factor):
    # data: list, smoothing_factor: float
    # the function that smooths the data, using the smoothing factor
    # returns new_data

    new_data = []
    for i in range(len(data)):
        if i == 0:
            new_data.append((1 - smoothing_factor/2) * data[i] + smoothing_factor/2 * data[i+1])
        elif i == len(data) - 1:
            new_data.append((1 - smoothing_factor/2) * data[i] + smoothing_factor/2 * data[i-1])
        else:
            new_data.append((1 - smoothing_factor) * data[i] + smoothing_factor/2 * data[i+1] + smoothing_factor/2 * data[i-1])
    
    return new_data

def locate_pen(x, y):
    # x, y: int
    # moves the pen to the given coordinates

    penup()
    goto(x, y)
    pendown()

def draw_line_coord(x, y, x2, y2, size=1):
    # x, y, x2, y2: int, size: int
    # draws a line from (x, y) to (x2, y2)

    pensize(size)
    locate_pen(x, y)
    goto(x2, y2)

def draw_line_dir(angle, length, size=2):
    # angle: int, length: int, size: int
    # draws a line in the given angle and length

    pensize(size)

    left(angle)
    forward(length)
    left(180)

    penup()
    forward(length)
    pendown()
    left(angle)

def draw_bar(x, y, width, height, color, size=3):
    # x, y, width, height: int, color: str, size: int
    # draws a bar in the given coordinates and size

    pensize(size)
    locate_pen(x, y)
    fillcolor(color)

    begin_fill()
    goto(x + width, y)
    goto(x + width, y + height)
    goto(x, y + height)
    goto(x, y)
    end_fill()

def draw_bar_chart(data, x, y, width=400, height=350):
    # data: list, x, y: int, width, height: int
    # draws a bar chart in the given data, using the function draw_bar

    spacing = 40
    horizontal_space = 20
    bar_color = ['red', 'blue', 'yellow', 'purple']
    bar_multiple = height / max(data)

    draw_line_coord(x, y, x + width + horizontal_space, y, 3)
    
    i = 0
    while(i + spacing <= height):
        i = i + spacing
        draw_line_coord(x, y + i, x + width, y + i, 1)
    
    bar_width = (width - (len(data)-1) * horizontal_space) / len(data)

    for i in range(len(data)):
        draw_bar(x + i * (bar_width + horizontal_space), y, bar_width, data[i] * bar_multiple, bar_color[i % len(bar_color)])

def draw_pie_slice(radius, angle):
    # radius: int, angle: int
    # draws a pie slice in the given radius and angle

    pensize(2)

    draw_line_dir(90, radius)
    circle(radius, angle)
    draw_line_dir(90, radius)

def draw_pie_chart(data, x, y, radius=200, angle=90):
    # data: list, x, y: int, radius, angle: int
    # draws a pie chart in the given data, using the function draw_pie_slice

    pie_multiple = 360 / sum(data)

    locate_pen(x + radius, y)
    setheading(angle)

    for i in range(len(data)):
        draw_pie_slice(radius, data[i] * pie_multiple)

if __name__ == '__main__':
    n = int(input('How many values do you want to enter? '))

    values = []
    for i in range(n):
        values.append(int(input(f'Enter value {i+1}: ')))
    
    smoothing_factor = float(input('Enter a smoothing factor: '))

    init()
    
    draw_bar_chart(values, 0, 25)
    draw_bar_chart(smooth(values, smoothing_factor), 0, -375)

    draw_pie_chart(values, -250, 0)

    done()
