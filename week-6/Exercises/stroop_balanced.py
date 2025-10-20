import itertools
import random
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_BLUE, C_GREEN, C_RED, C_EXPYRIMENT_ORANGE, K_r, K_b, K_o, K_g

# work with Yves Appriou
#have to write input in the terminal to launch the experyment

""" Constants """
KEYS_MAP ={'red':K_r, 'blue':K_b, 'green':K_g, 'orange':K_o}
TRIAL_TYPES = ['match','mismatch']
COLORS = ['red','blue','green','orange']
KEYS=list(KEYS_MAP.values())
COLOR_MAP={'red':C_RED, 'blue':C_BLUE, 'green':C_GREEN, 'orange':C_EXPYRIMENT_ORANGE}

N_BLOCKS = 8
N_TRIAL_TOTAL = 128
N_TRIALS_IN_BLOCK = N_TRIAL_TOTAL//N_BLOCKS

INSTR_START = """
In this task, you have to indicate the color the onscreen word is written in.
Press r if it's red, b if blue, g if green, and o if orange.\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """well done! """
FEEDBACK_INCORRECT = """try again! """

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

def derangements(lst):
    ders=[]
    for perm in itertools.permutations(lst):
        if all(original != perm[idx] for idx, original in enumerate(lst)):
            ders.append(list(perm))
    return ders

PERMS = derangements(COLORS)

""" Global settings """
exp = design.Experiment(name="Stroop_balanced", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)
    correct = (key == KEYS_MAP[color])
    trial_type="match" if word==color else "mismatch"
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

def generate_trials(subject_id):
    order=(subject_id-1)%len(PERMS)
    trials=([{"trial_type":"match","word":c,"color":c}for c in COLORS]+[{"trial_type":"mismatch","word":w,"color":c}for w,c in zip(COLORS,PERMS[order])])
    return trials

subject_id= int(input("Enter subject ID:"))

control.start(subject_id=subject_id)

present_instructions(INSTR_START)
base_trials = generate_trials(subject_id) 
for block_id in range(1, N_BLOCKS + 1):
    block_trials = base_trials * 2
    random.shuffle(block_trials)
    for trial_id, trial in enumerate(block_trials, start=1):
        run_trial(block_id, trial_id, trial["word"], trial["color"])
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
present_instructions(INSTR_END)

control.end()