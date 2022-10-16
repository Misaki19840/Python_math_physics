import numpy as np
import matplotlib.pyplot as plt

# axis0
eg = np.array([[1, 0], [0, 1]])
g_origin = np.array([0, 0])
eg_x = {'start': g_origin,'end': [g_origin[0] + eg[0][0], g_origin[1] + eg[0][1]]}
eg_y = {'start': g_origin,'end': [g_origin[0] + eg[1][0], g_origin[1] + eg[1][1]]}

# axis1
theta = np.deg2rad(90)
Rot= np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
gl = np.dot(Rot, eg)
l_origin = np.array([5, 5])
el_x = {'start': l_origin,'end': [l_origin[0] + gl[0][0], l_origin[1] + gl[1][0]]}
el_y = {'start': l_origin,'end': [l_origin[0] + gl[0][1], l_origin[1] + gl[1][1]]}

# point_g
point_g = np.array([[-2, 4, 6], [3, 8, 3]])
print("point_g")
print(point_g)

# calc 
T = l_origin - g_origin
M = Rot
# point_l = np.dot(M.T, point_g)[:,0] - np.dot(M.T, T)
point_l_ = np.array( [np.dot(M.T, point_g)[:,0] - np.dot(M.T, T), np.dot(M.T, point_g)[:,1] - np.dot(M.T, T), np.dot(M.T, point_g)[:,2] - np.dot(M.T, T)])
print(point_l_)
print("point_l")
print(point_l_.T)
point_l = point_l_.T

fig_dpi = 100
fig_w_px = 1920
fig_h_px = 1080
fig = plt.figure( dpi=fig_dpi, figsize=(fig_w_px/fig_dpi, fig_h_px/fig_dpi))
ax1 = fig.add_subplot(1, 1, 1)

name1 = ""
# axis0
ax1.plot(*eg_x['start'], 'o', color="black")
ax1.plot(*eg_x['end'], 'o', color="blue")
ax1.annotate('', xy=eg_x['end'], xytext=eg_x['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor='blue', edgecolor='blue'))

ax1.plot(*eg_y['start'], 'o', color="black")
ax1.plot(*eg_y['end'], 'o', color="red")
ax1.annotate('', xy=eg_y['end'], xytext=eg_y['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor='red', edgecolor='red'))

p_show = ( eg_x['start'] + eg_x['end'] ) / 2
ax1.annotate('eg_x', xy=p_show, size=20)
p_show = ( eg_y['start'] + eg_y['end'] ) / 2
ax1.annotate('eg_y', xy=p_show, size=20)

# axis1
ax1.plot(*el_x['start'], 'o', color="black")
ax1.plot(*el_x['end'], 'o', color="blue")
ax1.annotate('', xy=el_x['end'], xytext=el_x['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor='blue', edgecolor='blue'))

ax1.plot(*el_y['start'], 'o', color="black")
ax1.plot(*el_y['end'], 'o', color="red")
ax1.annotate('', xy=el_y['end'], xytext=el_y['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor='red', edgecolor='red'))

p_show = ( el_x['start'] + el_x['end'] ) / 2
ax1.annotate('el_x', xy=p_show, size=20)
p_show = ( el_y['start'] + el_y['end'] ) / 2
ax1.annotate('eg_y', xy=p_show, size=20)

ax1.plot(point_g[0],point_g[1], 'o', color="black")
txt = "point_g (x,y) = ({:.1f}".format(point_g[0][0]) + ", {:.1f})".format(point_g[1][0]) \
+ "\n" + "point_l (x,y) = ({:.1f}".format(point_l[0][0]) + ", {:.1f})".format(point_l[1][0])
ax1.annotate(txt, xy=(point_g[0][0], point_g[1][0]), size=10)

txt = "point_g (x,y) = ({:.1f}".format(point_g[0][1]) + ", {:.1f})".format(point_g[1][1]) \
+ "\n" + "point_l (x,y) = ({:.1f}".format(point_l[0][1]) + ", {:.1f})".format(point_l[1][1])
ax1.annotate(txt, xy=(point_g[0][1], point_g[1][1]), size=10)

txt = "point_g (x,y) = ({:.1f}".format(point_g[0][2]) + ", {:.1f})".format(point_g[1][2]) \
+ "\n" + "point_l (x,y) = ({:.1f}".format(point_l[0][2]) + ", {:.1f})".format(point_l[1][2])
ax1.annotate(txt, xy=(point_g[0][2], point_g[1][2]), size=10)


# ax1.legend()
# ax1.set_xlim([p_obj_x-1, -p_obj_x+1])
ax1.grid(which = "both", color = "gray", linestyle="--")

plt.show()

csvName = "python_transformAxis"
fig.savefig(csvName + ".png")