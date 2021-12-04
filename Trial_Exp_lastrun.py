#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Fri Dec  3 20:06:53 2021
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

import random, xlrd
import csv

#randomize the seed
random.seed()
#stimulus file
infile = '/Users/cmml/Documents/Pupillometry_Experiment/looptemplate3.xlsx'



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Trial_Exp'  # from the Builder filename that created this script
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
    originPath='/Users/cmml/Documents/Pupillometry_Experiment/Trial_Exp_lastrun.py',
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

# Initialize components for Routine "init_code"
init_codeClock = core.Clock()
stim_words = ['Audio/820.0.wav','Audio/826.0.wav','Audio/832.0.wav','Audio/838.0.wav','Audio/844.0.wav','Audio/850.0.wav','Audio/856.0.wav','Audio/862.0.wav','Audio/868.0.wav','Audio/874.0.wav','Audio/880.0.wav']   
stimulus_array1 = []
stimulus_array2 = []
stimulus_array3 =[]
stimulus_array4 = []
stimulus_array5 =[]
practice_array=['Audio/820.0.wav','Audio/874.0.wav','Audio/826.0.wav','Audio/874.0.wav']
stim_names = [stimulus_array1,stimulus_array2,stimulus_array3,stimulus_array4,stimulus_array5]
practice_answers=['lshift','rshift','lshift','rshift']
answer_array1 = []
answer_array2 = []
answer_array3 = []
answer_array4 = []
answer_array5 = []
stim_answers = [answer_array1,answer_array2,answer_array3,answer_array4,answer_array5]
cntr1 = 0
cntr2 =0
cntr3 = 0
cntr4 = 0
cntr5 = 0
cntr_practice=0
for i in stim_names:
    for row in stim_words:
        i.append(row)
    random.shuffle(i)
cntr = 0
for i in stim_names:
    for f in i:
        if(int(f[6:9])<850):
            stim_answers[cntr].append('lshift')
        elif(int(f[6:9])>=850):
            stim_answers[cntr].append('rshift')
    cntr+=1
name = expInfo['participant'] 
file_name1 = '/Users/cmml/Documents/Pupillometry_Experiment/data/'+name+'stims.npy'
file_name2 = '/Users/cmml/Documents/Pupillometry_Experiment/data/'+name+'stimAnswers.npy'
with open(file_name1, 'wb') as f:
    np.save(f, np.array(stim_names))
with open(file_name2, 'wb') as f:
    np.save(f, np.array(stim_answers))
    



