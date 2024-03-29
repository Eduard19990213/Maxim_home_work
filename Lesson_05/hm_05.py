# Написать функции по отрисовке правильного многоугольника с n сторонами с любым начальным углом поворота
# Угол в правильном n-угольнике составляет 180*(n-2)/n в градусах, сделать все через линии,
# чтобы цвета можно было менять, как в нашей сетке


import simple_draw as sd

sd.background_color = (255, 255, 255)
sd.resolution = (1200, 900)
sd.caption = 'Моё рабочее пространство'
first_point = sd.get_point(800, 500)
n = int(input('Введите число сторон в правильном многоугольнике: '))
x = 180*(1 - (n-2)/n)
#second_point = sd.get_point(500, 700)
# v1 = sd.get_vector(start_point=first_point, angle=0, length=150, width=5, )
# v1.draw()
# v2 = sd.get_vector(second_point, 90, 200, 10)
# v2.draw()

def mnogougolnik(start_point, length=100, angle=0):
    for number in range(n):
        vector = sd.get_vector(start_point=start_point, width=3, length=length, angle=angle + x * number)
        vector.draw(color=sd.COLOR_BLACK)
        start_point = vector.end_point

mnogougolnik(start_point=first_point)



def grid(resolution=sd.resolution, step=50):
    x = resolution[0]
    y = resolution[1]
    x_os = sd.line(start_point=sd.get_point(0, y/2), end_point=sd.get_point(x, y/2), color=sd.COLOR_BLACK,
                     width=4)
    y_os = sd.line(start_point=sd.get_point(x/2, 0), end_point=sd.get_point(x/2, y), color=sd.COLOR_BLACK,
                   width=4)
    x_grid = step
    y_grid = step
    while x_grid < x:
        xl = sd.line(start_point=sd.get_point(x_grid, 0), end_point=sd.get_point(x_grid, y), color=sd.COLOR_BLACK,
                     width=1)
        x_grid += step

        xl2 = sd.line(start_point=sd.get_point(x_grid-50,465), end_point=sd.get_point(x_grid-50,435),
                      color=sd.COLOR_BLACK, width=4)





    while y_grid < y:
        yl = sd.line(start_point=sd.get_point(0, y_grid), end_point=sd.get_point(x, y_grid), color=sd.COLOR_BLACK,
                     width=1)
        y_grid += step
        xl2 = sd.line(start_point=sd.get_point(585, y_grid), end_point=sd.get_point(615, y_grid),
                      color=sd.COLOR_BLACK, width=4)




grid()

sd.pause()
