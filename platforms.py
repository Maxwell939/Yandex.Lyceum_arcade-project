import arcade


class Platform(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("textures/platforms/platform.png")
        self.scale_y = 0.7
        self.scale_x = 1.1

    def update(self, delta_time: float = 1 / 60) -> None:
        super().update(delta_time)

        if self.top < 0:
            self.kill()


class MovingPlatform(Platform):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("textures/platforms/moving_platform.png")