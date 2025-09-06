from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import loadPrcFile

from src.input_manager import setInputs
from src.scene_manager import scenes

loadPrcFile('config/config.prc') # type: ignore

class Game(ShowBase):
    
    def __init__(self):
        super().__init__()
        
        self.scenes = scenes
        self.current_scene = "main"        
        self.active_scene = self.scenes[self.current_scene](self)
        
        setInputs(self)
        
        self.taskMgr.add(self.update, "update")
    
    def update(self, task):
        dt = globalClock.getDt() # type: ignore
        
        if (self.active_scene.ready()):
            self.active_scene.update(dt)
        
        return Task.cont
        
game = Game()
game.run()