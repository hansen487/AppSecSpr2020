from PIL import Image
filepath = input("Enter a file path for the picture:")

im = Image.open(filepath)
#print(im.info)
width, height = im.size[0], im.size[1]
if width > height:
    width = im.size[1]
else:
    height = im.size[0]
im_resized = im.resize((width, height))
new_filepath = filepath.split('.')
new_filepath = new_filepath[0] + "square." + new_filepath[1]
print(new_filepath)
im_resized.save(new_filepath)
im.close()
