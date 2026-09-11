from locations.castle import *
from locations.forest import *
from inventory import inventory
import images
from playsound3 import playsound

print(images.castle)
playsound("kave_msri-flickering-neon-316717.mp3")

location = "forest"

while location != "end":
    if inventory:
        print(f"Ваш инвентарь: {', '.join(inventory)}")

    if location == "forest":
        location = forest()
    elif location == "cave":
        location = cave()
    elif location == "river":
        location = river()
    elif location == "mountains":
        location = mountains()
    elif location == "village":
        location = village()
    elif location == "swamp":
        location = swamp()
    elif location == "castle":
        location = castle()
    elif location == "castle_hall":
        location = castle_hall()
    elif location == "garden":
        location = garden()
    elif location == "dungeon":
        location = dungeon()
    elif location == "tower":
        location = tower()
