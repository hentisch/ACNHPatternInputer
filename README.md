# ACNHPatternInputer
A project which will automatically input a pattern from acpatterns.com, allowing for utilization of native ACNH features as well as the publishing of created patterns.

### Installation:
First, install [NXBT](https://github.com/Brikwerk/nxbt), following the instructions on their Github page. Due to the low-level nature of what the libary does - making your computer pretend to be a Switch Pro Controller over Bluetooth - this library will only run on Linux computers which allow for low-level configuration of bluetooth devices. 

After installing NXBT, clone this repo into a folder of your choice

### Usage:
First, go to [acpatterns.com](acpatterns.com), and create a pattern you would like to have on your Island. Make sure to save it as the .ACNH (Animal Crossing New Horizons File), not as an .ACNL (Animal Crossing New Leaf) file. You can place this anywhere on your computer, just make sure to save the file path.

Now, turn on your Switch and open Animal Crossing New Horizons. Open up a pattern, and make sure that your pen tool is at the default starting location (don't mess with anything after opening the pattern). This pattern does not have to be blank.

On your Nintendo Switch, navigate to the "Change Grip/Order" menu. Due to certain quirks with controller emulation, make sure to pair your emulated controller before any other controllers. You may use additional, real controllers along with this emulated controller used to input the pattern, however connect those after paring your emulated controller. Once you are in the directory you cloned this repo into, run "sudo python3 controller.py <path to pattern file>" in the command line. Note that this needs to be run in sudo due to certain permissions the NXBT library requires. If you would like to avoid giving the library root permissions (which is possibly a good idea), there is a guide on their github on how to add your user account into a specific group which has specific access to the bluetooth permissions.
  
Once your program runs it should connect to your Switch, and then wait for further input to start drawing the pattern. Use your touch controlls or another controller you coneccted to navigate to the design pattern you would like to draw your new pattern in. Once you have selected this pattern, press enter and wait for the pattern to be drawn. The program should print "Done!", at which point you can quit the program.
  
### Issues and Contributions:
If you experience any issues with getting this project running on your computer and Switch, feel free to create a Github issue. Additionally, if you have a feature request for this project you can either ask for it via a Github issue, or prefferably code a solution to yourself and submit a Pull Request. 
