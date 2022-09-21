#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on septiembre 13, 2022, at 17:49
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'MDP'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
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
    originPath='C:\\Users\\LAURA\\Documents\\UDEA\\Gruneco\\Proyecto Resonador\\Paradigma y áreas función motora\\manos_pie_dedospie\\MDP_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Bienvenido"
BienvenidoClock = core.Clock()
fondo_negro = visual.Rect(
    win=win, name='fondo_negro',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
bienvenido = visual.TextStim(win=win, name='bienvenido',
    text='BIENVENIDO\n\nEn breves segundos comenzará a realizar las actividades previamente indicadas',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "indicaciones"
indicacionesClock = core.Clock()
fondo_negro_3 = visual.Rect(
    win=win, name='fondo_negro_3',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
indicaciones_ = visual.TextStim(win=win, name='indicaciones_',
    text='MUEVA LOS DEDOS SEÑALADOS EN ROJO',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mov_mano_derecha"
mov_mano_derechaClock = core.Clock()
fondo_negro_2 = visual.Rect(
    win=win, name='fondo_negro_2',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
mov_derecha = visual.TextStim(win=win, name='mov_derecha',
    text='DEDOS MANO DERECHA\n',
    font='Open Sans',
    pos=(0, 0.26), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_mano_derecha = visual.ImageStim(
    win=win,
    name='image_mano_derecha', 
    image='dedos1_mano_derecha.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "CAMBIO"
CAMBIOClock = core.Clock()
fondo_negro_8 = visual.Rect(
    win=win, name='fondo_negro_8',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
cambio = visual.TextStim(win=win, name='cambio',
    text='CAMBIO',
    font='Open Sans',
    pos=(0, 0), height=0.18, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mov_mano_izquierda"
mov_mano_izquierdaClock = core.Clock()
fondo_negro_4 = visual.Rect(
    win=win, name='fondo_negro_4',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
mov_izquierda = visual.TextStim(win=win, name='mov_izquierda',
    text='DEDOS MANO IZQUIERDA',
    font='Open Sans',
    pos=(0, 0.26), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_mano_izquierda = visual.ImageStim(
    win=win,
    name='image_mano_izquierda', 
    image='dedos1_mano_izquierda.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.11), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "DESCANSO"
DESCANSOClock = core.Clock()
fondo_negro_7 = visual.Rect(
    win=win, name='fondo_negro_7',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
descanso = visual.TextStim(win=win, name='descanso',
    text='DESCANSO',
    font='Open Sans',
    pos=(0, 0), height=0.17, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mov_2_mano_derecha"
mov_2_mano_derechaClock = core.Clock()
fondo_negro_5 = visual.Rect(
    win=win, name='fondo_negro_5',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
ind_mano_izquierda = visual.TextStim(win=win, name='ind_mano_izquierda',
    text='DEDOS MANO DERECHA',
    font='Open Sans',
    pos=(0, 0.26), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_mano_izquierda_2 = visual.ImageStim(
    win=win,
    name='image_mano_izquierda_2', 
    image='dedos_mano.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "CAMBIO"
CAMBIOClock = core.Clock()
fondo_negro_8 = visual.Rect(
    win=win, name='fondo_negro_8',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
cambio = visual.TextStim(win=win, name='cambio',
    text='CAMBIO',
    font='Open Sans',
    pos=(0, 0), height=0.18, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mov_2_mano_izquierda"
mov_2_mano_izquierdaClock = core.Clock()
fondo_negro_6 = visual.Rect(
    win=win, name='fondo_negro_6',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
text_6 = visual.TextStim(win=win, name='text_6',
    text='DEDOS MANO IZQUIERDA',
    font='Open Sans',
    pos=(0, 0.26), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='dedos_mano_izq.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "DESCANSO"
DESCANSOClock = core.Clock()
fondo_negro_7 = visual.Rect(
    win=win, name='fondo_negro_7',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
descanso = visual.TextStim(win=win, name='descanso',
    text='DESCANSO',
    font='Open Sans',
    pos=(0, 0), height=0.17, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "flexion_pie_derecho"
flexion_pie_derechoClock = core.Clock()
fondo_negro_9 = visual.Rect(
    win=win, name='fondo_negro_9',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
flexion_pie = visual.TextStim(win=win, name='flexion_pie',
    text='PIE DERECHO',
    font='Comic Sans',
    pos=(0, 0.23), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_pie_derecho = visual.ImageStim(
    win=win,
    name='image_pie_derecho', 
    image='pie_derecho_flechas_rojas.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.15), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "CAMBIO"
CAMBIOClock = core.Clock()
fondo_negro_8 = visual.Rect(
    win=win, name='fondo_negro_8',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
cambio = visual.TextStim(win=win, name='cambio',
    text='CAMBIO',
    font='Open Sans',
    pos=(0, 0), height=0.18, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "flexion_pie_izquierdo"
flexion_pie_izquierdoClock = core.Clock()
fondo_negro_10 = visual.Rect(
    win=win, name='fondo_negro_10',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
image_flexion_pie_izquierdo = visual.ImageStim(
    win=win,
    name='image_flexion_pie_izquierdo', 
    image='pie_izquierdo_flechas_rojas.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.15), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
flexion_pie_izquierdo_ = visual.TextStim(win=win, name='flexion_pie_izquierdo_',
    text='PIE IZQUIERDO',
    font='Open Sans',
    pos=(0, 0.23), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "DESCANSO"
DESCANSOClock = core.Clock()
fondo_negro_7 = visual.Rect(
    win=win, name='fondo_negro_7',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
descanso = visual.TextStim(win=win, name='descanso',
    text='DESCANSO',
    font='Open Sans',
    pos=(0, 0), height=0.17, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "dedos_pie_derecho"
dedos_pie_derechoClock = core.Clock()
fondo_negro_11 = visual.Rect(
    win=win, name='fondo_negro_11',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
ind_dedos_derecho = visual.TextStim(win=win, name='ind_dedos_derecho',
    text='DEDOS PIE DERECHO',
    font='Open Sans',
    pos=(0, 0.2), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_dedos_pie_derecho = visual.ImageStim(
    win=win,
    name='image_dedos_pie_derecho', 
    image='dedos_pie_derecho_flecha_roja.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.2), size=(1.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "CAMBIO"
CAMBIOClock = core.Clock()
fondo_negro_8 = visual.Rect(
    win=win, name='fondo_negro_8',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
cambio = visual.TextStim(win=win, name='cambio',
    text='CAMBIO',
    font='Open Sans',
    pos=(0, 0), height=0.18, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "dedos_pie_izquierdo"
dedos_pie_izquierdoClock = core.Clock()
fondo_negro_12 = visual.Rect(
    win=win, name='fondo_negro_12',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
ind_dedos_izquierdo = visual.TextStim(win=win, name='ind_dedos_izquierdo',
    text='DEDOS PIE IZQUIERDO',
    font='Open Sans',
    pos=(0, 0.2), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_dedos_pie_izquierdo = visual.ImageStim(
    win=win,
    name='image_dedos_pie_izquierdo', 
    image='dedos_pie_izquierdo_flecha_roja.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.2), size=(1.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "DESCANSO"
DESCANSOClock = core.Clock()
fondo_negro_7 = visual.Rect(
    win=win, name='fondo_negro_7',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
descanso = visual.TextStim(win=win, name='descanso',
    text='DESCANSO',
    font='Open Sans',
    pos=(0, 0), height=0.17, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Bienvenido"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
BienvenidoComponents = [fondo_negro, bienvenido]
for thisComponent in BienvenidoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BienvenidoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Bienvenido"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BienvenidoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BienvenidoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fondo_negro* updates
    if fondo_negro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fondo_negro.frameNStart = frameN  # exact frame index
        fondo_negro.tStart = t  # local t and not account for scr refresh
        fondo_negro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fondo_negro, 'tStartRefresh')  # time at next scr refresh
        fondo_negro.setAutoDraw(True)
    if fondo_negro.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fondo_negro.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            fondo_negro.tStop = t  # not accounting for scr refresh
            fondo_negro.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fondo_negro, 'tStopRefresh')  # time at next scr refresh
            fondo_negro.setAutoDraw(False)
    
    # *bienvenido* updates
    if bienvenido.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bienvenido.frameNStart = frameN  # exact frame index
        bienvenido.tStart = t  # local t and not account for scr refresh
        bienvenido.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bienvenido, 'tStartRefresh')  # time at next scr refresh
        bienvenido.setAutoDraw(True)
    if bienvenido.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bienvenido.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            bienvenido.tStop = t  # not accounting for scr refresh
            bienvenido.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bienvenido, 'tStopRefresh')  # time at next scr refresh
            bienvenido.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BienvenidoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Bienvenido"-------
for thisComponent in BienvenidoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fondo_negro.started', fondo_negro.tStartRefresh)
thisExp.addData('fondo_negro.stopped', fondo_negro.tStopRefresh)
thisExp.addData('bienvenido.started', bienvenido.tStartRefresh)
thisExp.addData('bienvenido.stopped', bienvenido.tStopRefresh)

# ------Prepare to start Routine "indicaciones"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
indicacionesComponents = [fondo_negro_3, indicaciones_]
for thisComponent in indicacionesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
indicacionesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "indicaciones"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = indicacionesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=indicacionesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fondo_negro_3* updates
    if fondo_negro_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fondo_negro_3.frameNStart = frameN  # exact frame index
        fondo_negro_3.tStart = t  # local t and not account for scr refresh
        fondo_negro_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fondo_negro_3, 'tStartRefresh')  # time at next scr refresh
        fondo_negro_3.setAutoDraw(True)
    if fondo_negro_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fondo_negro_3.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            fondo_negro_3.tStop = t  # not accounting for scr refresh
            fondo_negro_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fondo_negro_3, 'tStopRefresh')  # time at next scr refresh
            fondo_negro_3.setAutoDraw(False)
    
    # *indicaciones_* updates
    if indicaciones_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicaciones_.frameNStart = frameN  # exact frame index
        indicaciones_.tStart = t  # local t and not account for scr refresh
        indicaciones_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicaciones_, 'tStartRefresh')  # time at next scr refresh
        indicaciones_.setAutoDraw(True)
    if indicaciones_.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > indicaciones_.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            indicaciones_.tStop = t  # not accounting for scr refresh
            indicaciones_.frameNStop = frameN  # exact frame index
            win.timeOnFlip(indicaciones_, 'tStopRefresh')  # time at next scr refresh
            indicaciones_.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in indicacionesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "indicaciones"-------
for thisComponent in indicacionesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fondo_negro_3.started', fondo_negro_3.tStartRefresh)
thisExp.addData('fondo_negro_3.stopped', fondo_negro_3.tStopRefresh)
thisExp.addData('indicaciones_.started', indicaciones_.tStartRefresh)
thisExp.addData('indicaciones_.stopped', indicaciones_.tStopRefresh)

# set up handler to look after randomisation of conditions etc
repeticion_mano_204s_3_4min = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeticion_mano_204s_3_4min')
thisExp.addLoop(repeticion_mano_204s_3_4min)  # add the loop to the experiment
thisRepeticion_mano_204s_3_4min = repeticion_mano_204s_3_4min.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeticion_mano_204s_3_4min.rgb)
if thisRepeticion_mano_204s_3_4min != None:
    for paramName in thisRepeticion_mano_204s_3_4min:
        exec('{} = thisRepeticion_mano_204s_3_4min[paramName]'.format(paramName))

for thisRepeticion_mano_204s_3_4min in repeticion_mano_204s_3_4min:
    currentLoop = repeticion_mano_204s_3_4min
    # abbreviate parameter names if possible (e.g. rgb = thisRepeticion_mano_204s_3_4min.rgb)
    if thisRepeticion_mano_204s_3_4min != None:
        for paramName in thisRepeticion_mano_204s_3_4min:
            exec('{} = thisRepeticion_mano_204s_3_4min[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "mov_mano_derecha"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    mov_mano_derechaComponents = [fondo_negro_2, mov_derecha, image_mano_derecha]
    for thisComponent in mov_mano_derechaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mov_mano_derechaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mov_mano_derecha"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mov_mano_derechaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mov_mano_derechaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_2* updates
        if fondo_negro_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_2.frameNStart = frameN  # exact frame index
            fondo_negro_2.tStart = t  # local t and not account for scr refresh
            fondo_negro_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_2, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_2.setAutoDraw(True)
        if fondo_negro_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_2.tStop = t  # not accounting for scr refresh
                fondo_negro_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_2, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_2.setAutoDraw(False)
        
        # *mov_derecha* updates
        if mov_derecha.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mov_derecha.frameNStart = frameN  # exact frame index
            mov_derecha.tStart = t  # local t and not account for scr refresh
            mov_derecha.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mov_derecha, 'tStartRefresh')  # time at next scr refresh
            mov_derecha.setAutoDraw(True)
        if mov_derecha.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mov_derecha.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                mov_derecha.tStop = t  # not accounting for scr refresh
                mov_derecha.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mov_derecha, 'tStopRefresh')  # time at next scr refresh
                mov_derecha.setAutoDraw(False)
        
        # *image_mano_derecha* updates
        if image_mano_derecha.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_mano_derecha.frameNStart = frameN  # exact frame index
            image_mano_derecha.tStart = t  # local t and not account for scr refresh
            image_mano_derecha.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_mano_derecha, 'tStartRefresh')  # time at next scr refresh
            image_mano_derecha.setAutoDraw(True)
        if image_mano_derecha.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_mano_derecha.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image_mano_derecha.tStop = t  # not accounting for scr refresh
                image_mano_derecha.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_mano_derecha, 'tStopRefresh')  # time at next scr refresh
                image_mano_derecha.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mov_mano_derechaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mov_mano_derecha"-------
    for thisComponent in mov_mano_derechaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_mano_204s_3_4min.addData('fondo_negro_2.started', fondo_negro_2.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('fondo_negro_2.stopped', fondo_negro_2.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('mov_derecha.started', mov_derecha.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('mov_derecha.stopped', mov_derecha.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('image_mano_derecha.started', image_mano_derecha.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('image_mano_derecha.stopped', image_mano_derecha.tStopRefresh)
    
    # ------Prepare to start Routine "CAMBIO"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CAMBIOComponents = [fondo_negro_8, cambio]
    for thisComponent in CAMBIOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CAMBIOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "CAMBIO"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CAMBIOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CAMBIOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_8* updates
        if fondo_negro_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_8.frameNStart = frameN  # exact frame index
            fondo_negro_8.tStart = t  # local t and not account for scr refresh
            fondo_negro_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_8, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_8.setAutoDraw(True)
        if fondo_negro_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_8.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_8.tStop = t  # not accounting for scr refresh
                fondo_negro_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_8, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_8.setAutoDraw(False)
        
        # *cambio* updates
        if cambio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cambio.frameNStart = frameN  # exact frame index
            cambio.tStart = t  # local t and not account for scr refresh
            cambio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cambio, 'tStartRefresh')  # time at next scr refresh
            cambio.setAutoDraw(True)
        if cambio.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cambio.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                cambio.tStop = t  # not accounting for scr refresh
                cambio.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cambio, 'tStopRefresh')  # time at next scr refresh
                cambio.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CAMBIOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CAMBIO"-------
    for thisComponent in CAMBIOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_mano_204s_3_4min.addData('fondo_negro_8.started', fondo_negro_8.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('fondo_negro_8.stopped', fondo_negro_8.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('cambio.started', cambio.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('cambio.stopped', cambio.tStopRefresh)
    
    # ------Prepare to start Routine "mov_mano_izquierda"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    mov_mano_izquierdaComponents = [fondo_negro_4, mov_izquierda, image_mano_izquierda]
    for thisComponent in mov_mano_izquierdaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mov_mano_izquierdaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mov_mano_izquierda"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mov_mano_izquierdaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mov_mano_izquierdaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_4* updates
        if fondo_negro_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_4.frameNStart = frameN  # exact frame index
            fondo_negro_4.tStart = t  # local t and not account for scr refresh
            fondo_negro_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_4, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_4.setAutoDraw(True)
        if fondo_negro_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_4.tStop = t  # not accounting for scr refresh
                fondo_negro_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_4, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_4.setAutoDraw(False)
        
        # *mov_izquierda* updates
        if mov_izquierda.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            mov_izquierda.frameNStart = frameN  # exact frame index
            mov_izquierda.tStart = t  # local t and not account for scr refresh
            mov_izquierda.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mov_izquierda, 'tStartRefresh')  # time at next scr refresh
            mov_izquierda.setAutoDraw(True)
        if mov_izquierda.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mov_izquierda.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                mov_izquierda.tStop = t  # not accounting for scr refresh
                mov_izquierda.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mov_izquierda, 'tStopRefresh')  # time at next scr refresh
                mov_izquierda.setAutoDraw(False)
        
        # *image_mano_izquierda* updates
        if image_mano_izquierda.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_mano_izquierda.frameNStart = frameN  # exact frame index
            image_mano_izquierda.tStart = t  # local t and not account for scr refresh
            image_mano_izquierda.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_mano_izquierda, 'tStartRefresh')  # time at next scr refresh
            image_mano_izquierda.setAutoDraw(True)
        if image_mano_izquierda.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_mano_izquierda.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image_mano_izquierda.tStop = t  # not accounting for scr refresh
                image_mano_izquierda.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_mano_izquierda, 'tStopRefresh')  # time at next scr refresh
                image_mano_izquierda.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mov_mano_izquierdaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mov_mano_izquierda"-------
    for thisComponent in mov_mano_izquierdaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_mano_204s_3_4min.addData('fondo_negro_4.started', fondo_negro_4.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('fondo_negro_4.stopped', fondo_negro_4.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('mov_izquierda.started', mov_izquierda.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('mov_izquierda.stopped', mov_izquierda.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('image_mano_izquierda.started', image_mano_izquierda.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('image_mano_izquierda.stopped', image_mano_izquierda.tStopRefresh)
    
    # ------Prepare to start Routine "DESCANSO"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DESCANSOComponents = [fondo_negro_7, descanso]
    for thisComponent in DESCANSOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DESCANSOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "DESCANSO"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DESCANSOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DESCANSOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_7* updates
        if fondo_negro_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_7.frameNStart = frameN  # exact frame index
            fondo_negro_7.tStart = t  # local t and not account for scr refresh
            fondo_negro_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_7, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_7.setAutoDraw(True)
        if fondo_negro_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_7.tStop = t  # not accounting for scr refresh
                fondo_negro_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_7, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_7.setAutoDraw(False)
        
        # *descanso* updates
        if descanso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            descanso.frameNStart = frameN  # exact frame index
            descanso.tStart = t  # local t and not account for scr refresh
            descanso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(descanso, 'tStartRefresh')  # time at next scr refresh
            descanso.setAutoDraw(True)
        if descanso.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > descanso.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                descanso.tStop = t  # not accounting for scr refresh
                descanso.frameNStop = frameN  # exact frame index
                win.timeOnFlip(descanso, 'tStopRefresh')  # time at next scr refresh
                descanso.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DESCANSOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DESCANSO"-------
    for thisComponent in DESCANSOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_mano_204s_3_4min.addData('fondo_negro_7.started', fondo_negro_7.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('fondo_negro_7.stopped', fondo_negro_7.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('descanso.started', descanso.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('descanso.stopped', descanso.tStopRefresh)
    
    # ------Prepare to start Routine "mov_2_mano_derecha"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    mov_2_mano_derechaComponents = [fondo_negro_5, ind_mano_izquierda, image_mano_izquierda_2]
    for thisComponent in mov_2_mano_derechaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mov_2_mano_derechaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mov_2_mano_derecha"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mov_2_mano_derechaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mov_2_mano_derechaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_5* updates
        if fondo_negro_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_5.frameNStart = frameN  # exact frame index
            fondo_negro_5.tStart = t  # local t and not account for scr refresh
            fondo_negro_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_5, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_5.setAutoDraw(True)
        if fondo_negro_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_5.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_5.tStop = t  # not accounting for scr refresh
                fondo_negro_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_5, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_5.setAutoDraw(False)
        
        # *ind_mano_izquierda* updates
        if ind_mano_izquierda.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ind_mano_izquierda.frameNStart = frameN  # exact frame index
            ind_mano_izquierda.tStart = t  # local t and not account for scr refresh
            ind_mano_izquierda.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ind_mano_izquierda, 'tStartRefresh')  # time at next scr refresh
            ind_mano_izquierda.setAutoDraw(True)
        if ind_mano_izquierda.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ind_mano_izquierda.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ind_mano_izquierda.tStop = t  # not accounting for scr refresh
                ind_mano_izquierda.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ind_mano_izquierda, 'tStopRefresh')  # time at next scr refresh
                ind_mano_izquierda.setAutoDraw(False)
        
        # *image_mano_izquierda_2* updates
        if image_mano_izquierda_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_mano_izquierda_2.frameNStart = frameN  # exact frame index
            image_mano_izquierda_2.tStart = t  # local t and not account for scr refresh
            image_mano_izquierda_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_mano_izquierda_2, 'tStartRefresh')  # time at next scr refresh
            image_mano_izquierda_2.setAutoDraw(True)
        if image_mano_izquierda_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_mano_izquierda_2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image_mano_izquierda_2.tStop = t  # not accounting for scr refresh
                image_mano_izquierda_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_mano_izquierda_2, 'tStopRefresh')  # time at next scr refresh
                image_mano_izquierda_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mov_2_mano_derechaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mov_2_mano_derecha"-------
    for thisComponent in mov_2_mano_derechaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_mano_204s_3_4min.addData('fondo_negro_5.started', fondo_negro_5.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('fondo_negro_5.stopped', fondo_negro_5.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('ind_mano_izquierda.started', ind_mano_izquierda.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('ind_mano_izquierda.stopped', ind_mano_izquierda.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('image_mano_izquierda_2.started', image_mano_izquierda_2.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('image_mano_izquierda_2.stopped', image_mano_izquierda_2.tStopRefresh)
    
    # ------Prepare to start Routine "CAMBIO"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CAMBIOComponents = [fondo_negro_8, cambio]
    for thisComponent in CAMBIOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CAMBIOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "CAMBIO"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CAMBIOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CAMBIOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_8* updates
        if fondo_negro_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_8.frameNStart = frameN  # exact frame index
            fondo_negro_8.tStart = t  # local t and not account for scr refresh
            fondo_negro_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_8, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_8.setAutoDraw(True)
        if fondo_negro_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_8.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_8.tStop = t  # not accounting for scr refresh
                fondo_negro_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_8, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_8.setAutoDraw(False)
        
        # *cambio* updates
        if cambio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cambio.frameNStart = frameN  # exact frame index
            cambio.tStart = t  # local t and not account for scr refresh
            cambio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cambio, 'tStartRefresh')  # time at next scr refresh
            cambio.setAutoDraw(True)
        if cambio.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cambio.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                cambio.tStop = t  # not accounting for scr refresh
                cambio.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cambio, 'tStopRefresh')  # time at next scr refresh
                cambio.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CAMBIOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CAMBIO"-------
    for thisComponent in CAMBIOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_mano_204s_3_4min.addData('fondo_negro_8.started', fondo_negro_8.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('fondo_negro_8.stopped', fondo_negro_8.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('cambio.started', cambio.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('cambio.stopped', cambio.tStopRefresh)
    
    # ------Prepare to start Routine "mov_2_mano_izquierda"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    mov_2_mano_izquierdaComponents = [fondo_negro_6, text_6, image_3]
    for thisComponent in mov_2_mano_izquierdaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mov_2_mano_izquierdaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mov_2_mano_izquierda"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mov_2_mano_izquierdaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mov_2_mano_izquierdaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_6* updates
        if fondo_negro_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_6.frameNStart = frameN  # exact frame index
            fondo_negro_6.tStart = t  # local t and not account for scr refresh
            fondo_negro_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_6, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_6.setAutoDraw(True)
        if fondo_negro_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_6.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_6.tStop = t  # not accounting for scr refresh
                fondo_negro_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_6, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_6.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mov_2_mano_izquierdaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mov_2_mano_izquierda"-------
    for thisComponent in mov_2_mano_izquierdaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_mano_204s_3_4min.addData('fondo_negro_6.started', fondo_negro_6.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('fondo_negro_6.stopped', fondo_negro_6.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('text_6.started', text_6.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('text_6.stopped', text_6.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('image_3.started', image_3.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('image_3.stopped', image_3.tStopRefresh)
    
    # ------Prepare to start Routine "DESCANSO"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DESCANSOComponents = [fondo_negro_7, descanso]
    for thisComponent in DESCANSOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DESCANSOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "DESCANSO"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DESCANSOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DESCANSOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_7* updates
        if fondo_negro_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_7.frameNStart = frameN  # exact frame index
            fondo_negro_7.tStart = t  # local t and not account for scr refresh
            fondo_negro_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_7, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_7.setAutoDraw(True)
        if fondo_negro_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_7.tStop = t  # not accounting for scr refresh
                fondo_negro_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_7, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_7.setAutoDraw(False)
        
        # *descanso* updates
        if descanso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            descanso.frameNStart = frameN  # exact frame index
            descanso.tStart = t  # local t and not account for scr refresh
            descanso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(descanso, 'tStartRefresh')  # time at next scr refresh
            descanso.setAutoDraw(True)
        if descanso.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > descanso.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                descanso.tStop = t  # not accounting for scr refresh
                descanso.frameNStop = frameN  # exact frame index
                win.timeOnFlip(descanso, 'tStopRefresh')  # time at next scr refresh
                descanso.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DESCANSOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DESCANSO"-------
    for thisComponent in DESCANSOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_mano_204s_3_4min.addData('fondo_negro_7.started', fondo_negro_7.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('fondo_negro_7.stopped', fondo_negro_7.tStopRefresh)
    repeticion_mano_204s_3_4min.addData('descanso.started', descanso.tStartRefresh)
    repeticion_mano_204s_3_4min.addData('descanso.stopped', descanso.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'repeticion_mano_204s_3_4min'


# set up handler to look after randomisation of conditions etc
repeticion_pie_102seg_1_7min = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeticion_pie_102seg_1_7min')
thisExp.addLoop(repeticion_pie_102seg_1_7min)  # add the loop to the experiment
thisRepeticion_pie_102seg_1_7min = repeticion_pie_102seg_1_7min.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeticion_pie_102seg_1_7min.rgb)
if thisRepeticion_pie_102seg_1_7min != None:
    for paramName in thisRepeticion_pie_102seg_1_7min:
        exec('{} = thisRepeticion_pie_102seg_1_7min[paramName]'.format(paramName))

for thisRepeticion_pie_102seg_1_7min in repeticion_pie_102seg_1_7min:
    currentLoop = repeticion_pie_102seg_1_7min
    # abbreviate parameter names if possible (e.g. rgb = thisRepeticion_pie_102seg_1_7min.rgb)
    if thisRepeticion_pie_102seg_1_7min != None:
        for paramName in thisRepeticion_pie_102seg_1_7min:
            exec('{} = thisRepeticion_pie_102seg_1_7min[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "flexion_pie_derecho"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    flexion_pie_derechoComponents = [fondo_negro_9, flexion_pie, image_pie_derecho]
    for thisComponent in flexion_pie_derechoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    flexion_pie_derechoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "flexion_pie_derecho"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = flexion_pie_derechoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=flexion_pie_derechoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_9* updates
        if fondo_negro_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_9.frameNStart = frameN  # exact frame index
            fondo_negro_9.tStart = t  # local t and not account for scr refresh
            fondo_negro_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_9, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_9.setAutoDraw(True)
        if fondo_negro_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_9.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_9.tStop = t  # not accounting for scr refresh
                fondo_negro_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_9, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_9.setAutoDraw(False)
        
        # *flexion_pie* updates
        if flexion_pie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            flexion_pie.frameNStart = frameN  # exact frame index
            flexion_pie.tStart = t  # local t and not account for scr refresh
            flexion_pie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flexion_pie, 'tStartRefresh')  # time at next scr refresh
            flexion_pie.setAutoDraw(True)
        if flexion_pie.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > flexion_pie.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                flexion_pie.tStop = t  # not accounting for scr refresh
                flexion_pie.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flexion_pie, 'tStopRefresh')  # time at next scr refresh
                flexion_pie.setAutoDraw(False)
        
        # *image_pie_derecho* updates
        if image_pie_derecho.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_pie_derecho.frameNStart = frameN  # exact frame index
            image_pie_derecho.tStart = t  # local t and not account for scr refresh
            image_pie_derecho.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pie_derecho, 'tStartRefresh')  # time at next scr refresh
            image_pie_derecho.setAutoDraw(True)
        if image_pie_derecho.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pie_derecho.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image_pie_derecho.tStop = t  # not accounting for scr refresh
                image_pie_derecho.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pie_derecho, 'tStopRefresh')  # time at next scr refresh
                image_pie_derecho.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in flexion_pie_derechoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "flexion_pie_derecho"-------
    for thisComponent in flexion_pie_derechoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_pie_102seg_1_7min.addData('fondo_negro_9.started', fondo_negro_9.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('fondo_negro_9.stopped', fondo_negro_9.tStopRefresh)
    repeticion_pie_102seg_1_7min.addData('flexion_pie.started', flexion_pie.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('flexion_pie.stopped', flexion_pie.tStopRefresh)
    repeticion_pie_102seg_1_7min.addData('image_pie_derecho.started', image_pie_derecho.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('image_pie_derecho.stopped', image_pie_derecho.tStopRefresh)
    
    # ------Prepare to start Routine "CAMBIO"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CAMBIOComponents = [fondo_negro_8, cambio]
    for thisComponent in CAMBIOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CAMBIOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "CAMBIO"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CAMBIOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CAMBIOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_8* updates
        if fondo_negro_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_8.frameNStart = frameN  # exact frame index
            fondo_negro_8.tStart = t  # local t and not account for scr refresh
            fondo_negro_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_8, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_8.setAutoDraw(True)
        if fondo_negro_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_8.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_8.tStop = t  # not accounting for scr refresh
                fondo_negro_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_8, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_8.setAutoDraw(False)
        
        # *cambio* updates
        if cambio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cambio.frameNStart = frameN  # exact frame index
            cambio.tStart = t  # local t and not account for scr refresh
            cambio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cambio, 'tStartRefresh')  # time at next scr refresh
            cambio.setAutoDraw(True)
        if cambio.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cambio.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                cambio.tStop = t  # not accounting for scr refresh
                cambio.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cambio, 'tStopRefresh')  # time at next scr refresh
                cambio.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CAMBIOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CAMBIO"-------
    for thisComponent in CAMBIOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_pie_102seg_1_7min.addData('fondo_negro_8.started', fondo_negro_8.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('fondo_negro_8.stopped', fondo_negro_8.tStopRefresh)
    repeticion_pie_102seg_1_7min.addData('cambio.started', cambio.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('cambio.stopped', cambio.tStopRefresh)
    
    # ------Prepare to start Routine "flexion_pie_izquierdo"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    flexion_pie_izquierdoComponents = [fondo_negro_10, image_flexion_pie_izquierdo, flexion_pie_izquierdo_]
    for thisComponent in flexion_pie_izquierdoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    flexion_pie_izquierdoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "flexion_pie_izquierdo"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = flexion_pie_izquierdoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=flexion_pie_izquierdoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_10* updates
        if fondo_negro_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_10.frameNStart = frameN  # exact frame index
            fondo_negro_10.tStart = t  # local t and not account for scr refresh
            fondo_negro_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_10, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_10.setAutoDraw(True)
        if fondo_negro_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_10.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_10.tStop = t  # not accounting for scr refresh
                fondo_negro_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_10, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_10.setAutoDraw(False)
        
        # *image_flexion_pie_izquierdo* updates
        if image_flexion_pie_izquierdo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_flexion_pie_izquierdo.frameNStart = frameN  # exact frame index
            image_flexion_pie_izquierdo.tStart = t  # local t and not account for scr refresh
            image_flexion_pie_izquierdo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_flexion_pie_izquierdo, 'tStartRefresh')  # time at next scr refresh
            image_flexion_pie_izquierdo.setAutoDraw(True)
        if image_flexion_pie_izquierdo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_flexion_pie_izquierdo.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image_flexion_pie_izquierdo.tStop = t  # not accounting for scr refresh
                image_flexion_pie_izquierdo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_flexion_pie_izquierdo, 'tStopRefresh')  # time at next scr refresh
                image_flexion_pie_izquierdo.setAutoDraw(False)
        
        # *flexion_pie_izquierdo_* updates
        if flexion_pie_izquierdo_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            flexion_pie_izquierdo_.frameNStart = frameN  # exact frame index
            flexion_pie_izquierdo_.tStart = t  # local t and not account for scr refresh
            flexion_pie_izquierdo_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flexion_pie_izquierdo_, 'tStartRefresh')  # time at next scr refresh
            flexion_pie_izquierdo_.setAutoDraw(True)
        if flexion_pie_izquierdo_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > flexion_pie_izquierdo_.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                flexion_pie_izquierdo_.tStop = t  # not accounting for scr refresh
                flexion_pie_izquierdo_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flexion_pie_izquierdo_, 'tStopRefresh')  # time at next scr refresh
                flexion_pie_izquierdo_.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in flexion_pie_izquierdoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "flexion_pie_izquierdo"-------
    for thisComponent in flexion_pie_izquierdoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_pie_102seg_1_7min.addData('fondo_negro_10.started', fondo_negro_10.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('fondo_negro_10.stopped', fondo_negro_10.tStopRefresh)
    repeticion_pie_102seg_1_7min.addData('image_flexion_pie_izquierdo.started', image_flexion_pie_izquierdo.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('image_flexion_pie_izquierdo.stopped', image_flexion_pie_izquierdo.tStopRefresh)
    repeticion_pie_102seg_1_7min.addData('flexion_pie_izquierdo_.started', flexion_pie_izquierdo_.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('flexion_pie_izquierdo_.stopped', flexion_pie_izquierdo_.tStopRefresh)
    
    # ------Prepare to start Routine "DESCANSO"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DESCANSOComponents = [fondo_negro_7, descanso]
    for thisComponent in DESCANSOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DESCANSOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "DESCANSO"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DESCANSOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DESCANSOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_7* updates
        if fondo_negro_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_7.frameNStart = frameN  # exact frame index
            fondo_negro_7.tStart = t  # local t and not account for scr refresh
            fondo_negro_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_7, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_7.setAutoDraw(True)
        if fondo_negro_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_7.tStop = t  # not accounting for scr refresh
                fondo_negro_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_7, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_7.setAutoDraw(False)
        
        # *descanso* updates
        if descanso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            descanso.frameNStart = frameN  # exact frame index
            descanso.tStart = t  # local t and not account for scr refresh
            descanso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(descanso, 'tStartRefresh')  # time at next scr refresh
            descanso.setAutoDraw(True)
        if descanso.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > descanso.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                descanso.tStop = t  # not accounting for scr refresh
                descanso.frameNStop = frameN  # exact frame index
                win.timeOnFlip(descanso, 'tStopRefresh')  # time at next scr refresh
                descanso.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DESCANSOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DESCANSO"-------
    for thisComponent in DESCANSOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_pie_102seg_1_7min.addData('fondo_negro_7.started', fondo_negro_7.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('fondo_negro_7.stopped', fondo_negro_7.tStopRefresh)
    repeticion_pie_102seg_1_7min.addData('descanso.started', descanso.tStartRefresh)
    repeticion_pie_102seg_1_7min.addData('descanso.stopped', descanso.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'repeticion_pie_102seg_1_7min'


# set up handler to look after randomisation of conditions etc
repeticion_dedos_pie_102seg_1_7min = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeticion_dedos_pie_102seg_1_7min')
thisExp.addLoop(repeticion_dedos_pie_102seg_1_7min)  # add the loop to the experiment
thisRepeticion_dedos_pie_102seg_1_7min = repeticion_dedos_pie_102seg_1_7min.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeticion_dedos_pie_102seg_1_7min.rgb)
if thisRepeticion_dedos_pie_102seg_1_7min != None:
    for paramName in thisRepeticion_dedos_pie_102seg_1_7min:
        exec('{} = thisRepeticion_dedos_pie_102seg_1_7min[paramName]'.format(paramName))

for thisRepeticion_dedos_pie_102seg_1_7min in repeticion_dedos_pie_102seg_1_7min:
    currentLoop = repeticion_dedos_pie_102seg_1_7min
    # abbreviate parameter names if possible (e.g. rgb = thisRepeticion_dedos_pie_102seg_1_7min.rgb)
    if thisRepeticion_dedos_pie_102seg_1_7min != None:
        for paramName in thisRepeticion_dedos_pie_102seg_1_7min:
            exec('{} = thisRepeticion_dedos_pie_102seg_1_7min[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "dedos_pie_derecho"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    dedos_pie_derechoComponents = [fondo_negro_11, ind_dedos_derecho, image_dedos_pie_derecho]
    for thisComponent in dedos_pie_derechoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    dedos_pie_derechoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "dedos_pie_derecho"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dedos_pie_derechoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=dedos_pie_derechoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_11* updates
        if fondo_negro_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_11.frameNStart = frameN  # exact frame index
            fondo_negro_11.tStart = t  # local t and not account for scr refresh
            fondo_negro_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_11, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_11.setAutoDraw(True)
        if fondo_negro_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_11.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_11.tStop = t  # not accounting for scr refresh
                fondo_negro_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_11, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_11.setAutoDraw(False)
        
        # *ind_dedos_derecho* updates
        if ind_dedos_derecho.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ind_dedos_derecho.frameNStart = frameN  # exact frame index
            ind_dedos_derecho.tStart = t  # local t and not account for scr refresh
            ind_dedos_derecho.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ind_dedos_derecho, 'tStartRefresh')  # time at next scr refresh
            ind_dedos_derecho.setAutoDraw(True)
        if ind_dedos_derecho.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ind_dedos_derecho.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ind_dedos_derecho.tStop = t  # not accounting for scr refresh
                ind_dedos_derecho.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ind_dedos_derecho, 'tStopRefresh')  # time at next scr refresh
                ind_dedos_derecho.setAutoDraw(False)
        
        # *image_dedos_pie_derecho* updates
        if image_dedos_pie_derecho.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_dedos_pie_derecho.frameNStart = frameN  # exact frame index
            image_dedos_pie_derecho.tStart = t  # local t and not account for scr refresh
            image_dedos_pie_derecho.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_dedos_pie_derecho, 'tStartRefresh')  # time at next scr refresh
            image_dedos_pie_derecho.setAutoDraw(True)
        if image_dedos_pie_derecho.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_dedos_pie_derecho.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image_dedos_pie_derecho.tStop = t  # not accounting for scr refresh
                image_dedos_pie_derecho.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_dedos_pie_derecho, 'tStopRefresh')  # time at next scr refresh
                image_dedos_pie_derecho.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dedos_pie_derechoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dedos_pie_derecho"-------
    for thisComponent in dedos_pie_derechoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_dedos_pie_102seg_1_7min.addData('fondo_negro_11.started', fondo_negro_11.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('fondo_negro_11.stopped', fondo_negro_11.tStopRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('ind_dedos_derecho.started', ind_dedos_derecho.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('ind_dedos_derecho.stopped', ind_dedos_derecho.tStopRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('image_dedos_pie_derecho.started', image_dedos_pie_derecho.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('image_dedos_pie_derecho.stopped', image_dedos_pie_derecho.tStopRefresh)
    
    # ------Prepare to start Routine "CAMBIO"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CAMBIOComponents = [fondo_negro_8, cambio]
    for thisComponent in CAMBIOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CAMBIOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "CAMBIO"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CAMBIOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CAMBIOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_8* updates
        if fondo_negro_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_8.frameNStart = frameN  # exact frame index
            fondo_negro_8.tStart = t  # local t and not account for scr refresh
            fondo_negro_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_8, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_8.setAutoDraw(True)
        if fondo_negro_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_8.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_8.tStop = t  # not accounting for scr refresh
                fondo_negro_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_8, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_8.setAutoDraw(False)
        
        # *cambio* updates
        if cambio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cambio.frameNStart = frameN  # exact frame index
            cambio.tStart = t  # local t and not account for scr refresh
            cambio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cambio, 'tStartRefresh')  # time at next scr refresh
            cambio.setAutoDraw(True)
        if cambio.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cambio.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                cambio.tStop = t  # not accounting for scr refresh
                cambio.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cambio, 'tStopRefresh')  # time at next scr refresh
                cambio.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CAMBIOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CAMBIO"-------
    for thisComponent in CAMBIOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_dedos_pie_102seg_1_7min.addData('fondo_negro_8.started', fondo_negro_8.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('fondo_negro_8.stopped', fondo_negro_8.tStopRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('cambio.started', cambio.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('cambio.stopped', cambio.tStopRefresh)
    
    # ------Prepare to start Routine "dedos_pie_izquierdo"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    dedos_pie_izquierdoComponents = [fondo_negro_12, ind_dedos_izquierdo, image_dedos_pie_izquierdo]
    for thisComponent in dedos_pie_izquierdoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    dedos_pie_izquierdoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "dedos_pie_izquierdo"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dedos_pie_izquierdoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=dedos_pie_izquierdoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_12* updates
        if fondo_negro_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_12.frameNStart = frameN  # exact frame index
            fondo_negro_12.tStart = t  # local t and not account for scr refresh
            fondo_negro_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_12, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_12.setAutoDraw(True)
        if fondo_negro_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_12.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_12.tStop = t  # not accounting for scr refresh
                fondo_negro_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_12, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_12.setAutoDraw(False)
        
        # *ind_dedos_izquierdo* updates
        if ind_dedos_izquierdo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ind_dedos_izquierdo.frameNStart = frameN  # exact frame index
            ind_dedos_izquierdo.tStart = t  # local t and not account for scr refresh
            ind_dedos_izquierdo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ind_dedos_izquierdo, 'tStartRefresh')  # time at next scr refresh
            ind_dedos_izquierdo.setAutoDraw(True)
        if ind_dedos_izquierdo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ind_dedos_izquierdo.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ind_dedos_izquierdo.tStop = t  # not accounting for scr refresh
                ind_dedos_izquierdo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ind_dedos_izquierdo, 'tStopRefresh')  # time at next scr refresh
                ind_dedos_izquierdo.setAutoDraw(False)
        
        # *image_dedos_pie_izquierdo* updates
        if image_dedos_pie_izquierdo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_dedos_pie_izquierdo.frameNStart = frameN  # exact frame index
            image_dedos_pie_izquierdo.tStart = t  # local t and not account for scr refresh
            image_dedos_pie_izquierdo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_dedos_pie_izquierdo, 'tStartRefresh')  # time at next scr refresh
            image_dedos_pie_izquierdo.setAutoDraw(True)
        if image_dedos_pie_izquierdo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_dedos_pie_izquierdo.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image_dedos_pie_izquierdo.tStop = t  # not accounting for scr refresh
                image_dedos_pie_izquierdo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_dedos_pie_izquierdo, 'tStopRefresh')  # time at next scr refresh
                image_dedos_pie_izquierdo.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dedos_pie_izquierdoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dedos_pie_izquierdo"-------
    for thisComponent in dedos_pie_izquierdoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_dedos_pie_102seg_1_7min.addData('fondo_negro_12.started', fondo_negro_12.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('fondo_negro_12.stopped', fondo_negro_12.tStopRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('ind_dedos_izquierdo.started', ind_dedos_izquierdo.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('ind_dedos_izquierdo.stopped', ind_dedos_izquierdo.tStopRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('image_dedos_pie_izquierdo.started', image_dedos_pie_izquierdo.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('image_dedos_pie_izquierdo.stopped', image_dedos_pie_izquierdo.tStopRefresh)
    
    # ------Prepare to start Routine "DESCANSO"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DESCANSOComponents = [fondo_negro_7, descanso]
    for thisComponent in DESCANSOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DESCANSOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "DESCANSO"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DESCANSOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DESCANSOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_7* updates
        if fondo_negro_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_7.frameNStart = frameN  # exact frame index
            fondo_negro_7.tStart = t  # local t and not account for scr refresh
            fondo_negro_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_7, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_7.setAutoDraw(True)
        if fondo_negro_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_7.tStop = t  # not accounting for scr refresh
                fondo_negro_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_7, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_7.setAutoDraw(False)
        
        # *descanso* updates
        if descanso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            descanso.frameNStart = frameN  # exact frame index
            descanso.tStart = t  # local t and not account for scr refresh
            descanso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(descanso, 'tStartRefresh')  # time at next scr refresh
            descanso.setAutoDraw(True)
        if descanso.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > descanso.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                descanso.tStop = t  # not accounting for scr refresh
                descanso.frameNStop = frameN  # exact frame index
                win.timeOnFlip(descanso, 'tStopRefresh')  # time at next scr refresh
                descanso.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DESCANSOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DESCANSO"-------
    for thisComponent in DESCANSOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_dedos_pie_102seg_1_7min.addData('fondo_negro_7.started', fondo_negro_7.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('fondo_negro_7.stopped', fondo_negro_7.tStopRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('descanso.started', descanso.tStartRefresh)
    repeticion_dedos_pie_102seg_1_7min.addData('descanso.stopped', descanso.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'repeticion_dedos_pie_102seg_1_7min'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
