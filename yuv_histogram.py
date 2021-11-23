# EX2 # - Roger Viñeta

import os

def yuv_histogram():
    terminal_command = "ffmpeg -i vid2.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay -c:a copy video_w_histogram.mp4"
    os.system(terminal_command)
    print("Done it!")


if __name__ == '__main__':
    yuv_histogram()

