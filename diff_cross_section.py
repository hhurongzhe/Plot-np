import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# * format with following command by autopep8:
# autopep8 --in-place --aggressive --aggressive cross_section.py

data_theta = [11.0, 15.2, 19.4, 23.6, 27.6, 31.6, 35.5, 39.4, 43.1, 46.8, 50.3]
data_cross = [8.48, 7.66, 7.05, 6.55, 6.10, 5.16, 5.03, 4.70, 4.25, 3.70, 3.68]

theory_theta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180]

theory_cross_J = [9.31859, 9.29674, 9.26066, 9.21084, 9.14794, 9.07277, 8.9863, 8.88956, 8.78368, 8.66984, 8.54922, 8.42299, 8.29228, 8.15815, 8.02159, 7.88349, 7.74463, 7.60567, 7.46716, 7.32954, 7.19316, 7.05823, 6.92491, 6.79329, 6.66337, 6.53513, 6.40851, 6.28343, 6.15979, 6.0375, 5.91649, 5.79668, 5.67803, 5.5605, 5.44409, 5.32881, 5.21471, 5.10182, 4.99022, 4.87999, 4.77122, 4.66398, 4.55838, 4.45451, 4.35244, 4.25227, 4.15407, 4.05789, 3.9638, 3.87185, 3.78208, 3.69453, 3.60922, 3.52618, 3.44545, 3.36703, 3.29097, 3.21729, 3.14602, 3.0772, 3.01086, 2.94706, 2.88583, 2.82724, 2.77134, 2.71818, 2.66782, 2.62031, 2.57572, 2.53408, 2.49545, 2.45985, 2.42732, 2.39787, 2.37153, 2.34828, 2.32813, 2.31108, 2.29708, 2.28614, 2.27822, 2.27328, 2.27132, 2.2723, 2.27619, 2.28299, 2.29269, 2.30527, 2.32074, 2.33912, 2.36042, 2.38466, 2.41187, 2.44209, 2.47535, 2.51167, 2.55109, 2.59363, 2.6393, 2.6881, 2.74003, 2.79506, 2.85316, 2.91426, 2.9783, 3.04517, 3.11478, 3.18699, 3.26167, 3.33867, 3.41783, 3.49898, 3.58195, 3.66657, 3.75269, 3.84014, 3.92877, 4.01846, 4.10908, 4.20053, 4.29272, 4.38559, 4.47908, 4.57316, 4.66779, 4.76296, 4.85866, 4.95488, 5.05161, 5.14886, 5.2466, 5.34481, 5.44348, 5.54257, 5.64205, 5.74188, 5.84202, 5.94246,
6.04317, 6.14419, 6.24555, 6.34735, 6.44973, 6.5529, 6.65716, 6.76285, 6.87044, 6.98048, 7.0936, 7.21054, 7.33209, 7.45913, 7.59257, 7.73335, 7.88236, 8.04049, 8.20847, 8.38695, 8.57634, 8.77683, 8.98834, 9.21046, 9.4424, 9.68301, 9.93075, 10.1837, 10.4395, 10.6954, 10.9486, 11.1957, 11.4335, 11.6583, 11.8668, 12.0554, 12.2212, 12.3611, 12.4727, 12.5539, 12.6032, 12.6198]


PWA_theta = []
PWA = []
with open('./data/np_DSG_143MeV_Nijmegen.csv', 'r') as f:
    next(f)  # skip the first line
    for line in f:
        data = line.split()
        nu = float(data[1].strip().replace('D', 'e'))
        PWA.append(nu)
        the = float(data[0].strip())
        PWA_theta.append(the)


# size and dpi.
fig = plt.figure(figsize=(6, 6), dpi=160)

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
    theory_theta,
    theory_cross_J,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=2)

plt.scatter(
    PWA_theta[::5],
    PWA[::5],
    marker='o',
    facecolors='none',
    edgecolors='green',
    s=14,
    alpha=1.0,
    zorder=1)

# plt.scatter(
#     data_theta,
#     data_cross,
#     marker='o',
#     facecolors='none',
#     edgecolors=marker_c,
#     s=marker_s,
#     alpha=marker_a,
#     zorder=2)

plt.xlabel(r"$\theta_{CM} \;(deg)$", fontsize=14)
plt.ylabel(r"$d\sigma / d\Omega \;(mb/sr)$", fontsize=14)
plt.ylim(0, 15)  # set y-axis limits
plt.xlim(0, 180)    # set x-axis limits
plt.xticks([0, 60, 120, 180], ['0', '60', '120', '180'], fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([0, 5, 10, 15], ['0', '5', '10', '15'], fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.tick_params(direction='in', width=width_ticks, length=length_ticks)
tk = plt.gca()
tk.spines['bottom'].set_linewidth(width_frame)
tk.spines['top'].set_linewidth(width_frame)
tk.spines['left'].set_linewidth(width_frame)
tk.spines['right'].set_linewidth(width_frame)

plt.legend(["N3LO","Nijmegen PWA"],
           loc='upper left', fontsize=10, shadow=False, edgecolor='black')

plt.savefig('diff_cross_section.png', bbox_inches='tight', dpi=600)
plt.show()
