# Import the main modules of expyriment
from expyriment import design, control, stimuli
import math

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "labeled shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create 2, 50 large square
def vertices_triangle(side):
    h = ((3)**0.5 / 2) * side
    return [(0, h/2), (-side/2, -h/2), (side/2, -h/2)]
triangle = stimuli.Shape(vertex_list=vertices_triangle(50), colour=(255, 0, 255)) 

def vertices_hexagon(radius):
    vertices = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append((x, y))
    return vertices

hexagon = stimuli.Shape(vertex_list=vertices_hexagon(25), colour=(0, 255, 255))  
#position
triangle.position = (-100,0)
hexagon.position = (100,0)

# Create vertical lines
ligneT = stimuli.Line(start_point=(0,0), end_point=(0, -50), line_width=3, colour=(255,255,255))
ligneH = stimuli.Line(start_point=(0,0), end_point=(0, -50), line_width=3, colour=(255,255,255))

ligneT.position = triangle.position
ligneH.position = hexagon.position

labelT = stimuli.TextLine(text="triangle", text_colour=(255,255,255), text_size=20)
labelH = stimuli.TextLine(text="hexagon", text_colour=(255,255,255), text_size=20)

labelT.position=triangle.position +[20]
labelH.position=hexagon.position +[20]

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross in the square
triangle.present(clear=False, update=True)
ligneT.present(clear=False, update=True)
labelT.present(clear=False, update=True)
hexagon.present(clear=False, update=True)
ligneH.present(clear=False, update=True)
labelH.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()