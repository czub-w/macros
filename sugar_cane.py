from pynput.keyboard import Listener, Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
# Inicjalizacja kontrolera klawiatury
keyboard = KeyboardController()
mouse = MouseController()

stop_loop = False

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

# Sekwencja naciskania klawiszy FARMA SUGAR CANE
def key_sequence():
    time.sleep(0.1)
    press_and_hold('a',19)  # Trzymanie 'w' i 'a' przez 2 sekundy
    time.sleep(0.1)
    press_and_hold('w',1)
    time.sleep(0.1)
    press_and_hold('s',19)
    time.sleep(0.1)
    press_and_hold('d',1.5)
    time.sleep(0.1)
    press_and_hold('a',1)


def on_press(key):
    """Funkcja nasłuchująca naciśnięcie klawisza."""
    global stop_loop
    try:
        if key.char == 'q':  # Sprawdzamy, czy naciśnięto 'q'
            print("Naciśnięto 'q', zatrzymywanie pętli.")
            stop_loop = True
            return False  # Zatrzymanie nasłuchu
    except AttributeError:
        pass

def garden():
    time.sleep(0.1)
    press_and_hold_mouse(Button.left,0.3)
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
    time.sleep(0.1)
    press_and_hold_mouse(Button.left,3)



def main():
    global stop_loop
    # Tworzenie listenera do nasłuchiwania klawiszy
    for _ in range(15):  # Pętla, która wykona key_sequence() 15 razy
        key_sequence()  # Wywołanie sekwencji klawiszy
    garden()
        
    

if __name__ == "__main__":
    time.sleep(3)
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    