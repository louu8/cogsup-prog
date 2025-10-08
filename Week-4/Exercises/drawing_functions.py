from tkinter import Canvas
from expyriment import design, control, stimuli
import random

from networkx import draw

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(exp,stims):
    t0=exp.clock.time
    for stim in stims:
        stim.present(clear=False,update=False)
        exp.screen.update()
    t1=exp.clock.time
    return t1-t0
    # return the time it took to draw

def present_for(exp,stims,t=1000):
    t0=timed_draw(exp,stims)
    exp.clock.wait(t-t0)
    exp.screen.clear()


