import random as rand
import nxbt
import time
import sys

from Pattern import Pattern
from Color import Color

class Controller():
    def __init__(self) -> None:
        self.nx = nxbt.Nxbt()
        self.pro_controller = self.nx.create_controller(nxbt.PRO_CONTROLLER)
        self.nx.wait_for_connection(self.pro_controller)
        self.total_index_changes = 0 #This mod 16 will give the current color index
    
    def reset_canvas_pos(self) -> None:
        for x in range(16):
            self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.DPAD_UP, nxbt.Buttons.DPAD_LEFT])

    def select_color_tool(self) -> None:
        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.X])
        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.DPAD_UP, nxbt.Buttons.DPAD_RIGHT], down=0.1)
        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.A])
    
    def select_pencil_from_color_tool(self) -> None:
        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.DPAD_DOWN, nxbt.Buttons.DPAD_LEFT], down=0.1)
        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.A])

    def adjust_slider(self, value:int, reset_time:float) -> None:
        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.DPAD_LEFT], down=reset_time) #This resets the slider value to 0
        for x in range(value):
            self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.DPAD_RIGHT]) #Adjusting slider to desired value
    
    def adjust_color(self, hue:int, vividness:int, brighness:int) -> None:
        self.adjust_slider(hue, 3) #Changing the hue slider to the desired value

        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.DPAD_DOWN]) #Moving to vividness slider
        self.adjust_slider(vividness, 2.75)

        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.DPAD_DOWN]) #Moving to brightness slider
        self.adjust_slider(brighness, 2.75)

    def adjust_palette(self, palette:'list[Color]') -> None:
        self.select_color_tool()
        for x in palette:
            time.sleep(1)
            self.adjust_color(x.hue, x.vividness, x.brightness)
            time.sleep(1)
            self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.R])
            self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.DPAD_DOWN])
        self.nx.press_buttons(self.pro_controller, [nxbt.Buttons.A])
    
    def change_color(self, color_index:int) -> None:
        if color_index > 15:
            raise ValueError("Color index cannot be larger than 15")
            
        normal_change = color_index - self.total_index_changes % 16
        #wrapped_change = min(15 - color_index, color_index)
        change = normal_change #Change this to select the most efficent method
        if change > 0:
            action = nxbt.Buttons.R
        else:
            action = nxbt.Buttons.L
        
        for x in range(abs(change)):
            self.nx.press_buttons(self.pro_controller, [action]) #Moving to brightness slider
        
        self.total_index_changes += change



def main():
    control = Controller()
    pattern = Pattern.load_from_file(sys.argv[1])
    input("Press enter to continue with script execution: ")
    control.reset_canvas_pos()
    time.sleep(1)
    #control.adjust_palette(pattern.palette) #After this, press A to exit the menu
    time.sleep(1)
    #control.select_pencil_from_color_tool()
    while True:
        num = rand.randint(0, 15)
        print("Moving color to " + str(num))
        control.change_color(num)
        time.sleep(5)
    control.change_color(4)
    control.change_color(7)
    control.change_color(13)
    control.change_color(9)
    control.change_color(14)


if __name__ == "__main__":
    main()