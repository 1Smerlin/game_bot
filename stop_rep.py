import keyboard
import time

run = True


def stop():
    global run  # Globale Variable ändern
    run = False


# Hotkey definieren
keyboard.add_hotkey("esc", stop)

# Schleife
round = 0
while run:
    round += 1
    print(f"Runde: {round}")
    time.sleep(1)
    if round == 5:
        break

print("Schleife beendet.")
