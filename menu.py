import os
from moviepy.editor import *


def cut_from_beg(N, file, name_cut):
    # loading video dsa gfg intro video
    clip = VideoFileClip(file)

    # getting only first 5 seconds
    clip = clip.subclip(0, N)

    clip.write_videofile(name_cut)
    print("Done it")


def yuv_histogram():
    terminal_command = "ffmpeg -i vid2.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay -c:a copy video_w_histogram.mp4"
    os.system(terminal_command)
    print("Done it!")

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

def stereo2mono():
    value = input("Type 1 first, second type 2, finally 0 to exit: ")
    while value != 0:
        if value == "1":
            terminal_command1 = "ffmpeg -i vid2.mp4 -c:v copy -ac 1 mono-output.mp4"
            os.system(terminal_command1)
            value = input("Type 1 first, then type 2: ")
        elif value == "2":
            terminal_command2 = "ffmpeg -i mono-output.mp4 -acodec mp3 -vcodec copy mono_dif_codec.mp4"
            os.system(terminal_command2)
            value = input("Type 1 first, then type 2: ")
        else:
            break
    print("Done it! ")


if __name__ == '__main__':
    input_v = input("Introduce the oprion that you prefer. \n1) Cut N seconds\n2) Display YUV histogram \
                       \n3) Resize the video \n4) Convert it to mono and change the codec\nPut the option here: ")
    if input_v == "1":
        file = input("Type the path of the video: ")
        N = input("Type the int number of s you want to cut the video: ")
        cut_from_beg(N, file, "vid2.mp4")

    elif input_v == "2":
        yuv_histogram()

    elif input_v == "3":
        resize()

    elif input_v == "4":
        stereo2mono()

    print("Thank you for using it! <3 ")
