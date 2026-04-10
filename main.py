import pydirectinput
import keyboard
import time
import sys

# Settings + steam bypass
pydirectinput.PAUSE = 0 

LEFT_PAW = 'a'      
RIGHT_PAW = 'd'      
START_COMBO = ['ctrl', 'f8'] 
STOP_KEY = 'esc'

# Steam usually ignores anything faster than 0.03s.
# 0.05 is safe and still very fast pace.
HOLD_TIME = 0.05 
# Gap between left paw and right paw.
GAP_TIME = 0.02 

# The drumming loop
def bongo_frenzy():
    print(f"\n>>> Drumming has started! Press [{STOP_KEY.upper()}] to stop.")
    time.sleep(0.3) 
    
    # Check for the stop key
    while True:
        if keyboard.is_pressed(STOP_KEY):
            print(f"\n>>> Drumming has stopped! Press [{' + '.join(START_COMBO).upper()}] to Start.")
            time.sleep(0.5)
            return

        # Perform the drumming
        pydirectinput.keyDown(LEFT_PAW)
        time.sleep(HOLD_TIME) 
        pydirectinput.keyUp(LEFT_PAW)
        
        time.sleep(GAP_TIME) 
        
        pydirectinput.keyDown(RIGHT_PAW)
        time.sleep(HOLD_TIME) 
        pydirectinput.keyUp(RIGHT_PAW)
        
        time.sleep(GAP_TIME)

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
    print("        BONGO CAT (STEAM VERSION) READY... ")
    print(f"                START: {' + '.join(START_COMBO).upper()} ")
    print(f"                 STOP: {STOP_KEY.upper()} ")
    print("=========================================================")
    print("Waiting to start...")
    
    while True:
        # Check for the start combo
        if all(keyboard.is_pressed(k) for k in START_COMBO):
            bongo_frenzy()
        if keyboard.is_pressed(STOP_KEY):
            sys.exit()
        time.sleep(0.05)

        # Check for program exit
        if keyboard.is_pressed(STOP_KEY):
            print("\nExiting Program... Bye!")
            sys.exit()

        # Idle sleep to prevent high CPU usage
        time.sleep(0.05)

if __name__ == "__main__":
    main()