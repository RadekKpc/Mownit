import numpy as np
from scipy import linalg
import imageio
from PIL import Image

def low_rank_approximation(k):
    image = Image.open("lenna.png")
    image = np.array(image)

    r_u,r_s,r_vh = np.linalg.svd(image[:,:,0])
    g_u,g_s,g_vh = np.linalg.svd(image[:,:,1])
    b_u,b_s,b_vh = np.linalg.svd(image[:,:,2])

    r_u = np.matrix(r_u[:,:k])
    g_u = np.matrix(g_u[:,:k])
    b_u = np.matrix(b_u[:,:k])

    r_s = np.diag(r_s[:k])
    g_s = np.diag(g_s[:k])
    b_s = np.diag(b_s[:k])

    r_vh = np.matrix(r_vh[:k,:])
    g_vh = np.matrix(g_vh[:k,:])
    b_vh = np.matrix(b_vh[:k,:])

    matrix_r = r_u * r_s * r_vh
    matrix_g = g_u * g_s * g_vh
    matrix_b = b_u * b_s * b_vh

    new_image = np.zeros((512,512,3), 'uint8')
    new_image[...,0] = matrix_r
    new_image[...,1] = matrix_g
    new_image[...,2] = matrix_b
    out_image = Image.fromarray(new_image)
    out_image.save("lenna_"+str(k)+".png")


low_rank_approximation(1)
low_rank_approximation(2)
low_rank_approximation(4)
low_rank_approximation(8)
low_rank_approximation(16)
low_rank_approximation(32)
low_rank_approximation(64)
low_rank_approximation(128)
low_rank_approximation(256)
low_rank_approximation(512)