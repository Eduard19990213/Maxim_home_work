import simple_draw as sd

from Maxim_home_work.Lesson_06.draw_class import DrawClass as DC

sd.background_color = (128, 25, 146)
sd.resolution = (1600, 900)
my_draw = DC(resolution=sd.resolution, number_of_angles=10, color=sd.COLOR_GREEN, width=2, length=60, angle=60,
             first_point=sd.get_point(200, 200), step_for_grid=50)
my_draw.n_ugolnik()
# my_draw.snow_fall()
sd.pause()

# Изменить функцию сетки с отрисовкой штрихов единиц измерения
# изменить функцию падения снежинок, чтобы они падали на с разным смещением и на разной высоте
# добавит функци рисования кирпичной стены
# Расширить возможности функции многоугольников с возможностью передать списки списков с числом углов, начальной точкой и цветом
