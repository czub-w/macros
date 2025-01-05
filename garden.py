from pynput.keyboard import Listener, Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

keyboard = KeyboardController()
mouse=MouseController()
def press_and_hold_multiple(keys, duration):
    """Trzyma wiele klawiszy przez określony czas."""
    print(f"Trzymam klawisze {keys} przez {duration} sekund...")
    for key in keys:
        keyboard.press(key)  # Naciskamy klawisze

    time.sleep(duration)  # Czekamy określoną ilość czasu

    for key in keys:
        keyboard.release(key)  # Zwolnienie klawiszy
    print(f"Zwolniono klawisze {keys}.")
def press_and_hold(key, duration):
    """Przytrzymuje klawisz przez określony czas."""
    print(f"Trzymam klawisz {key} przez {duration} sekund...")
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)
    print(f"Zwolniono klawisz {key}.")

def press_and_hold_mouse(button, duration):
    """Przytrzymuje klawisz przez określony czas."""
    print(f"Trzymam klawisz {button} przez {duration} sekund...")
    mouse.press(button)
    time.sleep(duration)
    mouse.release(button)
    print(f"Zwolniono klawisz {button}.")    


def garden():
    time.sleep(0.1)
    press_and_hold('/',0.1)
    time.sleep(0.1)
    press_and_hold('g',0.1)
    time.sleep(0.1)
    press_and_hold('a',0.1)
    time.sleep(0.1)
    press_and_hold('r',0.1)
    time.sleep(0.1)
    press_and_hold('d',0.1)
    time.sleep(0.1)
    press_and_hold('e',0.1)
    time.sleep(0.1)
    press_and_hold('n',0.1)
    time.sleep(0.1)
    press_and_hold(Key.enter,1)



if __name__ == "__main__":
    time.sleep(3)
    garden()
    