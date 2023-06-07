import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.ticker import FixedLocator, FixedFormatter

# * format with following command by autopep8:
# autopep8 --in-place --aggressive --aggressive cross_section.py


theory = [4262.96, 2914.6, 2292.55, 1906.07, 1634.52, 1430.5, 1270.51, 1141.24, 1034.42, 944.568, 867.917, 801.747, 744.05, 693.309, 648.35, 608.252, 572.282, 539.407, 510.461, 483.728,
459.313, 436.938, 416.367, 397.397, 379.857, 363.599, 348.492, 334.425, 321.3, 309.031, 297.54, 286.761, 276.633, 267.102, 258.122, 249.649, 241.643, 234.071, 226.901, 220.103, 213.652, 207.524, 201.697, 196.152, 190.87, 185.835, 181.031, 176.444, 172.062, 167.871, 163.861, 160.021, 156.343, 152.816, 149.433, 146.186, 143.068, 140.072, 137.191, 134.42, 131.754, 129.187, 126.714, 124.331, 122.033, 119.817, 117.679, 115.614, 113.621, 111.695, 109.833, 108.034, 106.293, 104.609, 102.979, 101.401, 99.8728, 98.3921, 96.9571, 95.566, 94.2171, 92.9086, 91.639, 90.4068, 89.2105, 88.0488, 86.9203, 85.8239, 84.7584, 83.7225, 82.7154, 81.7358, 80.7829, 79.8556, 78.9531, 78.0746, 77.2192, 76.386, 75.5745, 74.7838, 74.0132, 73.2621, 72.5299, 71.8158, 71.1194, 70.4401, 69.7774, 69.1306, 68.4994, 67.8832, 67.2816, 66.6941, 66.1203, 65.5598, 65.0122, 64.4771, 63.9542, 63.443, 62.9433, 62.4547, 61.9769, 61.5096, 61.0525, 60.6054, 60.1678, 59.7397, 59.3206, 58.9104, 58.5089, 58.1157, 57.7307, 57.3537, 56.9844, 56.6226, 56.2682, 55.9209, 55.5806, 55.2471, 54.9202, 54.5997, 54.2855, 53.9775, 53.6754, 53.3791, 53.0885, 52.8035, 52.5238, 52.2495, 51.9802, 51.716, 51.4567, 51.2021, 50.9522, 50.7069, 50.466, 50.2294, 49.9971, 49.7689, 49.5447, 49.3245, 49.1081, 48.8955, 48.6865, 48.4812, 48.2793, 48.0808, 47.8857, 47.6939, 47.5052, 47.3196, 47.1371, 46.9576, 46.7809, 46.6071, 46.436, 46.2677, 46.1019, 45.9388, 45.7782, 45.62, 45.4642, 45.3108, 45.1596, 45.0107, 44.864, 44.7193, 44.5768, 44.4363, 44.2977, 44.1611, 44.0264, 43.8934, 43.7623, 43.6329, 43.5053, 43.3792, 43.2548, 43.132, 43.0106, 42.8908, 42.7724, 42.6554, 42.5398, 42.4255, 42.3126, 42.2009, 42.0904, 41.981, 41.8729, 41.7659, 41.6599, 41.555, 41.4511, 41.3482, 41.2463, 41.1453, 41.0451, 40.9459, 40.8474, 40.7498, 40.6529, 40.5568, 40.4614, 40.3667, 40.2726, 40.1792, 40.0864, 39.9941, 39.9024, 39.8113, 39.7206, 39.6304, 39.5407, 39.4513, 39.3624, 39.2739, 39.1857, 39.0978, 39.0103, 38.923, 38.836, 38.7492, 38.6627, 38.5763, 38.4901, 38.4041, 38.3182, 38.2324, 38.1467, 38.0611, 37.9755, 37.89, 37.8045, 37.7189, 37.6334, 37.5478, 37.4621, 37.3764, 37.2905, 37.2045, 37.1185, 37.0322, 36.9458, 36.8592, 36.7724, 36.6854, 36.5982, 36.5107, 36.4229, 36.3349, 36.2465, 36.1579, 36.0689, 35.9796, 35.89, 35.8, 35.7096, 35.6188, 35.5276, 35.4359, 35.3439, 35.2514, 35.1584, 35.065, 34.9711, 34.8766, 34.7817, 34.6863, 34.5903, 34.4938, 34.3967, 34.2991, 34.2009, 34.1021, 34.0027, 33.9027, 33.8021, 33.7009, 33.599, 33.4965]

Tlab = []
PWA = []
with open('./data/np_SGT_Nijmegen.csv', 'r') as f:
    next(f)  # skip the first line
    for line in f:
        data = line.split()
        tlab = float(data[0].strip())
        nu = float(data[1].strip())
        Tlab.append(tlab)
        PWA.append(nu)

# size and dpi.
fig = plt.figure(figsize=(6, 6), dpi=600)

# font family, weight and size of x, y labels:
font_family = 'Arial'
font_weight = 600
font_size = 10
font_my = {'family': font_family, 'weight': font_weight, 'size': font_size}
# font dict of LSJ symbols:
font_LSJ = {'family': 'arial', 'size': 16}
# ticks width and length:
width_ticks = 1.0
length_ticks = 5
# frame width:
width_frame = 1.0
# mathfont of LSJ symbols:
config = {"mathtext.fontset": 'stix', 'font.family':'Times New Roman'}
rcParams.update(config)
# relative positions of LSJ symbols:
position_x = 0.5
position_y = 0.9
# line style:
lwith = 1.0
# marker color, size and alpha:
marker_c = "black"
marker_s = 18
marker_a = 1.0


plt.plot(
    Tlab,
    theory,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=2)


plt.scatter(
    Tlab[::7],
    PWA[::7],
    marker='o',
    facecolors='none',
    edgecolors='green',
    s=14,
    alpha=1.0,
    zorder=1)


plt.yscale('log')

plt.xlabel(r"$T_{lab} \;(MeV)$", fontsize=14)
plt.ylabel(r"$\sigma_{total} \;(mb)$", fontsize=14)
plt.xlim(0, 300)    # set x-axis limits
plt.ylim(10, 1000)
plt.xticks([0, 100, 200, 300], ['0', '100', '200', '300'], fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([1e1, 1e2, 1e3, 1e4], [r"$\mathbf{10^1}$", r"$\mathbf{10^2}$", r"$\mathbf{10^3}$", r"$\mathbf{10^4}$"])
plt.tick_params(direction='in', width=width_ticks, length=length_ticks)
tk = plt.gca()
tk.spines['bottom'].set_linewidth(width_frame)
tk.spines['top'].set_linewidth(width_frame)
tk.spines['left'].set_linewidth(width_frame)
tk.spines['right'].set_linewidth(width_frame)


plt.legend(["N3LO","Nijmegen PWA"],
           loc='upper right', fontsize=10, shadow=False, edgecolor='black')

plt.savefig('total_cross_section.png', bbox_inches='tight', dpi=600)
plt.show()
