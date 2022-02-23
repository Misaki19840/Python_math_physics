import numpy as np
import matplotlib.pyplot as plt

#df = pd.read_csv(csvName, encoding='shift_jis', usecols= colNames )

R = 1.00
d = -5
M = R / (2.0*d - R)

w_obj = 0.8
p_obj_x = d
p_obj_y = 0

w_mirror = 0.5
p_mirror_x = 0
p_mirror_y = 0

p_obsewrver_x = -0.5
p_obsewrver_y = 0

fig_dpi = 100
fig_w_px = 1920
fig_h_px = 1080
fig = plt.figure( dpi=fig_dpi, figsize=(fig_w_px/fig_dpi, fig_h_px/fig_dpi))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

c1,c2,c3,c4 = "blue","green","red","black"      # 各プロットの色

x_00 = np.array([p_obj_x, p_obj_x])
tmp = p_obj_y + w_obj
y_00 = np.array([p_obj_y, tmp])

x_01 = np.array([M*d, M*d])
tmp = p_obj_y + np.abs(M) * w_obj
y_01 = np.array([p_obj_y, tmp])

x_02 = np.array([p_mirror_x, p_mirror_x])
tmp = p_mirror_y + w_mirror
y_02 = np.array([p_mirror_y, tmp])

x_03 = np.array([p_obsewrver_x])
y_03 = np.array([p_obsewrver_y])

x_04 = np.array([p_obsewrver_x, x_01[0]])
y_04 = np.array([p_obsewrver_y, y_01[0]])

a1 = (y_04[1] - y_04[0]) / (x_04[1] - x_04[0])
b1 = y_04[1] - a1 * x_04[1]
x_041 = p_mirror_x
y_041 = a1 * x_041 + b1

x_05 = np.array([p_obsewrver_x, x_01[1]])
y_05 = np.array([p_obsewrver_y, y_01[1]])

a2 = (y_05[1] - y_05[0]) / (x_05[1] - x_05[0])
b2 = y_05[1] - a2 * x_05[1]
x_051 = p_mirror_x
y_051 = a2 * x_051 + b2

x_06 = np.array([x_041, x_051])
y_06 = np.array([y_041, y_051])

theta_rad = np.arange(0,359,1) * np.pi / 180.0
x_07_tmp = np.cos(theta_rad) + R
y_07_tmp = np.sin(theta_rad)
l_0r = np.sqrt(x_07_tmp * x_07_tmp + y_07_tmp * y_07_tmp)
l_0r_a = (l_0r <= w_mirror) & ( y_07_tmp > 0)
x_07 = x_07_tmp[l_0r_a]
y_07 = y_07_tmp[l_0r_a]

name1 = ""
ax1.plot(x_00, y_00, marker='o', markersize=3, color=c1, label=name1)
ax1.plot(x_01, y_01, marker='o', markersize=3, color=c2, label=name1)
ax1.plot(x_02, y_02, marker='o', markersize=3, color="gray", label=name1)
ax1.plot(x_03, y_03, marker='o', markersize=3, color="black", label=name1)
ax1.plot(x_04, y_04, marker='', markersize=3, linestyle = "dashed", linewidth = 1, color="black", label=name1)
ax1.plot(x_05, y_05, marker='', markersize=3, linestyle = "dashed", linewidth = 1, color="black", label=name1)
ax1.plot(x_06, y_06, marker='o', markersize=3, color="black", label=name1)
#ax1.plot(x_07_tmp, y_07_tmp, marker='o', markersize=1, color="gray", label=name1)
ax1.plot(x_07, y_07, marker='o', markersize=1, color="gray", label=name1)
ax1.legend()
ax1.set_xlim([p_obj_x-1, -p_obj_x+1])
#ax1.set_xticks(np.arange(t_min, t_max+1, step=t_step))
#ax1.set_ylim([x_min, x_max])
#ax1.set_yticks(np.arange(x_min, x_max+1, step=x_step))
#ax1.minorticks_on()
ax1.grid(which = "both", color = "gray", linestyle="--")

