import SpriteSheet


class Boi:
    width = 80
    height = 100
    jumpSpeed = 500
    walkSpeed = 400
    floor = 300
    animations = {
        "moving": [
            {"x": 25, "y": 13, "w": 80, "h": 100, "duration": 200},
            {"x": 105, "y": 13, "w": 80, "h": 100, "duration": 200},
            {"x": 185, "y": 13, "w": 80, "h": 100, "duration": 200},
            {"x": 265, "y": 13, "w": 80, "h": 100, "duration": 200}
        ],
        "idle": [
            {"x": 25, "y": 13, "w": 80, "h": 100, "duration": 200}
        ]
    }

    def __init__(self):
        self.sheet = SpriteSheet.SpriteSheet("test_sprite.bmp")
        self.currentFrame = 0
        self.x = 400
        self.y = 200
        self.speed_x = 0
        self.speed_y = 0
        self.elapsedTime = 0
        self.currentAnimation = None
        self.images = []
        self.animate_idle()
        self.load_images()
        self.is_moving = False
        self.is_on_the_ground = False
        self.should_jump = False

    def load_images(self):
        frames = Boi.animations[self.currentAnimation]
        rects = [(frame["x"], frame["y"], frame["w"], frame["h"]) for frame in frames]
        self.images = self.sheet.images_at(rects, (255, 255, 255))

    def get_durations(self):
        frames = Boi.animations[self.currentAnimation]
        return [frame["duration"] for frame in frames]

    def update(self, dt):
        gravity = 1000
        max_falling_speed = 1000
        dt = dt/1000
        
        self.x += self.speed_x * dt
        self.x = max(0, self.x)
        self.x = min(720, self.x)

        if self.should_jump:
            self.speed_y = -Boi.jumpSpeed
            self.should_jump = False

        if self.y < Boi.floor:
            self.is_on_the_ground = False
            self.speed_y += gravity * dt
        else:
            self.is_on_the_ground = True
            self.speed_y = min(0, self.speed_y)
        self.speed_y = min(self.speed_y, max_falling_speed)
        self.y += self.speed_y * dt

        self.speed_x = 0

    # dt: Time from previous frame, in milliseconds
    def draw(self, surface, dt):
        self.update(dt)
        duration = self.get_durations()[self.currentFrame]
        self.elapsedTime += dt
        if self.elapsedTime > duration:
            self.currentFrame = (self.currentFrame + 1) % len(self.images)
            self.elapsedTime = 0
        image = self.images[self.currentFrame]
        surface.blit(image, (self.x, self.y))
        if self.currentFrame == 0 and not self.is_moving:
            self.animate_idle()
        self.is_moving = False

    def animate_moving(self):
        self.is_moving = True
        self.currentAnimation = "moving"
        self.load_images()

    def animate_idle(self):
        self.currentAnimation = "idle"
        self.load_images()

    def move_up(self, dt):
        self.animate_moving()
        self.should_jump = True

    def move_down(self, dt):
        self.animate_moving()

    def move_left(self, dt):
        self.animate_moving()
        self.speed_x = -Boi.walkSpeed

    def move_right(self, dt):
        self.animate_moving()
        self.speed_x = Boi.walkSpeed
