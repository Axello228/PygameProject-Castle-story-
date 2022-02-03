import pygame


class Board:
    def __init__(self):
        self.map = []
        self.location_my_castle = (0, 0)
        self.location_bot_castle = (0, 0)
        self.player1 = [1000, 1000, 1000]
        self.builds_player1 = []
        self.edifice_player1 = []
        self.player2 = [1000, 1000, 1000]
        self.builds_player2 = []
        self.edifice_player2 = []
        self.motion = 1
        self.alchemistry_stage_player1 = 0
        self.alchemistry_stage_player2 = 0
        self.castle_stage_player1 = 0
        self.castle_stage_player2 = 0
        self.edifice_functions = [self.house, self.sawmill, self.alchemistry, self.mine, self.smithy]
        self.house_place_player1 = 0
        self.house_place_player2 = 0
        self.cords_for_sawmill = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.alchemistry_cost = [(10, 0, 0), (15, 10, -0), (20, 15, 10), "1Беги!!!1"]
        self.warriors_cost = {"swordsman": (10, 0, 7)}
        self.castle_cost = [(25, 0, 0), (50, 0, 10), (100, 0, 30), "1Беги!!!1"]
        self.square_castle = [1, 2, 3, 4]
        self.selection_cell = (0, 0)
        self.army_player1 = []
        self.army_player2 = []
        self.move_swordsman = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
        self.pos = (0, 0)
        self.past_pos = (0, 0)

    def load(self, lst_bool, lst_int, lst_lst, lst_map):
        pass

    def save(self, lst_int, lst_bool):
        lst_int.extend([self.motion, self.alchemistry_stage_player1, self.alchemistry_stage_player2, self.castle_stage_player1,
                       self.castle_stage_player2,  self.house_place_player1,  self.house_place_player2])
        for i in range(len(lst_int)):
            lst_int[i] = str(lst_int[i])
        for i in range(len(lst_bool)):
            lst_bool[i] = str(lst_bool[i])
        lst_lst = [self.player1, self.player2, self.builds_player1, self.builds_player2, self.edifice_player1, self.edifice_player2,
                   self.army_player1, self.army_player2]
        for i in range(len(lst_lst)):
            for j in range(len(lst_lst[i])):
                lst_lst[i][j] = str(lst_lst[i][j])
        for i in range(len(lst_lst)):
            lst_lst[i] = " ".join(lst_lst[i])
        file = open(r"saves_and_loads\\1_VS_1", mode="w", encoding="utf8")
        file.write(", ".join(lst_bool) + "\n")
        file.write(", ".join(lst_int) + "\n")
        file.write(", ".join(lst_lst) + "\n")
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.map[i][j] = str(self.map[i][j])
        for i in range(len(self.map) - 1):
            file.write(", ".join(self.map[i]) + "\n")
        file.write(", ".join(self.map[-1]))
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.map[i][j] = int(self.map[i][j])

    def new_game(self):
        for i in range(17):
            for j in range(32):
                if self.map[i][j] == 2:
                    self.location_my_castle = (j, i)
                if self.map[i][j] == 3:
                    self.location_bot_castle = (j, i)
        self.player1 = [1000, 1000, 1000]
        self.builds_player1 = []
        self.edifice_player1 = []
        self.player2 = [1000, 1000, 1000]
        self.builds_player2 = []
        self.edifice_player2 = []
        self.motion = 1
        self.alchemistry_stage_player1 = 0
        self.alchemistry_stage_player2 = 0
        self.castle_stage_player1 = 0
        self.castle_stage_player2 = 0
        self.house_place_player1 = 0
        self.house_place_player2 = 0
        self.selection_cell = (0, 0)
        self.army_player1 = []
        self.army_player2 = []
        self.pos = (0, 0)
        self.past_pos = (0, 0)

    def get_player(self):
        if self.motion == 1:
            return self.player1
        else:
            return self.player2

    def course_change(self, stage):
        if stage == "map_VS":
            if self.motion == 1:
                builds_player = self.builds_player2
                edifice_player = self.edifice_player2
                army = self.army_player2
                self.house_place_player2 = 0
            else:
                builds_player = self.builds_player1
                edifice_player = self.edifice_player1
                army = self.army_player1
                self.house_place_player1 = 0
            self.pos = (0, 0)
            self.past_pos = (0, 0)
            i = 0
            while i < len(builds_player):
                if builds_player[i][1] > 0:
                    builds_player[i][1] -= 1
                if builds_player[i][1] == 0:
                    self.map[builds_player[i][2][1]][builds_player[i][2][0]] = builds_player[i][0]
                    edifice_player.append([builds_player[i][0], (builds_player[i][-1])])
                    builds_player[i], builds_player[-1] = builds_player[-1], builds_player[i]
                    builds_player.pop()
                i += 1
            for elem in edifice_player:
                self.edifice_functions[elem[0] % 16](elem[-1])
            for warior in army:
                warior.go = True
            if self.motion == 1:
                self.motion = 2
                self.builds_player2 = builds_player
                self.edifice_player2 = edifice_player
                self.army_player2 = army
            else:
                self.motion = 1
                self.builds_player1 = builds_player
                self.edifice_player1 = edifice_player
                self.army_player1 = army

    def build(self, what_build, cell):
        if self.motion == 1:
            self.builds_player1.append([what_build, self.get_how_build(), cell])
        else:
            self.builds_player2.append([what_build, self.get_how_build(), cell])

    def get_how_build(self):
        if self.motion == 2:
            return max(abs(self.location_bot_castle[0] - self.selection_cell[0]), abs(self.location_bot_castle[1] - self.selection_cell[1]))
        else:
            return max(abs(self.location_my_castle[0] - self.selection_cell[0]), abs(self.location_my_castle[1] - self.selection_cell[1]))

    def sawmill(self, pos):
        cout_wood = 0
        for elem in self.cords_for_sawmill:
            if self.map[pos[1] + elem[1]][pos[0] + elem[0]] == 1:
                cout_wood += 1
        if self.motion == 2:
            self.player1[0] += cout_wood
        else:
            self.player2[0] += cout_wood

    def mine(self, pos):
        if self.motion == 2:
            self.player1[1] += 1
        else:
            self.player2[1] += 1

    def smithy(self, pos):
        if self.motion == 1:
            player = self.player2
        else:
            player = self.player1
        if player[1] >= 2 and player[0] >= 2:
            player[1] -= 2
            player[0] -= 2
            player[2] += 1
        if self.motion == 1:
            self.player2 = player
        else:
            self.player1 = player

    def alchemistry(self, pos):
        pass

    def house(self, pos):
        if self.motion == 1:
            self.house_place_player2 += 2
        else:
            self.house_place_player1 += 2

    def get_alchemistry_stage(self):
        if self.motion == 1:
            return self.alchemistry_stage_player1
        else:
            return self.alchemistry_stage_player2

    def up_alchemistry(self):
        if self.motion == 1:
            player = self.player1
            alchemistry_stage = self.alchemistry_stage_player1
        else:
            player = self.player2
            alchemistry_stage = self.alchemistry_stage_player2
        for i in range(3):
            player[i] -= self.alchemistry_cost[alchemistry_stage][i]
        alchemistry_stage += 1
        if self.motion == 1:
            self.player1 = player
            self.alchemistry_stage_player1 += 1
        else:
            self.player2 = player
            self.alchemistry_stage_player2 += 1

    def cost_construction(self, build):
        if self.motion == 1:
            player = self.player1
        else:
            player = self.player2
        for i in range(len(build)):
            player[i] -= build[i]
        if self.motion == 1:
            self.player1 = player
        else:
            self.player2 = player

    def get_castle_stage(self):
        if self.motion == 1:
            return self.castle_stage_player1
        else:
            return self.castle_stage_player2

    def up_castle(self):
        if self.motion == 1:
            player = self.player1
            stage = self.castle_stage_player1
        else:
            player = self.player2
            stage = self.castle_stage_player2
        is_ok = True
        for i in range(3):
            if player[i] < self.castle_cost[stage][i]:
                is_ok = False
        if is_ok:
            for i in range(3):
                player[i] -= self.castle_cost[stage][i]
        if self.motion == 1:
            self.player1 = player
            self.castle_stage_player1 += 1
        else:
            self.player2 = player
            self.castle_stage_player2 += 1

    def build_swordsman(self):
        pos = player = 0
        if self.motion == 1 and self.map[self.location_my_castle[1] + 1][self.location_my_castle[0]] == 0:
            player = self.player1
            is_ok = True
            pos = self.location_my_castle
        elif self.map[self.location_bot_castle[1] + 1][self.location_bot_castle[0]] == 0 and self.motion == 2:
            player = self.player2
            is_ok = True
            pos = self.location_bot_castle
        else:
            is_ok = False
        if is_ok:
            for i in range(3):
                if player[i] < self.warriors_cost["swordsman"][i]:
                    is_ok = False
            if is_ok:
                for i in range(3):
                    player[i] -= self.warriors_cost["swordsman"][i]
            if self.motion == 1:
                self.player1 = player
                self.army_player1.append(Swordsman(pos))
                self.map[pos[1] + 1][pos[0]] = 14
            else:
                self.player2 = player
                self.army_player2.append(Swordsman(pos))
                self.map[pos[1] + 1][pos[0]] = 13

    def load_map(self, name):
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


