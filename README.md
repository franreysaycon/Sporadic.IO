# SPORADIC.IO

Sometimes you just have an itch in your head and you want to implement such code, no matter how weird and non-standard it is in practice.
Of course, as engineers you would do your best to make sure it is still efficient and takes into account optimal solutions.
This is a SPORADIC.IO! A place where you just have fun and implement even the weirdest of problems!

Some CRAAAZZYY ideas i've implemented so far.

## Pixel To Div
I just had an epiphany while staring at display grids. Then it hit me, I can recreate how images are rendered in the first place.
Why not get the rgba values of small images and convert them into html and css! 

### Installation
1. Install everything, very recommended you do this in a virtualenv, `Python >3.7` and above.
2. `pip install -r pixel-to-div/requirements.txt`
3. Run the script. `pixel-to-div.py` 
4. Check out the output.html!

For now, everything was hardcode. You can edit the ASPECT_RATIO to a higher size if you want your image to be bigger. It automatically gets the pixel width and height of the image input so you don't have to worry about that.

Take note: The generated html will be slow loading because, what did you expect? You are basically loading thousands of divs (dependent on the size of your image, on one html file.) That's why I recommend doing this for pixel art! Possible optimization, extend divs based on neighbor, an interesting problem don't you think? (You can do a PR for that)

