keys = {
    "up" : False,
    "down" : False,
    "left" : False,
    "right" : False,
    "shoot" : False
}

def setInputs(game):
    game.accept("w", updateKeys, ["up", True])
    game.accept("w-up", updateKeys, ["up", False])
    game.accept("s", updateKeys, ["down", True])
    game.accept("s-up", updateKeys, ["down", False])
    game.accept("a", updateKeys, ["left", True])
    game.accept("a-up", updateKeys, ["left", False])
    game.accept("d", updateKeys, ["right", True])
    game.accept("d-up", updateKeys, ["right", False])
    game.accept("mouse1", updateKeys, ["shoot", True])
    game.accept("mouse1-up", updateKeys, ["shoot", False])


def updateKeys(controlName, controlState):
    keys[controlName] = controlState
