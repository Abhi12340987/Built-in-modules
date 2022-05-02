import time
import os

while True:
    if os.path.exists("Built-in modules/vegetable.txt"):

        with open("Built-in modules/vegetable.txt") as file:
            print(file.read())
    else: 
        print("File does not exist.")

    time.sleep(5)






