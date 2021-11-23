# EX3 # - Roger Viñeta

import os


def resize():
    menu = input("Choose your option:\n 1(1280x720):\n 2(640x480):\n 3(360x240):\n 4(160x120): ")
    if menu == "1":
        terminal_command = "ffmpeg -i vid2.mp4 -s 1280x720 -c:a copy resized1280x720.mp4"
        os.system(terminal_command)
    elif menu == "2":
        terminal_command = "ffmpeg -i vid2.mp4 -s 640x480 -c:a copy resized640x480.mp4"
        os.system(terminal_command)
    elif menu == "3":
        terminal_command = "ffmpeg -i vid2.mp4 -s 360x240 -c:a copy resized360x240.mp4"
        os.system(terminal_command)
    elif menu == "4":
        terminal_command = "ffmpeg -i vid2.mp4 -s 160x120 -c:a copy resized160x120.mp4"
        os.system(terminal_command)
    print("Done it!")


if __name__ == '__main__':
    resize()
