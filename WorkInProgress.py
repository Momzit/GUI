from __future__ import division, print_function
from visual import *
from visual.graph import *
import wx
import numpy as np

L = 320
Hgraph = 400
# Create a window. Note that w.win is the wxPython "Frame" (the window).
# window.dwidth and window.dheight are the extra width and height of the window
# compared to the display region inside the window. If there is a menu bar,
# there is an additional height taken up, of amount window.menuheight.
# The default style is wx.DEFAULT_FRAME_STYLE; the style specified here
# does not enable resizing, minimizing, or full-sreening of the window.
w = window(width=2*(L+window.dwidth), height=L+window.dheight+window.menuheight+Hgraph,
           menus=True, title='Widgets',
           style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

d = 1
disp = display(window=w, x=d, y=d, width=1000-2*d, height=500-2*d, forward=-vector(0,1,2))
gdisplay(window=w, y=disp.height+50, width=2*(L+window.dwidth), height=Hgraph)

Sun = sphere(pos=vector(0,0,0), radius=100, color=color.yellow)
Earth = sphere(pos=vector(200,0,0), radius=10, material=materials.earth, make_trail=True)
Earth.v = vector(0,-8,0)

for ii in range(1000):
    rate(100)

    rmag = np.sqrt(Earth.x**2 + Earth.y**2 + Earth.z**2)
    rhat = (Sun.pos - Earth.pos)/rmag
    F12 = (10000*rhat)/rmag**2
    Earth.v += F12
    Earth.pos += Earth.v
