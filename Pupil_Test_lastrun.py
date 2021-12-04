#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Sat Nov 27 20:06:20 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

eyetracking ='1'


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Pupil_Test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/cmml/Documents/Pupillometry_Experiment/Pupil_Test_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome to the Pupillometry Experiment.\npress spacebar to continue',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
textbox = visual.TextBox2(
     win, text='Enter_ID', font='Open Sans',
     pos=(0, -6),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox',
     autoLog=True,
)

# Initialize components for Routine "Pupil"
PupilClock = core.Clock()

# Initialize components for Routine "Ready_Tone"
Ready_ToneClock = core.Clock()
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.3,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
Ready = sound.Sound('Audio/start.wav', secs=1.0, stereo=True, hamming=True,
    name='Ready')
Ready.setVolume(1.0)
import numpy

# Initialize components for Routine "Reference_Tone"
Reference_ToneClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_1 = sound.Sound('Audio/850.0.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# Initialize components for Routine "Comparison_Tone"
Comparison_ToneClock = core.Clock()
polygon_5 = visual.ShapeStim(
    win=win, name='polygon_5', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "End_Tone"
End_ToneClock = core.Clock()
polygon_6 = visual.ShapeStim(
    win=win, name='polygon_6', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_3 = sound.Sound('Audio/Answer.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
sounds = ['Audio/right_tick.wav','Audio/wrong_buzz.wav']
Response = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Response')
Response.setVolume(1.0)
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "Block_1"
Block_1Clock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
Ready_tone = sound.Sound('Audio/650.wav', secs=-1, stereo=True, hamming=True,
    name='Ready_tone')
Ready_tone.setVolume(0.5)
Reference_tone = sound.Sound('Audio/850.0.wav', secs=-1, stereo=True, hamming=True,
    name='Reference_tone')
Reference_tone.setVolume(0.5)
comparison_tone = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='comparison_tone')
comparison_tone.setVolume(0.5)
Stop_tone = sound.Sound('Audio/650.wav', secs=-1, stereo=True, hamming=True,
    name='Stop_tone')
Stop_tone.setVolume(0.5)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
sounds = ['Audio/right_tick.wav','Audio/wrong_buzz.wav']
Response = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Response')
Response.setVolume(1.0)
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "Break"
BreakClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press Spacebar to Continue',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Pupil"
PupilClock = core.Clock()

# Initialize components for Routine "Block_1"
Block_1Clock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
Ready_tone = sound.Sound('Audio/650.wav', secs=-1, stereo=True, hamming=True,
    name='Ready_tone')
Ready_tone.setVolume(0.5)
Reference_tone = sound.Sound('Audio/850.0.wav', secs=-1, stereo=True, hamming=True,
    name='Reference_tone')
Reference_tone.setVolume(0.5)
comparison_tone = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='comparison_tone')
comparison_tone.setVolume(0.5)
Stop_tone = sound.Sound('Audio/650.wav', secs=-1, stereo=True, hamming=True,
    name='Stop_tone')
Stop_tone.setVolume(0.5)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
sounds = ['Audio/right_tick.wav','Audio/wrong_buzz.wav']
Response = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Response')
Response.setVolume(1.0)
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "Break"
BreakClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press Spacebar to Continue',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
textbox.reset()
# keep track of which components have finished
trialComponents = [text, key_resp, textbox]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # was this correct?
            if (key_resp.keys == str("'space'")) or (key_resp.keys == "'space'"):
                key_resp.corr = 1
            else:
                key_resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       key_resp.corr = 1;  # correct non-response
    else:
       key_resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp.keys',key_resp.keys)
thisExp.addData('key_resp.corr', key_resp.corr)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Pupil"-------
continueRoutine = True
# update component parameters for each repeat
if eyetracking == '1':
    import zmq
    import msgpack as serializer

    from time import sleep, time

    # Setup zmq context and remote helper
    ctx = zmq.Context()
    pupil_remote = zmq.Socket(ctx, zmq.REQ)
    pupil_remote.connect('tcp://127.0.0.1:50020')

    pupil_remote.send_string("PUB_PORT")
    pub_port = pupil_remote.recv_string()
    pub_socket = zmq.Socket(ctx, zmq.PUB)
    pub_socket.connect("tcp://127.0.0.1:" + str(pub_port))

    # set time to psychopy clock
    time_fn = core.monotonicClock.getTime

    # set pupil's time to psychopy time
    pupil_remote.send_string("T " + str(time_fn()))
    print(pupil_remote.recv_string())

    sleep(2.)

    # send notification:
    def notify(notification):
        """Sends ``notification`` to Pupil Remote"""
        topic = "notify." + notification["subject"]
        payload = serializer.dumps(notification, use_bin_type=True)
        pupil_remote.send_string(topic, flags=zmq.SNDMORE)
        pupil_remote.send(payload)
        return pupil_remote.recv_string()

    def send_trigger(trigger):
        payload = serializer.dumps(trigger, use_bin_type=True)
        pub_socket.send_string(trigger["topic"], flags=zmq.SNDMORE)
        pub_socket.send(payload)

    # Start the annotations plugin
    notify({"subject": "start_plugin", "name": "Annotation_Capture", "args": {}})

    # start recording
    pupil_remote.send_string('R pupil_Labs')
    print(pupil_remote.recv_string())
    sleep(1.)
    

    def new_trigger(label, duration):
        return {
        "topic": "annotation",
        "label": label,
        "timestamp": time_fn(),
        "duration": duration,
        }

    label = "start_experiment"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)

else:
    continueRoutine = False
# keep track of which components have finished
PupilComponents = []
for thisComponent in PupilComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PupilClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pupil"-------
while continueRoutine:
    # get current time
    t = PupilClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PupilClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PupilComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pupil"-------
for thisComponent in PupilComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Pupil" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=None, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loopTemplate1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Ready_Tone"-------
    continueRoutine = True
    # update component parameters for each repeat
    Ready.setSound('Audio/start.wav', secs=1.0, hamming=True)
    Ready.setVolume(1.0, log=False)
    ready_wait = np.random.choice(np.arange(2,7),1)[0]
    # keep track of which components have finished
    Ready_ToneComponents = [polygon_3, Ready]
    for thisComponent in Ready_ToneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Ready_ToneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Ready_Tone"-------
    while continueRoutine:
        # get current time
        t = Ready_ToneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Ready_ToneClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + ready_wait-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        # start/stop Ready
        if Ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ready.frameNStart = frameN  # exact frame index
            Ready.tStart = t  # local t and not account for scr refresh
            Ready.tStartRefresh = tThisFlipGlobal  # on global time
            Ready.play(when=win)  # sync with win flip
        if Ready.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Ready.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Ready.tStop = t  # not accounting for scr refresh
                Ready.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Ready, 'tStopRefresh')  # time at next scr refresh
                Ready.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ready_ToneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready_Tone"-------
    for thisComponent in Ready_ToneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_3.started', polygon_3.tStartRefresh)
    trials.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    Ready.stop()  # ensure sound has stopped at end of routine
    trials.addData('Ready.started', Ready.tStartRefresh)
    trials.addData('Ready.stopped', Ready.tStopRefresh)
    # the Routine "Ready_Tone" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Reference_Tone"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_1.setSound('Audio/850.0.wav', secs=1.0, hamming=True)
    sound_1.setVolume(1.0, log=False)
    # keep track of which components have finished
    Reference_ToneComponents = [polygon_4, sound_1]
    for thisComponent in Reference_ToneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Reference_ToneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Reference_Tone"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Reference_ToneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Reference_ToneClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Reference_ToneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Reference_Tone"-------
    for thisComponent in Reference_ToneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_4.started', polygon_4.tStartRefresh)
    trials.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1.started', sound_1.tStartRefresh)
    trials.addData('sound_1.stopped', sound_1.tStopRefresh)
    
    # ------Prepare to start Routine "Comparison_Tone"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_2.setSound(sound_files, secs=1.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    Comparison_ToneComponents = [polygon_5, sound_2]
    for thisComponent in Comparison_ToneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comparison_ToneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comparison_Tone"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Comparison_ToneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comparison_ToneClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        if polygon_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_5.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_5.tStop = t  # not accounting for scr refresh
                polygon_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
                polygon_5.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comparison_ToneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comparison_Tone"-------
    for thisComponent in Comparison_ToneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_5.started', polygon_5.tStartRefresh)
    trials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    
    # ------Prepare to start Routine "End_Tone"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_3.setSound('Audio/Answer.wav', secs=1.0, hamming=True)
    sound_3.setVolume(1.0, log=False)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    End_ToneComponents = [polygon_6, sound_3, key_resp_4]
    for thisComponent in End_ToneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_ToneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_Tone"-------
    while continueRoutine:
        # get current time
        t = End_ToneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_ToneClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_6* updates
        if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(True)
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play(when=win)  # sync with win flip
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
                sound_3.stop()
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['lshift', 'rshift'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # was this correct?
                if (key_resp_4.keys == str(answer)) or (key_resp_4.keys == answer):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_ToneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_Tone"-------
    for thisComponent in End_ToneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_6.started', polygon_6.tStartRefresh)
    trials.addData('polygon_6.stopped', polygon_6.tStopRefresh)
    sound_3.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_3.started', sound_3.tStartRefresh)
    trials.addData('sound_3.stopped', sound_3.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    trials.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "End_Tone" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    if key_resp_2.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    
    Response.setSound(sound, hamming=True)
    Response.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedbackComponents = [Response, polygon_2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop Response
        if Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            Response.play(when=win)  # sync with win flip
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + fourth_time-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Response.stop()  # ensure sound has stopped at end of routine
    trials.addData('Response.started', Response.tStartRefresh)
    trials.addData('Response.stopped', Response.tStopRefresh)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed None repeats of 'trials'


# set up handler to look after randomisation of conditions etc
practice_block = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loopTemplate3.xlsx'),
    seed=None, name='practice_block')
thisExp.addLoop(practice_block)  # add the loop to the experiment
thisPractice_block = practice_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_block.rgb)
if thisPractice_block != None:
    for paramName in thisPractice_block:
        exec('{} = thisPractice_block[paramName]'.format(paramName))

for thisPractice_block in practice_block:
    currentLoop = practice_block
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_block.rgb)
    if thisPractice_block != None:
        for paramName in thisPractice_block:
            exec('{} = thisPractice_block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    Ready_tone.setSound('Audio/650.wav', hamming=True)
    Ready_tone.setVolume(0.5, log=False)
    Reference_tone.setSound('Audio/850.0.wav', hamming=True)
    Reference_tone.setVolume(0.5, log=False)
    comparison_tone.setSound(sound_files, hamming=True)
    comparison_tone.setVolume(0.5, log=False)
    Stop_tone.setSound('Audio/650.wav', hamming=True)
    Stop_tone.setVolume(0.5, log=False)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    Block_1Components = [polygon, Ready_tone, Reference_tone, comparison_tone, Stop_tone, key_resp_2]
    for thisComponent in Block_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_1"-------
    while continueRoutine:
        # get current time
        t = Block_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        # start/stop Ready_tone
        if Ready_tone.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Ready_tone.frameNStart = frameN  # exact frame index
            Ready_tone.tStart = t  # local t and not account for scr refresh
            Ready_tone.tStartRefresh = tThisFlipGlobal  # on global time
            Ready_tone.play(when=win)  # sync with win flip
        # start/stop Reference_tone
        if Reference_tone.status == NOT_STARTED and tThisFlip >= first_time-frameTolerance:
            # keep track of start time/frame for later
            Reference_tone.frameNStart = frameN  # exact frame index
            Reference_tone.tStart = t  # local t and not account for scr refresh
            Reference_tone.tStartRefresh = tThisFlipGlobal  # on global time
            Reference_tone.play(when=win)  # sync with win flip
        # start/stop comparison_tone
        if comparison_tone.status == NOT_STARTED and tThisFlip >= second_time-frameTolerance:
            # keep track of start time/frame for later
            comparison_tone.frameNStart = frameN  # exact frame index
            comparison_tone.tStart = t  # local t and not account for scr refresh
            comparison_tone.tStartRefresh = tThisFlipGlobal  # on global time
            comparison_tone.play(when=win)  # sync with win flip
        # start/stop Stop_tone
        if Stop_tone.status == NOT_STARTED and tThisFlip >= third_time-frameTolerance:
            # keep track of start time/frame for later
            Stop_tone.frameNStart = frameN  # exact frame index
            Stop_tone.tStart = t  # local t and not account for scr refresh
            Stop_tone.tStartRefresh = tThisFlipGlobal  # on global time
            Stop_tone.play(when=win)  # sync with win flip
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['z', 'right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(answer)) or (key_resp_2.keys == answer):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_1"-------
    for thisComponent in Block_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_block.addData('polygon.started', polygon.tStartRefresh)
    practice_block.addData('polygon.stopped', polygon.tStopRefresh)
    Ready_tone.stop()  # ensure sound has stopped at end of routine
    practice_block.addData('Ready_tone.started', Ready_tone.tStartRefresh)
    practice_block.addData('Ready_tone.stopped', Ready_tone.tStopRefresh)
    Reference_tone.stop()  # ensure sound has stopped at end of routine
    practice_block.addData('Reference_tone.started', Reference_tone.tStartRefresh)
    practice_block.addData('Reference_tone.stopped', Reference_tone.tStopRefresh)
    comparison_tone.stop()  # ensure sound has stopped at end of routine
    practice_block.addData('comparison_tone.started', comparison_tone.tStartRefresh)
    practice_block.addData('comparison_tone.stopped', comparison_tone.tStopRefresh)
    Stop_tone.stop()  # ensure sound has stopped at end of routine
    practice_block.addData('Stop_tone.started', Stop_tone.tStartRefresh)
    practice_block.addData('Stop_tone.stopped', Stop_tone.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_block (TrialHandler)
    practice_block.addData('key_resp_2.keys',key_resp_2.keys)
    practice_block.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        practice_block.addData('key_resp_2.rt', key_resp_2.rt)
    practice_block.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    practice_block.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Block_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    if key_resp_2.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    
    Response.setSound(sound, hamming=True)
    Response.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedbackComponents = [Response, polygon_2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop Response
        if Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            Response.play(when=win)  # sync with win flip
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + fourth_time-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Response.stop()  # ensure sound has stopped at end of routine
    practice_block.addData('Response.started', Response.tStartRefresh)
    practice_block.addData('Response.stopped', Response.tStopRefresh)
    practice_block.addData('polygon_2.started', polygon_2.tStartRefresh)
    practice_block.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'practice_block'


# ------Prepare to start Routine "Break"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
if eyetracking == '1':
    import zmq
    import msgpack as serializer

    from time import sleep, time

    # Setup zmq context and remote helper
    ctx = zmq.Context()
    pupil_remote = zmq.Socket(ctx, zmq.REQ)
    pupil_remote.connect('tcp://127.0.0.1:50020')

    pupil_remote.send_string("PUB_PORT")
    pub_port = pupil_remote.recv_string()
    pub_socket = zmq.Socket(ctx, zmq.PUB)
    pub_socket.connect("tcp://127.0.0.1:" + str(pub_port))

    # set time to psychopy clock
    time_fn = core.monotonicClock.getTime

    # set pupil's time to psychopy time
    pupil_remote.send_string("T " + str(time_fn()))
    print(pupil_remote.recv_string())

    sleep(2.)

    # send notification:
    def notify(notification):
        """Sends ``notification`` to Pupil Remote"""
        topic = "notify." + notification["subject"]
        payload = serializer.dumps(notification, use_bin_type=True)
        pupil_remote.send_string(topic, flags=zmq.SNDMORE)
        pupil_remote.send(payload)
        return pupil_remote.recv_string()

    def send_trigger(trigger):
        payload = serializer.dumps(trigger, use_bin_type=True)
        pub_socket.send_string(trigger["topic"], flags=zmq.SNDMORE)
        pub_socket.send(payload)

    # Start the annotations plugin
    notify({"subject": "start_plugin", "name": "Annotation_Capture", "args": {}})

    # start recording
    pupil_remote.send_string('r')
    print(pupil_remote.recv_string())
    sleep(1.)
    

    def new_trigger(label, duration):
        return {
        "topic": "annotation",
        "label": label,
        "timestamp": time_fn(),
        "duration": duration,
        }

    label = "stop_experiment"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)

else:
    continueRoutine = False
# keep track of which components have finished
BreakComponents = [text_2, key_resp_3]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Pupil"-------
continueRoutine = True
# update component parameters for each repeat
if eyetracking == '1':
    import zmq
    import msgpack as serializer

    from time import sleep, time

    # Setup zmq context and remote helper
    ctx = zmq.Context()
    pupil_remote = zmq.Socket(ctx, zmq.REQ)
    pupil_remote.connect('tcp://127.0.0.1:50020')

    pupil_remote.send_string("PUB_PORT")
    pub_port = pupil_remote.recv_string()
    pub_socket = zmq.Socket(ctx, zmq.PUB)
    pub_socket.connect("tcp://127.0.0.1:" + str(pub_port))

    # set time to psychopy clock
    time_fn = core.monotonicClock.getTime

    # set pupil's time to psychopy time
    pupil_remote.send_string("T " + str(time_fn()))
    print(pupil_remote.recv_string())

    sleep(2.)

    # send notification:
    def notify(notification):
        """Sends ``notification`` to Pupil Remote"""
        topic = "notify." + notification["subject"]
        payload = serializer.dumps(notification, use_bin_type=True)
        pupil_remote.send_string(topic, flags=zmq.SNDMORE)
        pupil_remote.send(payload)
        return pupil_remote.recv_string()

    def send_trigger(trigger):
        payload = serializer.dumps(trigger, use_bin_type=True)
        pub_socket.send_string(trigger["topic"], flags=zmq.SNDMORE)
        pub_socket.send(payload)

    # Start the annotations plugin
    notify({"subject": "start_plugin", "name": "Annotation_Capture", "args": {}})

    # start recording
    pupil_remote.send_string('R pupil_Labs')
    print(pupil_remote.recv_string())
    sleep(1.)
    

    def new_trigger(label, duration):
        return {
        "topic": "annotation",
        "label": label,
        "timestamp": time_fn(),
        "duration": duration,
        }

    label = "start_experiment"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)

else:
    continueRoutine = False
# keep track of which components have finished
PupilComponents = []
for thisComponent in PupilComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PupilClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pupil"-------
while continueRoutine:
    # get current time
    t = PupilClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PupilClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PupilComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pupil"-------
for thisComponent in PupilComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Pupil" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block1 = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loopTemplate2.xlsx'),
    seed=None, name='Block1')
thisExp.addLoop(Block1)  # add the loop to the experiment
thisBlock1 = Block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1:
        exec('{} = thisBlock1[paramName]'.format(paramName))

for thisBlock1 in Block1:
    currentLoop = Block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1:
            exec('{} = thisBlock1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    Ready_tone.setSound('Audio/650.wav', hamming=True)
    Ready_tone.setVolume(0.5, log=False)
    Reference_tone.setSound('Audio/850.0.wav', hamming=True)
    Reference_tone.setVolume(0.5, log=False)
    comparison_tone.setSound(sound_files, hamming=True)
    comparison_tone.setVolume(0.5, log=False)
    Stop_tone.setSound('Audio/650.wav', hamming=True)
    Stop_tone.setVolume(0.5, log=False)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    Block_1Components = [polygon, Ready_tone, Reference_tone, comparison_tone, Stop_tone, key_resp_2]
    for thisComponent in Block_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_1"-------
    while continueRoutine:
        # get current time
        t = Block_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        # start/stop Ready_tone
        if Ready_tone.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Ready_tone.frameNStart = frameN  # exact frame index
            Ready_tone.tStart = t  # local t and not account for scr refresh
            Ready_tone.tStartRefresh = tThisFlipGlobal  # on global time
            Ready_tone.play(when=win)  # sync with win flip
        # start/stop Reference_tone
        if Reference_tone.status == NOT_STARTED and tThisFlip >= first_time-frameTolerance:
            # keep track of start time/frame for later
            Reference_tone.frameNStart = frameN  # exact frame index
            Reference_tone.tStart = t  # local t and not account for scr refresh
            Reference_tone.tStartRefresh = tThisFlipGlobal  # on global time
            Reference_tone.play(when=win)  # sync with win flip
        # start/stop comparison_tone
        if comparison_tone.status == NOT_STARTED and tThisFlip >= second_time-frameTolerance:
            # keep track of start time/frame for later
            comparison_tone.frameNStart = frameN  # exact frame index
            comparison_tone.tStart = t  # local t and not account for scr refresh
            comparison_tone.tStartRefresh = tThisFlipGlobal  # on global time
            comparison_tone.play(when=win)  # sync with win flip
        # start/stop Stop_tone
        if Stop_tone.status == NOT_STARTED and tThisFlip >= third_time-frameTolerance:
            # keep track of start time/frame for later
            Stop_tone.frameNStart = frameN  # exact frame index
            Stop_tone.tStart = t  # local t and not account for scr refresh
            Stop_tone.tStartRefresh = tThisFlipGlobal  # on global time
            Stop_tone.play(when=win)  # sync with win flip
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['z', 'right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(answer)) or (key_resp_2.keys == answer):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_1"-------
    for thisComponent in Block_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1.addData('polygon.started', polygon.tStartRefresh)
    Block1.addData('polygon.stopped', polygon.tStopRefresh)
    Ready_tone.stop()  # ensure sound has stopped at end of routine
    Block1.addData('Ready_tone.started', Ready_tone.tStartRefresh)
    Block1.addData('Ready_tone.stopped', Ready_tone.tStopRefresh)
    Reference_tone.stop()  # ensure sound has stopped at end of routine
    Block1.addData('Reference_tone.started', Reference_tone.tStartRefresh)
    Block1.addData('Reference_tone.stopped', Reference_tone.tStopRefresh)
    comparison_tone.stop()  # ensure sound has stopped at end of routine
    Block1.addData('comparison_tone.started', comparison_tone.tStartRefresh)
    Block1.addData('comparison_tone.stopped', comparison_tone.tStopRefresh)
    Stop_tone.stop()  # ensure sound has stopped at end of routine
    Block1.addData('Stop_tone.started', Stop_tone.tStartRefresh)
    Block1.addData('Stop_tone.stopped', Stop_tone.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for Block1 (TrialHandler)
    Block1.addData('key_resp_2.keys',key_resp_2.keys)
    Block1.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        Block1.addData('key_resp_2.rt', key_resp_2.rt)
    Block1.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    Block1.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Block_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    if key_resp_2.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    
    Response.setSound(sound, hamming=True)
    Response.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedbackComponents = [Response, polygon_2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop Response
        if Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            Response.play(when=win)  # sync with win flip
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + fourth_time-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Response.stop()  # ensure sound has stopped at end of routine
    Block1.addData('Response.started', Response.tStartRefresh)
    Block1.addData('Response.stopped', Response.tStopRefresh)
    Block1.addData('polygon_2.started', polygon_2.tStartRefresh)
    Block1.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Block1'


# ------Prepare to start Routine "Break"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
if eyetracking == '1':
    import zmq
    import msgpack as serializer

    from time import sleep, time

    # Setup zmq context and remote helper
    ctx = zmq.Context()
    pupil_remote = zmq.Socket(ctx, zmq.REQ)
    pupil_remote.connect('tcp://127.0.0.1:50020')

    pupil_remote.send_string("PUB_PORT")
    pub_port = pupil_remote.recv_string()
    pub_socket = zmq.Socket(ctx, zmq.PUB)
    pub_socket.connect("tcp://127.0.0.1:" + str(pub_port))

    # set time to psychopy clock
    time_fn = core.monotonicClock.getTime

    # set pupil's time to psychopy time
    pupil_remote.send_string("T " + str(time_fn()))
    print(pupil_remote.recv_string())

    sleep(2.)

    # send notification:
    def notify(notification):
        """Sends ``notification`` to Pupil Remote"""
        topic = "notify." + notification["subject"]
        payload = serializer.dumps(notification, use_bin_type=True)
        pupil_remote.send_string(topic, flags=zmq.SNDMORE)
        pupil_remote.send(payload)
        return pupil_remote.recv_string()

    def send_trigger(trigger):
        payload = serializer.dumps(trigger, use_bin_type=True)
        pub_socket.send_string(trigger["topic"], flags=zmq.SNDMORE)
        pub_socket.send(payload)

    # Start the annotations plugin
    notify({"subject": "start_plugin", "name": "Annotation_Capture", "args": {}})

    # start recording
    pupil_remote.send_string('r')
    print(pupil_remote.recv_string())
    sleep(1.)
    

    def new_trigger(label, duration):
        return {
        "topic": "annotation",
        "label": label,
        "timestamp": time_fn(),
        "duration": duration,
        }

    label = "stop_experiment"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)

else:
    continueRoutine = False
# keep track of which components have finished
BreakComponents = [text_2, key_resp_3]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
