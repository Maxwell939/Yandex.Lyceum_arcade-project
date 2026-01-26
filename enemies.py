import random

import arcade

from constants import RIGHT_FACING, LEFT_FACING, SCREEN_WIDTH, ENEMY_BIRD_SPEED


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()

    def update(self, player, delta_time: float = 1 / 60) -> None:
        super().update(delta_time)
        if self.collides_with_sprite(player):
            self.kill()


class EnemyBird(Enemy):
    def __init__(self):
        super().__init__()
        for i in range(1, 10):
            self.textures.append(arcade.load_texture(f"textures/bird/bird{i}"))

        self.cur_texture_index = 0
        self.texture_change_time = 0
        self.texture_change_delay = 0.05  # секунд на кадр

        self.direction = random.choice((RIGHT_FACING, LEFT_FACING))
        if self.direction == RIGHT_FACING:
            self.left = 0
        elif self.direction == LEFT_FACING:
            self.right = SCREEN_WIDTH

        self.scale = self.direction * -1
        self.change_x = self.direction * ENEMY_BIRD_SPEED

    def update(self, player, delta_time: float = 1 / 60) -> None:
        super().update(delta_time)
        if self.left == 0 or self.right == SCREEN_WIDTH:
            self.direction *= -1
            self.scale = -1 if self.direction == RIGHT_FACING else 1

    def update_animation(self, delta_time: float = 1 / 60):
        self.texture_change_time += delta_time
        if self.texture_change_time >= self.texture_change_delay:
            self.texture_change_time = 0
            self.cur_texture_index += 1
            if self.cur_texture_index >= len(self.textures):
                self.cur_texture_index = 0