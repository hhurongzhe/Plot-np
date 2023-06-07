import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# * format with following command by autopep8:
# autopep8 --in-place --aggressive --aggressive main.py

# * function that reads the data from file and stores each column in a separate list:


def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # extract column headers and remove newline character
    headers = lines[0].split()
    headers = [header.strip() for header in headers]

    # initialize empty lists for each column
    data = [[] for i in range(len(headers))]

    # extract data from each line and store in corresponding list
    for line in lines[1:]:
        values = line.split()
        for i, value in enumerate(values):
            data[i].append(float(value))

    # create a dictionary with column headers as keys and corresponding data
    # list as values
    data_dict = dict(zip(headers, data))

    return data_dict


# * Load data from file:
partial_wave_data = {}
with open('./data/Nijmegen.csv', 'r') as f:
    next(f)  # skip the first line
    for line in f:
        data = line.strip().split(',')
        Tlab = int(data[0].strip())
        partial_wave = data[1].strip()
        pn = data[2].strip()
        delta = float(data[3].strip())
        error = float(data[4].strip())
        if partial_wave not in partial_wave_data:
            partial_wave_data[partial_wave] = [[], []]
        if Tlab <= 300:
            partial_wave_data[partial_wave][0].append(Tlab)
            partial_wave_data[partial_wave][1].append(delta)


# * calculated phase shift:
data = read_data('./data/NNScattering.trace')
Tlab = data['Tlab']
phase1F3 = data['1F3']
phase3F2 = data['3F2']
phase3F3 = data['3F3']
phase3F4 = data['3F4']


# size and dpi.
fig = plt.figure(figsize=(9, 9), dpi=600)
# set spacing between subplots
fig.subplots_adjust(hspace=0.3, wspace=0.3)

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
config = {"mathtext.fontset": 'stix'}
rcParams.update(config)
# relative positions of LSJ symbols:
position_x = 0.5
position_y = 0.9
# line style:
lwith = 1.7
# marker color, size and alpha:
marker_c = "black"
marker_s = 12
marker_a = 1.0

# ! 1F3
plt.subplot(2, 2, 1)
plt.plot(
    Tlab,
    phase1F3,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['1F3'][0],
    partial_wave_data['1F3'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-6, 0)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-6, -4, -2, 0], ['-6', '-4', '-2', '0'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.tick_params(direction='in', width=width_ticks, length=length_ticks)
tk = plt.gca()
tk.spines['bottom'].set_linewidth(width_frame)
tk.spines['top'].set_linewidth(width_frame)
tk.spines['left'].set_linewidth(width_frame)
tk.spines['right'].set_linewidth(width_frame)
plt.text(
    position_x,
    position_y,
    r"$\mathrm{{}^1 F_3}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)

# ! 3F2
plt.subplot(2, 2, 2)
plt.plot(
    Tlab,
    phase3F2,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3F2'][0],
    partial_wave_data['3F2'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(0, 4)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([0, 2, 4], ['0', '2', '4'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.tick_params(direction='in', width=width_ticks, length=length_ticks)
tk = plt.gca()
tk.spines['bottom'].set_linewidth(width_frame)
tk.spines['top'].set_linewidth(width_frame)
tk.spines['left'].set_linewidth(width_frame)
tk.spines['right'].set_linewidth(width_frame)
plt.text(
    position_x,
    position_y,
    r"$\mathrm{{}^3 F_2}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)

# ! 3F3
plt.subplot(2, 2, 3)
plt.plot(
    Tlab,
    phase3F3,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3F3'][0],
    partial_wave_data['3F3'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-4, 0)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-4, -2, 0], ['-4', '-2', '0'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.tick_params(direction='in', width=width_ticks, length=length_ticks)
tk = plt.gca()
tk.spines['bottom'].set_linewidth(width_frame)
tk.spines['top'].set_linewidth(width_frame)
tk.spines['left'].set_linewidth(width_frame)
tk.spines['right'].set_linewidth(width_frame)
plt.text(
    position_x,
    position_y,
    r"$\mathrm{{}^3 F_3}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)

# ! 3F4
plt.subplot(2, 2, 4)
plt.plot(
    Tlab,
    phase3F4,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3F4'][0],
    partial_wave_data['3F4'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(0, 4)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([0,2,4], ['0', '2', '4'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.tick_params(direction='in', width=width_ticks, length=length_ticks)
tk = plt.gca()
tk.spines['bottom'].set_linewidth(width_frame)
tk.spines['top'].set_linewidth(width_frame)
tk.spines['left'].set_linewidth(width_frame)
tk.spines['right'].set_linewidth(width_frame)
plt.text(
    position_x,
    position_y,
    r"$\mathrm{{}^3 F_4}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)



plt.savefig('phase-F.png', bbox_inches='tight', dpi=600)
plt.show()