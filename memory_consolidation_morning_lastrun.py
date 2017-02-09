#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), Wed Jan 20 08:05:45 2016
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
expName = 'memory_consolidation_morning'  # from the Builder filename that created this script
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
    originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_morning.psyexp',
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

# Initialize components for Routine "morning_instructions"
morning_instructionsClock = core.Clock()
l = expInfo['list']
p = expInfo['participant']

morn_recall = 'morning_recall_list'+l+'sub'+p+'.csv'

instruc = visual.TextStim(win=win, ori=0, name='instruc',
    text='Good morning! \n\nRemember the memory task you completed last night? You studied word pairs and later I gave you one word and asked you to recall the other word in the pair.\nThis morning you are going to complete the same task with the word pairs you studied last night.\n\nPlease verbally recall the other word in the pair. It is important that you say the word before you hear the beep. \n\nYou will NOT see the correct answer after the beep.\n\nQuestions?',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ready"
readyClock = core.Clock()
ready_screen = visual.TextStim(win=win, ori=0, name='ready_screen',
    text='Ready? Please press the space bar to start the task',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "morning_test"
morning_testClock = core.Clock()
text_word = visual.TextStim(win=win, ori=0, name='text_word',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_1 = sound.Sound('B', secs=-1)
sound_1.setVolume(1)
text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "complete"
completeClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Task complete!\n\nThank you.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "morning_instructions"-------
t = 0
morning_instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
morning_instructionsComponents = []
morning_instructionsComponents.append(instruc)
morning_instructionsComponents.append(key_resp_2)
for thisComponent in morning_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "morning_instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = morning_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *instruc* updates
    if t >= 0.0 and instruc.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruc.tStart = t  # underestimates by a little under one frame
        instruc.frameNStart = frameN  # exact frame index
        instruc.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
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
    for thisComponent in morning_instructionsComponents:
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

#-------Ending Routine "morning_instructions"-------
for thisComponent in morning_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
readyComponents = []
readyComponents.append(ready_screen)
readyComponents.append(key_resp_3)
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
    
    # *ready_screen* updates
    if t >= 0.0 and ready_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_screen.tStart = t  # underestimates by a little under one frame
        ready_screen.frameNStart = frameN  # exact frame index
        ready_screen.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/memory_consolidation_morning.psyexp',
    trialList=data.importConditions(morn_recall),
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
    
    #------Prepare to start Routine "morning_test"-------
    t = 0
    morning_testClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    text_word.setText(word1)
    morning_test_mic = microphone.AdvAudioCapture(name='morning_test_mic', saveDir=wavDirName, stereo=False)
    # keep track of which components have finished
    morning_testComponents = []
    morning_testComponents.append(text_word)
    morning_testComponents.append(sound_1)
    morning_testComponents.append(morning_test_mic)
    morning_testComponents.append(text)
    for thisComponent in morning_testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "morning_test"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = morning_testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_word* updates
        if t >= 0.0 and text_word.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_word.tStart = t  # underestimates by a little under one frame
            text_word.frameNStart = frameN  # exact frame index
            text_word.setAutoDraw(True)
        if text_word.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_word.setAutoDraw(False)
        # start/stop sound_1
        if t >= 3.5 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED and t >= (3.5 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *morning_test_mic* updates
        if t >= 0.0 and morning_test_mic.status == NOT_STARTED:
            # keep track of start time/frame for later
            morning_test_mic.tStart = t  # underestimates by a little under one frame
            morning_test_mic.frameNStart = frameN  # exact frame index
            morning_test_mic.status = STARTED
            morning_test_mic.record(sec=4, block=False)  # start the recording thread
        
        if morning_test_mic.status == STARTED and not morning_test_mic.recorder.running:
            morning_test_mic.status = FINISHED
        
        # *text* updates
        if t >= 4 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        if text.status == STARTED and t >= (4 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in morning_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "morning_test"-------
    for thisComponent in morning_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop() #ensure sound has stopped at end of routine
    # morning_test_mic stop & responses
    morning_test_mic.stop()  # sometimes helpful
    if not morning_test_mic.savedFile:
        morning_test_mic.savedFile = None
    # store data for trials (TrialHandler)
    trials.addData('morning_test_mic.filename', morning_test_mic.savedFile)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "complete"-------
t = 0
completeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
completeComponents = []
completeComponents.append(text_2)
completeComponents.append(key_resp_4)
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
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
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
