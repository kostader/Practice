import pygame as pg

pg.init()
width, height = screen_size = (300, 200)
screen = pg.display.set_mode(screen_size)

# Here should draw
pg.display.update()

work_flag = True
while work_flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            work_flag = False

print("Program is finished!")
