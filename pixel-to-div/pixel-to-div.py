import numpy as np
from PIL import Image

ASPECT_RATIO = 5
img = Image.open('input.jpg')
arr = np.array(img) 

hexArray = [ 
    [ 
        f'rgb({rgb[0]}, {rgb[1]}, {rgb[2]})' for rgb in values 
    ] for values in arr 
]

gridRow = ["1fr" for i in range(len(hexArray))]
gridRow = " ".join(gridRow)
gridColumn = ["1fr" for i in range(len(hexArray[0]))]
gridColumn = " ".join(gridColumn)

image = []
for row in hexArray:
    for column in row:
        image.append(f'<div style="background-color: {column};"></div>')

htmlString = f'''
    <html>
        <body style="overflow: hidden;">
            <div style="display: flex; width: 100vw;
                height: 100vh; align-items: center;
                justify-content: center;">
                <div style="display: grid;
                    width: {ASPECT_RATIO*len(hexArray[0])}px; height: {ASPECT_RATIO*len(hexArray)}px;
                    grid-template-columns: {gridColumn};
                    grid-template-rows: {gridRow};">
                    {''.join(image)}
                </div>
            </div>
        </body>
    </html>
'''

f = open("output.html", "w+")
f.write(htmlString)
f.close()
