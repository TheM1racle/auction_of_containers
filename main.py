import subprocess

filename = "gallery/horse.jpg"

subprocess.run(['chafa', filename, '--size', '150x150'])