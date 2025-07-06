import pygame
import random
from Const import WIN_WIDTH, WIN_HEIGHT
from entity import Entity
from entityFactory import EntityFactory
from player import Player
from background import Background
from barrel import Barrel
from oil import Oil


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.active_backgrounds: list[Background] = []
        self.active_obstacles: list[Entity] = []

        self.all_pistas_names_sequence = ['Level1Pista0', 'Level1Pista1', 'Level1Pista0']
        self.current_sequence_index = 0
        self.pista_height = 0
        self.pista_width = 0

        player1_start_pos = (50, 150)
        player2_start_pos = (50, 400)

        player1_keys = {'right': pygame.K_RIGHT, 'left': pygame.K_LEFT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}
        player2_keys = {'right': pygame.K_d, 'left': pygame.K_a, 'up': pygame.K_w, 'down': pygame.K_s}

        self.player1 = Player('car_1', player1_start_pos, player1_keys)
        self.player2 = Player('car_2', player2_start_pos, player2_keys)

        self.entity_list.append(self.player1)
        self.entity_list.append(self.player2)

        self._initialize_pistas()

        self.scroll_trigger_x = WIN_WIDTH - 200
        self.scroll_speed = 3

        self.obstacle_spawn_timer = 0
        self.obstacle_spawn_interval = 180
        self.spawnable_items = ['Barrel01', 'Oil']

    def _initialize_pistas(self):
        first_pista_temp = Background(self.all_pistas_names_sequence[0], (0, 0))
        self.pista_height = first_pista_temp.rect.height
        self.pista_width = first_pista_temp.rect.width

        x_offset = (WIN_WIDTH - self.pista_width) // 2

        pista_name = self.all_pistas_names_sequence[self.current_sequence_index % len(self.all_pistas_names_sequence)]
        first_pista = Background(pista_name, (x_offset, 0))
        self.active_backgrounds.append(first_pista)
        self.current_sequence_index += 1

        self._add_new_pista_if_needed()

    def _add_new_pista_if_needed(self):
        if self.active_backgrounds and self.active_backgrounds[0].rect.right < 0:
            self.active_backgrounds.pop(0)

        while self.active_backgrounds and self.active_backgrounds[-1].rect.right < WIN_WIDTH:
            last_pista = self.active_backgrounds[-1]
            pista_name = self.all_pistas_names_sequence[
                self.current_sequence_index % len(self.all_pistas_names_sequence)]

            new_pista_x = last_pista.rect.right
            new_pista_y = last_pista.rect.y

            new_pista = Background(pista_name, (new_pista_x, new_pista_y))
            self.active_backgrounds.append(new_pista)
            self.current_sequence_index += 1

        if not self.active_backgrounds or self.active_backgrounds[-1].rect.right < WIN_WIDTH:
            if not self.active_backgrounds:
                pista_name = self.all_pistas_names_sequence[
                    self.current_sequence_index % len(self.all_pistas_names_sequence)]
                pista_x_pos = (WIN_WIDTH - self.pista_width) // 2
                new_pista = Background(pista_name, (pista_x_pos, 0))
                self.active_backgrounds.append(new_pista)
                self.current_sequence_index += 1
            self._add_new_pista_if_needed()

    def _spawn_obstacle(self):
        pista_left_edge = (WIN_WIDTH - self.pista_width) // 2
        pista_right_edge = pista_left_edge + self.pista_width

        item_name = random.choice(self.spawnable_items)

        temp_item = EntityFactory.get_entity(item_name, (0, 0))
        if not temp_item: return

        spawn_x = random.randint(pista_left_edge, pista_right_edge - temp_item.rect.width)
        spawn_y = WIN_HEIGHT

        new_obstacle = EntityFactory.get_entity(item_name, (spawn_x, spawn_y))
        if new_obstacle:
            self.active_obstacles.append(new_obstacle)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.K_ESCAPE:
                    running = False

            self.window.fill((0, 0, 0))

            self.player1.update()
            self.player2.update()
            self.player1.move()
            self.player2.move()

            most_right_player_x = max(self.player1.rect.right, self.player2.rect.right)

            if most_right_player_x >= self.scroll_trigger_x:
                for bg in self.active_backgrounds:
                    bg.rect.x -= self.scroll_speed
                for obs in self.active_obstacles:
                    obs.rect.x -= self.scroll_speed
                self.player1.rect.x -= self.scroll_speed
                self.player2.rect.x -= self.scroll_speed

            for bg in self.active_backgrounds:
                self.window.blit(source=bg.surf, dest=bg.rect)

            for obs in self.active_obstacles:
                obs.rect.y -= self.scroll_speed
                self.window.blit(source=obs.surf, dest=obs.rect)

            self.obstacle_spawn_timer += 1
            if self.obstacle_spawn_timer >= self.obstacle_spawn_interval:
                self._spawn_obstacle()
                self.obstacle_spawn_timer = 0

            self.active_obstacles = [obs for obs in self.active_obstacles if obs.rect.bottom > 0]

            self._add_new_pista_if_needed()

            self.window.blit(source=self.player1.surf, dest=self.player1.rect)
            self.window.blit(source=self.player2.surf, dest=self.player2.rect)

            for obs in self.active_obstacles:
                if self.player1.rect.colliderect(obs.rect):
                    obs.on_collide(self.player1)

                if self.player2.rect.colliderect(obs.rect):
                    obs.on_collide(self.player2)

            pygame.display.flip()
            clock.tick(60)

        return "menu"