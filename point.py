class point:
    def __init__(self, location, target):
        self.location = location
        self.target = target

class pixel:
    def __init__(self, location, pixelXY, color = (255,255,255)):
        self.location = location
        self.pixelXY = pixelXY
        self.color = color