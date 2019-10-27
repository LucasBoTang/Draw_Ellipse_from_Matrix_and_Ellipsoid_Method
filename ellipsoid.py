import numpy as np
from matplotlib.patches import Ellipse
from matplotlib import pyplot as plt

def ellipse(center, cov):
    vals, vecs = np.linalg.eig(cov)
    ang = np.degrees(np.arctan2(*vecs[:,0]))
    w, h = 2 * np.sqrt(vals)
    ellipse = Ellipse(center, width=w, height=h, angle=ang, color='c')
    ellipse.set_facecolor('none')
    return ellipse

plt.figure(figsize=(9,9))
plt.xlim(-3, 3)
plt.ylim(-3, 3)
ax = plt.subplot(111)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# polygon
p = [[0,0], [0, 1], [1,1], [1,0]]
patch = poly = plt.Polygon(p)
ax.add_patch(patch)

n = 2
c = np.ones((2, 1))
x0 = np.zeros((2, 1))
B0 = 2 * np.identity(2)
ax.add_artist(ellipse(x0, B0))

x1 = x0 + 1 / (n + 1) * (B0 @ c) / np.sqrt(c.T @ B0 @ c)
B1 = n ** 2 / (n ** 2 - 1) * (B0 - 2 / (n + 1) * (B0 @ c @ c.T @ B0) / (c.T @ B0 @ c))
ax.add_artist(ellipse(x1, B1))

x2 = x1 + 1 / (n + 1) * (B1 @ c) / np.sqrt(c.T @ B1 @ c)
B2 = n ** 2 / (n ** 2 - 1) * (B1 - 2 / (n + 1) * (B1 @ c @ c.T @ B1) / (c.T @ B1 @ c))
ax.add_artist(ellipse(x2, B2))

plt.show()
