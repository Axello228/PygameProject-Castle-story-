import pygame


class Castle:
    pass


class Sawmill:
    pass


class Mine:
    pass


class Forest:
    pass


class House:
    pass


class Alchemistry:
    pass


class Smithy:
    pass


class Swordman:
    pass


class Button:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active_clr = (204, 229, 255)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.active_clr, (x, y, self.width, self.height))
            if click[0] == 1 and action is not None:
                pygame.mixer.Sound.play(pygame.mixer.Sound(r'sounds\button_click.wav'))
                pygame.time.delay(150)
                action()

        print_text(font_size, message, (0, 0, 0), (x + 5, y + 5))


def print_text(size, message, color, location, fnt='serif'):
    screen.blit(pygame.font.SysFont(fnt, size).render(message, True, color), location)


def home_screen():
    global is_home_screen
    screen.blit(main_screen, (0, 0))
    Button(250, 45).draw(850, 500, "Начать новую игру", action=new_game)
    Button(250, 45).draw(850, 550, "Загрузить игру")
    Button(250, 45).draw(850, 600, "Настройки")


def new_game():
    global is_home_screen, is_mode_screen
    is_home_screen = False
    is_mode_screen = True


def VS():
    global is_mode_screen, is_map_VS
    is_mode_screen = False
    is_map_VS = True


def mode_selection_screen():
    screen.blit(main_screen, (0, 0))
    Button(135, 55).draw(200, 150, "1 VS 1", font_size=45, action=VS)
    Button(135, 55).draw(850, 150, "Waves", font_size=45)
    Button(170, 55).draw(1450, 150, "Invasion", font_size=45)


def map_VS():
    x, y = 0, 0
    for i in range(17):
        x = 0
        for j in range(32):
            screen.blit(pygame.image.load(lst_textures[lst_map_the_isle[i][j]]), (x, y))
            x += 60
        y += 60


def construction_window():
    x, y = get_cell()
    if lst_map_the_isle[y][x] == 0:
        print_text(50, "jgrejgejiger", (0, 0, 0), (100, 100))






def get_cell():
    mouse = pygame.mouse.get_pos()
    x = mouse[0] // 60
    y = mouse[1] // 60
    return x, y



main_screen = pygame.transform.scale(pygame.image.load(r"textures\background.jpg"), (1920, 1080))
is_home_screen = True
is_mode_screen = False
is_map_VS = False
is_while = True
is_pressed = False
size = 1920, 1020
pygame.init()
pygame.display.set_caption("Castle story")
screen = pygame.display.set_mode(size)
pygame.display.set_icon(pygame.image.load("textures\icon.png"))

lst_map_the_isle = [[8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 9],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 6],
         [7, 0, 0, 12, 0, 0, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 12, 12, 0, 0, 12, 12, 12, 0, 0, 12, 12, 0, 0, 0, 6],
         [7, 0, 0, 12, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 0, 0, 12, 12, 12, 0, 12, 12, 12, 3, 0, 0, 6],
         [7, 0, 0, 12, 12, 12, 0, 0, 0, 12, 12, 0, 0, 0, 0, 0, 12, 12, 12, 0, 0, 12, 12, 0, 0, 12, 12, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 12, 12, 0, 0, 12, 12, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 12, 12, 12, 12, 12, 12, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12, 12, 0, 0, 0, 0, 0, 12, 0, 0, 12, 12, 0, 0, 0, 12, 12, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 12, 0, 0, 12, 12, 12, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 12, 12, 0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 12, 0, 6],
         [7, 0, 0, 12, 12, 12, 12, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 6],
         [7, 0, 0, 12, 12, 12, 0, 0, 12, 0, 0, 0, 0, 12, 0, 0, 0, 0, 12, 12, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 12, 12, 0, 0, 0, 12, 12, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12, 0, 0, 0, 12, 0, 12, 12, 0, 0, 0, 6],
         [7, 0, 0, 0, 2, 0, 0, 0, 12, 12, 12, 12, 0, 0, 0, 12, 12, 0, 0, 12, 12, 12, 0, 0, 0, 0, 12, 12, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 12, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
         [11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10]]


lst_textures = ["textures\\field.png", "textures\house.png", "textures\my_castle.png", "textures\\bot_castle.png",
                "textures\\north_beach.png", "textures\south_beach.png", "textures\east_beach.png", "textures\west_beach.png",
                "textures\\nw_beach.png", "textures\\ne_beach.png", "textures\se_beach.png", "textures\sw_beach.png",
                "textures\\forest.png", "textures\my_swordsman_r.png", "textures\my_swordsman_l.png", "textures\\bot_swordsman_r.png",
                "textures\\bot_swordsman_l.png", "textures\sawmill.png", "textures\\alchemistry.png", "textures\mine.png",
                "textures\smithy.png"]


while is_while:
    if is_home_screen:
        home_screen()
    elif is_mode_screen:
        mode_selection_screen()
    elif is_map_VS:
        map_VS()
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0] == 1 and is_map_VS or is_pressed:
            is_pressed = True
            construction_window()
        if event.type == pygame.QUIT:
            is_while = False
        if event.type == pygame.K_ESCAPE:
            is_pressed = False

    pygame.display.flip()

