from pynput import mouse


# Funktion, die beim Mausklick aufgerufen wird
def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:  # Linksklick gedrückt
        print(f"Mausposition: ({x}, {y})")


# Listener starten
with mouse.Listener(on_click=on_click) as listener:
    print("Drücke die linke Maustaste, um die Position auszugeben. Zum Beenden STRG + C drücken.")
    listener.join()
