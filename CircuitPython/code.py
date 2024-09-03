# SPDX-FileCopyrightText: 2024 Matt Gray, mattg.co.uk
# SPDX-FileCopyrightText: Adapted from Liz Clark's 2023 EYESPI BFF example for Adafruit Industries https://learn.adafruit.com/adafruit-eyespi-bff
# SPDX-FileCopyrightText: In turn adapted from Phil B.'s 16bit_hello Arduino Code
#
# SPDX-License-Identifier: MIT

# Hardware:
# Pimoroni Pico Lipo, running CircuitPython 9.1.1
# Adafruit #5846 3.5" TFT 320x480 with Capacitive Touch Breakout Board - EYESPI
# Adafruit #5613 EYESPI Breakout Board - 18 Pin FPC Connector

# With SPI pin number changes, it should work on most CircuitPython boards.

import gc
import math
from random import randint
import time
import displayio
import board
import busio
import terminalio
import simpleio
from adafruit_hx8357 import HX8357
import adafruit_ft5336
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label, wrap_text_to_lines
from adafruit_display_shapes.rect import Rect

# If anything else is talking to the display, kill it.
displayio.release_displays()

# Set up the Pico Lipo's pinout based on how I wired it.
spi = busio.SPI(board.GP18, board.GP19, board.GP20)
tft_cs = board.GP7
tft_dc = board.GP8

# Define how we're talking ot the display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = HX8357(display_bus, width=480, height=320, rotation=0)

bitmap = displayio.Bitmap(display.width, display.height, 1)

palette = displayio.Palette(3)
palette[0] = 0x000000 # black
palette[1] = 0xffffff 
palette[2] = 0xff5500
palette.make_transparent(0)

tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Define the groups I use to arrange the display
topgroup = displayio.Group()
group = displayio.Group()
title_group = displayio.Group()

# topgroup is the main container.
display.root_group = topgroup

# Load in bitmap fonts, one for each size.
reg_16 = bitmap_font.load_font("/ProFont-Regular-16.pcf")
reg_20 = bitmap_font.load_font("/ProFont-Regular-20.pcf")
reg_24 = bitmap_font.load_font("/ProFont-Regular-24.pcf")
reg_32 = bitmap_font.load_font("/ProFont-Regular-32.pcf")

orange = 0xe08028
dark_orange = 0xff5500
black = 0x000000
white = 0xffffff


def clean_up(group_name):
    for _ in range(len(group_name)):
        group_name.pop()
    gc.collect()

def textpos(font, string, x, y, anchor_x:0, anchor_y:0):
    text = label.Label(font, text=string, color=orange)
    text.anchor_point = (anchor_x, anchor_y)
    text.anchored_position = (x,y)
    return text

def loading():
    gc.collect()

    group.append(textpos(reg_16, "Calculating Timelines", 20, (display.height / 2),0,0))
    time.sleep(1)
    group.append(textpos(reg_16, "Enumerating Variants", 20, (display.height / 2)+20,0,0))
    time.sleep(1)
    group.append(textpos(reg_16, "Reticulating Splines", 20, (display.height / 2)+40,0,0))
    time.sleep(1)

    dots="."
    group.append(textpos(reg_20, dots, 20, (display.height / 2)+60,0,0))      
    display.refresh()
    for x in range(11):
        time.sleep(0.2)
        dots +="  ."
        group.append(textpos(reg_20, dots, 20, (display.height / 2)+100,0,0))      
        group.pop(-2)

    clean_up(group)
    del dots
    gc.collect()


def show_bitmap(sleep, filename):
    gc.collect()
    bitmap = displayio.OnDiskBitmap(filename)
    grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

    group.append(grid)

    time.sleep(sleep)

    clean_up(group)
    del grid
    del bitmap
    gc.collect()

def mugshot(sleep, imagepath, name, variant):
    photo = displayio.Group(scale=1, x=20, y=100)
    title = displayio.Group(scale=1, x=140, y=100)

    # Title
    rect = Rect(0,0,320,40, fill=orange)
    title.append(rect)

    text = label.Label(reg_24, text=variant, color=white)
    text.anchor_point = (0.5, 0.5)
    text.anchored_position = (150,20)
    title.append(text)

    group.append(title)

    # Photo
    rect = Rect(0,0,106,139, fill=orange)
    photo.append(rect)
    bitmap = displayio.OnDiskBitmap(imagepath)
    bitmap_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader, x=3,y=3)

    photo.append(textpos(reg_16, name, 53, 145, anchor_x=0.5, anchor_y=0))
    photo.append(bitmap_grid)

    group.append(photo)

    time.sleep(sleep)

    clean_up(group)
    del rect
    gc.collect()

def timeline(sleep):
    gc.collect()
    tl = displayio.Group(scale=1, x=0, y=70)

    bitmap = displayio.OnDiskBitmap("timeline.bmp")
    grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

    tl.append(grid)
    
    group.append(tl)

    time.sleep(sleep/4)

    prune = label.Label(reg_16, text="PRUNED", color=dark_orange)
    prune.anchor_point = (0,0)
    prune.anchored_position = (50, 55)
    tl.append(prune)

    time.sleep(sleep/4)

    prune2 = label.Label(reg_16, text="PRUNED", color=dark_orange)
    prune2.anchor_point = (0,0)
    prune2.anchored_position = (200, 188)
    tl.append(prune2)

    time.sleep(sleep/4)
    time.sleep(sleep/4)

    clean_up(group)
    del prune
    del prune2
    del grid
    del bitmap
    gc.collect()


# Define header logo and title items which are on scren most of the time
header = displayio.Group(scale=1, x=0, y=0)
logo = displayio.Group(scale=1, x=20, y=20)

bitmap = displayio.OnDiskBitmap("tva.bmp")
bitmap_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader, x=3,y=3)
logo.append(bitmap_grid)
header.append(logo)

title_text = label.Label(reg_24, text="System Loading", color=orange)
title_text.anchor_point = (0.5, 0.5)
title_text.anchored_position = ((display.width / 2)+80, 50)
title_group.append(title_text)
header.append(title_group)

topgroup.append(header)
topgroup.append(group)

while True:
    title_text.text = "System Loading"
    loading()

    title_text.text = "Timeline"
    timeline(10)

    title_text.text = "Variant Details"
    mugshot(10, "loki-orange.bmp", "Loki", "Loki #43712")
    mugshot(10, "sylvie-orange.bmp", "Sylvie", "Loki #23554")

    show_bitmap(10, "miss_minutes.bmp")

del logo
del bitmap
del bitmap_grid
del title_text
clean_up(topgroup)
gc.collect()
