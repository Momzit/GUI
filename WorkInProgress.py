from __future__ import division, print_function
from visual import *
from visual.graph import *
import wx
import numpy as np

L = 500
Hgraph = 50

def solarSystem(evt):
    a = Vx.GetValue()
    b = Vy.GetValue()
    c = Vz.GetValue()
    Earth.v = vector(float(a),float(b),float(c))
    for ii in range(1000):
        rate(100)

        rmag = np.sqrt(Earth.x**2 + Earth.y**2 + Earth.z**2)
        rhat = (Sun.pos - Earth.pos)/rmag
        F12 = (10000*rhat)/rmag**2
        Earth.v += F12
        Earth.pos += Earth.v
    print(Earth.v)

def Box(evt):
    a = Vx.GetValue()
    b = Vy.GetValue()
    c = Vz.GetValue()
    print("("+ a + ","+ b + "," + c + ")")

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

p = w.panel
font = wx.Font(20,  wx.ROMAN, wx.NORMAL, wx.BOLD)
l1 = wx.StaticText(p, pos=(105,50), size=(110,50), label='Velocity',
              style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)
l1.SetFont(font)

Vx = wx.TextCtrl(p, pos=(90,100),value='0',
            size=(130,30))
Vx.SetInsertionPoint(len(Vx.GetValue())+1) # position cursor at end of text
Vx.SetFocus() # so that keypresses go to the TextCtrl without clicking it
# Note that disp.canvas.SetFocus() will put disp in keyboard focus.
l2 = wx.StaticText(p, pos=(50,95), label='x')
l2.SetFont(font)

Vy = wx.TextCtrl(p, pos=(90,150),value='-8',
            size=(130,30))
l3 = wx.StaticText(p, pos=(50,145), label='y')
l3.SetFont(font)


Vz = wx.TextCtrl(p, pos=(90,200), value='0',
            size=(130,30))
l4 = wx.StaticText(p, pos=(50,195), label='z')
l4.SetFont(font)


mainscreen = wx.Button(p, label='Main Screen', pos=(250,430), size=(110,50))
#start.Bind(wx.EVT_BUTTON, solarSystem)

pause = wx.Button(p, label='Pause', pos=(580,430), size=(110,50))
pause.Bind(wx.EVT_BUTTON, Box)

reset = wx.Button(p, label='Reset', pos=(900,430), size=(110,50))
# reset.Bind(wx.EVT_BUTTON, solarSystem)

start = wx.Button(p, label='Start', pos=(100,300), size=(110,50))
start.Bind(wx.EVT_BUTTON, solarSystem)

#
# items = []
# items.append('Earth-sun')
# items.append('Box')
# pulldown_menu = wx.Choice(p, choices=items, pos=(L+250,550))
# pulldown_menu.Bind(wx.EVT_CHOICE, choose)
# pulldown_menu.SetSelection(0)
