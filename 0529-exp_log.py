import numpy as np
import cv2 as cv

v1 = np.array([1,2,3], np.float32)
v2 = np.array([4,5,6], np.float32)
v3 = np.array([7,8,9], np.float32)

v_exp = cv.exp(v1)
m_exp = cv.exp(v2)
m_exp = cv.exp(v3)
v_log = cv.log(v1)
m_sqrt = cv.sqrt(v2)
m_pow = cv.pow(v3, 3)