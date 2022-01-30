import pygame


def render_map_VS():
    global map
    x, y = 0, 0
    for i in range(17):
        x = 0
        for j in range(32):
            screen.blit(pygame.image.load(lst_textures[map[i][j]]), (x, y))
            x += 60
        y += 60


def load_map(name):
    file = open(name, encoding="utf8", mode="r")
    lines = file.readlines()
    file.close()
    map = []
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-1]
    for elem in lines:
        map.append(elem.split(", "))
    for i in range(17):
        for j in range(32):
            map[i][j] = int(map[i][j])
    return map


lst_textures = ["textures\\field.png", "textures\\forest.png", "textures\my_castle.png", "textures\\bot_castle.png",
                "textures\\north_beach.png", "textures\south_beach.png", "textures\east_beach.png",
                "textures\west_beach.png", "textures\\nw_beach.png", "textures\\ne_beach.png", "textures\se_beach.png",
                "textures\sw_beach.png", "textures\\bot_swordsman_r.png", "textures\\bot_swordsman_l.png",
                "textures\my_swordsman_r.png", "textures\my_swordsman_l.png", "textures\house.png", "textures\sawmill.png",
                "textures\\alchemistry.png", "textures\mine.png", "textures\smithy.png", "textures\\byilding_table.png"]


map = load_map(r"maps\forest")
print(map)
running = True
size = 1920, 1020
pygame.init()
screen = pygame.display.set_mode(size)
while running:
    is_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    render_map_VS()
    pygame.display.flip()

"""0 = поле
1 = лес
2 = замок мой
3 = замок бота
4 = пляж вверх
5 = пляж вниз
6 = пляж вправо
7 = пляж влево
8 = угол сверху слева
9 = угол сверху справа
10 = угол снизу справа
11 = угол снизу слева
12 = бота мечник право
13 = бота мечник лево
14 = мой мечник право
15 = мой мечник лево
16 = дом
17 = лесопилка
18 = алхимия
19 = шахта
20 = кузня
21 = стротельная табличка"""
