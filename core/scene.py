class Scene:
    
    def __init__(self, game):
        self.game = game
        self.loaded = False
        self.objects = {}
        
    def start(self):
        self.loaded = True
        
    def ready(self):
        return self.loaded
        
    def destroy(self):
        for obj in self.objects:
            self.objects[obj].destroy()
            
    def change_scene(self, scene_name):
        self.destroy()
        self.game.active_scene = self.game.scenes[scene_name](self.game)
        
    def create(self):
        pass
    
    def update(self, dt):
        pass