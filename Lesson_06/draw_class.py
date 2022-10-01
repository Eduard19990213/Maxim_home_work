from random import random

import simple_draw as sd


class DrawClass:

    def __init__(self, resolution, number_of_angles, color, width, length, angle, first_point, step_for_grid):
        self.resolution = resolution
        self.number_of_angles = number_of_angles
        self.color = color
        self.width = width
        self.length = length
        self.angle = angle
        self.first_point = first_point
        self.step_for_grid = step_for_grid

    def grid(self):
        x = self.resolution[0]
        y = self.resolution[1]
        x_os = sd.line(start_point=sd.get_point(0, y / 2), end_point=sd.get_point(x, y / 2), color=sd.COLOR_BLACK,
                       width=4)
        y_os = sd.line(start_point=sd.get_point(x / 2, 0), end_point=sd.get_point(x / 2, y), color=sd.COLOR_BLACK,
                       width=4)
        x_grid = self.step_for_grid
        y_grid = self.step_for_grid
        while x_grid < x:
            xl = sd.line(start_point=sd.get_point(x_grid, 0), end_point=sd.get_point(x_grid, y), color=sd.COLOR_BLACK,
                         width=1)
            x_grid += self.step_for_grid
            xl2 = sd.line(start_point=sd.get_point(x_grid - self.step_for_grid, y / 2 + 0.3 * self.step_for_grid),
                          end_point=sd.get_point(x_grid - self.step_for_grid, y / 2 - 0.3 * self.step_for_grid),
                          color=sd.COLOR_BLACK, width=4)

        while y_grid < y:
            yl = sd.line(start_point=sd.get_point(0, y_grid), end_point=sd.get_point(x, y_grid), color=sd.COLOR_BLACK,
                         width=1)
            y_grid += self.step_for_grid
            yl2 = sd.line(start_point=sd.get_point(x / 2 + 0.3 * self.step_for_grid, y_grid - self.step_for_grid),
                          end_point=sd.get_point(x / 2 - 0.3 * self.step_for_grid, y_grid - self.step_for_grid),
                          color=sd.COLOR_BLACK, width=4)

    def n_ugolnik(self):
        self.grid()
        step_of_angle = 180 * (1 - (self.number_of_angles - 2) / self.number_of_angles)
        angle = self.angle
        start_point = self.first_point
        for number in range(self.number_of_angles):
            vector = sd.get_vector(start_point=start_point, width=self.width, length=self.length,
                                   angle=angle)
            angle += step_of_angle
            vector.draw(color=self.color)
            start_point = vector.end_point

    def snow_fall(self):
        x = self.resolution[0]
        y = self.resolution[1]
        x_snow = x / 20
        x_step = x / 20
        y_step = y / 20
        while True:
            sd.clear_screen()
            while x_snow < x:
                point = sd.get_point(x_snow, y * 19 / 20)
                sd.snowflake(point, length=min(x, y) / 25)
                x_snow += x_step
            x_snow = x_step
            y -= y_step
            if y <= y_step:
                break
            sd.sleep(0.1)
            if sd.user_want_exit():
                break
        sd.pause()

# sd.background_color = (128, 25, 146)
# sd.resolution = (1600, 900)
# my_draw = DrawClass(resolution=sd.resolution, number_of_angles=10, color=sd.COLOR_GREEN, width=2, length=60, angle=60,
#                     first_point=sd.get_point(200, 200), step_for_grid=50)
# my_draw.snow_fall()
# sd.pause()
