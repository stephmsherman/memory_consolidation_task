#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), Tue Jan 19 21:29:12 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, microphone
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'memory_consolidation_night'  # from the Builder filename that created this script
expInfo = {u'list': u'', u'session': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(size=(1920, 1200), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "study_instructions"
study_instructionsClock = core.Clock()
l = expInfo['list']
p = expInfo['participant']

pr = 'practice_list'+l+'.csv'
primy = 'primacy_list'+l+'.csv'
recy = 'recency_list'+l+'.csv'
study = 'study_list'+l+'sub'+p+'.csv'
study_recall = 'study_recall_list'+l+'sub'+p+'.csv'
night_recall = 'night_recall_list'+l+'sub'+p+'.csv'
beg_instruct = visual.TextStim(win=win, ori=0, name='beg_instruct',
    text="In this task, you will see two words on the screen. Please try to remember the words together. Later, we will give you one of the words in the pair and asks you to recall the other. \n\nLet's practice!",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "practice_study"
practice_studyClock = core.Clock()
practice_text1 = visual.TextStim(win=win, ori=0, name='practice_text1',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
practice_text2 = visual.TextStim(win=win, ori=0, name='practice_text2',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test_instructions_2"
test_instructions_2Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Practice Test: Please verbally recall the other word in the pair. It is important that you say the word before you hear the beep. \n\nOnce you hear the beep, the correct word will appear on the screen',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "practice_test"
practice_testClock = core.Clock()
prac_test = visual.TextStim(win=win, ori=0, name='prac_test',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_3 = sound.Sound('A', secs=-1)
sound_3.setVolume(1)
second_prac_test = visual.TextStim(win=win, ori=0, name='second_prac_test',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "before_actual_task_instr"
before_actual_task_instrClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Great Job! Questions?\n\nNow we are ready to start the task. Please try to remember the words together. \n\nThis memory task includes:\n\nStudy: presented about 50 word pairs\nTest 1: recall other word, correct answer will appear after beep \nTest 2: recall other word, will NOT see correct answer \nTest 3: In the morning, repeat the test\n\nBetween tests you will do math problems for 1 minute\n\nReady? Press the space bar to begin the task.',    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "primacy_trials"
primacy_trialsClock = core.Clock()
primacy = visual.TextStim(win=win, ori=0, name='primacy',
    text='default text',    font='Arial',
    pos=[0,.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
primacy2 = visual.TextStim(win=win, ori=0, name='primacy2',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
words = visual.TextStim(win=win, ori=0, name='words',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
words_second = visual.TextStim(win=win, ori=0, name='words_second',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "recency_trials"
recency_trialsClock = core.Clock()
rec = visual.TextStim(win=win, ori=0, name='rec',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
rec2 = visual.TextStim(win=win, ori=0, name='rec2',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "math_problems"
math_problemsClock = core.Clock()
math1 = visual.TextStim(win=win, ori=0, name='math1',
    text='Please complete as many math problems as you can until you hear the beep',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_1 = sound.Sound('B', secs=-1)
sound_1.setVolume(1)
done_math = visual.TextStim(win=win, ori=0, name='done_math',
    text='Please stop completing math problems',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test_instructions"
test_instructionsClock = core.Clock()
test_instruc = visual.TextStim(win=win, ori=0, name='test_instruc',
    text='Please verbally recall the other word in the pair. It is important that you say the word before you hear the beep. \n\nOnce you hear the beep, the correct word will appear on the screen',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "primacy_test"
primacy_testClock = core.Clock()
primTest_trials = visual.TextStim(win=win, ori=0, name='primTest_trials',
    text='default text',    font='Arial',
    pos=[0,.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_4 = sound.Sound('B', secs=-1)
sound_4.setVolume(1)
primTest_answer = visual.TextStim(win=win, ori=0, name='primTest_answer',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "test_trials"
test_trialsClock = core.Clock()
testTrials = visual.TextStim(win=win, ori=0, name='testTrials',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_2 = sound.Sound('B', secs=-1)
sound_2.setVolume(1)
second_word = visual.TextStim(win=win, ori=0, name='second_word',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "recencyTest"
recencyTestClock = core.Clock()
rec_test = visual.TextStim(win=win, ori=0, name='rec_test',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_5 = sound.Sound('B', secs=-1)
sound_5.setVolume(1)
rec_test2 = visual.TextStim(win=win, ori=0, name='rec_test2',
    text='default text',    font='Arial',
    pos=[0,-.1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "math_problems"
math_problemsClock = core.Clock()
math1 = visual.TextStim(win=win, ori=0, name='math1',
    text='Please complete as many math problems as you can until you hear the beep',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_1 = sound.Sound('B', secs=-1)
sound_1.setVolume(1)
done_math = visual.TextStim(win=win, ori=0, name='done_math',
    text='Please stop completing math problems',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "final_test_instruc"
final_test_instrucClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='Please verbally recall the other word in the pair. It is important that you say the word before you hear the beep. \n\nThis time, you will NOT see the correct answer.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_15 = visual.TextStim(win=win, ori=0, name='text_15',
    text='Ready? Press the space bar to begin the task.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "final_night_test_2"
final_night_test_2Clock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_6 = sound.Sound('B', secs=-1)
sound_6.setVolume(1)
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "complete"
completeClock = core.Clock()
text_14 = visual.TextStim(win=win, ori=0, name='text_14',
    text='Task complete!\n\nThank you',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "study_instructions"-------
t = 0
study_instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
study_instructionsComponents = []
study_instructionsComponents.append(beg_instruct)
study_instructionsComponents.append(key_resp_2)
for thisComponent in study_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "study_instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = study_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *beg_instruct* updates
    if t >= 0.0 and beg_instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        beg_instruct.tStart = t  # underestimates by a little under one frame
        beg_instruct.frameNStart = frameN  # exact frame index
        beg_instruct.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in study_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "study_instructions"-------
for thisComponent in study_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(pr),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5.keys():
        exec(paramName + '= thisTrial_5.' + paramName)

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5.keys():
            exec(paramName + '= thisTrial_5.' + paramName)
    
    #------Prepare to start Routine "practice_study"-------
    t = 0
    practice_studyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    practice_text1.setText(prac1)
    practice_text2.setText(prac2)
    # keep track of which components have finished
    practice_studyComponents = []
    practice_studyComponents.append(practice_text1)
    practice_studyComponents.append(practice_text2)
    practice_studyComponents.append(text_5)
    for thisComponent in practice_studyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practice_study"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_studyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_text1* updates
        if t >= 0.0 and practice_text1.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_text1.tStart = t  # underestimates by a little under one frame
            practice_text1.frameNStart = frameN  # exact frame index
            practice_text1.setAutoDraw(True)
        if practice_text1.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_text1.setAutoDraw(False)
        
        # *practice_text2* updates
        if t >= 0.0 and practice_text2.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_text2.tStart = t  # underestimates by a little under one frame
            practice_text2.frameNStart = frameN  # exact frame index
            practice_text2.setAutoDraw(True)
        if practice_text2.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_text2.setAutoDraw(False)
        
        # *text_5* updates
        if t >= 4 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # underestimates by a little under one frame
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        if text_5.status == STARTED and t >= (4 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_studyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "practice_study"-------
    for thisComponent in practice_studyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_5'


#------Prepare to start Routine "test_instructions_2"-------
t = 0
test_instructions_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
test_instructions_2Components = []
test_instructions_2Components.append(text)
test_instructions_2Components.append(key_resp_4)
for thisComponent in test_instructions_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "test_instructions_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = test_instructions_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "test_instructions_2"-------
for thisComponent in test_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(pr),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6.keys():
        exec(paramName + '= thisTrial_6.' + paramName)

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6.keys():
            exec(paramName + '= thisTrial_6.' + paramName)
    
    #------Prepare to start Routine "practice_test"-------
    t = 0
    practice_testClock.reset()  # clock 
    frameN = -1
    routineTimer.add(8.500000)
    # update component parameters for each repeat
    prac_test.setText(prac1)
    second_prac_test.setText(prac2)
    practice_mic = microphone.AdvAudioCapture(name='practice_mic', saveDir=wavDirName, stereo=False)
    # keep track of which components have finished
    practice_testComponents = []
    practice_testComponents.append(prac_test)
    practice_testComponents.append(sound_3)
    practice_testComponents.append(second_prac_test)
    practice_testComponents.append(practice_mic)
    practice_testComponents.append(text_6)
    for thisComponent in practice_testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practice_test"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_test* updates
        if t >= 0.0 and prac_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_test.tStart = t  # underestimates by a little under one frame
            prac_test.frameNStart = frameN  # exact frame index
            prac_test.setAutoDraw(True)
        if prac_test.status == STARTED and t >= (0.0 + (8-win.monitorFramePeriod*0.75)): #most of one frame period left
            prac_test.setAutoDraw(False)
        # start/stop sound_3
        if t >= 3.5 and sound_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_3.tStart = t  # underestimates by a little under one frame
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.play()  # start the sound (it finishes automatically)
        if sound_3.status == STARTED and t >= (3.5 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_3.stop()  # stop the sound (if longer than duration)
        
        # *second_prac_test* updates
        if t >= 4 and second_prac_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            second_prac_test.tStart = t  # underestimates by a little under one frame
            second_prac_test.frameNStart = frameN  # exact frame index
            second_prac_test.setAutoDraw(True)
        if second_prac_test.status == STARTED and t >= (4 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            second_prac_test.setAutoDraw(False)
        
        # *practice_mic* updates
        if t >= 0.0 and practice_mic.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_mic.tStart = t  # underestimates by a little under one frame
            practice_mic.frameNStart = frameN  # exact frame index
            practice_mic.status = STARTED
            practice_mic.record(sec=4, block=False)  # start the recording thread
        
        if practice_mic.status == STARTED and not practice_mic.recorder.running:
            practice_mic.status = FINISHED
        
        # *text_6* updates
        if t >= 8 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # underestimates by a little under one frame
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        if text_6.status == STARTED and t >= (8 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_6.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "practice_test"-------
    for thisComponent in practice_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_3.stop() #ensure sound has stopped at end of routine
    # practice_mic stop & responses
    practice_mic.stop()  # sometimes helpful
    if not practice_mic.savedFile:
        practice_mic.savedFile = None
    # store data for trials_6 (TrialHandler)
    trials_6.addData('practice_mic.filename', practice_mic.savedFile)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_6'


#------Prepare to start Routine "before_actual_task_instr"-------
t = 0
before_actual_task_instrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
before_actual_task_instrComponents = []
before_actual_task_instrComponents.append(text_2)
before_actual_task_instrComponents.append(key_resp_5)
for thisComponent in before_actual_task_instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "before_actual_task_instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = before_actual_task_instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in before_actual_task_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "before_actual_task_instr"-------
for thisComponent in before_actual_task_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
prim = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(primy),
    seed=None, name='prim')
thisExp.addLoop(prim)  # add the loop to the experiment
thisPrim = prim.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPrim.rgb)
if thisPrim != None:
    for paramName in thisPrim.keys():
        exec(paramName + '= thisPrim.' + paramName)

for thisPrim in prim:
    currentLoop = prim
    # abbreviate parameter names if possible (e.g. rgb = thisPrim.rgb)
    if thisPrim != None:
        for paramName in thisPrim.keys():
            exec(paramName + '= thisPrim.' + paramName)
    
    #------Prepare to start Routine "primacy_trials"-------
    t = 0
    primacy_trialsClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    primacy.setText(word1)
    primacy2.setText(word2)
    # keep track of which components have finished
    primacy_trialsComponents = []
    primacy_trialsComponents.append(primacy)
    primacy_trialsComponents.append(primacy2)
    primacy_trialsComponents.append(text_7)
    for thisComponent in primacy_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "primacy_trials"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = primacy_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *primacy* updates
        if t >= 0.0 and primacy.status == NOT_STARTED:
            # keep track of start time/frame for later
            primacy.tStart = t  # underestimates by a little under one frame
            primacy.frameNStart = frameN  # exact frame index
            primacy.setAutoDraw(True)
        if primacy.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            primacy.setAutoDraw(False)
        
        # *primacy2* updates
        if t >= 0.0 and primacy2.status == NOT_STARTED:
            # keep track of start time/frame for later
            primacy2.tStart = t  # underestimates by a little under one frame
            primacy2.frameNStart = frameN  # exact frame index
            primacy2.setAutoDraw(True)
        if primacy2.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            primacy2.setAutoDraw(False)
        
        # *text_7* updates
        if t >= 4 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t  # underestimates by a little under one frame
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        if text_7.status == STARTED and t >= (4 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_7.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in primacy_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "primacy_trials"-------
    for thisComponent in primacy_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'prim'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(study),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    words.setText(word1)
    words_second.setText(word2)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(words)
    trialComponents.append(words_second)
    trialComponents.append(text_8)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *words* updates
        if t >= 0.0 and words.status == NOT_STARTED:
            # keep track of start time/frame for later
            words.tStart = t  # underestimates by a little under one frame
            words.frameNStart = frameN  # exact frame index
            words.setAutoDraw(True)
        if words.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            words.setAutoDraw(False)
        
        # *words_second* updates
        if t >= 0.0 and words_second.status == NOT_STARTED:
            # keep track of start time/frame for later
            words_second.tStart = t  # underestimates by a little under one frame
            words_second.frameNStart = frameN  # exact frame index
            words_second.setAutoDraw(True)
        if words_second.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            words_second.setAutoDraw(False)
        
        # *text_8* updates
        if t >= 4 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        if text_8.status == STARTED and t >= (4 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_8.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(recy),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "recency_trials"-------
    t = 0
    recency_trialsClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    rec.setText(word1)
    rec2.setText(word2)
    # keep track of which components have finished
    recency_trialsComponents = []
    recency_trialsComponents.append(rec)
    recency_trialsComponents.append(rec2)
    recency_trialsComponents.append(text_9)
    for thisComponent in recency_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "recency_trials"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = recency_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec* updates
        if t >= 0.0 and rec.status == NOT_STARTED:
            # keep track of start time/frame for later
            rec.tStart = t  # underestimates by a little under one frame
            rec.frameNStart = frameN  # exact frame index
            rec.setAutoDraw(True)
        if rec.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            rec.setAutoDraw(False)
        
        # *rec2* updates
        if t >= 0.0 and rec2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rec2.tStart = t  # underestimates by a little under one frame
            rec2.frameNStart = frameN  # exact frame index
            rec2.setAutoDraw(True)
        if rec2.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            rec2.setAutoDraw(False)
        
        # *text_9* updates
        if t >= 4 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t  # underestimates by a little under one frame
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        if text_9.status == STARTED and t >= (4 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_9.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recency_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "recency_trials"-------
    for thisComponent in recency_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


#------Prepare to start Routine "math_problems"-------
t = 0
math_problemsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
math_problemsComponents = []
math_problemsComponents.append(math1)
math_problemsComponents.append(sound_1)
math_problemsComponents.append(done_math)
math_problemsComponents.append(key_resp_6)
for thisComponent in math_problemsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "math_problems"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = math_problemsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *math1* updates
    if t >= 0.0 and math1.status == NOT_STARTED:
        # keep track of start time/frame for later
        math1.tStart = t  # underestimates by a little under one frame
        math1.frameNStart = frameN  # exact frame index
        math1.setAutoDraw(True)
    if math1.status == STARTED and t >= (0.0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
        math1.setAutoDraw(False)
    # start/stop sound_1
    if t >= 60 and sound_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_1.tStart = t  # underestimates by a little under one frame
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.play()  # start the sound (it finishes automatically)
    if sound_1.status == STARTED and t >= (60 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_1.stop()  # stop the sound (if longer than duration)
    
    # *done_math* updates
    if t >= 60 and done_math.status == NOT_STARTED:
        # keep track of start time/frame for later
        done_math.tStart = t  # underestimates by a little under one frame
        done_math.frameNStart = frameN  # exact frame index
        done_math.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 60 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        key_resp_6.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in math_problemsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "math_problems"-------
for thisComponent in math_problemsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_1.stop() #ensure sound has stopped at end of routine
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()

#------Prepare to start Routine "test_instructions"-------
t = 0
test_instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
test_instructionsComponents = []
test_instructionsComponents.append(test_instruc)
test_instructionsComponents.append(key_resp_3)
for thisComponent in test_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "test_instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = test_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test_instruc* updates
    if t >= 0.0 and test_instruc.status == NOT_STARTED:
        # keep track of start time/frame for later
        test_instruc.tStart = t  # underestimates by a little under one frame
        test_instruc.frameNStart = frameN  # exact frame index
        test_instruc.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "test_instructions"-------
for thisComponent in test_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(primy),
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7.keys():
        exec(paramName + '= thisTrial_7.' + paramName)

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7.keys():
            exec(paramName + '= thisTrial_7.' + paramName)
    
    #------Prepare to start Routine "primacy_test"-------
    t = 0
    primacy_testClock.reset()  # clock 
    frameN = -1
    routineTimer.add(8.500000)
    # update component parameters for each repeat
    primTest_trials.setText(word1)
    primTest_answer.setText(word2)
    primacy_mic = microphone.AdvAudioCapture(name='primacy_mic', saveDir=wavDirName, stereo=False)
    # keep track of which components have finished
    primacy_testComponents = []
    primacy_testComponents.append(primTest_trials)
    primacy_testComponents.append(sound_4)
    primacy_testComponents.append(primTest_answer)
    primacy_testComponents.append(primacy_mic)
    primacy_testComponents.append(text_10)
    for thisComponent in primacy_testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "primacy_test"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = primacy_testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *primTest_trials* updates
        if t >= 0.0 and primTest_trials.status == NOT_STARTED:
            # keep track of start time/frame for later
            primTest_trials.tStart = t  # underestimates by a little under one frame
            primTest_trials.frameNStart = frameN  # exact frame index
            primTest_trials.setAutoDraw(True)
        if primTest_trials.status == STARTED and t >= (0.0 + (8-win.monitorFramePeriod*0.75)): #most of one frame period left
            primTest_trials.setAutoDraw(False)
        # start/stop sound_4
        if t >= 3.5 and sound_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_4.tStart = t  # underestimates by a little under one frame
            sound_4.frameNStart = frameN  # exact frame index
            sound_4.play()  # start the sound (it finishes automatically)
        if sound_4.status == STARTED and t >= (3.5 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_4.stop()  # stop the sound (if longer than duration)
        
        # *primTest_answer* updates
        if t >= 4 and primTest_answer.status == NOT_STARTED:
            # keep track of start time/frame for later
            primTest_answer.tStart = t  # underestimates by a little under one frame
            primTest_answer.frameNStart = frameN  # exact frame index
            primTest_answer.setAutoDraw(True)
        if primTest_answer.status == STARTED and t >= (4 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            primTest_answer.setAutoDraw(False)
        
        # *primacy_mic* updates
        if t >= 0.0 and primacy_mic.status == NOT_STARTED:
            # keep track of start time/frame for later
            primacy_mic.tStart = t  # underestimates by a little under one frame
            primacy_mic.frameNStart = frameN  # exact frame index
            primacy_mic.status = STARTED
            primacy_mic.record(sec=4, block=False)  # start the recording thread
        
        if primacy_mic.status == STARTED and not primacy_mic.recorder.running:
            primacy_mic.status = FINISHED
        
        # *text_10* updates
        if t >= 8 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        if text_10.status == STARTED and t >= (8 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_10.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in primacy_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "primacy_test"-------
    for thisComponent in primacy_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_4.stop() #ensure sound has stopped at end of routine
    # primacy_mic stop & responses
    primacy_mic.stop()  # sometimes helpful
    if not primacy_mic.savedFile:
        primacy_mic.savedFile = None
    # store data for trials_7 (TrialHandler)
    trials_7.addData('primacy_mic.filename', primacy_mic.savedFile)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_7'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(study_recall),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "test_trials"-------
    t = 0
    test_trialsClock.reset()  # clock 
    frameN = -1
    routineTimer.add(8.500000)
    # update component parameters for each repeat
    testTrials.setText(word1)
    second_word.setText(word2)
    study_recall_mic_1 = microphone.AdvAudioCapture(name='study_recall_mic_1', saveDir=wavDirName, stereo=False)
    # keep track of which components have finished
    test_trialsComponents = []
    test_trialsComponents.append(testTrials)
    test_trialsComponents.append(sound_2)
    test_trialsComponents.append(second_word)
    test_trialsComponents.append(study_recall_mic_1)
    test_trialsComponents.append(text_13)
    for thisComponent in test_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test_trials"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testTrials* updates
        if t >= 0.0 and testTrials.status == NOT_STARTED:
            # keep track of start time/frame for later
            testTrials.tStart = t  # underestimates by a little under one frame
            testTrials.frameNStart = frameN  # exact frame index
            testTrials.setAutoDraw(True)
        if testTrials.status == STARTED and t >= (0.0 + (8-win.monitorFramePeriod*0.75)): #most of one frame period left
            testTrials.setAutoDraw(False)
        # start/stop sound_2
        if t >= 3.5 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        if sound_2.status == STARTED and t >= (3.5 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_2.stop()  # stop the sound (if longer than duration)
        
        # *second_word* updates
        if t >= 4 and second_word.status == NOT_STARTED:
            # keep track of start time/frame for later
            second_word.tStart = t  # underestimates by a little under one frame
            second_word.frameNStart = frameN  # exact frame index
            second_word.setAutoDraw(True)
        if second_word.status == STARTED and t >= (4 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            second_word.setAutoDraw(False)
        
        # *study_recall_mic_1* updates
        if t >= 0.0 and study_recall_mic_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            study_recall_mic_1.tStart = t  # underestimates by a little under one frame
            study_recall_mic_1.frameNStart = frameN  # exact frame index
            study_recall_mic_1.status = STARTED
            study_recall_mic_1.record(sec=4, block=False)  # start the recording thread
        
        if study_recall_mic_1.status == STARTED and not study_recall_mic_1.recorder.running:
            study_recall_mic_1.status = FINISHED
        
        # *text_13* updates
        if t >= 8 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t  # underestimates by a little under one frame
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        if text_13.status == STARTED and t >= (8 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_13.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test_trials"-------
    for thisComponent in test_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop() #ensure sound has stopped at end of routine
    # study_recall_mic_1 stop & responses
    study_recall_mic_1.stop()  # sometimes helpful
    if not study_recall_mic_1.savedFile:
        study_recall_mic_1.savedFile = None
    # store data for trials_3 (TrialHandler)
    trials_3.addData('study_recall_mic_1.filename', study_recall_mic_1.savedFile)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(recy),
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8.keys():
        exec(paramName + '= thisTrial_8.' + paramName)

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8.keys():
            exec(paramName + '= thisTrial_8.' + paramName)
    
    #------Prepare to start Routine "recencyTest"-------
    t = 0
    recencyTestClock.reset()  # clock 
    frameN = -1
    routineTimer.add(8.500000)
    # update component parameters for each repeat
    rec_test.setText(word1)
    rec_test2.setText(word2)
    recency_mic = microphone.AdvAudioCapture(name='recency_mic', saveDir=wavDirName, stereo=False)
    # keep track of which components have finished
    recencyTestComponents = []
    recencyTestComponents.append(rec_test)
    recencyTestComponents.append(sound_5)
    recencyTestComponents.append(rec_test2)
    recencyTestComponents.append(recency_mic)
    recencyTestComponents.append(text_11)
    for thisComponent in recencyTestComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "recencyTest"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = recencyTestClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec_test* updates
        if t >= 0.0 and rec_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            rec_test.tStart = t  # underestimates by a little under one frame
            rec_test.frameNStart = frameN  # exact frame index
            rec_test.setAutoDraw(True)
        if rec_test.status == STARTED and t >= (0.0 + (8-win.monitorFramePeriod*0.75)): #most of one frame period left
            rec_test.setAutoDraw(False)
        # start/stop sound_5
        if t >= 3.5 and sound_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_5.tStart = t  # underestimates by a little under one frame
            sound_5.frameNStart = frameN  # exact frame index
            sound_5.play()  # start the sound (it finishes automatically)
        if sound_5.status == STARTED and t >= (3.5 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_5.stop()  # stop the sound (if longer than duration)
        
        # *rec_test2* updates
        if t >= 4 and rec_test2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rec_test2.tStart = t  # underestimates by a little under one frame
            rec_test2.frameNStart = frameN  # exact frame index
            rec_test2.setAutoDraw(True)
        if rec_test2.status == STARTED and t >= (4 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            rec_test2.setAutoDraw(False)
        
        # *recency_mic* updates
        if t >= 0.0 and recency_mic.status == NOT_STARTED:
            # keep track of start time/frame for later
            recency_mic.tStart = t  # underestimates by a little under one frame
            recency_mic.frameNStart = frameN  # exact frame index
            recency_mic.status = STARTED
            recency_mic.record(sec=4, block=False)  # start the recording thread
        
        if recency_mic.status == STARTED and not recency_mic.recorder.running:
            recency_mic.status = FINISHED
        
        # *text_11* updates
        if t >= 8 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        if text_11.status == STARTED and t >= (8 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_11.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recencyTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "recencyTest"-------
    for thisComponent in recencyTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_5.stop() #ensure sound has stopped at end of routine
    # recency_mic stop & responses
    recency_mic.stop()  # sometimes helpful
    if not recency_mic.savedFile:
        recency_mic.savedFile = None
    # store data for trials_8 (TrialHandler)
    trials_8.addData('recency_mic.filename', recency_mic.savedFile)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_8'


#------Prepare to start Routine "math_problems"-------
t = 0
math_problemsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
math_problemsComponents = []
math_problemsComponents.append(math1)
math_problemsComponents.append(sound_1)
math_problemsComponents.append(done_math)
math_problemsComponents.append(key_resp_6)
for thisComponent in math_problemsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "math_problems"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = math_problemsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *math1* updates
    if t >= 0.0 and math1.status == NOT_STARTED:
        # keep track of start time/frame for later
        math1.tStart = t  # underestimates by a little under one frame
        math1.frameNStart = frameN  # exact frame index
        math1.setAutoDraw(True)
    if math1.status == STARTED and t >= (0.0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
        math1.setAutoDraw(False)
    # start/stop sound_1
    if t >= 60 and sound_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_1.tStart = t  # underestimates by a little under one frame
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.play()  # start the sound (it finishes automatically)
    if sound_1.status == STARTED and t >= (60 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_1.stop()  # stop the sound (if longer than duration)
    
    # *done_math* updates
    if t >= 60 and done_math.status == NOT_STARTED:
        # keep track of start time/frame for later
        done_math.tStart = t  # underestimates by a little under one frame
        done_math.frameNStart = frameN  # exact frame index
        done_math.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 60 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        key_resp_6.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in math_problemsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "math_problems"-------
for thisComponent in math_problemsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_1.stop() #ensure sound has stopped at end of routine
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()

#------Prepare to start Routine "final_test_instruc"-------
t = 0
final_test_instrucClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
final_test_instrucComponents = []
final_test_instrucComponents.append(text_3)
final_test_instrucComponents.append(key_resp_7)
for thisComponent in final_test_instrucComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "final_test_instruc"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = final_test_instrucClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_test_instrucComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "final_test_instruc"-------
for thisComponent in final_test_instrucComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_8.status = NOT_STARTED
# keep track of which components have finished
readyComponents = []
readyComponents.append(text_15)
readyComponents.append(key_resp_8)
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ready"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if t >= 0.0 and text_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_15.tStart = t  # underestimates by a little under one frame
        text_15.frameNStart = frameN  # exact frame index
        text_15.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t  # underestimates by a little under one frame
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_night.psyexp',
    trialList=data.importConditions(night_recall),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    #------Prepare to start Routine "final_night_test_2"-------
    t = 0
    final_night_test_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    text_4.setText(word1)
    night_test_mic = microphone.AdvAudioCapture(name='night_test_mic', saveDir=wavDirName, stereo=False)
    # keep track of which components have finished
    final_night_test_2Components = []
    final_night_test_2Components.append(text_4)
    final_night_test_2Components.append(sound_6)
    final_night_test_2Components.append(night_test_mic)
    final_night_test_2Components.append(text_12)
    for thisComponent in final_night_test_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "final_night_test_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = final_night_test_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        if text_4.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_4.setAutoDraw(False)
        # start/stop sound_6
        if t >= 3.5 and sound_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_6.tStart = t  # underestimates by a little under one frame
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.play()  # start the sound (it finishes automatically)
        if sound_6.status == STARTED and t >= (3.5 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_6.stop()  # stop the sound (if longer than duration)
        
        # *night_test_mic* updates
        if t >= 0.0 and night_test_mic.status == NOT_STARTED:
            # keep track of start time/frame for later
            night_test_mic.tStart = t  # underestimates by a little under one frame
            night_test_mic.frameNStart = frameN  # exact frame index
            night_test_mic.status = STARTED
            night_test_mic.record(sec=4, block=False)  # start the recording thread
        
        if night_test_mic.status == STARTED and not night_test_mic.recorder.running:
            night_test_mic.status = FINISHED
        
        # *text_12* updates
        if t >= 4 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t  # underestimates by a little under one frame
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        if text_12.status == STARTED and t >= (4 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_12.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in final_night_test_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "final_night_test_2"-------
    for thisComponent in final_night_test_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_6.stop() #ensure sound has stopped at end of routine
    # night_test_mic stop & responses
    night_test_mic.stop()  # sometimes helpful
    if not night_test_mic.savedFile:
        night_test_mic.savedFile = None
    # store data for trials_4 (TrialHandler)
    trials_4.addData('night_test_mic.filename', night_test_mic.savedFile)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


#------Prepare to start Routine "complete"-------
t = 0
completeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_9.status = NOT_STARTED
# keep track of which components have finished
completeComponents = []
completeComponents.append(text_14)
completeComponents.append(key_resp_9)
for thisComponent in completeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "complete"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = completeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t  # underestimates by a little under one frame
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # underestimates by a little under one frame
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in completeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "complete"-------
for thisComponent in completeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()