# Initialize components for Routine "Introduction"
IntroductionClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Hello and Welcome!\n\nThis study aims to replicate an oft-cited experiment from 1967 (Hahnemann & Beatty, 1967) but using modern pupillometry hardware and software. \n\nThis study has been reviewed by the Georgia Tech Institutional Review Board (IRB), and has been identified as “Minimal risk research under 45 CFR 46. (Protocol 21153). This study contains neither any personal benefits nor any known risks to you.\n\nThe experiment should take approximately 15 - 20 minutes to complete. Your participation is extremely valuable to us and we thank you for taking the time to help us.\n\nPlease click “CONTINUE” to read the full instructions.\n',
    font='Open Sans',
    pos=(0, 0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_2 = visual.ButtonStim(win, 
    text='CONTINUE', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.1,
    size=[0.7,0.2], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_2'
)
button_2.buttonClock = core.Clock()

# Initialize components for Routine "hello"
helloClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Confidentiality: The data from this experiment will be collected anonymously. Collected data will be shared with collaborators at the Georgia Institute of Technology. Data obtained will only be connected to your anonymous participant number, and will be securely stored on a password-protected and encrypted computer for a minimum of 5 years. Your identity is not recorded, nor are you identifiable from the data we record. Neither your identity nor agreement to participate will be disclosed in any publication resulting from this research.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Consent_form"
Consent_formClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Participant rights: You may refuse or discontinue your voluntary participation in this research study at any time. There is no direct benefit to you in participating in this study. However, only participants’ data who complete the full experiment will be included in the final results and dissemination.\nContacts and Questions: For questions, concerns, or complaints about the study, you may contact the PI, Dr. Claire Arthur at: claire.arthur[at]gatech.edu, or you may directly reach out to Georgia Tech’s Office of Research Integrity by contacting irb[at]gatech.edu.\nFeel free to print or save a copy of this page.\n\nBy providing consent, you are agreeing to participate. Please click “I Consent” to read the full instructions and begin the practice trials.',
    font='Open Sans',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button = visual.ButtonStim(win, 
    text='I consent', font='Arvo',
    pos=(0,-0.4),
    letterHeight=0.05,
    size=[0.28,0.1], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()

# Initialize components for Routine "Intro_contd"
Intro_contdClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=' A fixation cross appears on the screen and you will have to maintain your gaze on the cross for the duration of the experiment as much as possible. Each block of this experiment consists of 11 tones, there are a total of 5 blocks.\nThe time between blocks is used to give participants a break from the fixation cross. All cues to perform tasks are presented aurally. First, a "ready tone" of 650 Hz tells you that the trial is starting. After 2-4s you hear a standard tone of 850 Hz, followed by a randomly selected interval of silence lasting between 2-6 seconds, followed by a comparison tone (range from 820-880 Hz), followed by a 4 second pause, followed by a "response tone" which tells you to enter your response, use the keyboard ‘left shift’ if you feel the tone is lower, ‘right shift’ if you feel the tone is higher to the standard. \n\n\nPress Spacebar to start the practice trials.',
    font='Open Sans',
    pos=(0, 0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "Ready_practice"
Ready_practiceClock = core.Clock()
polygon_26 = visual.ShapeStim(
    win=win, name='polygon_26', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_26 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_26')
sound_26.setVolume(1.0)

# Initialize components for Routine "reference_practice"
reference_practiceClock = core.Clock()
polygon_27 = visual.ShapeStim(
    win=win, name='polygon_27', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_27 = sound.Sound('Audio/850.0.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_27')
sound_27.setVolume(1.0)

# Initialize components for Routine "comparison_practice"
comparison_practiceClock = core.Clock()
polygon_28 = visual.ShapeStim(
    win=win, name='polygon_28', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_28 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_28')
sound_28.setVolume(1.0)

# Initialize components for Routine "End_tonepractice"
End_tonepracticeClock = core.Clock()
polygon_29 = visual.ShapeStim(
    win=win, name='polygon_29', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_29 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_29')
sound_29.setVolume(1.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "feedback_practice"
feedback_practiceClock = core.Clock()
polygon_30 = visual.ShapeStim(
    win=win, name='polygon_30', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_30 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_30')
sound_30.setVolume(1.0)
sounds = ['Audio/right_tick.wav','Audio/wrong_buzz.wav']

# Initialize components for Routine "StartWelcome"
StartWelcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.0005, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
eyetracking='1'


# Initialize components for Routine "Pupil"
PupilClock = core.Clock()
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
def new_trigger(label, duration):
    return {
    "topic": "annotation",
    "label": label,
    "timestamp": 0.56,#time_fn(),
    "duration": duration,
    }
time_fn = core.monotonicClock.getTime

# set pupil's time to psychopy time
pupil_remote.send_string("T " + str(time_fn()))
print(pupil_remote.recv_string())
sleep(2.)


# Initialize components for Routine "Ready_tone"
Ready_toneClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.3,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_1 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
import numpy

# Initialize components for Routine "reference_tone"
reference_toneClock = core.Clock()
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_2 = sound.Sound('Audio/850.0.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "comparison_tone"
comparison_toneClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_3 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)

# Initialize components for Routine "End_tone"
End_toneClock = core.Clock()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
key_resp = keyboard.Keyboard()
sound_4 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)

# Initialize components for Routine "feedback_2"
feedback_2Clock = core.Clock()
sounds = ['Audio/right_tick.wav','Audio/wrong_buzz.wav']
polygon_5 = visual.ShapeStim(
    win=win, name='polygon_5', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
sound_5 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1.0)

# Initialize components for Routine "stop_pupil"
stop_pupilClock = core.Clock()

# Initialize components for Routine "EndBlock"
EndBlockClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Block Complete, press spacebar to continue when ready\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Pupil_2"
Pupil_2Clock = core.Clock()

# Initialize components for Routine "Ready_tone2_2"
Ready_tone2_2Clock = core.Clock()
polygon_6 = visual.ShapeStim(
    win=win, name='polygon_6', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_6 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1.0)

# Initialize components for Routine "reference_tone2"
reference_tone2Clock = core.Clock()
polygon_7 = visual.ShapeStim(
    win=win, name='polygon_7', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_7 = sound.Sound('Audio/850.0.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)

# Initialize components for Routine "comparison_tone2"
comparison_tone2Clock = core.Clock()
polygon_8 = visual.ShapeStim(
    win=win, name='polygon_8', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_8 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)

# Initialize components for Routine "End_tone2_2"
End_tone2_2Clock = core.Clock()
polygon_9 = visual.ShapeStim(
    win=win, name='polygon_9', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
key_resp_4 = keyboard.Keyboard()
sound_9 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1.0)

# Initialize components for Routine "feedback2_2"
feedback2_2Clock = core.Clock()
polygon_24 = visual.ShapeStim(
    win=win, name='polygon_24', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_24 = sound.Sound(sound, secs=-1, stereo=True, hamming=True,
    name='sound_24')
sound_24.setVolume(1.0)

# Initialize components for Routine "stop_pupil"
stop_pupilClock = core.Clock()

# Initialize components for Routine "EndBlock"
EndBlockClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Block Complete, press spacebar to continue when ready\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Pupil_3"
Pupil_3Clock = core.Clock()

# Initialize components for Routine "Ready_tone3"
Ready_tone3Clock = core.Clock()
polygon_10 = visual.ShapeStim(
    win=win, name='polygon_10', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_10 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_10')
sound_10.setVolume(1.0)

# Initialize components for Routine "reference_tone3"
reference_tone3Clock = core.Clock()
polygon_11 = visual.ShapeStim(
    win=win, name='polygon_11', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_11 = sound.Sound('Audio/850.0.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)

# Initialize components for Routine "comparison_tone3"
comparison_tone3Clock = core.Clock()
polygon_12 = visual.ShapeStim(
    win=win, name='polygon_12', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_12 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_12')
sound_12.setVolume(1.0)

# Initialize components for Routine "End_tone3"
End_tone3Clock = core.Clock()
polygon_13 = visual.ShapeStim(
    win=win, name='polygon_13', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
key_resp_5 = keyboard.Keyboard()
sound_13 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_13')
sound_13.setVolume(1.0)

# Initialize components for Routine "feedback_3"
feedback_3Clock = core.Clock()
polygon_25 = visual.ShapeStim(
    win=win, name='polygon_25', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_25 = sound.Sound(sound, secs=-1, stereo=True, hamming=True,
    name='sound_25')
sound_25.setVolume(1.0)

# Initialize components for Routine "stop_pupil"
stop_pupilClock = core.Clock()

# Initialize components for Routine "EndBlock"
EndBlockClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Block Complete, press spacebar to continue when ready\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Ready_Tone4"
Ready_Tone4Clock = core.Clock()
polygon_14 = visual.ShapeStim(
    win=win, name='polygon_14', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_14 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_14')
sound_14.setVolume(1.0)

# Initialize components for Routine "Reference_tone4"
Reference_tone4Clock = core.Clock()
polygon_15 = visual.ShapeStim(
    win=win, name='polygon_15', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_15 = sound.Sound('Audio/850.0.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_15')
sound_15.setVolume(1.0)

# Initialize components for Routine "comparison_tone4"
comparison_tone4Clock = core.Clock()
polygon_16 = visual.ShapeStim(
    win=win, name='polygon_16', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_16 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_16')
sound_16.setVolume(1.0)

# Initialize components for Routine "End_tone4"
End_tone4Clock = core.Clock()
sound_17 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_17')
sound_17.setVolume(1.0)
polygon_17 = visual.ShapeStim(
    win=win, name='polygon_17', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "feedback_4"
feedback_4Clock = core.Clock()
sounds = ['Audio/right_tick.wav','Audio/wrong_buzz.wav']
polygon_18 = visual.ShapeStim(
    win=win, name='polygon_18', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
sound_18 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_18')
sound_18.setVolume(1.0)

# Initialize components for Routine "stop_pupil"
stop_pupilClock = core.Clock()

# Initialize components for Routine "EndBlock"
EndBlockClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Block Complete, press spacebar to continue when ready\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Ready_tone5"
Ready_tone5Clock = core.Clock()
polygon_19 = visual.ShapeStim(
    win=win, name='polygon_19', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_19 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_19')
sound_19.setVolume(1.0)

# Initialize components for Routine "reference_tone5"
reference_tone5Clock = core.Clock()
polygon_20 = visual.ShapeStim(
    win=win, name='polygon_20', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_20 = sound.Sound('Audio/850.0.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_20')
sound_20.setVolume(1.0)

# Initialize components for Routine "comparison_tone5"
comparison_tone5Clock = core.Clock()
polygon_21 = visual.ShapeStim(
    win=win, name='polygon_21', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_21 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_21')
sound_21.setVolume(1.0)

# Initialize components for Routine "End_tone5"
End_tone5Clock = core.Clock()
polygon_22 = visual.ShapeStim(
    win=win, name='polygon_22', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sound_22 = sound.Sound('Audio/650.wav', secs=1.0, stereo=True, hamming=True,
    name='sound_22')
sound_22.setVolume(1.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "feedback5"
feedback5Clock = core.Clock()
polygon_23 = visual.ShapeStim(
    win=win, name='polygon_23', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sounds = ['Audio/right_tick.wav','Audio/wrong_buzz.wav']
sound_23 = sound.Sound(sound, secs=-1, stereo=True, hamming=True,
    name='sound_23')
sound_23.setVolume(1.0)

# Initialize components for Routine "stop_pupil"
stop_pupilClock = core.Clock()

# Initialize components for Routine "End_Experiment"
End_ExperimentClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Thank You For Taking Part In This Experiment\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "init_code"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
init_codeComponents = []
for thisComponent in init_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
init_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "init_code"-------
while continueRoutine:
    # get current time
    t = init_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=init_codeClock)
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
    for thisComponent in init_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "init_code"-------
for thisComponent in init_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "init_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Introduction"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
IntroductionComponents = [text_6, button_2]
for thisComponent in IntroductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Introduction"-------
while continueRoutine:
    # get current time
    t = IntroductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *button_2* updates
    if button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_2.frameNStart = frameN  # exact frame index
        button_2.tStart = t  # local t and not account for scr refresh
        button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
        button_2.setAutoDraw(True)
    if button_2.status == STARTED:
        # check whether button_2 has been pressed
        if button_2.isClicked:
            if not button_2.wasClicked:
                button_2.timesOn.append(button_2.buttonClock.getTime()) # store time of first click
                button_2.timesOff.append(button_2.buttonClock.getTime()) # store time clicked until
            else:
                button_2.timesOff[-1] = button_2.buttonClock.getTime() # update time clicked until
            if not button_2.wasClicked:
                continueRoutine = False  # end routine when button_2 is clicked
                None
            button_2.wasClicked = True  # if button_2 is still clicked next frame, it is not a new click
        else:
            button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    else:
        button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction"-------
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('button_2.started', button_2.tStartRefresh)
thisExp.addData('button_2.stopped', button_2.tStopRefresh)
thisExp.addData('button_2.numClicks', button_2.numClicks)
if button_2.numClicks:
   thisExp.addData('button_2.timesOn', button_2.timesOn)
   thisExp.addData('button_2.timesOff', button_2.timesOff)
else:
   thisExp.addData('button_2.timesOn', "")
   thisExp.addData('button_2.timesOff', "")
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hello"-------
continueRoutine = True
routineTimer.add(8.000000)
# update component parameters for each repeat
# keep track of which components have finished
helloComponents = [text_8]
for thisComponent in helloComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
helloClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hello"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = helloClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=helloClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    if text_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_8.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            text_8.tStop = t  # not accounting for scr refresh
            text_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
            text_8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in helloComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hello"-------
for thisComponent in helloComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)

# ------Prepare to start Routine "Consent_form"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Consent_formComponents = [text_4, button]
for thisComponent in Consent_formComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Consent_formClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Consent_form"-------
while continueRoutine:
    # get current time
    t = Consent_formClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Consent_formClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Consent_formComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Consent_form"-------
for thisComponent in Consent_formComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('button.numClicks', button.numClicks)
if button.numClicks:
   thisExp.addData('button.timesOn', button.timesOn)
   thisExp.addData('button.timesOff', button.timesOff)
else:
   thisExp.addData('button.timesOn', "")
   thisExp.addData('button.timesOff', "")
# the Routine "Consent_form" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro_contd"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
Intro_contdComponents = [text_7, key_resp_8]
for thisComponent in Intro_contdComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro_contdClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro_contd"-------
while continueRoutine:
    # get current time
    t = Intro_contdClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro_contdClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_contdComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro_contd"-------
for thisComponent in Intro_contdComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro_contd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Ready_practice"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    sound_26.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_26.setVolume(1.0, log=False)
    # keep track of which components have finished
    Ready_practiceComponents = [polygon_26, sound_26]
    for thisComponent in Ready_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Ready_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Ready_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Ready_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Ready_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_26* updates
        if polygon_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_26.frameNStart = frameN  # exact frame index
            polygon_26.tStart = t  # local t and not account for scr refresh
            polygon_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_26, 'tStartRefresh')  # time at next scr refresh
            polygon_26.setAutoDraw(True)
        if polygon_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_26.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_26.tStop = t  # not accounting for scr refresh
                polygon_26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_26, 'tStopRefresh')  # time at next scr refresh
                polygon_26.setAutoDraw(False)
        # start/stop sound_26
        if sound_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_26.frameNStart = frameN  # exact frame index
            sound_26.tStart = t  # local t and not account for scr refresh
            sound_26.tStartRefresh = tThisFlipGlobal  # on global time
            sound_26.play(when=win)  # sync with win flip
        if sound_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_26.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_26.tStop = t  # not accounting for scr refresh
                sound_26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_26, 'tStopRefresh')  # time at next scr refresh
                sound_26.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ready_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready_practice"-------
    for thisComponent in Ready_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_6.addData('polygon_26.started', polygon_26.tStartRefresh)
    trials_6.addData('polygon_26.stopped', polygon_26.tStopRefresh)
    sound_26.stop()  # ensure sound has stopped at end of routine
    trials_6.addData('sound_26.started', sound_26.tStartRefresh)
    trials_6.addData('sound_26.stopped', sound_26.tStopRefresh)
    
    # ------Prepare to start Routine "reference_practice"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_27.setSound('Audio/850.0.wav', secs=1.0, hamming=True)
    sound_27.setVolume(1.0, log=False)
    sound_files = practice_array[cntr_practice]
    # keep track of which components have finished
    reference_practiceComponents = [polygon_27, sound_27]
    for thisComponent in reference_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reference_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reference_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = reference_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reference_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_27* updates
        if polygon_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_27.frameNStart = frameN  # exact frame index
            polygon_27.tStart = t  # local t and not account for scr refresh
            polygon_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_27, 'tStartRefresh')  # time at next scr refresh
            polygon_27.setAutoDraw(True)
        if polygon_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_27.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_27.tStop = t  # not accounting for scr refresh
                polygon_27.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_27, 'tStopRefresh')  # time at next scr refresh
                polygon_27.setAutoDraw(False)
        # start/stop sound_27
        if sound_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_27.frameNStart = frameN  # exact frame index
            sound_27.tStart = t  # local t and not account for scr refresh
            sound_27.tStartRefresh = tThisFlipGlobal  # on global time
            sound_27.play(when=win)  # sync with win flip
        if sound_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_27.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_27.tStop = t  # not accounting for scr refresh
                sound_27.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_27, 'tStopRefresh')  # time at next scr refresh
                sound_27.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reference_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reference_practice"-------
    for thisComponent in reference_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_6.addData('polygon_27.started', polygon_27.tStartRefresh)
    trials_6.addData('polygon_27.stopped', polygon_27.tStopRefresh)
    sound_27.stop()  # ensure sound has stopped at end of routine
    trials_6.addData('sound_27.started', sound_27.tStartRefresh)
    trials_6.addData('sound_27.stopped', sound_27.tStopRefresh)
    
    # ------Prepare to start Routine "comparison_practice"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_28.setSound(sound_files, secs=1.0, hamming=True)
    sound_28.setVolume(1.0, log=False)
    # keep track of which components have finished
    comparison_practiceComponents = [polygon_28, sound_28]
    for thisComponent in comparison_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    comparison_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "comparison_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = comparison_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=comparison_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_28* updates
        if polygon_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_28.frameNStart = frameN  # exact frame index
            polygon_28.tStart = t  # local t and not account for scr refresh
            polygon_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_28, 'tStartRefresh')  # time at next scr refresh
            polygon_28.setAutoDraw(True)
        if polygon_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_28.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_28.tStop = t  # not accounting for scr refresh
                polygon_28.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_28, 'tStopRefresh')  # time at next scr refresh
                polygon_28.setAutoDraw(False)
        # start/stop sound_28
        if sound_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_28.frameNStart = frameN  # exact frame index
            sound_28.tStart = t  # local t and not account for scr refresh
            sound_28.tStartRefresh = tThisFlipGlobal  # on global time
            sound_28.play(when=win)  # sync with win flip
        if sound_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_28.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_28.tStop = t  # not accounting for scr refresh
                sound_28.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_28, 'tStopRefresh')  # time at next scr refresh
                sound_28.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in comparison_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "comparison_practice"-------
    for thisComponent in comparison_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_6.addData('polygon_28.started', polygon_28.tStartRefresh)
    trials_6.addData('polygon_28.stopped', polygon_28.tStopRefresh)
    sound_28.stop()  # ensure sound has stopped at end of routine
    trials_6.addData('sound_28.started', sound_28.tStartRefresh)
    trials_6.addData('sound_28.stopped', sound_28.tStopRefresh)
    answers = practice_answers[cntr_practice]
    
    # ------Prepare to start Routine "End_tonepractice"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_29.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_29.setVolume(1.0, log=False)
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # keep track of which components have finished
    End_tonepracticeComponents = [polygon_29, sound_29, key_resp_10]
    for thisComponent in End_tonepracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_tonepracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_tonepractice"-------
    while continueRoutine:
        # get current time
        t = End_tonepracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_tonepracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_29* updates
        if polygon_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_29.frameNStart = frameN  # exact frame index
            polygon_29.tStart = t  # local t and not account for scr refresh
            polygon_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_29, 'tStartRefresh')  # time at next scr refresh
            polygon_29.setAutoDraw(True)
        # start/stop sound_29
        if sound_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_29.frameNStart = frameN  # exact frame index
            sound_29.tStart = t  # local t and not account for scr refresh
            sound_29.tStartRefresh = tThisFlipGlobal  # on global time
            sound_29.play(when=win)  # sync with win flip
        if sound_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_29.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_29.tStop = t  # not accounting for scr refresh
                sound_29.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_29, 'tStopRefresh')  # time at next scr refresh
                sound_29.stop()
        
        # *key_resp_10* updates
        waitOnFlip = False
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['lshift', 'rshift'], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                # was this correct?
                if (key_resp_10.keys == str(answers)) or (key_resp_10.keys == answers):
                    key_resp_10.corr = 1
                else:
                    key_resp_10.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_tonepracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_tonepractice"-------
    for thisComponent in End_tonepracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_6.addData('polygon_29.started', polygon_29.tStartRefresh)
    trials_6.addData('polygon_29.stopped', polygon_29.tStopRefresh)
    sound_29.stop()  # ensure sound has stopped at end of routine
    trials_6.addData('sound_29.started', sound_29.tStartRefresh)
    trials_6.addData('sound_29.stopped', sound_29.tStopRefresh)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
        # was no response the correct answer?!
        if str(answers).lower() == 'none':
           key_resp_10.corr = 1;  # correct non-response
        else:
           key_resp_10.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_6 (TrialHandler)
    trials_6.addData('key_resp_10.keys',key_resp_10.keys)
    trials_6.addData('key_resp_10.corr', key_resp_10.corr)
    if key_resp_10.keys != None:  # we had a response
        trials_6.addData('key_resp_10.rt', key_resp_10.rt)
    trials_6.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    trials_6.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    # the Routine "End_tonepractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback_practice"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    sound_30.setSound(sound, secs=1.0, hamming=True)
    sound_30.setVolume(1.0, log=False)
    if key_resp_10.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    
    # keep track of which components have finished
    feedback_practiceComponents = [polygon_30, sound_30]
    for thisComponent in feedback_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_30* updates
        if polygon_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_30.frameNStart = frameN  # exact frame index
            polygon_30.tStart = t  # local t and not account for scr refresh
            polygon_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_30, 'tStartRefresh')  # time at next scr refresh
            polygon_30.setAutoDraw(True)
        if polygon_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_30.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                polygon_30.tStop = t  # not accounting for scr refresh
                polygon_30.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_30, 'tStopRefresh')  # time at next scr refresh
                polygon_30.setAutoDraw(False)
        # start/stop sound_30
        if sound_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_30.frameNStart = frameN  # exact frame index
            sound_30.tStart = t  # local t and not account for scr refresh
            sound_30.tStartRefresh = tThisFlipGlobal  # on global time
            sound_30.play(when=win)  # sync with win flip
        if sound_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_30.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_30.tStop = t  # not accounting for scr refresh
                sound_30.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_30, 'tStopRefresh')  # time at next scr refresh
                sound_30.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_practice"-------
    for thisComponent in feedback_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_6.addData('polygon_30.started', polygon_30.tStartRefresh)
    trials_6.addData('polygon_30.stopped', polygon_30.tStopRefresh)
    sound_30.stop()  # ensure sound has stopped at end of routine
    trials_6.addData('sound_30.started', sound_30.tStartRefresh)
    trials_6.addData('sound_30.stopped', sound_30.tStopRefresh)
    cntr_practice+=1
    
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'trials_6'


# ------Prepare to start Routine "StartWelcome"-------
continueRoutine = True
# update component parameters for each repeat
text.setText('Welcome to the Pupillometry Experiment, thank you for taking your time to help us out today.\n\nPress Spacebar to continue\n')
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
StartWelcomeComponents = [text, key_resp_2]
for thisComponent in StartWelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartWelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartWelcome"-------
while continueRoutine:
    # get current time
    t = StartWelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartWelcomeClock)
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
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # was this correct?
            if (key_resp_2.keys == str("'space'")) or (key_resp_2.keys == "'space'"):
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
    for thisComponent in StartWelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartWelcome"-------
for thisComponent in StartWelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       key_resp_2.corr = 1;  # correct non-response
    else:
       key_resp_2.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
thisExp.addData('key_resp_2.corr', key_resp_2.corr)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "StartWelcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Pupil"-------
continueRoutine = True
# update component parameters for each repeat
if eyetracking == '1':    
    time_fn = core.monotonicClock.getTime
    name = expInfo['participant']
    rstring ='R '+ str(name) 
    pupil_remote.send_string(rstring)
    print(pupil_remote.recv_string())
    label = "start_of_experiment"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(0.25)
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
trials = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "Ready_tone"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_1.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_1.setVolume(1.0, log=False)
    wait_ready = np.random.choice(np.arange(2,7),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "Ready_Tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    Ready_toneComponents = [polygon, sound_1]
    for thisComponent in Ready_toneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Ready_toneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Ready_tone"-------
    while continueRoutine:
        # get current time
        t = Ready_toneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Ready_toneClock)
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
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + wait_ready-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
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
        for thisComponent in Ready_toneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready_tone"-------
    for thisComponent in Ready_toneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1.started', sound_1.tStartRefresh)
    trials.addData('sound_1.stopped', sound_1.tStopRefresh)
    # the Routine "Ready_tone" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reference_tone"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_2.setSound('Audio/850.0.wav', secs=1.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    time_fn = core.monotonicClock.getTime
    label = "Reference_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    reference_toneComponents = [polygon_3, sound_2]
    for thisComponent in reference_toneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reference_toneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reference_tone"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = reference_toneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reference_toneClock)
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
            if tThisFlipGlobal > polygon_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
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
        for thisComponent in reference_toneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reference_tone"-------
    for thisComponent in reference_toneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_3.started', polygon_3.tStartRefresh)
    trials.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    sound_files = stimulus_array1[cntr1]
    
    # ------Prepare to start Routine "comparison_tone"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_3.setSound(sound_files, secs=1.0, hamming=True)
    sound_3.setVolume(1.0, log=False)
    
    
    time_fn = core.monotonicClock.getTime
    label = "comparison_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    comparison_toneComponents = [polygon_4, sound_3]
    for thisComponent in comparison_toneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    comparison_toneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "comparison_tone"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = comparison_toneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=comparison_toneClock)
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in comparison_toneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "comparison_tone"-------
    for thisComponent in comparison_toneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_4.started', polygon_4.tStartRefresh)
    trials.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    sound_3.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_3.started', sound_3.tStartRefresh)
    trials.addData('sound_3.stopped', sound_3.tStopRefresh)
    answers = answer_array1[cntr1]
    cntr1+=1
    print(cntr1)
    
    
    # ------Prepare to start Routine "End_tone"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    sound_4.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_4.setVolume(1.0, log=False)
    
    
    time_fn = core.monotonicClock.getTime
    label = "Answe_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    End_toneComponents = [polygon_2, key_resp, sound_4]
    for thisComponent in End_toneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_toneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_tone"-------
    while continueRoutine:
        # get current time
        t = End_toneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_toneClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
            theseKeys = key_resp.getKeys(keyList=['lshift', 'rshift'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(answers)) or (key_resp.keys == answers):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_4
        if sound_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_4.frameNStart = frameN  # exact frame index
            sound_4.tStart = t  # local t and not account for scr refresh
            sound_4.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4.play(when=win)  # sync with win flip
        if sound_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_4.tStop = t  # not accounting for scr refresh
                sound_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
                sound_4.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_toneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_tone"-------
    for thisComponent in End_toneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(answers).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    sound_4.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_4.started', sound_4.tStartRefresh)
    trials.addData('sound_4.stopped', sound_4.tStopRefresh)
    # the Routine "End_tone" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if key_resp.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    next_wait = np.random.choice(np.arange(6,11),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "feedback_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    sound_5.setSound(sound, hamming=True)
    sound_5.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedback_2Components = [polygon_5, sound_5]
    for thisComponent in feedback_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback_2"-------
    while continueRoutine:
        # get current time
        t = feedback_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback_2Clock)
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
            if tThisFlipGlobal > polygon_5.tStartRefresh + next_wait-frameTolerance:
                # keep track of stop time/frame for later
                polygon_5.tStop = t  # not accounting for scr refresh
                polygon_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
                polygon_5.setAutoDraw(False)
        # start/stop sound_5
        if sound_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_5.frameNStart = frameN  # exact frame index
            sound_5.tStart = t  # local t and not account for scr refresh
            sound_5.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_2"-------
    for thisComponent in feedback_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_5.started', polygon_5.tStartRefresh)
    trials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
    sound_5.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_5.started', sound_5.tStartRefresh)
    trials.addData('sound_5.stopped', sound_5.tStopRefresh)
    # the Routine "feedback_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials'


# ------Prepare to start Routine "stop_pupil"-------
continueRoutine = True
# update component parameters for each repeat
time_fn = core.monotonicClock.getTime
pupil_remote.send_string('r')
print(pupil_remote.recv_string())
label = "End_of_Block"
duration = 0.
minimal_trigger = new_trigger(label, duration)
send_trigger(minimal_trigger)
sleep(1.)
# keep track of which components have finished
stop_pupilComponents = []
for thisComponent in stop_pupilComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stop_pupilClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stop_pupil"-------
while continueRoutine:
    # get current time
    t = stop_pupilClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stop_pupilClock)
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
    for thisComponent in stop_pupilComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stop_pupil"-------
for thisComponent in stop_pupilComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "stop_pupil" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EndBlock"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
EndBlockComponents = [text_2, key_resp_3]
for thisComponent in EndBlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndBlock"-------
while continueRoutine:
    # get current time
    t = EndBlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndBlockClock)
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
            # was this correct?
            if (key_resp_3.keys == str("'space'")) or (key_resp_3.keys == "'space'"):
                key_resp_3.corr = 1
            else:
                key_resp_3.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndBlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndBlock"-------
for thisComponent in EndBlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       key_resp_3.corr = 1;  # correct non-response
    else:
       key_resp_3.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
thisExp.addData('key_resp_3.corr', key_resp_3.corr)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndBlock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Pupil_2"-------
continueRoutine = True
# update component parameters for each repeat
if eyetracking == '1':    
    time_fn = core.monotonicClock.getTime
    name = expInfo['participant']
    rstring ='R '
    pupil_remote.send_string(rstring)
    print(pupil_remote.recv_string())
    label = "Begin Block2"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(0.25)
else:
    continueRoutine = False
# keep track of which components have finished
Pupil_2Components = []
for thisComponent in Pupil_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Pupil_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pupil_2"-------
while continueRoutine:
    # get current time
    t = Pupil_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Pupil_2Clock)
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
    for thisComponent in Pupil_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pupil_2"-------
for thisComponent in Pupil_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Pupil_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Ready_tone2_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    wait_ready = np.random.choice(np.arange(2,7),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "Ready_Tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    sound_6.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_6.setVolume(1.0, log=False)
    # keep track of which components have finished
    Ready_tone2_2Components = [polygon_6, sound_6]
    for thisComponent in Ready_tone2_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Ready_tone2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Ready_tone2_2"-------
    while continueRoutine:
        # get current time
        t = Ready_tone2_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Ready_tone2_2Clock)
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
        if polygon_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_6.tStartRefresh + wait_ready-frameTolerance:
                # keep track of stop time/frame for later
                polygon_6.tStop = t  # not accounting for scr refresh
                polygon_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
                polygon_6.setAutoDraw(False)
        # start/stop sound_6
        if sound_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.tStart = t  # local t and not account for scr refresh
            sound_6.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6.play(when=win)  # sync with win flip
        if sound_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_6.tStop = t  # not accounting for scr refresh
                sound_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_6, 'tStopRefresh')  # time at next scr refresh
                sound_6.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ready_tone2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready_tone2_2"-------
    for thisComponent in Ready_tone2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('polygon_6.started', polygon_6.tStartRefresh)
    trials_2.addData('polygon_6.stopped', polygon_6.tStopRefresh)
    sound_6.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('sound_6.started', sound_6.tStartRefresh)
    trials_2.addData('sound_6.stopped', sound_6.tStopRefresh)
    # the Routine "Ready_tone2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reference_tone2"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_7.setSound('Audio/850.0.wav', secs=1.0, hamming=True)
    sound_7.setVolume(1.0, log=False)
    time_fn = core.monotonicClock.getTime
    label = "Reference_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    reference_tone2Components = [polygon_7, sound_7]
    for thisComponent in reference_tone2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reference_tone2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reference_tone2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = reference_tone2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reference_tone2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_7* updates
        if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_7.frameNStart = frameN  # exact frame index
            polygon_7.tStart = t  # local t and not account for scr refresh
            polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
            polygon_7.setAutoDraw(True)
        if polygon_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_7.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_7.tStop = t  # not accounting for scr refresh
                polygon_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_7, 'tStopRefresh')  # time at next scr refresh
                polygon_7.setAutoDraw(False)
        # start/stop sound_7
        if sound_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.tStart = t  # local t and not account for scr refresh
            sound_7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7.play(when=win)  # sync with win flip
        if sound_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_7.tStop = t  # not accounting for scr refresh
                sound_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
                sound_7.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reference_tone2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reference_tone2"-------
    for thisComponent in reference_tone2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('polygon_7.started', polygon_7.tStartRefresh)
    trials_2.addData('polygon_7.stopped', polygon_7.tStopRefresh)
    sound_7.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('sound_7.started', sound_7.tStartRefresh)
    trials_2.addData('sound_7.stopped', sound_7.tStopRefresh)
    sound_files = stimulus_array2[cntr2]
    
    # ------Prepare to start Routine "comparison_tone2"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_8.setSound(sound_files, secs=1.0, hamming=True)
    sound_8.setVolume(1.0, log=False)
    
    time_fn = core.monotonicClock.getTime
    label = "comparison_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    comparison_tone2Components = [polygon_8, sound_8]
    for thisComponent in comparison_tone2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    comparison_tone2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "comparison_tone2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = comparison_tone2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=comparison_tone2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_8* updates
        if polygon_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_8.frameNStart = frameN  # exact frame index
            polygon_8.tStart = t  # local t and not account for scr refresh
            polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
            polygon_8.setAutoDraw(True)
        if polygon_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_8.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_8.tStop = t  # not accounting for scr refresh
                polygon_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_8, 'tStopRefresh')  # time at next scr refresh
                polygon_8.setAutoDraw(False)
        # start/stop sound_8
        if sound_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.tStart = t  # local t and not account for scr refresh
            sound_8.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8.play(when=win)  # sync with win flip
        if sound_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_8.tStop = t  # not accounting for scr refresh
                sound_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                sound_8.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in comparison_tone2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "comparison_tone2"-------
    for thisComponent in comparison_tone2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('polygon_8.started', polygon_8.tStartRefresh)
    trials_2.addData('polygon_8.stopped', polygon_8.tStopRefresh)
    sound_8.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('sound_8.started', sound_8.tStartRefresh)
    trials_2.addData('sound_8.stopped', sound_8.tStopRefresh)
    answers = answer_array2[cntr2]
    cntr2+=1
    print(cntr2)
    
    
    # ------Prepare to start Routine "End_tone2_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    sound_9.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_9.setVolume(1.0, log=False)
    
    
    time_fn = core.monotonicClock.getTime
    label = "Answe_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    End_tone2_2Components = [polygon_9, key_resp_4, sound_9]
    for thisComponent in End_tone2_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_tone2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_tone2_2"-------
    while continueRoutine:
        # get current time
        t = End_tone2_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_tone2_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_9* updates
        if polygon_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_9.frameNStart = frameN  # exact frame index
            polygon_9.tStart = t  # local t and not account for scr refresh
            polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
            polygon_9.setAutoDraw(True)
        
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
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['lshift', 'rshift'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # was this correct?
                if (key_resp_4.keys == str(answers)) or (key_resp_4.keys == answers):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_9
        if sound_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.tStart = t  # local t and not account for scr refresh
            sound_9.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9.play(when=win)  # sync with win flip
        if sound_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_9.tStop = t  # not accounting for scr refresh
                sound_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9, 'tStopRefresh')  # time at next scr refresh
                sound_9.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_tone2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_tone2_2"-------
    for thisComponent in End_tone2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('polygon_9.started', polygon_9.tStartRefresh)
    trials_2.addData('polygon_9.stopped', polygon_9.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str(answers).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_4.keys',key_resp_4.keys)
    trials_2.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials_2.addData('key_resp_4.rt', key_resp_4.rt)
    trials_2.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials_2.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    sound_9.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('sound_9.started', sound_9.tStartRefresh)
    trials_2.addData('sound_9.stopped', sound_9.tStopRefresh)
    # the Routine "End_tone2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback2_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_24.setSound(sound, hamming=True)
    sound_24.setVolume(1.0, log=False)
    if key_resp_4.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    next_wait = np.random.choice(np.arange(6,11),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "feedback_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    feedback2_2Components = [polygon_24, sound_24]
    for thisComponent in feedback2_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback2_2"-------
    while continueRoutine:
        # get current time
        t = feedback2_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback2_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_24* updates
        if polygon_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_24.frameNStart = frameN  # exact frame index
            polygon_24.tStart = t  # local t and not account for scr refresh
            polygon_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_24, 'tStartRefresh')  # time at next scr refresh
            polygon_24.setAutoDraw(True)
        if polygon_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_24.tStartRefresh + next_wait-frameTolerance:
                # keep track of stop time/frame for later
                polygon_24.tStop = t  # not accounting for scr refresh
                polygon_24.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_24, 'tStopRefresh')  # time at next scr refresh
                polygon_24.setAutoDraw(False)
        # start/stop sound_24
        if sound_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_24.frameNStart = frameN  # exact frame index
            sound_24.tStart = t  # local t and not account for scr refresh
            sound_24.tStartRefresh = tThisFlipGlobal  # on global time
            sound_24.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback2_2"-------
    for thisComponent in feedback2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('polygon_24.started', polygon_24.tStartRefresh)
    trials_2.addData('polygon_24.stopped', polygon_24.tStopRefresh)
    sound_24.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('sound_24.started', sound_24.tStartRefresh)
    trials_2.addData('sound_24.stopped', sound_24.tStopRefresh)
    # the Routine "feedback2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_2'


# ------Prepare to start Routine "stop_pupil"-------
continueRoutine = True
# update component parameters for each repeat
time_fn = core.monotonicClock.getTime
pupil_remote.send_string('r')
print(pupil_remote.recv_string())
label = "End_of_Block"
duration = 0.
minimal_trigger = new_trigger(label, duration)
send_trigger(minimal_trigger)
sleep(1.)
# keep track of which components have finished
stop_pupilComponents = []
for thisComponent in stop_pupilComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stop_pupilClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stop_pupil"-------
while continueRoutine:
    # get current time
    t = stop_pupilClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stop_pupilClock)
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
    for thisComponent in stop_pupilComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stop_pupil"-------
for thisComponent in stop_pupilComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "stop_pupil" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EndBlock"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
EndBlockComponents = [text_2, key_resp_3]
for thisComponent in EndBlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndBlock"-------
while continueRoutine:
    # get current time
    t = EndBlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndBlockClock)
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
            # was this correct?
            if (key_resp_3.keys == str("'space'")) or (key_resp_3.keys == "'space'"):
                key_resp_3.corr = 1
            else:
                key_resp_3.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndBlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndBlock"-------
for thisComponent in EndBlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       key_resp_3.corr = 1;  # correct non-response
    else:
       key_resp_3.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
thisExp.addData('key_resp_3.corr', key_resp_3.corr)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndBlock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Pupil_3"-------
continueRoutine = True
# update component parameters for each repeat
if eyetracking == '1':    
    time_fn = core.monotonicClock.getTime
    name = expInfo['participant']
    rstring ='R '+ str(name) 
    pupil_remote.send_string(rstring)
    print(pupil_remote.recv_string())
    label = "start_of_experiment"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(0.25)
else:
    continueRoutine = False
# keep track of which components have finished
Pupil_3Components = []
for thisComponent in Pupil_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Pupil_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pupil_3"-------
while continueRoutine:
    # get current time
    t = Pupil_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Pupil_3Clock)
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
    for thisComponent in Pupil_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pupil_3"-------
for thisComponent in Pupil_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Pupil_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Ready_tone3"-------
    continueRoutine = True
    # update component parameters for each repeat
    wait_ready = np.random.choice(np.arange(2,7),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "Ready_Tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    sound_10.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_10.setVolume(1.0, log=False)
    # keep track of which components have finished
    Ready_tone3Components = [polygon_10, sound_10]
    for thisComponent in Ready_tone3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Ready_tone3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Ready_tone3"-------
    while continueRoutine:
        # get current time
        t = Ready_tone3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Ready_tone3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_10* updates
        if polygon_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_10.frameNStart = frameN  # exact frame index
            polygon_10.tStart = t  # local t and not account for scr refresh
            polygon_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_10, 'tStartRefresh')  # time at next scr refresh
            polygon_10.setAutoDraw(True)
        if polygon_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_10.tStartRefresh + wait_ready-frameTolerance:
                # keep track of stop time/frame for later
                polygon_10.tStop = t  # not accounting for scr refresh
                polygon_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_10, 'tStopRefresh')  # time at next scr refresh
                polygon_10.setAutoDraw(False)
        # start/stop sound_10
        if sound_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_10.frameNStart = frameN  # exact frame index
            sound_10.tStart = t  # local t and not account for scr refresh
            sound_10.tStartRefresh = tThisFlipGlobal  # on global time
            sound_10.play(when=win)  # sync with win flip
        if sound_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_10.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_10.tStop = t  # not accounting for scr refresh
                sound_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_10, 'tStopRefresh')  # time at next scr refresh
                sound_10.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ready_tone3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready_tone3"-------
    for thisComponent in Ready_tone3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('polygon_10.started', polygon_10.tStartRefresh)
    trials_3.addData('polygon_10.stopped', polygon_10.tStopRefresh)
    sound_10.stop()  # ensure sound has stopped at end of routine
    trials_3.addData('sound_10.started', sound_10.tStartRefresh)
    trials_3.addData('sound_10.stopped', sound_10.tStopRefresh)
    # the Routine "Ready_tone3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reference_tone3"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_11.setSound('Audio/850.0.wav', secs=1.0, hamming=True)
    sound_11.setVolume(1.0, log=False)
    time_fn = core.monotonicClock.getTime
    label = "Reference_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    reference_tone3Components = [polygon_11, sound_11]
    for thisComponent in reference_tone3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reference_tone3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reference_tone3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = reference_tone3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reference_tone3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_11* updates
        if polygon_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_11.frameNStart = frameN  # exact frame index
            polygon_11.tStart = t  # local t and not account for scr refresh
            polygon_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_11, 'tStartRefresh')  # time at next scr refresh
            polygon_11.setAutoDraw(True)
        if polygon_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_11.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_11.tStop = t  # not accounting for scr refresh
                polygon_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_11, 'tStopRefresh')  # time at next scr refresh
                polygon_11.setAutoDraw(False)
        # start/stop sound_11
        if sound_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.tStart = t  # local t and not account for scr refresh
            sound_11.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11.play(when=win)  # sync with win flip
        if sound_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_11.tStop = t  # not accounting for scr refresh
                sound_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11, 'tStopRefresh')  # time at next scr refresh
                sound_11.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reference_tone3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reference_tone3"-------
    for thisComponent in reference_tone3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('polygon_11.started', polygon_11.tStartRefresh)
    trials_3.addData('polygon_11.stopped', polygon_11.tStopRefresh)
    sound_11.stop()  # ensure sound has stopped at end of routine
    trials_3.addData('sound_11.started', sound_11.tStartRefresh)
    trials_3.addData('sound_11.stopped', sound_11.tStopRefresh)
    sound_files = stimulus_array3[cntr3]
    
    # ------Prepare to start Routine "comparison_tone3"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_12.setSound(sound_files, secs=1.0, hamming=True)
    sound_12.setVolume(1.0, log=False)
    time_fn = core.monotonicClock.getTime
    label = "comparison_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    comparison_tone3Components = [polygon_12, sound_12]
    for thisComponent in comparison_tone3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    comparison_tone3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "comparison_tone3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = comparison_tone3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=comparison_tone3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_12* updates
        if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_12.frameNStart = frameN  # exact frame index
            polygon_12.tStart = t  # local t and not account for scr refresh
            polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
            polygon_12.setAutoDraw(True)
        if polygon_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_12.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_12.tStop = t  # not accounting for scr refresh
                polygon_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_12, 'tStopRefresh')  # time at next scr refresh
                polygon_12.setAutoDraw(False)
        # start/stop sound_12
        if sound_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_12.frameNStart = frameN  # exact frame index
            sound_12.tStart = t  # local t and not account for scr refresh
            sound_12.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12.play(when=win)  # sync with win flip
        if sound_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_12.tStop = t  # not accounting for scr refresh
                sound_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12, 'tStopRefresh')  # time at next scr refresh
                sound_12.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in comparison_tone3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "comparison_tone3"-------
    for thisComponent in comparison_tone3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('polygon_12.started', polygon_12.tStartRefresh)
    trials_3.addData('polygon_12.stopped', polygon_12.tStopRefresh)
    sound_12.stop()  # ensure sound has stopped at end of routine
    trials_3.addData('sound_12.started', sound_12.tStartRefresh)
    trials_3.addData('sound_12.stopped', sound_12.tStopRefresh)
    answers = answer_array3[cntr3]
    cntr3+=1
    print(cntr3)
    
    # ------Prepare to start Routine "End_tone3"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    time_fn = core.monotonicClock.getTime
    label = "Answe_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    sound_13.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_13.setVolume(1.0, log=False)
    # keep track of which components have finished
    End_tone3Components = [polygon_13, key_resp_5, sound_13]
    for thisComponent in End_tone3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_tone3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_tone3"-------
    while continueRoutine:
        # get current time
        t = End_tone3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_tone3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_13* updates
        if polygon_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_13.frameNStart = frameN  # exact frame index
            polygon_13.tStart = t  # local t and not account for scr refresh
            polygon_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
            polygon_13.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['lshift', 'rshift'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # was this correct?
                if (key_resp_5.keys == str(answers)) or (key_resp_5.keys == answers):
                    key_resp_5.corr = 1
                else:
                    key_resp_5.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_13
        if sound_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_13.frameNStart = frameN  # exact frame index
            sound_13.tStart = t  # local t and not account for scr refresh
            sound_13.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13.play(when=win)  # sync with win flip
        if sound_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_13.tStop = t  # not accounting for scr refresh
                sound_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13, 'tStopRefresh')  # time at next scr refresh
                sound_13.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_tone3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_tone3"-------
    for thisComponent in End_tone3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('polygon_13.started', polygon_13.tStartRefresh)
    trials_3.addData('polygon_13.stopped', polygon_13.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
        # was no response the correct answer?!
        if str(answers).lower() == 'none':
           key_resp_5.corr = 1;  # correct non-response
        else:
           key_resp_5.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_5.keys',key_resp_5.keys)
    trials_3.addData('key_resp_5.corr', key_resp_5.corr)
    if key_resp_5.keys != None:  # we had a response
        trials_3.addData('key_resp_5.rt', key_resp_5.rt)
    trials_3.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials_3.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    sound_13.stop()  # ensure sound has stopped at end of routine
    trials_3.addData('sound_13.started', sound_13.tStartRefresh)
    trials_3.addData('sound_13.stopped', sound_13.tStopRefresh)
    # the Routine "End_tone3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_25.setSound(sound, hamming=True)
    sound_25.setVolume(1.0, log=False)
    if key_resp_5.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    next_wait = np.random.choice(np.arange(6,11),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "feedback_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    feedback_3Components = [polygon_25, sound_25]
    for thisComponent in feedback_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback_3"-------
    while continueRoutine:
        # get current time
        t = feedback_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_25* updates
        if polygon_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_25.frameNStart = frameN  # exact frame index
            polygon_25.tStart = t  # local t and not account for scr refresh
            polygon_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_25, 'tStartRefresh')  # time at next scr refresh
            polygon_25.setAutoDraw(True)
        if polygon_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_25.tStartRefresh + next_wait-frameTolerance:
                # keep track of stop time/frame for later
                polygon_25.tStop = t  # not accounting for scr refresh
                polygon_25.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_25, 'tStopRefresh')  # time at next scr refresh
                polygon_25.setAutoDraw(False)
        # start/stop sound_25
        if sound_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_25.frameNStart = frameN  # exact frame index
            sound_25.tStart = t  # local t and not account for scr refresh
            sound_25.tStartRefresh = tThisFlipGlobal  # on global time
            sound_25.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_3"-------
    for thisComponent in feedback_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('polygon_25.started', polygon_25.tStartRefresh)
    trials_3.addData('polygon_25.stopped', polygon_25.tStopRefresh)
    sound_25.stop()  # ensure sound has stopped at end of routine
    trials_3.addData('sound_25.started', sound_25.tStartRefresh)
    trials_3.addData('sound_25.stopped', sound_25.tStopRefresh)
    # the Routine "feedback_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_3'


