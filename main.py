import pygame


class Board:
    def __init__(self):
        for i in range(17):
            for j in range(32):
                if map[i][j] == 2:
                    self.location_my_castle = (j, i)
                if map[i][j] == 3:
                    self.location_bot_castle = (j, i)
        self.player1 = [100, 100, 100]
        self.builds_player1 = []
        self.edifice_player1 = []
        self.player2 = [10, 0, 0]
        self.builds_player2 = []
        self.edifice_player2 = []
        self.motion = 1
        self.alchemistry_stage_player1 = 0
        self.alchemistry_stage_player2 = 0
        self.edifice_functions = [self.house, self.sawmill, self.alchemistry, self.mine, self.smithy]
        self.house_place_player1 = 0
        self.house_place_player2 = 0
        self.cords_for_sawmill = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.alchemistry_cost = [(10, 0, 0), (15, 10, -0), (20, 15, 10), "1Беги!!!1"]
        self.warriors_cost = {"swordsman": (10, 0, 7)}

    def get_player(self):
        if self.motion == 1:
            return self.player1
        else:
            return self.player2

    def get_cell(self):
        mouse = pygame.mouse.get_pos()
        return mouse[0] // 60, mouse[1] // 60

    def course_change(self):
        if game.return_action_stage() == "map_VS":
            if self.motion == 1:
                self.motion = 2
                i = 0
                while i < len(self.builds_player2):
                    if self.builds_player2[i][1] > 0:
                        self.builds_player2[i][1] -= 1
                    if self.builds_player2[i][1] == 0:
                        map[self.builds_player2[i][2][1]][self.builds_player2[i][2][0]] = self.builds_player2[i][0]
                        self.edifice_player2.append([self.builds_player2[i][0], (self.builds_player2[i][-1])])
                        self.builds_player2[i], self.builds_player2[-1] = self.builds_player2[-1], self.builds_player2[i]
                        self.builds_player2.pop()
                    i += 1
                for elem in self.edifice_player2:
                    self.edifice_functions[elem[0] % 16](elem[-1])
            else:
                self.motion = 1
                i = 0
                while i < len(self.builds_player1):
                    if self.builds_player1[i][1] > 0:
                        self.builds_player1[i][1] -= 1
                    if self.builds_player1[i][1] == 0:
                        map[self.builds_player1[i][2][1]][self.builds_player1[i][2][0]] = self.builds_player1[i][0]
                        self.edifice_player1.append([self.builds_player1[i][0], (self.builds_player1[i][-1])])
                        self.builds_player1[i], self.builds_player1[-1] = self.builds_player1[-1], self.builds_player1[i]
                        self.builds_player1.pop()
                    i += 1
                for elem in self.edifice_player1:
                    self.edifice_functions[elem[0] % 16](elem[-1])

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

    def sawmill(self, pos):
        cout_wood = 0
        for elem in self.cords_for_sawmill:
            if map[pos[1] + elem[1]][pos[0] + elem[0]] == 1:
                cout_wood += 1
        if self.motion == 1:
            self.player1[0] += cout_wood
        else:
            self.player2[0] += cout_wood

    def mine(self, pos):
        if self.motion == 1:
            self.player1[1] += 1
        else:
            self.player2[1] += 1

    def smithy(self, pos):
        if self.motion == 1:
            if self.player1[1] >= 2 and self.player1[0] >= 2:
                self.player1[1] -= 2
                self.player1[0] -= 2
                self.player1[2] += 1
        else:
            if self.player2[1] >= 2 and self.player2[0] >= 2:
                self.player2[1] -= 2
                self.player2[0] -= 2
                self.player2[2] += 1

    def alchemistry(self, pos):
        pass

    def house(self, pos):
        pass

    def get_alchemistry_stage(self):
        if self.motion == 1:
            return self.alchemistry_stage_player1
        else:
            return self.alchemistry_stage_player2

    def up_alchemistry(self):
        if self.motion == 1:
            for i in range(3):
                self.player1[i] -= self.alchemistry_cost[self.alchemistry_stage_player1][i]
            self.alchemistry_stage_player1 += 1
        else:
            for i in range(3):
                self.player2[i] -= self.alchemistry_cost[self.alchemistry_stage_player2][i]
            self.alchemistry_stage_player2 += 1

    def cost_construction(self, build):
        if self.motion == 1:
            for i in range(len(build)):
                self.player1[i] -= build[i]
        else:
            for i in range(len(build)):
                self.player2[i] -= build[i]


