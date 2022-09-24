import math

import simple_draw as sd

sd.background_color = (255, 255, 255)
sd.resolution = (1200, 900)
sd.caption = 'Наше рабочее пространство'
first_point = sd.get_point(500, 500)


#vector_1 = sd.get_vector(first_point, 0, 150, 5)
# vector_1.draw()
# vector_2 = sd.get_vector(start_point=vector_1.end_point, width=5, length=200, angle=45)
# vector_2.draw()

def benzol(start_point, length=200, angle=90):
    # start_point = sd.get_point(start_point.x + length, start_point.y + length / 2)
    # x_circle = start_point.x + length * math.sin(math.pi / 3) - length * 1.75
    # y_circle = start_point.y + length * math.cos(math.pi / 3)
    # circle = sd.circle(center_position=sd.get_point(x_circle, y_circle), radius=length * 0.68, color=sd.COLOR_BLACK,
    #                    width=10)

    for number in range(6):
        vector = sd.get_vector(start_point=start_point, width=10, length=length, angle=angle + 60 * number)
        vector.draw()
        start_point = vector.end_point


benzol(start_point=first_point)


# benzol(start_point=sd.get_point(280,350))

def grid(resolution=sd.resolution, step=50):
    x = resolution[0]
    y = resolution[1]
    x_grid = step
    y_grid = step
    while x_grid < x:
        x_line = sd.line(start_point=sd.get_point(x_grid, 0), end_point=sd.get_point(x_grid, y), color=sd.COLOR_BLACK,
                         width=1)
        x_grid += step

    while y_grid < y:
        y_line = sd.line(start_point=sd.get_point(0, y_grid), end_point=sd.get_point(x, y_grid), color=sd.COLOR_BLACK,
                         width=1)
        y_grid += step


grid()

sd.pause()
