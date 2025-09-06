from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import loadPrcFile, AntialiasAttrib, LVector4

from src.input_manager import setInputs
from src.scene_manager import scenes

loadPrcFile('config/config.prc') # type: ignore

class Game(ShowBase):
    
    def __init__(self):
        super().__init__()
        
        self.render.set_antialias(AntialiasAttrib.MMultisample)
        self.render.setShaderAuto()
        self.win.setClearColor(LVector4(0.53, 0.81, 0.92, 1))
        self.render.setShaderAuto()
        self.disableMouse()
        
        self.scenes = scenes
        self.current_scene = "menu"        
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