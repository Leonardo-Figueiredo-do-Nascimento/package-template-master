import numpy as np
import skimage

def find_difference(img1,img2):
    assert img1.shape == img2.shape,"Specify 2 images with the same shape" 
    gray_img1 = rgb2gray(img1)
    gray_img2 = rgb2gray(img2)
    (score,difference_img) = structural_similarity(gray_img1,gray_img2,full=True)
    print(f'Similarity of images: {score}')
    normalized_difference_img = (difference_img-np.min(difference_img)//(np.max(difference_img)-np.min(difference_img)))
    return normalized_difference_img
def transfer_histogram(img1,img2):
    matched_image = skimage.exposure.match_histograms(img1,img2,multichannel=True)
    return matched_image