import os


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
    stereo2mono()