# ------Prepare to start Routine "stop_pupil"-------
continueRoutine = True
# update component parameters for each repeat
time_fn = core.monotonicClock.getTime
pupil_remote.send_string('r')
print(pupil_remote.recv_string())
label = "End_of_Block"
duration = 0.
minimal_trigger = new_trigger(label, duration)
send_trigger(minimal_trigger)
sleep(1.)
# keep track of which components have finished
stop_pupilComponents = []
for thisComponent in stop_pupilComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stop_pupilClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stop_pupil"-------
while continueRoutine:
    # get current time
    t = stop_pupilClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stop_pupilClock)
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
    for thisComponent in stop_pupilComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stop_pupil"-------
for thisComponent in stop_pupilComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "stop_pupil" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EndBlock"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
EndBlockComponents = [text_2, key_resp_3]
for thisComponent in EndBlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndBlock"-------
while continueRoutine:
    # get current time
    t = EndBlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndBlockClock)
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
            # was this correct?
            if (key_resp_3.keys == str("'space'")) or (key_resp_3.keys == "'space'"):
                key_resp_3.corr = 1
            else:
                key_resp_3.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndBlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndBlock"-------
for thisComponent in EndBlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       key_resp_3.corr = 1;  # correct non-response
    else:
       key_resp_3.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
