# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

def hermann_grid(square_size, gap, rows,col,colour,background_colour):

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
    exp = design.Experiment(name = "hermann grid",background_colour=background_colour)

# Initialize the experiment: Must be done before presenting any stimulus
    control.initialize(exp)

    
    grid_width = col * square_size + (col) * gap
    grid_height = rows * square_size + (rows) * gap
    squares=[]
    
    for r in range(rows):
        for c in range(col):
            x=-grid_width//2+square_size//2+c*(square_size+gap)
            y=grid_height//2-square_size//2+r*(square_size+gap)
            square = stimuli.Rectangle((square_size,square_size), colour=colour, position = (x,y))
            squares.append(square)
    
   


# Start running the experiment
    control.start(subject_id=1)

# Present the 4 square
    squares[0].present(clear=True, update=False)
    for i in squares:
        i.present(clear=False, update=False)
    squares[-1].present(clear=False, update=True)
    

# Leave it on-screen until a key is pressed
    exp.keyboard.wait()

# End the current session and quit expyriment
    control.end()

hermann_grid(10,5,10,10,(255,255,255),(0,0,0))