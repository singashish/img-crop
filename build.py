import subprocess


def build():
    subprocess.run(["pyinstaller", "crop/crop.py", "--onefile", "--name", "ImgCrop"])

if __name__ == "__main__":
    build()