thisExp.addData('key_resp_3.corr', key_resp_3.corr)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndBlock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Ready_Tone4"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_14.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_14.setVolume(1.0, log=False)
    wait_ready = np.random.choice(np.arange(2,7),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "Ready_Tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    Ready_Tone4Components = [polygon_14, sound_14]
    for thisComponent in Ready_Tone4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Ready_Tone4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Ready_Tone4"-------
    while continueRoutine:
        # get current time
        t = Ready_Tone4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Ready_Tone4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_14* updates
        if polygon_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_14.frameNStart = frameN  # exact frame index
            polygon_14.tStart = t  # local t and not account for scr refresh
            polygon_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_14, 'tStartRefresh')  # time at next scr refresh
            polygon_14.setAutoDraw(True)
        if polygon_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_14.tStartRefresh + wait_ready-frameTolerance:
                # keep track of stop time/frame for later
                polygon_14.tStop = t  # not accounting for scr refresh
                polygon_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_14, 'tStopRefresh')  # time at next scr refresh
                polygon_14.setAutoDraw(False)
        # start/stop sound_14
        if sound_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_14.frameNStart = frameN  # exact frame index
            sound_14.tStart = t  # local t and not account for scr refresh
            sound_14.tStartRefresh = tThisFlipGlobal  # on global time
            sound_14.play(when=win)  # sync with win flip
        if sound_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_14.tStop = t  # not accounting for scr refresh
                sound_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_14, 'tStopRefresh')  # time at next scr refresh
                sound_14.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ready_Tone4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready_Tone4"-------
    for thisComponent in Ready_Tone4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('polygon_14.started', polygon_14.tStartRefresh)
    trials_4.addData('polygon_14.stopped', polygon_14.tStopRefresh)
    sound_14.stop()  # ensure sound has stopped at end of routine
    trials_4.addData('sound_14.started', sound_14.tStartRefresh)
    trials_4.addData('sound_14.stopped', sound_14.tStopRefresh)
    # the Routine "Ready_Tone4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Reference_tone4"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_15.setSound('Audio/850.0.wav', secs=1.0, hamming=True)
    sound_15.setVolume(1.0, log=False)
    time_fn = core.monotonicClock.getTime
    label = "Reference_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    Reference_tone4Components = [polygon_15, sound_15]
    for thisComponent in Reference_tone4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Reference_tone4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Reference_tone4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Reference_tone4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Reference_tone4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_15* updates
        if polygon_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_15.frameNStart = frameN  # exact frame index
            polygon_15.tStart = t  # local t and not account for scr refresh
            polygon_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_15, 'tStartRefresh')  # time at next scr refresh
            polygon_15.setAutoDraw(True)
        if polygon_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_15.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_15.tStop = t  # not accounting for scr refresh
                polygon_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_15, 'tStopRefresh')  # time at next scr refresh
                polygon_15.setAutoDraw(False)
        # start/stop sound_15
        if sound_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_15.frameNStart = frameN  # exact frame index
            sound_15.tStart = t  # local t and not account for scr refresh
            sound_15.tStartRefresh = tThisFlipGlobal  # on global time
            sound_15.play(when=win)  # sync with win flip
        if sound_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_15.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_15.tStop = t  # not accounting for scr refresh
                sound_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_15, 'tStopRefresh')  # time at next scr refresh
                sound_15.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Reference_tone4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Reference_tone4"-------
    for thisComponent in Reference_tone4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('polygon_15.started', polygon_15.tStartRefresh)
    trials_4.addData('polygon_15.stopped', polygon_15.tStopRefresh)
    sound_15.stop()  # ensure sound has stopped at end of routine
    trials_4.addData('sound_15.started', sound_15.tStartRefresh)
    trials_4.addData('sound_15.stopped', sound_15.tStopRefresh)
    sound_files = stimulus_array4[cntr4]
    
    # ------Prepare to start Routine "comparison_tone4"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_16.setSound(sound_files, secs=1.0, hamming=True)
    sound_16.setVolume(1.0, log=False)
    time_fn = core.monotonicClock.getTime
    label = "comparison_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    comparison_tone4Components = [polygon_16, sound_16]
    for thisComponent in comparison_tone4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    comparison_tone4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "comparison_tone4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = comparison_tone4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=comparison_tone4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_16* updates
        if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_16.frameNStart = frameN  # exact frame index
            polygon_16.tStart = t  # local t and not account for scr refresh
            polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
            polygon_16.setAutoDraw(True)
        if polygon_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_16.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_16.tStop = t  # not accounting for scr refresh
                polygon_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_16, 'tStopRefresh')  # time at next scr refresh
                polygon_16.setAutoDraw(False)
        # start/stop sound_16
        if sound_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_16.frameNStart = frameN  # exact frame index
            sound_16.tStart = t  # local t and not account for scr refresh
            sound_16.tStartRefresh = tThisFlipGlobal  # on global time
            sound_16.play(when=win)  # sync with win flip
        if sound_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_16.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_16.tStop = t  # not accounting for scr refresh
                sound_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_16, 'tStopRefresh')  # time at next scr refresh
                sound_16.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in comparison_tone4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "comparison_tone4"-------
    for thisComponent in comparison_tone4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('polygon_16.started', polygon_16.tStartRefresh)
    trials_4.addData('polygon_16.stopped', polygon_16.tStopRefresh)
    sound_16.stop()  # ensure sound has stopped at end of routine
    trials_4.addData('sound_16.started', sound_16.tStartRefresh)
    trials_4.addData('sound_16.stopped', sound_16.tStopRefresh)
    answers = answer_array4[cntr4]
    cntr4+=1
    print(cntr4)
    
    # ------Prepare to start Routine "End_tone4"-------
    continueRoutine = True
    # update component parameters for each repeat
    time_fn = core.monotonicClock.getTime
    label = "Answe_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    sound_17.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_17.setVolume(1.0, log=False)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    End_tone4Components = [sound_17, polygon_17, key_resp_6]
    for thisComponent in End_tone4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_tone4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_tone4"-------
    while continueRoutine:
        # get current time
        t = End_tone4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_tone4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_17
        if sound_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_17.frameNStart = frameN  # exact frame index
            sound_17.tStart = t  # local t and not account for scr refresh
            sound_17.tStartRefresh = tThisFlipGlobal  # on global time
            sound_17.play(when=win)  # sync with win flip
        if sound_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_17.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_17.tStop = t  # not accounting for scr refresh
                sound_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_17, 'tStopRefresh')  # time at next scr refresh
                sound_17.stop()
        
        # *polygon_17* updates
        if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_17.frameNStart = frameN  # exact frame index
            polygon_17.tStart = t  # local t and not account for scr refresh
            polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
            polygon_17.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['lshift', 'rshift'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # was this correct?
                if (key_resp_6.keys == str(answers)) or (key_resp_6.keys == answers):
                    key_resp_6.corr = 1
                else:
                    key_resp_6.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_tone4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_tone4"-------
    for thisComponent in End_tone4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_17.stop()  # ensure sound has stopped at end of routine
    trials_4.addData('sound_17.started', sound_17.tStartRefresh)
    trials_4.addData('sound_17.stopped', sound_17.tStopRefresh)
    trials_4.addData('polygon_17.started', polygon_17.tStartRefresh)
    trials_4.addData('polygon_17.stopped', polygon_17.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
        # was no response the correct answer?!
        if str(answers).lower() == 'none':
           key_resp_6.corr = 1;  # correct non-response
        else:
           key_resp_6.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('key_resp_6.keys',key_resp_6.keys)
    trials_4.addData('key_resp_6.corr', key_resp_6.corr)
    if key_resp_6.keys != None:  # we had a response
        trials_4.addData('key_resp_6.rt', key_resp_6.rt)
    trials_4.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    trials_4.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "End_tone4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback_4"-------
    continueRoutine = True
    # update component parameters for each repeat
    if key_resp_6.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    next_wait = np.random.choice(np.arange(6,11),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "feedback_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    sound_18.setSound(sound, secs=1.0, hamming=True)
    sound_18.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedback_4Components = [polygon_18, sound_18]
    for thisComponent in feedback_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback_4"-------
    while continueRoutine:
        # get current time
        t = feedback_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_18* updates
        if polygon_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_18.frameNStart = frameN  # exact frame index
            polygon_18.tStart = t  # local t and not account for scr refresh
            polygon_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_18, 'tStartRefresh')  # time at next scr refresh
            polygon_18.setAutoDraw(True)
        if polygon_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_18.tStartRefresh + next_wait-frameTolerance:
                # keep track of stop time/frame for later
                polygon_18.tStop = t  # not accounting for scr refresh
                polygon_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_18, 'tStopRefresh')  # time at next scr refresh
                polygon_18.setAutoDraw(False)
        # start/stop sound_18
        if sound_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_18.frameNStart = frameN  # exact frame index
            sound_18.tStart = t  # local t and not account for scr refresh
            sound_18.tStartRefresh = tThisFlipGlobal  # on global time
            sound_18.play(when=win)  # sync with win flip
        if sound_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_18.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_18.tStop = t  # not accounting for scr refresh
                sound_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_18, 'tStopRefresh')  # time at next scr refresh
                sound_18.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_4"-------
    for thisComponent in feedback_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('polygon_18.started', polygon_18.tStartRefresh)
    trials_4.addData('polygon_18.stopped', polygon_18.tStopRefresh)
    sound_18.stop()  # ensure sound has stopped at end of routine
    trials_4.addData('sound_18.started', sound_18.tStartRefresh)
    trials_4.addData('sound_18.stopped', sound_18.tStopRefresh)
    # the Routine "feedback_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_4'


