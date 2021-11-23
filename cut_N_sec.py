from moviepy.editor import *

def cut_from_beg(N, file, name_cut):
    # loading video dsa gfg intro video
    clip = VideoFileClip(file)

    # getting only first 5 seconds
    clip = clip.subclip(0, N)

    clip.write_videofile(name_cut)
    print("Done it")


if __name__ == '__main__':
    menu = input("Input 1 if you want to cut the video N sec from the beggining to N: ")
    file = input("Type the path of the video: ")
    if menu == "1":
        N = input("Type the int number of s you want to cut the video: ")
        cut_from_beg(N, file, "vid2.mp4")
    else:
        print("that was never an option ;) ")