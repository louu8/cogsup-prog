# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

def kanizsa_rectangle(ratio, rectangle_scale, circle_scale):

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
    exp = design.Experiment(name = "kanizsa square",background_colour=(128,128,128))

# Initialize the experiment: Must be done before presenting any stimulus
    control.initialize(exp)

    width, height = exp.screen.size
    rectangle_width=int(width*rectangle_scale/100)
    rectangle_height=int(rectangle_width/ratio)
    radius=int(width*circle_scale/100)

# Create 4 square, 4 circle
    square = stimuli.Rectangle((rectangle_width,rectangle_height), colour=(128,128,128))
    circle1 = stimuli.Circle(radius=radius, colour=(255,255,255))
    circle2 = stimuli.Circle(radius=radius, colour=(255,255,255))
    circle3 = stimuli.Circle(radius=radius, colour=(0,0,0))
    circle4 = stimuli.Circle(radius=radius, colour=(0,0,0))
#postion
    circle2.position=(-rectangle_width//2,-rectangle_height//2)
    circle3.position=(-rectangle_width//2,rectangle_height//2)
    circle4.position=(rectangle_width//2,rectangle_height//2)
    circle1.position=(rectangle_width//2,-rectangle_height//2)

# Start running the experiment
    control.start(subject_id=1)

# Present the 4 square

    circle2.present(clear=True, update=False)
    circle3.present(clear=False, update=False)
    circle1.present(clear=False, update=False)
    circle4.present(clear=False, update=False)
    square.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
    exp.keyboard.wait()

# End the current session and quit expyriment
    control.end()

kanizsa_rectangle(1,30,10)