import subprocess


filename = "gallery/horse.jpg"

subprocess.run(['chafa', filename, '--size', '100x100'])