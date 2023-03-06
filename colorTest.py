from PIL import Image
picture = Image.open("on-accent.png")
picture = picture.convert("RGB")

# Get the size of the image
d = picture.getdata()

new_image = []
# 0, 127, 255

for item in d:
    if item[0] in list(range(0, 127, 255)):
        new_image.append((50, 168, 82))
    else:
        new_image.append(item)
        
# update image data
picture.putdata(new_image)
 
# save new image
picture.save("flower_image_altered.jpg")
# Process every pixel
# for x in width:
#    for y in height:
#        current_color = picture.getpixel( (x,y) )
#        ####################################################################
#        # Do your logic here and create a new (R,G,B) tuple called new_color
#        ####################################################################
#        new_color = (50, 168, 82)
       
#        picture.putpixel( (x,y), new_color)