class Game:
    def __init__(self):
        self.lst_textures = ["textures\\field.png", "textures\\forest.png", "textures\my_castle.png", "textures\\bot_castle.png",
                "textures\\north_beach.png", "textures\south_beach.png", "textures\east_beach.png",
                "textures\west_beach.png", "textures\\nw_beach.png", "textures\\ne_beach.png", "textures\se_beach.png",
                "textures\sw_beach.png", "textures\\bot_swordsman_r.png", "textures\\bot_swordsman_l.png",
                "textures\my_swordsman_r.png", "textures\my_swordsman_l.png", "textures\house.png", "textures\sawmill.png",
                "textures\\alchemistry.png", "textures\mine.png", "textures\smithy.png", "textures\\byilding_table.png"]
        self.amogus_fleks = [r"textures\amogus1.jpg", r"textures\amogus2.jpg", r"textures\amogus3.jpg", r"textures\amogus4.jpg", r"textures\amogus5.jpg", r"textures\amogus6.jpg"]
        self.cout_amogus_fleks = 0
        self.resources = ["Дерево: ", "Руда: ", "Слитки: "]
        self.actions_in_the_game = {"up_alchemistry": self.up_alchemistry, "exit_alchemistry": self.off_alchemistry_window,
                                    'exit': self.exit, "up_castle": self.up_castle, "exit_smithy": self.off_smithy_window,
                                    "exit_castle": self.off_castle_window}
        self.past_action_stage = "main_menu"
        self.action_stage = "main_menu"
        self.render_functions = {"main_menu": self.render_home_screen, "mode_selection": self.render_mode_selection_screen,
                    "map_VS": self.render_map_VS, "settings": self.render_settings_window, "maps": self.render_selection_map_window,
                                 "load_selection": self.render_load_mode_screen}
        self.building = {"house": [16, 20, 0, 5], "sawmill": [17, 5, 0, 0], "alchemistry": [18, 10, 0, 0],
                         "mine": [19, 15, 0, 0], "smithy": [20, 20, 10, 0]}
        self.settings = {"on_music": self.on_soundtrack, "off_music": self.off_sondtrack, "on_sounds": self.on_sounds,
                         "off_sounds": self.off_sounds}
        self.loads = {"isle": self.load_isle, "forest": self.load_forest, "save": self.save, "load": self.load}
        self.build_warriors = {"swordsman": self.build_swordsman}
        self.active_clr = (204, 229, 255)
        self.is_construction_window = False
        self.is_alchemistry_window = False
        self.is_sounds = True
        self.is_esc = False
        self.exit = False
        self.is_smithy_window = False
        self.board = Board()
        self.is_castle_window = False
        self.is_warior_window = False
        self.is_win_window = False

    def load(self):
        file = open("saves_and_loads\\1_VS_1", encoding="utf8", mode="r")
        lines = file.readlines()
        lst_bool = lines[0][:-1].split(", ")
        lst_int = lines[1][:-1].split(", ")
        lst_lst = lines[2][:-1].split(", ")
        lst_map = []
        for i in range(len(lines[3:])):
            lst_map.append(lines[i][:-1].split(", "))
        if lst_bool[0] == "True":
            self.is_win_window = True
        else:
            self.is_win_window = False
        del lst_bool[0]
        self.cout_amogus_fleks = int(lst_int[0])
        del lst_int[0]
        self.board.load(lst_bool, lst_int, lst_lst, lst_map)
        self.action_stage = "map_VS"

    def save(self):
        self.board.save([self.cout_amogus_fleks], [self.is_win_window])

    def get_cell(self):
        mouse = pygame.mouse.get_pos()
        return mouse[0] // 60, mouse[1] // 60

    def off_castle_window(self):
        self.is_castle_window = False

    def off_smithy_window(self):
        self.is_smithy_window = False

    def exit(self):
        self.exit = True

    def off_alchemistry_window(self):
        self.is_alchemistry_window = False

    def up_castle(self):
        if self.is_sounds:
            pygame.mixer.Sound.play(pygame.mixer.Sound(r"sounds/up_castle.mp3"))
        self.board.up_castle()

    def up_alchemistry(self):
        if self.board.motion == 1:
            resurs = self.board.player1
            stage = self.board.alchemistry_stage_player1
        else:
            resurs = self.board.player2
            stage = self.board.alchemistry_stage_player2
        is_ok = True
        for i in range(3):
            if resurs[i] - self.board.alchemistry_cost[stage][i] < 0:
                is_ok = False
        if is_ok:
            if self.is_sounds:
                pygame.mixer.Sound.play(pygame.mixer.Sound(r'sounds/up_alchemistry.mp3'))
            self.board.up_alchemistry()

    def click(self):
        if self.return_action_stage() == "map_VS":
            self.board.selection_cell = self.get_cell()
            self.board.past_pos = self.board.pos
            self.board.pos = self.get_cell()
            is_ok = False
            if self.board.motion == 1:
                if self.board.get_how_build() <= self.board.square_castle[self.board.castle_stage_player1]:
                    is_ok = True
            else:
                if self.board.get_how_build() <= self.board.square_castle[self.board.castle_stage_player2]:
                    is_ok = True
            if not self.is_construction_window:
                if is_ok:
                    self.is_construction_window = True
            elif pygame.mouse.get_pos()[0] > 380 or pygame.mouse.get_pos()[1] > 490:
                self.is_construction_window = False
            if self.board.map[self.board.pos[1]][self.board.pos[0]] == 18 and not self.is_alchemistry_window and is_ok:
                self.alchemistry_pos = self.get_cell()
                self.is_alchemistry_window = True
            if self.board.map[self.board.pos[1]][self.board.pos[0]] == 20 and not self.is_smithy_window and is_ok:
                self.smithy_pos = self.get_cell()
                self.is_smithy_window = True
            if self.board.map[self.board.pos[1]][self.board.pos[0]] == 2 and self.board.motion == 1:
                self.castle_pos = self.board.location_my_castle
                self.is_castle_window = True
            if self.board.map[self.board.pos[1]][self.board.pos[0]] == 3 and self.board.motion == 2:
                self.castle_pos = self.board.location_bot_castle
                self.is_castle_window = True
            if (self.board.map[self.board.past_pos[1]][self.board.past_pos[0]] == 14 or self.board.map[self.board.past_pos[1]][self.board.past_pos[0]] == 15) and self.board.motion == 1 or (self.board.map[self.board.past_pos[1]][self.board.past_pos[0]] == 13 or self.board.map[self.board.past_pos[1]][self.board.past_pos[0]] == 12) and self.board.motion == 2:
                self.is_warior_window = True
                if self.board.motion == 1:
                    army = self.board.army_player1
                    arm = self.board.army_player2
                    a = (14, 15)
                    b = (12, 13)
                    castle = self.board.location_bot_castle
                else:
                    army = self.board.army_player2
                    arm = self.board.army_player1
                    a = (12, 13)
                    b = (14, 15)
                    castle = self.board.location_my_castle
                for warior in army:
                    if warior.pos == self.board.past_pos and warior.go:
                        is_move = False
                        for pos in self.board.move_swordsman:
                            if self.board.past_pos[0] + pos[0] == self.board.pos[0] and self.board.past_pos[1] + pos[1] == self.board.pos[1]:
                                is_move = True
                        if self.board.map[self.board.pos[1]][self.board.pos[0]] == 0 and is_move:
                            warior.move(self.board.pos, self.board.past_pos, self.board.motion, self.is_sounds, pygame.mixer.Sound(r'sounds\go.mp3'), self.board.map)
                        if self.board.map[self.board.pos[1]][self.board.pos[0]] == self.board.map[self.board.past_pos[1]][self.board.past_pos[0]] and warior.go:
                            warior.treatment(self.is_sounds, pygame.mixer.Sound(r'sounds\healing.mp3'))
                        if self.board.map[self.board.past_pos[1]][self.board.past_pos[0]] in a and self.board.map[self.board.pos[1]][self.board.pos[0]] in b and is_move:
                            i = 0
                            while i < len(arm):
                                if arm[i].pos == self.board.pos:
                                    warior.hit(self.is_sounds, pygame.mixer.Sound(r'sounds\hit.mp3'))
                                    arm[i].damage()
                                    if arm[i].death:
                                        self.board.map[arm[i].pos[1]][arm[i].pos[0]] = 0
                                        del arm[i]
                                i += 1
                        if self.board.map[self.board.past_pos[1]][self.board.past_pos[0]] in a and self.board.pos == castle and is_move:
                            self.is_win_window = True

    def off_warior_window(self):
        self.is_warior_window = False

    def render(self):
        self.render_functions[self.action_stage]()
        if self.is_esc and self.action_stage != "main_menu":
            self.render_esc_window()

    def render_button(self, width, height, x, y, message, stage="None", font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            pygame.draw.rect(screen, self.active_clr, (x, y, width, height))
            if click[0] == 1:
                if self.is_sounds:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(r'sounds\button_click.wav'))
                pygame.time.delay(150)
                if stage in self.render_functions:
                    self.past_action_stage = self.action_stage
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
                if stage in self.loads:
                    self.loads[stage]()
        self.print_text(font_size, message, (x + 5, y + 5))

    def return_action_stage(self):
        return self.action_stage

    def render_map_VS(self):
        x, y = 0, 0
        for i in range(17):
            x = 0
            for j in range(32):
                screen.blit(pygame.image.load(self.lst_textures[self.board.map[i][j]]), (x, y))
                x += 60
            y += 60
        x, y = 500, 0
        lst_player = self.board.get_player()
        for i in range(3):
            pygame.draw.rect(screen, self.active_clr, (x, y, 250, 50))
            self.print_text(40, self.resources[i] + str(lst_player[i]), (x, y))
            x += 300
        pygame.draw.rect(screen, self.active_clr, (x + 100, y, 270, 50))
        game.print_text(40, "Ход игрока №" + str(self.board.motion), (x + 100, y))
        if self.is_construction_window:
            self.render_construction_window(self.board.selection_cell)
        if self.is_alchemistry_window:
            self.render_alchemistry_window()
        if self.is_smithy_window:
            self.render_smithy_window()
        if self.is_castle_window:
            self.render_castle_window()
        if self.is_win_window:
            self.render_win_window()

    def render_esc_window(self):
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (450, 500)), (720, 240))
        self.render_button(240, 50, 825, 340, "Продолжить игру", "map_VS")
        self.render_button(240, 50, 825, 400, "Главное меню", "main_menu")
        self.render_button(240, 50, 825, 460, "Сохранить", "save")
        self.render_button(240, 50, 825, 520, "Настройки", "settings")
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0] == 1 and 825 < mouse[0] < 1015 and 340 < mouse[1] < 570:
            self.is_esc = False

    def render_mode_selection_screen(self):
        screen.blit(main_screen, (0, 0))
        self.print_text(40, "Выбирите режим", (800, 10))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (800, 1100)), (-70, -50))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (800, 1100)), (560, -50))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (800, 1100)), (1190, -50))
        self.render_button(135, 55, 250, 80, "1 VS 1", "maps", font_size=45)
        self.render_button(135, 55, 890, 80, "Waves", font_size=45)
        self.render_button(170, 55, 1500, 80, "Invasion", font_size=45)
        self.print_text(30, "В бета тестировании", (110, 200))
        self.print_text(30, "В разработке", (740, 200))
        self.print_text(30, "В разработке", (1370, 200))

    def render_load_mode_screen(self):
        screen.blit(main_screen, (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (300, 350)), (810, 330))
        self.print_text(40, "Какой режим загрузить?", (780, 20))
        self.render_button(100, 40, 900, 410, "1 VS 1", "load")
        self.render_button(100, 40, 900, 470, "Waves")
        self.render_button(130, 40, 900, 530, "Invasion")

    def render_selection_map_window(self):
        screen.blit(main_screen, (0, 0))
        self.print_text(40, "Выбирите карту", (850, 10))
        self.render_button(596, 344, 90, 90, "", "isle")
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\isle_screen.PNG"), (576, 324)), (100, 100))
        self.render_button(596, 344, 700, 90, "", "forest")
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\forest_screen.PNG"), (576, 324)), (710, 100))

    def load_isle(self):
        self.board.map = self.board.load_map("maps/isle")
        self.new_game()

    def load_forest(self):
        self.board.map = self.board.load_map("maps/forest")
        self.new_game()

    def new_game(self):
        self.cout_amogus_fleks = 0
        self.is_construction_window = False
        self.is_alchemistry_window = False
        self.is_sounds = True
        self.is_esc = False
        self.exit = False
        self.is_smithy_window = False
        self.is_castle_window = False
        self.is_warior_window = False
        self.is_win_window = False
        self.board.new_game()
        self.past_action_stage = self.action_stage
        self.action_stage = "map_VS"

    def render_home_screen(self):
        screen.blit(main_screen, (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (460, 400)), (750, 320))
        self.render_button(250, 45, 850, 400, "Начать новую игру", "mode_selection")
        self.render_button(250, 45, 850, 450, "Загрузить игру", "load_selection")
        self.render_button(250, 45, 850, 500, "Настройки", "settings")
        self.render_button(250, 45, 850, 550, "Выход", "exit")

    def print_text(self, size, message, location, color=(0, 0, 0), fnt='serif'):
        screen.blit(pygame.font.SysFont(fnt, size).render(message, True, color), location)

    def render_construction_window(self, pos):
        if self.board.map[pos[1]][pos[0]] == 0:
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
            self.print_text(20, "Деревo: 20, Руда: 0, Слитки: 5", (110, 5))
            self.render_button(150, 50, 100, 130, "Лесопилка", "sawmill")
            self.print_text(20, "Деревo: 5, Руда: 0, Слитки: 0", (110, 105))
            self.render_button(290, 50, 100, 230, "Алхимическая платка", "alchemistry")
            self.print_text(20, "Деревo: 10, Руда: 0, Слитки: 0", (110, 205))
            if alchemistry > 0:
                self.render_button(90, 50, 100, 330, "Шахта", "mine")
                self.print_text(20, "Деревo: 15, Руда: 0, Слитки: 0", (110, 305))
            if alchemistry > 1:
                self.render_button(90, 50, 100, 430, "Кузня", "smithy")
                self.print_text(20, "Деревo: 20, Руда: 10, Слитки: 0", (110, 405))

    def off_sondtrack(self):
        pygame.mixer.music.pause()

    def on_soundtrack(self):
        pygame.mixer.music.unpause()

    def render_build(self, what_build):
        self.is_construction_window = False
        if self.is_sounds:
            pygame.mixer.Sound.play(pygame.mixer.Sound(r'sounds\build.mp3'))
        self.board.map[self.board.selection_cell[1]][self.board.selection_cell[0]] = 21
        self.board.build(what_build, self.board.selection_cell)

    def render_settings_window(self):
        screen.blit(main_screen, (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (580, 600)), (680, 150))
        if self.past_action_stage == "map_VS":
            self.render_button(240, 50, 850, 260, "Продолжить игру", "map_VS")
        self.render_button(240, 50, 850, 320, "Главное меню", "main_menu")
        self.render_button(260, 50, 850, 380, "Отключить музыку", "off_music")
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
        self.board.course_change(game.return_action_stage())

    def render_alchemistry_window(self):
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (300, 350)), (810, 365))
        if self.board.get_alchemistry_stage() != 3:
            self.render_button(120, 35, 890, 445, "Улучшить", "up_alchemistry", font_size=25)
            self.print_text(25, "Стоимость:", (890, 485))
            self.print_text(25, "Уровень: " + str(self.board.get_alchemistry_stage()), (890, 565))
            self.print_text(25, str(self.board.alchemistry_cost[self.board.get_alchemistry_stage()])[1:-1], (890, 525))
        else:
            self.print_text(25, "Максимальный", (880, 445))
            self.print_text(25, "уровень", (880, 485))
        self.render_button(100, 35, 890, 605, "Выход", "exit_alchemistry", font_size=25)

    def render_smithy_window(self):
        if self.board.get_alchemistry_stage() == 3:
            screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (300, 350)), (810, 365))
            self.render_button(120, 35, 890, 435, "Мечник", "swordsman", font_size=25)
            self.print_text(25, "Цена: " + str(self.board.warriors_cost["swordsman"])[1:-1], (890, 475))
            self.render_button(100, 35, 890, 605, "Выход", "exit_smithy", font_size=25)

    def render_castle_window(self):
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (300, 350)), (810, 365))
        if self.board.get_castle_stage() < 3:
            self.render_button(120, 35, 880, 435, "Улучшить", "up_castle", font_size=25)
            self.print_text(25, "Стоимость:", (885, 470))
            self.print_text(25, str(self.board.castle_cost[self.board.get_castle_stage()])[1:-1], (885, 505))
            self.print_text(25, "Уровень: " + str(self.board.get_castle_stage()), (885, 540))
        else:
            self.print_text(25, "Максимальный", (885, 445))
            self.print_text(25, "уровень", (885, 485))
        self.render_button(120, 35, 880, 575, "Выход", "exit_castle", font_size=25)

    def build_swordsman(self):
        self.off_smithy_window()
        self.board.build_swordsman()

    def render_win_window(self):
        if self.cout_amogus_fleks == 0 and self.is_sounds:
            pygame.mixer.Sound.play(pygame.mixer.Sound(r'sounds\win.mp3'))
        screen.blit(pygame.transform.scale(pygame.image.load(r"textures\scroll.png"), (450, 500)), (720, 240))
        if self.cout_amogus_fleks == len(self.amogus_fleks) or self.cout_amogus_fleks == 0:
            self.cout_amogus_fleks = 1
        screen.blit(pygame.transform.scale(pygame.image.load(self.amogus_fleks[self.cout_amogus_fleks - 1]), (200, 150)), (830, 390))
        self.cout_amogus_fleks += 1
        self.print_text(25, "Победил игрок номер " + str(self.board.motion), (815, 350))
        self.render_button(80, 35, 820, 600, "Выход", "main_menu", font_size=25)


