from instance import Instance


class Player(Instance):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.vx = 0
        self.vy = 0

    def handle_event(self, event_name, event):
        if event_name == "keyPressed":
            self.movement(event)
        elif event_name == "keyReleased":
            self.stop_movement(event)

    def movement(self, event):
        if event.keysym == "Left":
            self.vx = -self.speed
        elif event.keysym == "Right":
            self.vx = self.speed
        elif event.keysym == "Up":
            self.vy = -self.speed
        elif event.keysym == "Down":
            self.vy = self.speed

    def stop_movement(self, event):
        if event.keysym in ("Left", "Right"):
            self.vx = 0
        if event.keysym in ("Up", "Down"):
            self.vy = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Stay within boundaries
        # self.x = max(0, min(WIDTH - 50, self.x))
        # self.y = max(0, min(HEIGHT - 50, self.y))

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill="red")
