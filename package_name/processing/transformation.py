from skimage.transform import resize

def resize_image(img,proportion):
    assert 0 <= proportion <= 1,"Specify a valid proportion between 1 and 0"
    height = round(img.shape[0]*proportion)
    width = round(img.shape[1]*proportion)
    img_resize = resize(img,(height,width),anti_aliasing=True)
    return img_resize