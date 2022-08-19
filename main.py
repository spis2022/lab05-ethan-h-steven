from PIL import Image # imports the image from the Python Imaging Library
bear = Image.open( "bear.png" ) # opens the image

#print("Running lab05Warmup_Steven.py") # let us know it's running lab05Warmup_Steven.py

#import lab05Warmup_Steven             # this will cause lab05Warmup_Steven.py to run

#print("Running lab05Warmup_Ethan.py")  # let us know it's running lab05Warmup_Ethan.py

#import lab05Warmup_Ethan               # this will cause lab05Warmup_Ethan.py to run


def grayscale( im ): # defines grayscale function

    (width, height) = im.size # sets the size based on the image width and height

    for x in range( width ):

        for y in range( height ): # "loop to select the entire image area to modify"

            (red, green, blue) = im.getpixel((x, y)) ## gets pixel
            red = int(red*.21)
            green = int(green*.72)
            blue = int(blue*.07)
            gVal = red + green + blue
            im.putpixel((x,y),(gVal,gVal,gVal)) ## puts the changed pixel
    return im ##returns the modified image

def binarize(im, thresh, startx, starty, endx, endy): # define "binarize" function

      (width, height) = im.size # sets the size based on the image width and height
      if (thresh>=255 and thresh<=255 and startx<=0 and starty>=0 and endx<= width and endy>=height):
    
        for x in range(startx,endx):
  
          for y in range(starty,endy): # "loop to select the entire image area to modify"
  
              (red, green, blue) = im.getpixel((x, y)) ## gets pixel
              red = int(red*.21)
              green = int(green*.72)
              blue = int(blue*.07)
              gVal = red + green + blue
              
              if (gVal > thresh):
                im.putpixel((x,y),(255,255,255))
              else:
                im.putpixel((x,y),(0,0,0))
      else:
        print("Warning") # Otherwise print warning

      return im  ##returns the modified image  

def mirrorVert(im): # Defines mirrorVert function using im
  (width,height) = im.size # sets the width and height based on the image size
  for x in range(width):
    for y in range(height//2): # Bear image area selection
      pixel1 = im.getpixel((x,y)) # Gets the pixel
      mirrorLoc = height - y - 1
      im.putpixel((x,mirrorLoc),pixel1) # Puts back the pixel
  
  return im ##returns the modified image

def mirrorHoriz(im): # Defines mirrorVert function using im
  (width,height) = im.size # sets the width and height based on the image size
  for x in range (width//2):
    for y in range (height):
      pixel1 = im.getpixel((x,y)) # gets the pixel
      pixelX = width - 1 - x
      im.putpixel((pixelX,y),pixel1) # puts the modified pixel back
  
  return im ##returns the modified image

def flipVert(im): # defines flipVert function
  (width,height) = im.size # sets the width and height based on the image size
  for x in range(width):
    for y in range(height//2):
      hMinusY = (height - y - 1)
      pixelStorage = im.getpixel((x,hMinusY))
      im.putpixel(((x,hMinusY)),im.getpixel((x,y)))
      im.putpixel((x,y),pixelStorage)
      
  return im ##returns the modified image


def scale(im1): # defines scale function
  (width,height) = im1.size
  im = Image.new('RGB',(width//2,height//2))
  for x in range (0,width,2):
    for y in range (0,height,2):
      im.putpixel((x//2,y//2),im1.getpixel((x,y)))
    
  return im ##returns the modified image

  
def blur(im1): # defines blur function
  (width,height) = im1.size # sets the width and height based on the image size
  im = Image.new('RGB',(width,height))

  rSum = 0
  gSum = 0
  bSum = 0
  
  for x in range (0,width,5):
    for y in range (0,height,5):
      rSum = 0
      gSum = 0
      bSum = 0
      for z in range (x,x+5):
        for k in range (y,y+5):
          (rHolder,gHolder,bHolder) = im1.getpixel((z,k))
          rSum += rHolder
          gSum += gHolder
          bSum += bHolder
      rSum = rSum//25
      gSum = gSum//25
      bSum = bSum//25
      for m in range (x,x+5):
        for n in range (y,y+5):
          im.putpixel((m,n),(rSum,gSum,bSum))
  return im ##returns the modified image

  


blurBear = blur(bear) # name the function

blurBear.save("blurBear.png")   # create/overwrite bear