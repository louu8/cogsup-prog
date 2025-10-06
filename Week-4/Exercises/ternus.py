from tkinter import Canvas
from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE

#doesn't work

exp = design.Experiment(name="ternus")

def add_tags(circle,radius):
    pos=(radius//2, -radius//2)
    tag = stimuli.Circle(int(radius/4), colour=(255,0,0))
    tag.plot(circle,pos)

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

def present_for(stims,frame):
    stims.present()
    exp.clock.wait(int(round(frame * 1000 / 60.0)))
    exp.screen.clear()

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
        present_for(canv1, 100)   # 100 ms approx
        if isi > 0:
            exp.clock.wait(int(round(isi * 1000 / 60.0)))
        present_for(canv2, 100)
        if exp.keyboard.check(K_SPACE):
            break


""" Test functions """

control.set_develop_mode()
control.initialize(exp)



run_trial(50, 6, True)

control.end()