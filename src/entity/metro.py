class Metro:
    
    def __init__(self, game):
        self.game = game
        
        self.create()
    
    def create(self):
        self.object = self.game.loader.loadModel("assets/scene.glb")
        self.object.reparent_to(self.game.render)
    
    def update(self):
        pass