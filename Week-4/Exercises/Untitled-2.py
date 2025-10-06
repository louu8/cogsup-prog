#!/usr/bin/env python
# -*- coding: utf-8 -*-

from expyriment import design, control, stimuli, misc
from expyriment.misc.constants import K_SPACE

### ----------- Global settings -----------
control.set_develop_mode(True)
exp = design.Experiment("Ternus display")
control.initialize(exp)

screen_w, screen_h = exp.screen.size
bg_col = (0, 0, 0)
circle_col = (255, 255, 255)

### ----------- Helper functions -----------

def present_for(stim, nframes):
    """Present stimulus for nframes (16.67ms each)."""
    stim.present()
    exp.clock.wait(int(round(nframes * 1000 / 60.0)))

def make_circles(radius=50, with_tags=False):
    """Return three circle stimuli aligned horizontally."""
    dist = radius * 3
    circles = []
    for i in range(3):
        c = stimuli.Circle(radius, colour=circle_col, position=((i - 1) * dist, 0))
        if with_tags:
            add_tags(c, radius)
        c.preload()
        circles.append(c)
    return circles

def add_tags(circle, radius):
    """Add a small color tag to a circle stimulus surface."""
    tag = stimuli.Circle(int(radius/4), colour=(255,0,0))
    tag_position = (radius//2, -radius//2)
    tag.plot(circle, position=tag_position)

def run_trial(radius=50, isi_frames=0, with_tags=False):
    """Run one Ternus trial with two successive displays."""
    # First frame: left 3 circles
    c1 = make_circles(radius, with_tags)
    canv1 = stimuli.BlankScreen(colour=bg_col)
    for c in c1: c.plot(canv1)

    # Second frame: right-shifted 3 circles
    c2 = make_circles(radius, with_tags)
    shift = radius * 3
    for c in c2: c.move((shift,0))
    canv2 = stimuli.BlankScreen(colour=bg_col)
    for c in c2: c.plot(canv2)

    # Loop until SPACE is pressed
    while True:
        present_for(canv1, 6)   # 100 ms approx
        if isi_frames > 0:
            exp.clock.wait(int(round(isi_frames * 1000 / 60.0)))
        present_for(canv2, 6)
        if exp.keyboard.check(K_SPACE):
            break

### ----------- Run the experiment -----------

control.start(skip_ready_screen=True)

stimuli.TextLine("Element motion (low ISI, no tags)\nPress SPACE to stop").present()
exp.clock.wait(1500)
run_trial(radius=50, isi_frames=1, with_tags=False)

stimuli.TextLine("Group motion (high ISI, no tags)\nPress SPACE to stop").present()
exp.clock.wait(1500)
run_trial(radius=50, isi_frames=12, with_tags=False)

stimuli.TextLine("Element motion (high ISI, with tags)\nPress SPACE to stop").present()
exp.clock.wait(1500)
run_trial(radius=50, isi_frames=12, with_tags=True)

control.end()
