class GameStateManager:
    def __init__(self):
        self.states = []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        self.states.pop()

    def set(self, state):
        self.pop()
        self.push(state)

    def update(self, dt):
        self.states[-1].update(dt)

    def render(self, screen):
        self.states[-1].render(screen)

class GameState:
    def __init__(self, gsm):
        self.gsm = gsm

    def handle_input(self):
        pass

    def update(self, dt, events):
        pass

    def render(self, screen):
        pass
