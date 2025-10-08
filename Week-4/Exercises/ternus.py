from tkinter import Canvas
from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE
from drawing_functions import *

#collaboration with Yves Appriou

exp = design.Experiment(name="ternus")

control.set_develop_mode()
control.initialize(exp)

def add_tags(circle,radius):
    pos=(0,0)
    #pos=(radius//2, -radius//2)
    tag = stimuli.Circle(int(radius/3), colour=(255,0,0),position=pos)
    tag.plot(circle)

def make_circles(radius,tags):
    dist = radius * 3 
    circles = []
    for i in range(2):
        circle = stimuli.Circle(radius, colour=(255,255,255), position=((i - 1) * dist, 0))
        if tags:
            add_tags(circle, radius)
        circle.preload()
        circles.append(circle)
    return circles

def run_trial(radius, isi, tags):
    # First frame: left 3 circles
    circle1 = make_circles(radius, tags)
    canv1 = stimuli.BlankScreen(colour=(0,0,0))
    for c in circle1: 
        c.plot(canv1)

    # Second frame: right-shifted 3 circles
    circle2 = make_circles(radius, tags)
    shift = radius * 3
    for c in circle2: 
        c.move((shift,0))
    canv2 = stimuli.BlankScreen(colour=(0,0,0))
    for c in circle2: 
        c.plot(canv2)

    # Loop until SPACE is pressed
    while True:
        if isi > 0:
            exp.screen.update()
            exp.clock.wait(int(isi * 1000/60))
        present_for(exp,canv1, 200)   # 200 ms approx
        if isi > 0:
            exp.screen.update()
            exp.clock.wait(int(isi * 1000/60))
        present_for(exp,canv2, 200)
        
        if exp.keyboard.check(K_SPACE):
            break


""" Test functions """

run_trial(50, 0, True)


control.end()