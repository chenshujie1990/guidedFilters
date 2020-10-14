import numpy as np
from cv2 import cv2

def meanFilter(img, win):
    '均值滤波'
    kernel = np.ones(win) / np.prod(win)
    return cv2.filter2D(img,-1,kernel)


def imguidedFilter(img_target, img_guide, smoothing=1e-3, win=(3,3)):
    '标准导向滤波函数'
    if img_target.max()>1:
        img_target = img_target / 255
    if img_guide.max()>1:
        img_guide = img_guide / 255
    x = img_target
    g = img_guide
    xm = meanFilter(x, win)
    gm = meanFilter(g, win)
    xn = x - xm
    gn = g - gm
    cov_xg = meanFilter(xn*gn, win)
    var_gg = meanFilter(gn*gn, win)
    a = cov_xg / (var_gg + smoothing)
    b = xm - a*gm
    a = meanFilter(a, win)
    b = meanFilter(b, win)
    fout = a*g + b
    # fout[fout<0] = 0
    # fout[fout>1] = 1
    return (255*fout).astype(np.uint8)


def imnoise(noise_typ, image):
    '图像加噪声'
    if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy.astype(np.uint8)
    elif noise_typ == "s&p":
        row,col,ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 1

      # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        out[coords] = 0
        return out.astype(np.uint8)

    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy.astype(np.uint8)

    elif noise_typ =="speckle":
        row,col,ch = image.shape
        gauss = np.random.randn(row,col,ch)
        gauss = gauss.reshape(row,col,ch)        
        noisy = image + image * gauss
        return noisy.astype(np.uint8)
    else:
        return image