ax2_tex_offset = 0.01
w_mirrorImg = np.abs(y_06[0]-y_06[1])
name2 = ""
ax2.plot(-y_02, -x_02, marker='o', markersize=3, color="gray", label=name2)
ax2.plot(-y_06, -x_06, marker='o', markersize=3, color="black", label=name2)
tex = "[ " + '{:.3f}'.format(-y_06[0]) + ", " + '{:.3f}'.format(-x_06[0]) + "]"
ax2.text(-y_06[0], -x_06[0] + ax2_tex_offset, tex, size=10, horizontalalignment="left")
tex = "[ " + '{:.3f}'.format(-y_06[1]) + ", " + '{:.3f}'.format(-x_06[1]) + "]"
ax2.text(-y_06[1], -x_06[1] + ax2_tex_offset * 2, tex, size=10, horizontalalignment="left")
tex = "w_mirrorImg = " + '{:.3f}'.format(w_mirrorImg)
ax2.text(-y_06[0], -x_06[0] + ax2_tex_offset * 3, tex, size=10, horizontalalignment="center")
ax2.legend()
ax2.grid(which = "both", color = "gray", linestyle="--")

x_30 = np.array([p_obj_x, p_obj_x])
tmp = p_obj_y + w_obj
y_30 = np.array([p_obj_y, tmp])

x_31 = np.array([-p_obj_x, -p_obj_x])
y_31 = np.array([p_obj_y, tmp])

x_32 = np.array([p_mirror_x, p_mirror_x])
tmp = p_mirror_y + w_mirror
y_32 = np.array([p_mirror_y, tmp])

x_33 = np.array([p_obsewrver_x])
y_33 = np.array([p_obsewrver_y])

x_34 = np.array([p_obsewrver_x, x_31[0]])
y_34 = np.array([p_obsewrver_y, y_31[0]])

a1 = (y_34[1] - y_34[0]) / (x_34[1] - x_34[0])
b1 = y_34[1] - a1 * x_34[1]
x_341 = p_mirror_x
y_341 = a1 * x_341 + b1

x_35 = np.array([p_obsewrver_x, x_31[1]])
y_35 = np.array([p_obsewrver_y, y_31[1]])

a2 = (y_35[1] - y_35[0]) / (x_35[1] - x_35[0])
b2 = y_35[1] - a2 * x_35[1]
x_351 = p_mirror_x
y_351 = a2 * x_351 + b2

x_36 = np.array([x_341, x_351])
y_36 = np.array([y_341, y_351])

name3 = ""
ax3.plot(x_30, y_30, marker='o', markersize=3, color=c1, label=name3)
ax3.plot(x_31, y_31, marker='o', markersize=3, color=c2, label=name3)
ax3.plot(x_32, y_32, marker='o', markersize=3, color="gray", label=name3)
ax3.plot(x_33, y_33, marker='o', markersize=3, color="black", label=name3)
ax3.plot(x_34, y_34, marker='', markersize=3, linestyle = "dashed", linewidth = 1, color="black", label=name3)
ax3.plot(x_35, y_35, marker='', markersize=3, linestyle = "dashed", linewidth = 1, color="black", label=name3)
ax3.plot(x_36, y_36, marker='o', markersize=3, color="black", label=name3)
ax3.legend
ax3.set_xlim([p_obj_x-1, -p_obj_x+1])
#ax1.set_xticks(np.arange(t_min, t_max+1, step=t_step))
#ax1.set_ylim([x_min, x_max])
#ax1.set_yticks(np.arange(x_min, x_max+1, step=x_step))
#ax1.minorticks_on()
ax3.grid(which = "both", color = "gray", linestyle="--")

ax4_tex_offset = 0.01
w_mirrorImg = np.abs(y_36[0]-y_36[1])
name4 = ""
ax4.plot(-y_32, -x_32, marker='o', markersize=3, color="gray", label=name3)
ax4.plot(-y_36, -x_36, marker='o', markersize=3, color="black", label=name3)
tex = "[ " + '{:.3f}'.format(-y_36[0]) + ", " + '{:.3f}'.format(-x_36[0]) + "]"
ax4.text(-y_36[0], -x_36[0] + ax4_tex_offset, tex, size=10, horizontalalignment="left")
tex = "[ " + '{:.3f}'.format(-y_36[1]) + ", " + '{:.3f}'.format(-x_36[1]) + "]"
ax4.text(-y_36[1], -x_36[1] + ax4_tex_offset * 2, tex, size=10, horizontalalignment="left")
tex = "w_mirrorImg = " + '{:.3f}'.format(w_mirrorImg)
ax4.text(-y_36[0], -x_36[0] + ax4_tex_offset * 3, tex, size=10, horizontalalignment="center")
ax4.legend()
ax4.grid(which = "both", color = "gray", linestyle="--")

plt.show()

csvName = "pythonMirror"
fig.savefig(csvName + ".png")