# coding:utf8
from Q2 import rgb1gray
from Q3 import twodConv
from Q4 import gaussKernel
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

if __name__ == '__main__':
    cameraman_img = rgb1gray(f='cameraman.tif', showflag=False)
    einstein_img = rgb1gray(f='einstein.tif', showflag=False)
    lena_img = rgb1gray(f='lena512color.tiff', showflag=False)
    mandril_img = rgb1gray(f='mandril_color.tif', showflag=False)
    for i in [1, 2, 3, 5]:
        kernel = gaussKernel(i)
        conv_cameraman = twodConv(cameraman_img, kernel, 'replicate')
        conv_einstein = twodConv(einstein_img, kernel, 'replicate')
        conv_lena = twodConv(lena_img, kernel, 'replicate')
        conv_mandril = twodConv(mandril_img, kernel, 'replicate')
        plt.figure()
        plt.imshow(conv_cameraman, 'gray')
        plt.axis('off')
        plt.savefig('figures/cameraman_conv_sig%d.png' % i, dpi=800, bbox_inches='tight')
        plt.title('cameraman conv sigma=%d' % i)
        plt.figure()
        plt.imshow(conv_einstein, 'gray')
        plt.axis('off')
        plt.savefig('figures/einstein_conv_sig%d.png' % i, dpi=800, bbox_inches='tight')
        plt.title('einstein conv sigma=%d' % i)
        plt.figure()
        plt.imshow(conv_lena, 'gray')
        plt.axis('off')
        plt.savefig('figures/lena_conv_sig%d.png' % i, dpi=800, bbox_inches='tight')
        plt.title('lena conv sigma=%d' % i)
        plt.figure()
        plt.imshow(conv_mandril, 'gray')
        plt.axis('off')
        plt.savefig('figures/mandril_conv_sig%d.png' % i, dpi=800, bbox_inches='tight')
        plt.title('mandril conv sigma=%d' % i)
    kernel = gaussKernel(1)
    conv_cameraman = twodConv(cameraman_img, kernel, 'replicate')
    conv_cv = cv.GaussianBlur(cameraman_img, (3, 3), sigmaX=1, sigmaY=1, borderType=cv.BORDER_REPLICATE)
    conv_cv = np.array(conv_cv, dtype=np.int)
    conv_cameraman = np.array(conv_cameraman, dtype=np.int)
    plt.figure()
    plt.imshow(conv_cameraman, 'gray')
    plt.axis('off')
    plt.savefig('figures/MyGauss_sig1_replicate.png', dpi=800, bbox_inches='tight')
    plt.title('My Gauss(sigma=1, replicate)')
    plt.figure()
    plt.imshow(conv_cv, 'gray')
    plt.axis('off')
    plt.savefig('figures/OpenCv_sig1_replicate.png', dpi=800, bbox_inches='tight')
    plt.title('opencv gauss(sigma=1, replicate)')
    diff1 = ((conv_cv - conv_cameraman)).sum()
    print(diff1)
    conv_cameraman = twodConv(cameraman_img, kernel, 'zero')
    conv_cv = cv.GaussianBlur(cameraman_img, (3, 3), sigmaX=1, sigmaY=1, borderType=cv.BORDER_CONSTANT)
    conv_cv = np.array(conv_cv, dtype=np.int)
    conv_cameraman = np.array(conv_cameraman, dtype=np.int)
    plt.figure()
    plt.imshow(conv_cameraman, 'gray')
    plt.axis('off')
    plt.savefig('figures/MyGauss_sig1_zero.png', dpi=800, bbox_inches='tight')
    plt.title('My Gauss(sigma=1, zero)')
    plt.figure()
    plt.imshow(conv_cv, 'gray')
    plt.axis('off')
    plt.savefig('figures/OpenCV_sig1_zero.png', dpi=800, bbox_inches='tight')
    plt.title('opencv gauss(sigma=1, zero)')
    diff2 = ((conv_cv - conv_cameraman)).sum()
    print(diff2)
    plt.show()
