#!/usr/bin/python

import os
# from os import listdir
# from os.path import isfile, join
import sys
import time
from PIL import Image
from shutil import copyfile
# from subprocess import call

mypath = os.getcwd()
currentimage = ''
resultimage = ''
totalheight = 0
totalwidth = 0
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#
# file1 = onlyfiles[0]
# file2 = onlyfiles[1]
# print '',file1, file2


if len(sys.argv) == 1:
    print "You can also give filename as a command line argument"
    filename = raw_input("Enter Filename: ")
else:
    filename = sys.argv[1]

# data = [line.strip() for line in open(filename, 'r')]
print "filename:", filename
f = open(filename)
lines = f.readlines()
f.close()


def get_num_pixels(filepath):
    width, height = Image.open(open(filepath)).size
    return width, height
    # return width*height

# image1 ... imageN, bgcolor(name), V(ertical)/H(orizontal), gapsize(pixels)
# image1 image2 image3, black, V, 25
for l in lines:
    # firstName, lastName = myString.split()
    # [x.strip() for x in my_string.split(',')]
    images, bgcolor, orientation, gapsize = l.split(',')
    bgcolor.strip()
    orientation.strip()
    gapsize.strip()

    print "images:", images
    print "bgcolor:", bgcolor, "orientation:", orientation, "gapsize:", gapsize
    imagelist = images.split(' ')
    totimages = len(imagelist)
    totgap = int(gapsize) * (int(totimages) - 1)
    # totgap = ((int(totimages) - 1) * int(gapsize))

    for i in imagelist:
        i_w, i_h = get_num_pixels(i)
        finalwidth = i_w
        finalheight = i_h
        if "h" in orientation:
            totalheight += i_h
            totalwidth = i_w
            finalheight = totalheight + totgap

        if "v" in orientation:
            totalheight = i_h
            totalwidth += i_w
            finalwidth = totalwidth + totgap

        # print i, i_w, i_h

    # print "tw:", totalwidth, "th:", totalheight
    # print "fw:", finalwidth, "fh:", finalwidth
    # print "ti:", totimages, "tg:", totgap

    running = True
    resultimage = "result.gif"
    while running:
        for g, elem in enumerate(imagelist):
            if (g <= 0):
                image_1 = elem
            else:
                image_1 = 'work.gif'

            print "g:", g, "currentimage:", currentimage
            if (g + 1) == totimages:
                currentimage = ''

                running = False
            else:
                image_2 = imagelist[(g + 1) % len(imagelist)]

                if currentimage == '':
                    currentimage = image_1
                else:
                    currentimage = resultimage
                # print "currentimage:", currentimage

                g_w, g_h = get_num_pixels(currentimage)
                g2_w, g2_h = get_num_pixels(image_2)

                if "h" in orientation:
                    repage_h = g_h + g2_h + int(gapsize)
                    repage_w = g_w
                    geo = g_h + int(gapsize)
                    command = "convert %s -background %s -repage %dx%d -coalesce null: \\( %s -coalesce \\) -geometry +0+%d -layers Composite %s" % \
                        (image_1, bgcolor, repage_w, repage_h, image_2, geo, resultimage)

                if "v" in orientation:
                    repage_h = g_h
                    repage_w = g_w + g2_w + int(gapsize)
                    geo = g_w + int(gapsize)
                    command = "convert %s -background %s -repage %dx%d -coalesce null: \\( %s -coalesce \\) -geometry +%d+0 -layers Composite %s" % \
                        (image_1, bgcolor, repage_w, repage_h, image_2, geo, resultimage)


                # command = "convert %s -background %s -repage %dx%d -coalesce null: \\( %s -coalesce \\) -geometry +%d+0 -layers Composite %s" % \
                    # (image_1, bgcolor, repage_w, repage_h, image_2, geo, resultimage)
                print command
                os.system(command)
                # print "convert %s -background %d -repage %dx%d -coalesce null: \\( %s coalesce \\) -geometry +%d+0 -layers Composite %s" % \
                # (image_1, bgcolor, repage_w, repage_h, image_2, geo, resultimage)
                copyfile(resultimage, "work.gif")
        finalname = str(int(time.time())) + ".gif"
        copyfile(resultimage, finalname)
        os.unlink(resultimage)
        os.unlink("work.gif")

# #Combine anim1.gif and anim2.gif (first row)
# convert large_1.gif -background black -repage 225x480 -coalesce null: \( large_2.gif -coalesce \) -geometry +125+0 -layers Composite anim1+2.gif
# #Combine anim3.gif and anim4.gif (1st part of last row)
# convert anim1+2.gif -background black -repage 350x480 -coalesce null: \( large_3.gif -coalesce \) -geometry +250+0 -layers Composite anim3+4.gif
# #Combine anim3+4.gif and anim5.gif (last row)
# convert anim3+4.gif -repage 425x480 -coalesce null: \( large_4.gif -coalesce \) -geometry +325+0 -layers Composite anim3+4+5.gif
# #Combine all, leaving one in the middle empty
# convert anim1+2.gif -repage 500x480 -coalesce null: \( anim3+4+5.gif -coalesce \) -geometry +400+0 -layers Composite anim_all.gif
# # convert anim3+4.gif -fill green -tint 100 green.gif

# for i in onlyfiles:
#     processfile = i
#
#     if ".gif" in processfile:
#         print processfile, get_num_pixels(processfile)
