import kdtree
class Color:

    def __init__(self, hue:int, vividness:int, brightness:int) -> None:
        if hue > 29:
            raise ValueError("Hue value cannot be larger than 30")
        if vividness > 14:
            raise ValueError("Vividness value cannot be larger than 15")
        if brightness > 14:
            raise ValueError("Brightness value cannot be larger than 15")

        self.hue = hue
        self.vividness = vividness
        self.brightness = brightness
    
    def __repr__ (self) -> str:
        return f"hue: {self.hue} vividness: {self.vividness} brightness: {self.brightness}"
    
    @staticmethod
    #This method is pretty much just copied from https://github.com/Thulinma/ACNLPatternTool/blob/bf2fd35a7a1c841b267f968ddfcfa043b4aaaa29/src/libs/ACNHFormat.js
    #and translated into python
    def from_rgb(r:int, g:int, b:int) -> 'tuple[int]':
        Sinc = 6.68
        Vstart = 7.843
        Vinc = 5.58

        r /= 255
        g /= 255
        b /= 255

        M = max(r, g, b)
        m = min(r, g, b)
        C = M - m

        h = 0

        if C == 0:
            h = 0
        elif M == r:
            h = ((g - b) / C) % 6
        elif M == g:
            h = (b - r) / C + 2
        else:
            h = (r - g) / C + 4

        if h < 0:
            h += 6
        
        if M == 0:
            s = 0
        else:
            s = (C/M) * 100
        
        v = M * 100

        values = (max(0, min(29, round(h * 5))),
        max(0, min(14, round(s / Sinc))),
        max(0, min(14, round((v - Vstart) / Vinc))))

        return Color(values[0], values[1], values[2])
    