# ------Prepare to start Routine "stop_pupil"-------
continueRoutine = True
# update component parameters for each repeat
time_fn = core.monotonicClock.getTime
pupil_remote.send_string('r')
print(pupil_remote.recv_string())
label = "End_of_Block"
duration = 0.
minimal_trigger = new_trigger(label, duration)
send_trigger(minimal_trigger)
sleep(1.)
# keep track of which components have finished
stop_pupilComponents = []
for thisComponent in stop_pupilComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stop_pupilClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stop_pupil"-------
while continueRoutine:
    # get current time
    t = stop_pupilClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stop_pupilClock)
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
    for thisComponent in stop_pupilComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stop_pupil"-------
for thisComponent in stop_pupilComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "stop_pupil" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EndBlock"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
EndBlockComponents = [text_2, key_resp_3]
for thisComponent in EndBlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndBlock"-------
while continueRoutine:
    # get current time
    t = EndBlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndBlockClock)
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
            # was this correct?
            if (key_resp_3.keys == str("'space'")) or (key_resp_3.keys == "'space'"):
                key_resp_3.corr = 1
            else:
                key_resp_3.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndBlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndBlock"-------
for thisComponent in EndBlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       key_resp_3.corr = 1;  # correct non-response
    else:
       key_resp_3.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