class Game:
    def __init__(self):
        self.lst_textures = ["textures\\field.png", "textures\\forest.png", "textures\my_castle.png", "textures\\bot_castle.png",
                "textures\\north_beach.png", "textures\south_beach.png", "textures\east_beach.png",
                "textures\west_beach.png", "textures\\nw_beach.png", "textures\\ne_beach.png", "textures\se_beach.png",
                "textures\sw_beach.png", "textures\\bot_swordsman_r.png", "textures\\bot_swordsman_l.png",
                "textures\my_swordsman_r.png", "textures\my_swordsman_l.png", "textures\house.png", "textures\sawmill.png",
                "textures\\alchemistry.png", "textures\mine.png", "textures\smithy.png", "textures\\byilding_table.png"]
        self.resources = ["Дерево: ", "Руда: ", "Слитки: "]
        self.actions_in_the_game = {"up_alchemistry": self.up_alchemistry, "exit_alchemistry": self.off_alchemistry_window,
                                    'exit': self.exit}
        self.action_stage = "main_menu"
        self.render_functions = {"main_menu": self.render_home_screen, "mode_selection": self.render_mode_selection_screen,
                    "map_VS": self.render_map_VS, "settings": self.render_settings_window}
        self.building = {"house": [16, 20, 0, 5], "sawmill": [17, 5, 0, 0], "alchemistry": [18, 10, 0, 0],
                         "mine": [19, 15, 0, 0], "smithy": [20, 20, 10, 0]}
        self.settings = {"on_music": self.on_soundtrack, "off_music": self.off_sondtrack, "on_sounds": self.on_sounds,
                         "off_sounds": self.off_sounds}
        self.build_warriors = {"swordsman": self.build_swordsman}
        self.active_clr = (204, 229, 255)
        self.is_construction_window = False
        self.selection_cell = (0, 0)
        self.is_alchemistry_window = False
        self.is_sounds = True
        self.is_esc = False
        self.alchemistry_pos = (0, 0)
        self.exit = False
        self.is_smithy_window = False
        self.smithy_pos = (0, 0)
        self.board = Board()

    def exit(self):
        self.exit = True

    def return_exit(self):
        return self.exit

    def off_alchemistry_window(self):
        self.is_alchemistry_window = False

    def up_alchemistry(self):
        if self.is_sounds:
            pygame.mixer.Sound.play(pygame.mixer.Sound(r'sounds/up_alchemistry.mp3'))
        self.board.up_alchemistry()

    def click(self):
        if self.return_action_stage() == "map_VS":
            if not self.is_construction_window:
                self.selection_cell = self.board.get_cell()
                self.is_construction_window = True
            elif pygame.mouse.get_pos()[0] > 400:
                self.is_construction_window = False
            pos = self.board.get_cell()
            if map[pos[1]][pos[0]] == 18 and not self.is_alchemistry_window:
                self.alchemistry_pos = self.board.get_cell()
                self.is_alchemistry_window = True
            if map[pos[1]][pos[0]] == 20 and not self.is_smithy_window:
                self.smithy_pos = self.board.get_cell()
                self.is_smithy_window = True


    def render(self):
        self.render_functions[self.action_stage]()
        if self.is_esc and self.action_stage != "main_menu":
            self.render_esc_window()

    def render_button(self, width, height, x, y, message, stage="None", font_size=30): # Кнопки живут своей жизнью, лутне все клики запихнуть в функцию click
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            pygame.draw.rect(screen, self.active_clr, (x, y, width, height))
            if click[0] == 1:
                if self.is_sounds:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(r'sounds\button_click.wav'))
                pygame.time.delay(150)
                if stage in self.render_functions:
                    self.action_stage = stage
                if stage in self.building:
                    is_building = True
                    cost_building = self.building[stage][1:]
                    resurses_player = self.board.get_player()
                    for i in range(3):
                        if resurses_player[i] < cost_building[i]:
                            is_building = False
                    if is_building:
                        self.board.cost_construction(cost_building)
                        self.render_build(self.building[stage][0])
                if stage in self.settings:
                    self.settings[stage]()
                if stage in self.actions_in_the_game:
                    self.actions_in_the_game[stage]()
                if stage in self.build_warriors:
                    self.build_warriors[stage]()

        self.print_text(font_size, message, (x + 5, y + 5))

    def return_action_stage(self):
        return self.action_stage

    def render_map_VS(self):
        x, y = 0, 0
        for i in range(17):
            x = 0
            for j in range(32):
                screen.blit(pygame.image.load(self.lst_textures[map[i][j]]), (x, y))
                x += 60
            y += 60
        x, y = 500, 0
        lst_player = self.board.get_player()
        for i in range(3):
            pygame.draw.rect(screen, self.active_clr, (x, y, 250, 50))
            self.print_text(40, self.resources[i] + str(lst_player[i]), (x, y))
            x += 300

        if self.is_construction_window:
            self.render_construction_window(self.selection_cell)
        if self.is_alchemistry_window:
            self.render_alchemistry_window()
        if self.is_smithy_window:
            self.render_smithy_window()

    def render_esc_window(self):
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (450, 500)), (720, 240))
        self.render_button(240, 50, 825, 340, "Продолжить игру", "map_VS")
        self.render_button(240, 50, 825, 400, "Главное меню", "main_menu")
        self.render_button(240, 50, 825, 460, "Сохранить")
        self.render_button(240, 50, 825, 520, "Настройки", "settings")
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0] == 1 and 825 < mouse[0] < 1015 and 340 < mouse[1] < 570:
            self.is_esc = False

    def render_mode_selection_screen(self):
        screen.blit(main_screen, (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (800, 1100)), (-70, -50))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (800, 1100)), (560, -50))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (800, 1100)), (1190, -50))
        self.render_button(135, 55, 250, 80, "1 VS 1", "map_VS", font_size=45)
        self.render_button(135, 55, 890, 80, "Waves", font_size=45)
        self.render_button(170, 55, 1500, 80, "Invasion", font_size=45)
        self.print_text(30, "В разработке", (110, 200))
        self.print_text(30, "В разработке", (740, 200))
        self.print_text(30, "В разработке", (1370, 200))

    def render_home_screen(self):
        screen.blit(main_screen, (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (460, 400)), (750, 320))
        self.render_button(250, 45, 850, 400, "Начать новую игру", "mode_selection")
        self.render_button(250, 45, 850, 450, "Загрузить игру")
        self.render_button(250, 45, 850, 500, "Настройки", "settings")
        self.render_button(250, 45, 850, 550, "Выход", "exit")

    def print_text(self, size, message, location, color=(0, 0, 0), fnt='serif'):
        screen.blit(pygame.font.SysFont(fnt, size).render(message, True, color), location)

    def render_construction_window(self, pos):
        if map[pos[1]][pos[0]] == 0:
            screen.blit(construction_window_screen, (0, 0))
            cout = 0
            alchemistry = self.board.get_alchemistry_stage()
            if alchemistry == 0:
                build = (16, 19)
            elif alchemistry == 1:
                build = (16, 20)
            else:
                build = (16, 21)
            for i in range(build[0], build[1]):
                screen.blit(pygame.image.load(self.lst_textures[i]), (20, 20 + cout))
                cout += 100
            self.render_button(70, 50, 100, 30, "Дом", "house")
            self.print_text(20, "Деревo: 20, Руда: 0, Железо: 5", (110, 5))
            self.render_button(150, 50, 100, 130, "Лесопилка", "sawmill")
            self.print_text(20, "Деревo: 5, Руда: 0, Железо: 0", (110, 105))
            self.render_button(290, 50, 100, 230, "Алхимическая платка", "alchemistry")
            self.print_text(20, "Деревo: 10, Руда: 0, Железо: 0", (110, 205))
            if alchemistry > 0:
                self.render_button(90, 50, 100, 330, "Шахта", "mine")
                self.print_text(20, "Деревo: 15, Руда: 0, Железо: 0", (110, 305))
            if alchemistry > 1:
                self.render_button(90, 50, 100, 430, "Кузня", "smithy")
                self.print_text(20, "Деревo: 20, Руда: 10, Железо: 0", (110, 405))

    def off_sondtrack(self):
        pygame.mixer.music.pause()

    def on_soundtrack(self):
        pygame.mixer.music.unpause()

    def render_build(self, what_build):
        self.is_construction_window = False
        map[self.selection_cell[1]][self.selection_cell[0]] = 21
        self.board.build(what_build)

    def get_pos(self):
        return self.selection_cell

    def render_settings_window(self):
        screen.blit(main_screen, (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (580, 600)), (680, 150))
        self.render_button(240, 50, 850, 260, "Продолжить игру", "map_VS") # нет условия на отрисовку этой кнопки!!!
        self.render_button(240, 50, 850, 320, "Главное меню", "main_menu")
        self.render_button(240, 50, 850, 380, "Отключить музыку", "off_music")
        self.render_button(240, 50, 850, 440, "Включить музыку", "on_music")
        self.render_button(240, 50, 850, 500, "Отключить звук", "off_sounds")
        self.render_button(240, 50, 850, 560, "Включить звук", "on_sounds")

    def on_sounds(self):
        self.is_sounds = True

    def off_sounds(self):
        self.is_sounds = False

    def click_esc(self):
        if self.action_stage == "map_VS":
            if self.is_esc:
                self.is_esc = False
            else:
                self.is_esc = True

    def course_change(self):
        self.board.course_change()

    def render_alchemistry_window(self):
        if self.board.get_alchemistry_stage() != 3:
            screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (300, 350)), (self.alchemistry_pos[0] * 60 - 120, self.alchemistry_pos[1] * 60 - 120))
            self.render_button(120, 35, self.alchemistry_pos[0] * 60 - 40, self.alchemistry_pos[1] * 60 - 40, "Улучшить", "up_alchemistry", font_size=25)
            self.print_text(25, "Стоимость:", (self.alchemistry_pos[0] * 60 - 40, self.alchemistry_pos[1] * 60))
            self.print_text(25, "Уровень: " + str(self.board.get_alchemistry_stage()), (self.alchemistry_pos[0] * 60 - 40, self.alchemistry_pos[1] * 60 + 80))
            self.print_text(25, str(self.board.alchemistry_cost[self.board.get_alchemistry_stage()])[1:-1], (self.alchemistry_pos[0] * 60 - 40, self.alchemistry_pos[1] * 60 + 40))
        else:
            screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (300, 350)), (self.alchemistry_pos[0] * 60 - 120, self.alchemistry_pos[1] * 60 - 120))
            self.print_text(25, "Максимальный", (self.alchemistry_pos[0] * 60 - 50, self.alchemistry_pos[1] * 60 - 40))
            self.print_text(25, "уровень", (self.alchemistry_pos[0] * 60 - 50, self.alchemistry_pos[1] * 60))
        self.render_button(100, 35, self.alchemistry_pos[0] * 60 - 40, self.alchemistry_pos[1] * 60 + 120, "Выход", "exit_alchemistry", font_size=25)

    def render_smithy_window(self):
        if self.board.get_alchemistry_stage() == 3:
            screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (300, 350)), (self.smithy_pos[0] * 60 - 120, self.smithy_pos[1] * 60 - 120))
            self.render_button(120, 35, self.smithy_pos[0] * 60 - 40, self.smithy_pos[1] * 60 - 50, "Мечник", "swordsman", font_size=25)
            self.print_text(25, "Цена: " + str(self.board.warriors_cost["swordsman"])[1:-1], (self.smithy_pos[0] * 60 - 40, self.smithy_pos[1] * 60 - 10))

    def build_swordsman(self):
        self.is_smithy_window = False # В начале должна запуститься функция в бэк енде на просчёт цены постройки или улутшения, а она в свою очередь должна как-то отнимать у игрока ресурсы


def load_map():
    file = open("maps/the_isle", encoding="utf8", mode="r")
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


map = load_map()
main_screen = pygame.transform.scale(pygame.image.load(r"textures\background.jpg"), (1920, 1080))
construction_window_screen = pygame.transform.scale(pygame.image.load(r"textures\background_construction_window.PNG"), (400, 1080))
running = True
size = 1920, 1020
pygame.init()
pygame.display.set_caption("Castle story")
screen = pygame.display.set_mode(size)
pygame.display.set_icon(pygame.image.load("textures\icon.png"))
game = Game()
pygame.mixer.music.load("sounds\soundtrack.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
fps = 60
clock = pygame.time.Clock()
while running:
    is_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or game.return_exit():
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not is_click:
            is_click = True
            game.click()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.course_change()
            if event.key == pygame.K_ESCAPE:
               game.click_esc()
    game.render()
    clock.tick(fps)

    pygame.display.flip()