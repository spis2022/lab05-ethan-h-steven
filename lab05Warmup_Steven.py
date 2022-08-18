from PIL import Image
# This imports the image from Python Imaging Library to make a copy and modify

bear = Image.open( "bear.png" ) # this opens the picture
print(bear.size) # This measures the size of the picture using pixel as units and printing 600, 800
bear.save("tmp_Steven.png") # create/overwrite tmp_Name.png with current image
pixel = bear.getpixel( ( 100, 200) ) # gets the pixel at the specific x, y coordinates. 100 and 200
print(pixel) # prints the pixel that you get from the bear
bear.putpixel( (100, 200), (0, 0, 0) ) # Puts the pixel back at that location

bear.save("ablackpixel_Steven.png")

for i in range(100):
# from 0 to 100
    bear.putpixel( (i, 200) , (0, 0, 0) )
    # put the pixel in that location based on the RGB color and (0,0,0) is black to that row
def invert( im ):
    # defines the function invert using image "im"

    (width, height) = im.size # set the width and height based of the size of the image


    # Loop over the entire image

    for x in range( width ):
    # loops the x range
        for y in range( height ):
        # loops the y range
            (red, green, blue) = im.getpixel((x, y))
            # Gets the pixel from the Image
            (red, green, blue) = ((255 - red), (255 - green), (255 - blue))
            # Inverts the image color
            im.putpixel((x, y), (red, green, blue))
            # puts back the inverted color pixel from the image
    return im # returns to the modified image "im"
bear.save("IB_Steven.png") # create/overwrite IB_Steven picture

def invert_block( im ):
# defines a new function
    ''' Invert the colors in the input image, im '''
    (width, height) = im.size # sets the width and height based on the image width and height
    for x in range( width//2, width): # loops the specific x area of pixels or "select"
        for y in range(0,height//2): # loops the specific x area of pixels or "select"
            (red, green, blue) = im.getpixel((x , y)) # gets pixel from the loops
            (red, green, blue) = ((255 - red), (255 - green), (255 - blue))  #  inverts those color from the pixels you get
            im.putpixel((x,y),(red,green,blue)) ## puts the inverted pixels
    return im # returns to the modified image "im"
blockBear = invert_block(bear) # give a name to the defined function
blockBear.save("invertedBlock_Steven.png") # create/overwrite "invertedBlock_Steven.png"