import math
import simple_draw as sd

from Maxim_home_work.Lesson_06.draw_class import DrawClass

sd.resolution = (1600, 900)


class ExtendDrawClass(DrawClass):

    def __init__(self, definition, **kwargs):
        self.definition = definition
        super().__init__(**kwargs)

    def base_function(self):
        self.grid()
        """  Область определения представляет собой крайние точки, отрезок между которыми разбивается на единицы

        :return: 
        """
        x = self.definition[0]
        return x

    def parabpla2(self):
        x = self.base_function()
        while x < self.definition[1]:
            x_coord = x + sd.resolution[0] / 2
            try:
                y_coord = x ** 2 + sd.resolution[1] / 2
                sd.circle(sd.get_point(x_coord, y_coord), radius=10, color=sd.random_color(), width=10)
            except Exception:
                print(f'Значение {x_coord} меньше нуля')
            x += 1

    def sqrt_graph(self):
        x = self.base_function()
        while x < self.definition[1]:
            x_coord = x + sd.resolution[0] / 2
            try:
                y_coord = math.sqrt(x) + sd.resolution[1] / 2
                sd.circle(sd.get_point(x_coord, y_coord), radius=10, color=sd.random_color(), width=10)
            except Exception:
                print(f'Значение {x_coord} меньше нуля')
            x += self.step_for_grid


my_draw = ExtendDrawClass(resolution=sd.resolution, number_of_angles=10, color=sd.COLOR_GREEN, width=2, length=60,
                          angle=60,
                          first_point=sd.get_point(200, 200), step_for_grid=50, definition=[-800, 800])
my_draw.sqrt_graph()
my_draw.parabpla2()
sd.pause()
