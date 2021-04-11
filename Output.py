from pywebio import input, output
from time import *

output.put_markdown("## Hi </fooders>")
output.put_markdown("<p>I am Jayant</p>")

output.put_table([
    ["Name", "code"],
    ['Food', 11],
    ['Water', 12],
    ['Sunlight', 13]
])

with output.popup("Subscribe to the page"):
    output.put_text("Join Other Customer!")

food = input.select("Choose Your Favorite Food", ['Maggi', 'Noodles'])
output.put_text("You Choose", food, "from given list")

output.put_processbar('bar')

for i in range(1, 11):
    output.set_processbar('bar', i / 10)
    sleep(0.1)

output.put_markdown("Your Order is ready")

if food == "Maggi":
    with open("maggi.jpg", "rb+") as f:
        image = f.read()
else:
    with open("noodles.jpg", "rb+") as f:
        image = f.read()

output.put_image(image, height="100", width="100")

output.put_file("You can download the food here", b"hello")
sleep(5)