from core.scene import Scene

class {{scene}}(Scene):
    
    def __init__(self, game):
        super().__init__(game)
        
        self.create()
        self.start()
        
    def create(self):
        ...
        
    def update(self, dt):
        ...