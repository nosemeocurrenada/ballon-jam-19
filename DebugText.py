from pygame.font import get_default_font, Font


class DebugText:
    def __init__(self):
        font_name = get_default_font()
        self.font = Font(font_name, 12)
        self.color = (255, 255, 255)
        self.position = (50, 50)
        self.displacement = (0, 24)
        self.toWrite = []

    def draw(self, surface, dt):
        last_position = self.position
        for t in self.toWrite:
            s = self.font.render(t, 0, self.color)
            surface.blit(s, last_position)
            last_position = [sum(x) for x in zip(last_position, self.displacement)]
        self.toWrite = []

    def write(self, text):
        self.toWrite.append(text)
