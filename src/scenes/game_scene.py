from core.scene import Scene

from direct.gui.OnscreenText import OnscreenText
from src.entity.skybox import SkyBox
from src.entity.metro import Metro
from src.input_manager import keys

class GameScene(Scene):
    
    def __init__(self, game):
        super().__init__(game)
        
        self.create()
        self.start()
        
    def create(self):
        self.game.camera.setPos(0, 0, 3)
        self.objects['skybox'] = SkyBox(self.game)
        self.objects['metro'] = Metro(self.game)
        
    def update(self, dt):
        if keys['up']:
            self.change_scene('menu')
            
    def destroy(self):
        self.objects['skybox'].object.removeNode()
        self.objects['metro'].object.removeNode()
        self.objects.clear()
        return super().destroy()