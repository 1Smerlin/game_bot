import os
import time
import json
from PIL import Image
import pyautogui as pg
import keyboard

# >>> Variablen

image_folder = "./items/"

triger_file = "./triger.json"

run = True


def stop():
    global run
    run = False


# >>> keyboard
keyboard.add_hotkey("esc", stop)


# >>> Triger


triger = {}


def load_triger():
    with open(triger_file, "r") as file:
        triger = json.load(file)


def count_triger(item_name):
    if item_name in triger:
        triger[item_name] += 1
    else:
        triger[item_name] = 1


def write_triger():
    with open(triger_file, "w") as file:
        json.dump(triger, file, indent=4)


# >>> Image name


def check_image_name(item_name, image_name):
    if image_name == "image.png":
        numbers = [int(f.replace(item_name, "").replace(".png", "")) for f in image_list if f.startswith(item_name) and f.endswith(".png")]
        numbers.sort()  # Sortiere die Zahlen
        next_number = numbers[-1] + 1 if numbers else 1  # Nächste freie Zahl ermitteln

        # Neuer Name
        new_image_name = f"{item_name}{next_number}.png"
        os.rename(f"{image_folder}{item_name}/{image_name}", f"{image_folder}{item_name}/{new_image_name}")  # Datei umbenennen
        return new_image_name
    else:
        return image_name


# >>> Image
def get_image_center(image_path):
    with Image.open(image_path) as img:
        width, height = img.size  # Breite und Höhe des Bildes
        x_center = width // 2  # Horizontale Mitte
        y_center = height // 2  # Vertikale Mitte
        return (x_center, y_center)


def checkNettle(item_name, image_name):
    image_name = check_image_name(item_name, image_name)
    image_path = image_folder + item_name + "/" + image_name
    if os.path.exists(image_path):
        try:
            pos = pg.locateOnScreen(image_path, confidence=0.75)
            center = get_image_center(image_path)
            pg.moveTo(pos.left + center[0], pos.top + center[1])
            pg.click()
            print(f"left: {pos.left} top: {pos.top}")
            print(f"Klick auf Bild: {image_path} an Position: {pos}")
            count_triger(item_name)
            time.sleep(10)
        except Exception as e:
            print(f"{image_path} nicht gefunden.")
            # print(f"Fehler bei der Bildsuche: {e}")
    else:
        print("path not exist")


# search_item = [0, 1]
search_item = [1]

item_list = ["eisen", "holz"]

load_triger()
while run:
    for search_number in search_item:
        item_name = item_list[search_number]
        image_list = [file for file in os.listdir(f"{image_folder}{item_name}") if os.path.isfile(os.path.join(f"{image_folder}{item_name}", file))]
        for image_name in image_list:
            checkNettle(item_name, image_name)
            if not run:
                break
        print(f"{item_name} Search Finish")

write_triger()
