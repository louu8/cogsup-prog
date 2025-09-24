# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "kanizsa square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

width, height = exp.screen.size
size=int(width/20)

# Create 4 square
square1 = stimuli.Rectangle((size,size), line_width=1, colour=(255,0,0))
square2 = stimuli.Rectangle((size,size), line_width=1, colour=(255,0,0))
square3 = stimuli.Rectangle((size,size), line_width=1, colour=(255,0,0))
square4 = stimuli.Rectangle((size,size), line_width=1, colour=(255,0,0))

#postion
square1.position=(-width//2+size//2,-height//2+size//2)
square2.position=(-width//2+size//2,height//2-size//2)
square3.position=(width//2-size//2,-height//2+size//2)
square4.position=(width//2-size//2,height//2-size//2)

# Start running the experiment
control.start(subject_id=1)

# Present the 4 square
square1.present(clear=True, update=False)
square2.present(clear=False, update=False)
square3.present(clear=False, update=False)
square4.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()