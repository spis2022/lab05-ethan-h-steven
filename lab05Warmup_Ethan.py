from PIL import Image

bear = Image.open( "bear.png" )

print(bear.size) ##prints bear size: 600,800
pixel = bear.getpixel( ( 100, 200) ) ##rgb val is 166,201,239
print(pixel)

bear.putpixel( (100, 200), (0, 0, 0) ) ##places a black pixel at 100,200

bear.save("singlePixelBear.png")

for i in range(100):  ##at y==200 make a row of black pixels

    bear.putpixel( (i, 200) , (0, 0, 0) )


def invert( im ):

    ''' Invert the colors in the input image, im '''

    (width, height) = im.size

    for x in range( width ):

        for y in range( height ):

            (red, green, blue) = im.getpixel((x, y)) ## gets pixel
            (red, green, blue) = ((255 - red), (255 - green), (255 - blue))  ## inverts
            im.putpixel((x,y),(red,green,blue)) ## puts the changed pixel
    return im ##returns the modified image

def invertBlock( im ):

    ''' Invert the colors in the input image, im '''

    (width, height) = im.size

    for x in range( width//2, width):

        for y in range(0,height//2):

            (red, green, blue) = im.getpixel((x , y)) ## gets pixel
            (red, green, blue) = ((255 - red), (255 - green), (255 - blue))  ## inverts
            im.putpixel((x,y),(red,green,blue)) ## puts the changed pixel
    return im ##returns the modified image


blockBear = invertBlock(bear)
blockBear.save("invertedBlockBear.png")


