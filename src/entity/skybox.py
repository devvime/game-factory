from panda3d.core import Texture, TexturePool, LoaderOptions, TextureStage, TexGenAttrib, TransformState

class SkyBox:
    def __init__(self, game):
        self.game = game
        lo = LoaderOptions(flags = LoaderOptions.TF_generate_mipmaps)
        
        texture_cube_map = Texture("world_cube_map")
        texture_cube_map.setup_cube_map()
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/right.png',  z = 0, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/left.png',   z = 1, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/bottom.png', z = 2, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/top.png',    z = 3, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/front.png',  z = 4, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/back.png',   z = 5, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        
        TexturePool.add_texture(texture_cube_map)
        
        self.object = self.game.loader.load_model('assets/models/sphere.bam')
        self.object.reparent_to(self.game.render)
        self.object.set_texture(texture_cube_map)
        
        ts = TextureStage.get_default()
        
        self.object.set_tex_gen(ts, TexGenAttrib.M_world_cube_map)
        self.object.set_tex_hpr(ts, (0, 90, 180))
        self.object.set_tex_scale(ts, (1, -1))
        self.object.set_light_off()
        self.object.set_material_off()
        self.object.setScale(1000)