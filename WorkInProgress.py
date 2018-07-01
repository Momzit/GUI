from __future__ import division, print_function
from visual import *
from visual.graph import *
import wx
import numpy as np

L = 500
Hgraph = 50

def solarSystem(evt):
    for ii in range(1000):
        rate(100)

        rmag = np.sqrt(Earth.x**2 + Earth.y**2 + Earth.z**2)
        rhat = (Sun.pos - Earth.pos)/rmag
        F12 = (10000*rhat)/rmag**2
        Earth.v += F12
        Earth.pos += Earth.v

def Box(evt):
    import visual as vs
    cube = vs.box(color=color.red)

def choose(evt):
    selected = evt.GetSelection()
    if selected == 0: solarSystem(evt)
    else: Box(evt)

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
disp = display(window=w, x=250, y=d, width=800-2*d, height=400-2*d, forward=-vector(0,1,2))
gdisplay(window=w, y=50, width=2*(L+window.dwidth), height=Hgraph)

Sun = sphere(pos=vector(0,0,0), radius=100, color=color.yellow)
Earth = sphere(pos=vector(200,0,0), radius=10, material=materials.earth, make_trail=True)
Earth.v = vector(0,-8,0)

p = w.panel
font = wx.Font(20,  wx.ROMAN, wx.NORMAL, wx.BOLD)
l1 = wx.StaticText(p, pos=(85,50), size=(110,50), label='Velocity',
              style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)
l1.SetFont(font)

start = wx.Button(p, label='Start', pos=(250,430), size=(110,50))
start.Bind(wx.EVT_BUTTON, solarSystem)

pause = wx.Button(p, label='Pause', pos=(580,430), size=(110,50))
# pause.Bind(wx.EVT_BUTTON, solarSystem)

reset = wx.Button(p, label='Reset', pos=(900,430), size=(110,50))
# reset.Bind(wx.EVT_BUTTON, solarSystem)

mainscreen = wx.Button(p, label='Main Screen', pos=(100,300), size=(110,50))
# mainscreen.Bind(wx.EVT_BUTTON, solarSystem)

#
# items = []
# items.append('Earth-sun')
# items.append('Box')
# pulldown_menu = wx.Choice(p, choices=items, pos=(L+250,550))
# pulldown_menu.Bind(wx.EVT_CHOICE, choose)
# pulldown_menu.SetSelection(0)
