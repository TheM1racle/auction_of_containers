import subprocess
import random
import time

filename0 = "gallery/horse.jpg"
filename1 = "gallery/begemot.jpeg"
filename2 = "gallery/tapir.png"
filename3 = "gallery/porsche.jpg"



class Logic():
    def __init__(self):
        pass
    
    def get_photo(self, filename):
        subprocess.run(['chafa', filename, '--size', '100x100'])
        

tabak = Logic()
file_result = random.choice([filename0, filename1, filename2, filename3])
tabak.get_photo(filename=file_result)