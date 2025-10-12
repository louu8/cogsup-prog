from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN,K_UP,K_LEFT,K_RIGHT,K_SPACE,K_2,K_1


""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode(False)
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(side):

    if side == "L":
        fixation_pos=[300,0]
        circle_pos=[-200,0]
        eye_instru = "cover your left eye"
    else:
        fixation_pos=[-300,0]
        circle_pos=[200,0]
        eye_instru = "cover your right eye"
    
    text_instru = f""" {eye_instru}
    Keep your open eye on the fixation cross.
    Use the arrow keys to move the circle and use the number key 1 to make the circle smaller or 2 to make it bigger.
    Adjust the circle until it disappears from your view.
    When you're finish press space. """

    instru= stimuli.TextScreen("Instructions",text_instru)
    instru.present()
    exp.keyboard.wait(keys=[K_SPACE])

    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)
    exp.screen.clear()
    fixation.present(True, False)
    circle.present(False, True)
    while True:
        key,_=exp.keyboard.wait(keys=[K_DOWN,K_UP,K_LEFT,K_RIGHT,K_1,K_2,K_SPACE])
        if key==K_DOWN:
            circle.move((0,-5))
        if key==K_UP:
            circle.move((0,5))
        if key== K_RIGHT:
            circle.move((5,0))
        if key==K_LEFT:
            circle.move((-5,0))
        if key==K_1:
            radius -= 3
            circle=make_circle(radius,pos=circle.position)
        if key==K_2:
            radius += 3
            circle=make_circle(radius,pos=circle.position)

        x,y=circle.position
        exp.data.add([side,key,radius,x,y])

        if key==K_SPACE:
            break
        
        exp.screen.clear()
        fixation.present(True, False)
        circle.present(False, True)



control.start(subject_id=1)

run_trial("L")
    
control.end()