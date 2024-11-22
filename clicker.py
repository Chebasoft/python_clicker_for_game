from ahk import AHK
import time
import random
import keyboard

ahk = AHK()
window_title = "Asterios"
running = False  # Flag for start/stop control

def toggle_running():
    global running
    running = not running
    if running:
        print("Script started")
    else:
        print("Script stopped")

# Assigning a hotkey to enable the clicker
keyboard.add_hotkey("tab", toggle_running)

try:
    window = ahk.find_window(title=window_title)
    if window:
        window.activate()
        time.sleep(7)

    while True:
        # If the flag is turned on, we start the cycle of using cans
        if running:
            if not window.is_active:
                print("Window not active, reactivating...")
                window.activate()
                reactivation_delay = random.uniform(1, 3)  # Random pause between 1 and 3 seconds
                time.sleep(reactivation_delay)
                print("Window activated after reactivation delay")

            print("Pressing F10")
            ahk.key_press('=')
            ahk.key_press('-')
            ahk.key_press('0')
            #ahk.key_press('F11')
            pause_time = random.uniform(0.7, 1.5)  # expanded the pause range of can presses
            print(f"Sleeping for {pause_time:.2f} seconds")
            time.sleep(pause_time)
        else:
            # pause to avoid overloading the processor when the script is paused
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Script interrupted by user.")
except Exception as e:
    print(f"An error occurred: {e}")