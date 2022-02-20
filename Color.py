class Color:

    color_conversions = {}
    with open("Colors.csv", "r") as f:
        for x in f.readlines():
            line = x.split(",")
            color_conversions[line[3]] = (int(line[0]), int(line[1]), int(line[2]))
            #In each tuple the values go "Hue", "Vividness", and "Brightness"
    
    def __init__(self, hue:int, vividness:int, brightness:int) -> None:
        if hue > 30:
            raise ValueError("Hue value cannot be larger than 30")
        if vividness > 15:
            raise ValueError("Vividness value cannot be larger than 15")
        if brightness > 15:
            raise ValueError("Brightness value cannot be larger than 15")

        self.hue = hue
        self.vividness = vividness
        self.brightness = brightness
    
    def __repr__ (self) -> str:
        return f"hue: {self.hue} vividness: {self.vividness} brightness: {self.brightness}"
    
    @staticmethod
    def color_from_hex(hex:str) -> 'Color':
        colors = Color.acnh_from_hex(hex)
        return Color(colors[0], colors[1], colors[2])

    @staticmethod
    def acnh_from_hex(hex:str) -> 'tuple[int]':
        return Color.color_conversions[hex]
    
    @staticmethod
    def int_to_color_hex(n:int):
        hex_value = hex(n)[2:]
        if n <= 16:
            hex_value = "0" + hex_value
        return hex_value

if __name__ == "__main__":
    col = Color.color_from_hex("C82248")
    