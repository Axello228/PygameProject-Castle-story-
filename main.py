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


class Board:
    def __init__(self):
        for i in range(17):
            for j in range(32):
                if lst_map_the_isle[i][j] == 2:
                    self.location_my_castle = (j, i)
                if lst_map_the_isle[i][j] == 3:
                    self.location_bot_castle = (j, i)
        self.player1 = [10, 0, 0]
        self.builds_player1 = []
        self.edifice_player1 = []
        self.player2 = [0, 0, 0]
        self.builds_player2 = []
        self.edifice_player2 = []
        self.motion = 1
        self.alchemistry_stage = 0

    def get_player(self):
        if self.motion == 1:
            return self.player1
        else:
            return self.player2

    def get_cell(self):
        mouse = pygame.mouse.get_pos()
        x = mouse[0] // 60
        y = mouse[1] // 60
        return x, y

    def course_change(self):
        if game.return_action_stage() == "map_VS":
            if self.motion == 1:
                self.motion = 2
                i = 0
                while i < len(self.builds_player2):
                    if self.builds_player2[i][1] > 0:
                        self.builds_player2[i][1] -= 1
                    if self.builds_player2[i][1] == 0:
                        lst_map_the_isle[self.builds_player2[i][2][1]][self.builds_player2[i][2][0]] = self.builds_player2[i][0]
                        self.edifice_player2.append(self.builds_player2[i][0])
                        self.builds_player2[i], self.builds_player2[-1] = self.builds_player2[-1], self.builds_player2[i]
                        self.builds_player2.pop()
                    i += 1
            else:
                self.motion = 1
                i = 0
                while i < len(self.builds_player1):
                    if self.builds_player1[i][1] > 0:
                        self.builds_player1[i][1] -= 1
                    if self.builds_player1[i][1] == 0:
                        lst_map_the_isle[self.builds_player1[i][2][1]][self.builds_player1[i][2][0]] = self.builds_player1[i][0]
                        self.edifice_player1.append(self.builds_player1[i][0])
                        self.builds_player1[i], self.builds_player1[-1] = self.builds_player1[-1], self.builds_player1[i]
                        self.builds_player1.pop()
                    i += 1

    def build(self, what_build):
        if self.motion == 1:
            self.builds_player1.append([what_build, self.get_how_build(), game.get_pos()])
        else:
            self.builds_player2.append([what_build, self.get_how_build(), game.get_pos()])

    def get_how_build(self):
        pos = game.get_pos()
        if self.motion == 2:
            return max(abs(self.location_bot_castle[0] - pos[0]), abs(self.location_bot_castle[1] - pos[1]))
        else:
            return max(abs(self.location_my_castle[0] - pos[0]), abs(self.location_my_castle[1] - pos[1]))


