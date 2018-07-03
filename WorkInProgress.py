from __future__ import division, print_function
from visual import *
from visual.graph import *
import wx
import numpy as np

running = True
L = 1000
Hgraph = 1000

#==========================================================Functions==========================================================
def pausefunc(evt):
    global running
    running = not running
    if running:
        pause.SetLabel("Pause")
    else:
        pause.SetLabel("Run")

def resetfunc(evt):
    global Earth, Sun

    w.delete_all()
    Sun = sphere(pos=vector(0,0,0), radius=100, color=color.yellow)
    Earth = sphere(pos=vector(200,0,0), radius=10, material=materials.earth, make_trail=True)

def solarSystem(evt):
    a = Vx.GetValue()
    b = Vy.GetValue()
    c = Vz.GetValue()
    Earth.v = vector(float(a),float(b),float(c))
    while True:
        rate(100)

        if running:
            rmag = np.sqrt(Earth.x**2 + Earth.y**2 + Earth.z**2)
            rhat = (Sun.pos - Earth.pos)/rmag
            F12 = (10000*rhat)/rmag**2
            Earth.v += F12
            Earth.pos += Earth.v
            Output.SetValue("The Earth now has this Velocity \n" + str(Earth.v))

#==========================================================Window==========================================================
#This creates a window, takes in different attributes
w = window(width=2*(L+window.dwidth), height=L+window.dheight+window.menuheight+Hgraph,
           menus=True, title='Widgets',
           style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

d = 1
disp = display(window=w, x=250, y=d, width=1500-2*d, height=850-2*d, forward=-vector(0,1,2))
gdisplay(window=w, y=50, width=2*(L+window.dwidth), height=Hgraph)

# #==========================================================Sun and Earth==========================================================
# #The Sun and Earth model
Sun = sphere(pos=vector(0,0,0), radius=100, color=color.yellow)
Earth = sphere(pos=vector(200,0,0), radius=10, material=materials.earth, make_trail=True)

#==========================================================Buttons and Widgets==========================================================
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

# font1 = wx.Font(16,  wx.ROMAN, wx.NORMAL, wx.BOLD)
l5 = wx.StaticText(p, pos=(20,450), label='Velocity Output')
l5.SetFont(font)
Output = wx.TextCtrl(p, pos=(10,500), style=wx.TE_MULTILINE,
            size=(210,100))

mainscreen = wx.Button(p, label='Main Screen', pos=(500,900), size=(110,50))
#start.Bind(wx.EVT_BUTTON, solarSystem)

pause = wx.Button(p, label='Pause', pos=(900,900), size=(110,50))
pause.Bind(wx.EVT_BUTTON, pausefunc)

reset = wx.Button(p, label='Reset', pos=(1300,900), size=(110,50))
reset.Bind(wx.EVT_BUTTON, resetfunc)

start = wx.Button(p, label='Input', pos=(100,300), size=(110,50))
start.Bind(wx.EVT_BUTTON, solarSystem)
