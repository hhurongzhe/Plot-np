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
phase1S0 = data['1S0']
phase1P1 = data['1P1']
phase3P0 = data['3P0']
phase3P1 = data['3P1']
phase1D2 = data['1D2']
phase3D2 = data['3D2']
phase1F3 = data['1F3']
phase3S1 = data['3S1']
phase3D1 = data['3D1']
phaseE1 = data['E1']
phase3P2 = data['3P2']
phase3F2 = data['3F2']
phaseE2 = data['E2']
phase3D3 = data['3D3']


# * special treatment for 3S1-3D1 channel due to atan problem:
for i in range(0, len(Tlab)):
    if Tlab[i] < 100 and phase3S1[i] < 0:
        phase3S1[i] = 180 + phase3S1[i]
    if phaseE1[i] < 0:
        phaseE1[i] = -phaseE1[i]

# size and dpi.
fig = plt.figure(figsize=(12, 9), dpi=600)
# set spacing between subplots
fig.subplots_adjust(hspace=0.5, wspace=0.3)

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
lwith = 1.3
# marker color, size and alpha:
marker_c = "black"
marker_s = 12
marker_a = 1.0

# ! 1S0
plt.subplot(3, 4, 1)
plt.plot(
    Tlab,
    phase1S0,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['1S0'][0],
    partial_wave_data['1S0'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-60, 120)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-40, 0, 40, 80, 120], ['-40', '0', '40', '80', '120'],
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
    r"$\mathrm{{}^1 S_0}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 3P0
plt.subplot(3, 4, 2)
plt.plot(
    Tlab,
    phase3P0,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3P0'][0],
    partial_wave_data['3P0'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-30, 60)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-20, 0, 20, 40, 60], ['-20', '0', '20', '40', '60'],
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
    r"$\mathrm{{}^3 P_0}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! E1
plt.subplot(3, 4, 3)
plt.plot(
    Tlab,
    phaseE1,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3S1-3D1'][0],
    partial_wave_data['3S1-3D1'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-5, 12.5)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-5, 0, 5, 10], ['-5', '0', '5', '10'],
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
    r"$\mathrm{\epsilon_1}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 1D2
plt.subplot(3, 4, 4)
plt.plot(
    Tlab,
    phase1D2,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['1D2'][0],
    partial_wave_data['1D2'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-2.5, 12.5)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([0, 5, 10], ['0', '5', '10'], fontfamily=font_family,
           fontweight=font_weight, fontsize=font_size)
plt.tick_params(direction='in', width=width_ticks, length=length_ticks)
tk = plt.gca()
tk.spines['bottom'].set_linewidth(width_frame)
tk.spines['top'].set_linewidth(width_frame)
tk.spines['left'].set_linewidth(width_frame)
tk.spines['right'].set_linewidth(width_frame)
plt.text(
    position_x,
    position_y,
    r"$\mathrm{{}^1 D_2}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 1P1
plt.subplot(3, 4, 5)
plt.plot(
    Tlab,
    phase1P1,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['1P1'][0],
    partial_wave_data['1P1'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-35, 10)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-30, -20, -10, 0, 10], ['-30', '-20', '-10', '0', '10'],
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
    r"$\mathrm{{}^1 P_1}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 3P1
plt.subplot(3, 4, 6)
plt.plot(
    Tlab,
    phase3P1,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3P1'][0],
    partial_wave_data['3P1'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-35, 10)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-30, -20, -10, 0, 10], ['-30', '-20', '-10', '0', '10'],
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
    r"$\mathrm{{}^3 P_1}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 3D2
plt.subplot(3, 4, 7)
plt.plot(
    Tlab,
    phase3D2,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3D2'][0],
    partial_wave_data['3D2'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-5, 40)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([0, 10, 20, 30, 40], ['0', '10', '20', '30', '40'],
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
    r"$\mathrm{{}^3 D_2}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 3P2
plt.subplot(3, 4, 8)
plt.plot(
    Tlab,
    phase3P2,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3P2'][0],
    partial_wave_data['3P2'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-5, 30)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([0, 10, 20, 30], ['0', '10', '20', '30'],
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
    r"$\mathrm{{}^3 P_2}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 3S1
plt.subplot(3, 4, 9)
plt.plot(
    Tlab,
    phase3S1,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3S1'][0],
    partial_wave_data['3S1'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-100, 250)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-100, 0, 100, 200], ['-100', '0', '100', '200'],
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
    r"$\mathrm{{}^3 S_1}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 3D1
plt.subplot(3, 4, 10)
plt.plot(
    Tlab,
    phase3D1,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3D1'][0],
    partial_wave_data['3D1'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-40, 10)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-40, -30, -20, -10, 0, 10], ['-40', '-30', '-20', '-10', '0', '10'],
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
    r"$\mathrm{{}^3 D_1}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! E2
plt.subplot(3, 4, 11)
plt.plot(
    Tlab,
    phaseE2,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3P2-3F2'][0],
    partial_wave_data['3P2-3F2'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-5, 1)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-4, -2, 0], ['-4', '-2', '0'], fontfamily=font_family,
           fontweight=font_weight, fontsize=font_size)
plt.tick_params(direction='in', width=width_ticks, length=length_ticks)
tk = plt.gca()
tk.spines['bottom'].set_linewidth(width_frame)
tk.spines['top'].set_linewidth(width_frame)
tk.spines['left'].set_linewidth(width_frame)
tk.spines['right'].set_linewidth(width_frame)
plt.text(
    position_x,
    position_y,
    r"$\mathrm{\epsilon_2}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)
# ! 3D3
plt.subplot(3, 4, 12)
plt.plot(
    Tlab,
    phase3D3,
    color='red',
    linestyle='-',
    linewidth=lwith,
    alpha=1.0,
    zorder=1)
plt.scatter(
    partial_wave_data['3D3'][0],
    partial_wave_data['3D3'][1],
    c=marker_c,
    s=marker_s,
    alpha=marker_a,
    zorder=2)
plt.xlabel('Lab. Energy (MeV)', fontdict=font_my)
plt.ylabel('Phase Shift (deg)', fontdict=font_my)
plt.ylim(-8, 10)  # set y-axis limits
plt.xlim(0, 400)    # set x-axis limits
plt.xticks([0, 100, 200, 300, 400], ['0', '100', '200', '300', '400'],
           fontfamily=font_family, fontweight=font_weight, fontsize=font_size)
plt.yticks([-8, -4, 0, 4, 8], ['-8', '-4', '0', '4', '8'],
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
    r"$\mathrm{{}^3 D_3}$",
    ha='center',
    va='center',
    transform=tk.transAxes,
    fontsize=20)


plt.savefig('phase-SPD.png', bbox_inches='tight', dpi=600)
plt.show()
