from core.scene import Scene

from direct.gui.OnscreenText import OnscreenText

class GameScene(Scene):
    
    def __init__(self, game):
        super().__init__(game)
        
        self.create()
        self.start()
        
    def create(self):
        self.objects['title'] = OnscreenText(
            text="Game scene",
            scale=0.1,
            pos=(0, 0.1)
        )
        
    def update(self, dt):
        ...