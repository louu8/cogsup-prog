# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two Squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create 2, 50 large square
squarer = stimuli.Rectangle(size=(50,50),colour=(0,255,0))
squarel = stimuli.Rectangle(size=(50,50),colour=(255,0,0))

# Start running the experiment
control.start(subject_id=1)

#position
squarel.position = (-300,0)

# Present the fixation cross in the square
squarel.present(clear=False, update=False)
squarer.present(clear=False, update=True)

# Leave it on-screen for 1 s
exp.clock.wait(1000)

def launching_function(spatial,tmp1,speed):
    tmp=0 #mesure the amount of time the red square moove
    while squarel.position[0]+25+spatial < squarer.position[0]-25: #until red square reach green square
        squarel.move((4,0))
        squarel.present(clear=True, update=False)
        squarer.present(clear=False, update=True)
        tmp+=1
    exp.clock.wait(tmp1)    
    for i in range(tmp):
        squarer.move((speed,0))
        squarel.present(clear=True, update=False)
        squarer.present(clear=False, update=True)
# Leave it on-screen until a key is pressed
launching_function(5,1000,4)
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()