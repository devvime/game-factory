from core.scene import Scene

from direct.gui.DirectGui import DirectButton
from direct.gui.OnscreenText import OnscreenText

class MenuScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        
        self.create()
        self.start()

    def create(self):
        self.objects['title'] = OnscreenText(text="Hello, world!", scale=0.1, pos=(0, 0.1))
        self.objects['start_button'] = DirectButton(
            text="Start game", scale=0.1, pos=(0, 0, -0.1), command=self.start_game
        )
        self.objects['exit_button'] = DirectButton(text="Exit", scale=0.1, pos=(0, 0, -0.3), command=exit)
        
    def start_game(self):
        self.change_scene('game')

    def update(self, dt): 
        ...
