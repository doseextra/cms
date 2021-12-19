from PIL import Image

image = Image.open('alternative.png')
image_name = image.filename.split('.')[0]
small_image = image.resize((image.width//8, image.height//8), Image.ANTIALIAS)
small_image.save(image_name + '-' + str(image.width//8) + 'x' + str(image.height//8) + '.png')
small_image.save(image_name + '-' + str(image.width//8) + 'x' + str(image.height//8) + '.webp', "WEBP")



medium_image = image.resize((image.width//4, image.height//4), Image.ANTIALIAS)
medium_image.save(image_name + '-' + str(image.width//4) + 'x' + str(image.height//4) + '.png')
medium_image.save(image_name + '-' + str(image.width//4) + 'x' + str(image.height//4) + '.webp', "WEBP")

large_image = image.resize((image.width//2, image.height//2), Image.ANTIALIAS)
large_image.save(image_name + '-' + str(image.width//2) + 'x' + str(image.height//2) + '.png')
large_image.save(image_name + '-' + str(image.width//2) + 'x' + str(image.height//2) + '.webp', "WEBP")