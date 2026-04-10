import pydirectinput
import keyboard
import time
import sys

# Settings
LEFT_PAW = 'a'      
RIGHT_PAW = 'd'      
START_COMBO = ['ctrl', 'f8'] 
STOP_KEY = 'esc'

# Speed: 0.01 is about 50 hits per second. 
SPEED = 0.01 

# The drumming loop
def bongo_frenzy():
    print(f"\n>>> Drumming has started! Press [{STOP_KEY.upper()}] to stop.")
    time.sleep(0.3) 
    
    while True:
        # Check for the stop key
        if keyboard.is_pressed(STOP_KEY):
            print(f"\n>>> Drumming has stopped! Press [{' + '.join(START_COMBO).upper()}] to Start.")
            time.sleep(0.5)
            return

        # Perform the drumming
        pydirectinput.press(LEFT_PAW)
        time.sleep(SPEED)
        pydirectinput.press(RIGHT_PAW)
        time.sleep(SPEED)

# Main menu and start/stop listener
def main():
    
    cat_art = r"""
                ⠀⠀⠀⠀⢠⡶⠚⢷⣤⡀⠀⠀⠀⠀⠀⣲⡶⠛⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⢠⡿⠁⠀⠀⠙⣷⣄⠀⢀⣴⡟⠁⠀⠀⢷⢹⡆      
                ⠀⠀⠀⣾⠃⠀⠠⠶⠚⠛⠛⠛⠛⠋⠀⠀⣀⡀⢸⠈⣿      
                ⠀⠀⢸⣏⡔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠉⠉⣿⠀⢹        
                ⠀⠀⢾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⢸⡇      
                ⠀⢠⣿⢠⣶⡆⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇     
                ⢒⡾⠁⠘⠟⠁⠀⠀⠀⠀⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⢸⡇      
                ⠉⣧⠀⠀⠀⠀⠃⠀⠀⠀⠈⠉⠠⣍⠀⠀⠀⠀⠀⠀⣸⡇        
                ⠀⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟ 
                ⠀⠀⠀⠛⣷⡦⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡴⠞⠋  
                ⠀⠀⠀⢰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣤⡀⢸⠃
                ⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣹⡄
                ⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⢿⣇
                ⠀⠀⠀⢸⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄
                ⠀⠀⠀⢸⡇⠘⡇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢸⣿
                ⠀⠀⠀⢸⡇⠀⠙⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⣿⠇
                ⠀⠀⠀⢸⡇⠀⢸⡆⠀⠀⠀⠀⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛
                ⠀⠀⠀⢸⣿⠀⠀⡇⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⢀⡇
                ⠀⠀⠀⠘⠿⠶⢶⢧⣦⣦⡴⢾⣥⣽⣤⣤⣤⣤⣤⣤⡴⣯⠤⠴⠶⠛⠋
    """
    
    print(cat_art)
    print("=========================================================")
    print("        BONGO CAT AUTO CLICKER READY TO DRUM... ")
    print(f"                START COMBO: {' + '.join(START_COMBO).upper()} ")
    print(f"                   STOP KEY: {STOP_KEY.upper()} ")
    print("=========================================================")
    print("Status: Waiting to start...")
    
    while True:
        # Check for the start combo
        if all(keyboard.is_pressed(k) for k in START_COMBO):
            bongo_frenzy()
            
        # Check for program exit
        if keyboard.is_pressed(STOP_KEY):
            print("\nExiting Program... Bye!")
            sys.exit()
        
        # Idle sleep to prevent high CPU usage
        time.sleep(0.05)

if __name__ == "__main__":
    main()