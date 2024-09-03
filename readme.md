# My Interpretation of Marvel's TVA Tempad
Hi, I'm [Matt Gray](https://mattg.co.uk). You may know me from [my YouTube channel](https://youtube.com/mattgrayyes), my work with [Tom Scott](https://tomscott.com) and [The Technical Difficulties](https://techdif.co.uk), or even as a [broadcast engineer](https://unnamed.media) working in radio and TV.

Watching the Loki TV series, I spotted the little handheld folding computer thing that the Time Variance Authority use and liked the look of it. After a quick search, I couldnt see anyone else who had made a replica with a working screen, so decided I should have a go!

![Photo of the finished product Tempad, showing a branching timeline on screen](Images/Tempad.jpg?raw=true)

I documented my build progress in this YouTube video:

### 📺 [I made a Marvel prop from Loki, and Deadpool & Wolverine!](https://www.youtube.com/watch?v=B-IjAkmit-Q)
[![YouTube video thumbnail, very similar to the previous image, but with a photos of me, deadpool and wolverine overlaid, and text saying "it works!"](Images/Youtube%20Thumbnail.jpg?raw=true)](https://www.youtube.com/watch?v=B-IjAkmit-Q)

## Hardware
*  [Pimoroni Pico Lipo 16Mb](https://shop.pimoroni.com/products/pimoroni-pico-lipo?variant=39335427080275), running [CircuitPython 9.1.1](https://circuitpython.org/board/pimoroni_picolipo_16mb/)
*  [Adafruit #5846 3.5" TFT 320x480 with Capacitive Touch Breakout Board - EYESPI](https://www.adafruit.com/product/5846)
*  [Adafruit #5613 EYESPI Breakout Board - 18 Pin FPC Connector](https://www.adafruit.com/product/5613)

With SPI pin number changes, it should work on most CircuitPython boards.

## 3D Printing
I've printed all the parts successfuly both with the [Bambu Lab A1 Combo](https://shareasale.com/r.cfm?b=2485357&u=4351340&m=138211&urllink=&afftrack=) and the [Bambu Lab X1 Carbon](https://shareasale.com/r.cfm?b=2353821&u=4351340&m=138211&urllink=&afftrack=).

In my final products, the base, base lid, and buttons are multi-material 3D prints.

I've exported the models as:

* 3MF files for BambuStudio, with multimaterial and support information.
* generic STL files.

Here's a render of what the 3D model would look like if it was made out of metal:

![Render of my Tempad 3D model, shiny metal on a grey void background](Images/Tempad%20Render.jpg?raw=true)
