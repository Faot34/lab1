import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def animate():
    frame1 = """
     *
    ***
   *****
    ***
     *
    """
    frame2 = """
     *
    ***
   * * *
    ***
     *
    """
    
    while True:
        clear_screen()
        print(frame1)
        time.sleep(0.5)  # Pause for 0.5 seconds
        clear_screen()
        print(frame2)
        time.sleep(0.5)

animate()