class Swordsman:
    def __init__(self, pos):
        self.pos = (pos[0], pos[1] + 1)
        self.health = 15
        self.go = True
        self.death = False

    def move(self, pos, past_pos, montion, is_sound, sound, map):
        if montion == 1:
            image = (14, 15)
        else:
            image = (12, 13)
        if pos[0] > past_pos[0]:
            map[past_pos[1]][past_pos[0]] = image[0]
        elif pos[0] < past_pos[0]:
            map[past_pos[1]][past_pos[0]] = image[1]
        map[pos[1]][pos[0]], map[past_pos[1]][past_pos[0]] = map[past_pos[1]][past_pos[0]], map[pos[1]][pos[0]]
        self.pos = pos
        self.go = False
        if is_sound:
            pygame.mixer.Sound.play(sound)

    def hit(self, is_sound, sound):
        self.go = False
        if is_sound:
            pygame.mixer.Sound.play(sound)

    def treatment(self, is_sound, sound):
        self.health += 5
        if self.health > 15:
            self.health = 15
        self.go = False
        if is_sound:
            pygame.mixer.Sound.play(sound)

    def damage(self):
        self.health -= 10
        if self.health <= 0:
            self.death = True


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
fps = 30
clock = pygame.time.Clock()
while running:
    is_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or game.exit:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not is_click:
            if event.button == 3:
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
"""После улутшения чего либо окно строительства открывается после Второго клика"""
"""Появилась проблема с мечниками он второго мечника убил за один раз хотя должен за два нужно отловить момент сбоя"""