class Game:
    def __init__(self):
        self.lst_textures = ["textures\\field.png", "textures\\forest.png", "textures\my_castle.png", "textures\\bot_castle.png",
                "textures\\north_beach.png", "textures\south_beach.png", "textures\east_beach.png",
                "textures\west_beach.png", "textures\\nw_beach.png", "textures\\ne_beach.png", "textures\se_beach.png",
                "textures\sw_beach.png", "textures\\bot_swordsman_r.png", "textures\\bot_swordsman_l.png",
                "textures\my_swordsman_r.png", "textures\my_swordsman_l.png", "textures\house.png", "textures\sawmill.png",
                "textures\\alchemistry.png", "textures\mine.png", "textures\smithy.png", "textures\\byilding_table.png"]
        self.action_stage = "main_menu"
        self.render_functions = {"main_menu": self.render_home_screen, "mode_selection": self.render_mode_selection_screen,
                    "map_VS": self.render_map_VS}
        self.building = {"house": 16, "sawmill": 17, "alchemistry": 18, "mine": 19, "smithy": 20}
        self.active_clr = (204, 229, 255)
        self.is_construction_window = False
        self.selection_cell = (0, 0)

    def click(self):
        if game.return_action_stage() == "map_VS" and not self.is_construction_window:
            self.selection_cell = board.get_cell()
            self.is_construction_window = True
        elif pygame.mouse.get_pos()[0] > 400:
            self.is_construction_window = False

    def render(self):
        self.render_functions[self.action_stage]()

    def draw_button(self, width, height, x, y, message, stage="None", font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            pygame.draw.rect(screen, self.active_clr, (x, y, width, height))
            if click[0] == 1:
                pygame.mixer.Sound.play(pygame.mixer.Sound(r'sounds\button_click.wav'))
                pygame.time.delay(150)
                if stage in self.render_functions:
                    self.action_stage = stage
                if stage in self.building:
                    self.render_build(self.building[stage])

        game.print_text(font_size, message, (0, 0, 0), (x + 5, y + 5))

    def return_action_stage(self):
        return self.action_stage

    def render_map_VS(self):
        x, y = 0, 0
        for i in range(17):
            x = 0
            for j in range(32):
                screen.blit(pygame.image.load(self.lst_textures[lst_map_the_isle[i][j]]), (x, y))
                x += 60
            y += 60
        x, y = 600, 0
        lst_player = board.get_player()
        for i in range(3):
            pygame.draw.rect(screen, self.active_clr, (x, y, 150, 50))
            game.print_text(40, str(lst_player[i]), (0, 0, 0), (x, y))
            x += 200

        if self.is_construction_window:
            game.render_construction_window(self.selection_cell)

    def render_mode_selection_screen(self):
        screen.blit(main_screen, (0, 0))
        game.draw_button(135, 55, 200, 150, "1 VS 1", "map_VS", font_size=45)
        game.draw_button(135, 55, 850, 150, "Waves", font_size=45)
        game.draw_button(170, 55, 1450, 150, "Invasion", font_size=45)

    def render_home_screen(self):
        screen.blit(main_screen, (0, 0))
        game.draw_button(250, 45, 850, 500, "Начать новую игру", "mode_selection")
        game.draw_button(250, 45, 850, 550, "Загрузить игру")
        game.draw_button(250, 45, 850, 600, "Настройки")

    def print_text(self, size, message, color, location, fnt='serif'):
        screen.blit(pygame.font.SysFont(fnt, size).render(message, True, color), location)

    def render_construction_window(self, pos):
        if lst_map_the_isle[pos[1]][pos[0]] == 0:
            screen.blit(construction_window_screen, (0, 0))
            cout = 0
            for i in range(16, 21):
                screen.blit(pygame.image.load(self.lst_textures[i]), (20, 20 + cout))
                cout += 100
            game.draw_button(70, 50, 100, 30, "Дом", "house")
            game.draw_button(150, 50, 100, 130, "Лесопилка", "sawmill")
            game.draw_button(290, 50, 100, 230, "Алхимическая платка", "alchemistry")
            game.draw_button(90, 50, 100, 330, "Шахта", "mine")
            game.draw_button(90, 50, 100, 430, "Кузня", "smithy")

    def start_game_soundtrack(self):
        pygame.mixer.music.load("sounds\soundtrack.mp3")
        pygame.mixer.music.play(-1)

    def stop_sondtrack(self):
        pygame.mixer.music.pause()

    def run_soundtrack(self):
        pygame.mixer.music.unpause()

    def render_build(self, what_build):
        self.is_construction_window = False
        lst_map_the_isle[self.selection_cell[1]][self.selection_cell[0]] = 21
        board.build(what_build)

    def get_pos(self):
        return self.selection_cell

lst_map_the_isle = [[8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 9],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 6],
         [7, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 6],
         [7, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 3, 0, 0, 6],
         [7, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 6],
         [7, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 6],
         [7, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 6],
         [7, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
         [11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10]]

main_screen = pygame.transform.scale(pygame.image.load(r"textures\background.jpg"), (1920, 1080))
construction_window_screen = pygame.transform.scale(pygame.image.load(r"textures\background_construction_window.PNG"), (400, 1080))
running = True
size = 1920, 1020
pygame.init()
pygame.display.set_caption("Castle story")
screen = pygame.display.set_mode(size)
pygame.display.set_icon(pygame.image.load("textures\icon.png"))
game = Game()
board = Board()
game.start_game_soundtrack()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.click()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                board.course_change()
    game.render()

    pygame.display.flip()

