import numpy as np
nums = np.loadtxt("first_chal.txt")
good_elements = [(i,j,k) for i in nums for j in nums for k in nums if i+j+k==2020]
print(good_elements[0][0]*good_elements[0][1]*good_elements[0][2])