thisExp.addData('key_resp_3.corr', key_resp_3.corr)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndBlock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Ready_tone5"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_19.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_19.setVolume(1.0, log=False)
    wait_ready = np.random.choice(np.arange(2,7),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "Ready_Tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    Ready_tone5Components = [polygon_19, sound_19]
    for thisComponent in Ready_tone5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Ready_tone5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Ready_tone5"-------
    while continueRoutine:
        # get current time
        t = Ready_tone5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Ready_tone5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_19* updates
        if polygon_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_19.frameNStart = frameN  # exact frame index
            polygon_19.tStart = t  # local t and not account for scr refresh
            polygon_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_19, 'tStartRefresh')  # time at next scr refresh
            polygon_19.setAutoDraw(True)
        if polygon_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_19.tStartRefresh + wait_ready-frameTolerance:
                # keep track of stop time/frame for later
                polygon_19.tStop = t  # not accounting for scr refresh
                polygon_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_19, 'tStopRefresh')  # time at next scr refresh
                polygon_19.setAutoDraw(False)
        # start/stop sound_19
        if sound_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_19.frameNStart = frameN  # exact frame index
            sound_19.tStart = t  # local t and not account for scr refresh
            sound_19.tStartRefresh = tThisFlipGlobal  # on global time
            sound_19.play(when=win)  # sync with win flip
        if sound_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_19.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_19.tStop = t  # not accounting for scr refresh
                sound_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_19, 'tStopRefresh')  # time at next scr refresh
                sound_19.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ready_tone5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready_tone5"-------
    for thisComponent in Ready_tone5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('polygon_19.started', polygon_19.tStartRefresh)
    trials_5.addData('polygon_19.stopped', polygon_19.tStopRefresh)
    sound_19.stop()  # ensure sound has stopped at end of routine
    trials_5.addData('sound_19.started', sound_19.tStartRefresh)
    trials_5.addData('sound_19.stopped', sound_19.tStopRefresh)
    # the Routine "Ready_tone5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reference_tone5"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_20.setSound('Audio/850.0.wav', secs=1.0, hamming=True)
    sound_20.setVolume(1.0, log=False)
    time_fn = core.monotonicClock.getTime
    label = "Reference_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    reference_tone5Components = [polygon_20, sound_20]
    for thisComponent in reference_tone5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reference_tone5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reference_tone5"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = reference_tone5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reference_tone5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_20* updates
        if polygon_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_20.frameNStart = frameN  # exact frame index
            polygon_20.tStart = t  # local t and not account for scr refresh
            polygon_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_20, 'tStartRefresh')  # time at next scr refresh
            polygon_20.setAutoDraw(True)
        if polygon_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_20.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_20.tStop = t  # not accounting for scr refresh
                polygon_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_20, 'tStopRefresh')  # time at next scr refresh
                polygon_20.setAutoDraw(False)
        # start/stop sound_20
        if sound_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_20.frameNStart = frameN  # exact frame index
            sound_20.tStart = t  # local t and not account for scr refresh
            sound_20.tStartRefresh = tThisFlipGlobal  # on global time
            sound_20.play(when=win)  # sync with win flip
        if sound_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_20.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_20.tStop = t  # not accounting for scr refresh
                sound_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_20, 'tStopRefresh')  # time at next scr refresh
                sound_20.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reference_tone5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reference_tone5"-------
    for thisComponent in reference_tone5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('polygon_20.started', polygon_20.tStartRefresh)
    trials_5.addData('polygon_20.stopped', polygon_20.tStopRefresh)
    sound_20.stop()  # ensure sound has stopped at end of routine
    trials_5.addData('sound_20.started', sound_20.tStartRefresh)
    trials_5.addData('sound_20.stopped', sound_20.tStopRefresh)
    sound_files = stimulus_array5[cntr5]
    
    # ------Prepare to start Routine "comparison_tone5"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_21.setSound(sound_files, secs=1.0, hamming=True)
    sound_21.setVolume(1.0, log=False)
    time_fn = core.monotonicClock.getTime
    label = "comparison_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    # keep track of which components have finished
    comparison_tone5Components = [polygon_21, sound_21]
    for thisComponent in comparison_tone5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    comparison_tone5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "comparison_tone5"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = comparison_tone5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=comparison_tone5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_21* updates
        if polygon_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_21.frameNStart = frameN  # exact frame index
            polygon_21.tStart = t  # local t and not account for scr refresh
            polygon_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_21, 'tStartRefresh')  # time at next scr refresh
            polygon_21.setAutoDraw(True)
        if polygon_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_21.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_21.tStop = t  # not accounting for scr refresh
                polygon_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_21, 'tStopRefresh')  # time at next scr refresh
                polygon_21.setAutoDraw(False)
        # start/stop sound_21
        if sound_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_21.frameNStart = frameN  # exact frame index
            sound_21.tStart = t  # local t and not account for scr refresh
            sound_21.tStartRefresh = tThisFlipGlobal  # on global time
            sound_21.play(when=win)  # sync with win flip
        if sound_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_21.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_21.tStop = t  # not accounting for scr refresh
                sound_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_21, 'tStopRefresh')  # time at next scr refresh
                sound_21.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in comparison_tone5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "comparison_tone5"-------
    for thisComponent in comparison_tone5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('polygon_21.started', polygon_21.tStartRefresh)
    trials_5.addData('polygon_21.stopped', polygon_21.tStopRefresh)
    sound_21.stop()  # ensure sound has stopped at end of routine
    trials_5.addData('sound_21.started', sound_21.tStartRefresh)
    trials_5.addData('sound_21.stopped', sound_21.tStopRefresh)
    answers = answer_array5[cntr5]
    cntr5+=1
    print(cntr5)
    
    # ------Prepare to start Routine "End_tone5"-------
    continueRoutine = True
    # update component parameters for each repeat
    time_fn = core.monotonicClock.getTime
    label = "Answe_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    sound_22.setSound('Audio/650.wav', secs=1.0, hamming=True)
    sound_22.setVolume(1.0, log=False)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    End_tone5Components = [polygon_22, sound_22, key_resp_7]
    for thisComponent in End_tone5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_tone5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_tone5"-------
    while continueRoutine:
        # get current time
        t = End_tone5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_tone5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_22* updates
        if polygon_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_22.frameNStart = frameN  # exact frame index
            polygon_22.tStart = t  # local t and not account for scr refresh
            polygon_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_22, 'tStartRefresh')  # time at next scr refresh
            polygon_22.setAutoDraw(True)
        # start/stop sound_22
        if sound_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_22.frameNStart = frameN  # exact frame index
            sound_22.tStart = t  # local t and not account for scr refresh
            sound_22.tStartRefresh = tThisFlipGlobal  # on global time
            sound_22.play(when=win)  # sync with win flip
        if sound_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_22.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_22.tStop = t  # not accounting for scr refresh
                sound_22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_22, 'tStopRefresh')  # time at next scr refresh
                sound_22.stop()
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['lshift', 'rshift'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # was this correct?
                if (key_resp_7.keys == str(answers)) or (key_resp_7.keys == answers):
                    key_resp_7.corr = 1
                else:
                    key_resp_7.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_tone5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_tone5"-------
    for thisComponent in End_tone5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('polygon_22.started', polygon_22.tStartRefresh)
    trials_5.addData('polygon_22.stopped', polygon_22.tStopRefresh)
    sound_22.stop()  # ensure sound has stopped at end of routine
    trials_5.addData('sound_22.started', sound_22.tStartRefresh)
    trials_5.addData('sound_22.stopped', sound_22.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
        # was no response the correct answer?!
        if str(answers).lower() == 'none':
           key_resp_7.corr = 1;  # correct non-response
        else:
           key_resp_7.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('key_resp_7.keys',key_resp_7.keys)
    trials_5.addData('key_resp_7.corr', key_resp_7.corr)
    if key_resp_7.keys != None:  # we had a response
        trials_5.addData('key_resp_7.rt', key_resp_7.rt)
    trials_5.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    trials_5.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "End_tone5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback5"-------
    continueRoutine = True
    # update component parameters for each repeat
    if key_resp_7.corr:
        sound = sounds[0]
    else:
        sound = sounds[1]
    next_wait = np.random.choice(np.arange(6,11),1)[0]
    time_fn = core.monotonicClock.getTime
    label = "feedback_tone"
    duration = 0.
    minimal_trigger = new_trigger(label, duration)
    send_trigger(minimal_trigger)
    sleep(1.)
    sound_23.setSound(sound, hamming=True)
    sound_23.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedback5Components = [polygon_23, sound_23]
    for thisComponent in feedback5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback5"-------
    while continueRoutine:
        # get current time
        t = feedback5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_23* updates
        if polygon_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_23.frameNStart = frameN  # exact frame index
            polygon_23.tStart = t  # local t and not account for scr refresh
            polygon_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_23, 'tStartRefresh')  # time at next scr refresh
            polygon_23.setAutoDraw(True)
        if polygon_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_23.tStartRefresh + next_wait-frameTolerance:
                # keep track of stop time/frame for later
                polygon_23.tStop = t  # not accounting for scr refresh
                polygon_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_23, 'tStopRefresh')  # time at next scr refresh
                polygon_23.setAutoDraw(False)
        # start/stop sound_23
        if sound_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_23.frameNStart = frameN  # exact frame index
            sound_23.tStart = t  # local t and not account for scr refresh
            sound_23.tStartRefresh = tThisFlipGlobal  # on global time
            sound_23.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback5"-------
    for thisComponent in feedback5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('polygon_23.started', polygon_23.tStartRefresh)
    trials_5.addData('polygon_23.stopped', polygon_23.tStopRefresh)
    sound_23.stop()  # ensure sound has stopped at end of routine
    trials_5.addData('sound_23.started', sound_23.tStartRefresh)
    trials_5.addData('sound_23.stopped', sound_23.tStopRefresh)
    # the Routine "feedback5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_5'


# ------Prepare to start Routine "stop_pupil"-------
continueRoutine = True
# update component parameters for each repeat
time_fn = core.monotonicClock.getTime
pupil_remote.send_string('r')
print(pupil_remote.recv_string())
label = "End_of_Block"
duration = 0.
minimal_trigger = new_trigger(label, duration)
send_trigger(minimal_trigger)
sleep(1.)
# keep track of which components have finished
stop_pupilComponents = []
for thisComponent in stop_pupilComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stop_pupilClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stop_pupil"-------
while continueRoutine:
    # get current time
    t = stop_pupilClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stop_pupilClock)
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
    for thisComponent in stop_pupilComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stop_pupil"-------
for thisComponent in stop_pupilComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "stop_pupil" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "End_Experiment"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
End_ExperimentComponents = [text_3]
for thisComponent in End_ExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End_ExperimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End_Experiment"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = End_ExperimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End_ExperimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_ExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End_Experiment"-------
for thisComponent in End_ExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

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
