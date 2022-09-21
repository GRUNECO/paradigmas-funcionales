#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on septiembre 13, 2022, at 17:52
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
expName = 'BL'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\LAURA\\Documents\\UDEA\\Gruneco\\Proyecto Resonador\\Paradigma y áreas función motora\\boca_lengua\\BL_lastrun.py',
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
bienvenida = visual.TextStim(win=win, name='bienvenida',
    text='BIENVENIDO\n\nEn breves segundos comenzará a realizar las actividades previamente indicadas',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "inicio_labios"
inicio_labiosClock = core.Clock()
fondo_negro_2 = visual.Rect(
    win=win, name='fondo_negro_2',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
ind_fruncir = visual.TextStim(win=win, name='ind_fruncir',
    text='FRUNCIR Y RELAJAR LABIOS',
    font='Open Sans',
    pos=(0, 0.25), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
video_fruncir = visual.MovieStim3(
    win=win, name='video_fruncir', units='',
    noAudio = True,
    filename='video_fruncir.mov',
    ori=0.0, pos=(0, -0.15), opacity=None,
    loop=True, anchor='center',
    size=(0.5,0.5),
    depth=-2.0,
    )

# Initialize components for Routine "DESCANSO"
DESCANSOClock = core.Clock()
fondo_negro_3 = visual.Rect(
    win=win, name='fondo_negro_3',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
ind_descanso = visual.TextStim(win=win, name='ind_descanso',
    text='DESCANSO',
    font='Open Sans',
    pos=(0, 0), height=0.17, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "inicio_lengua"
inicio_lenguaClock = core.Clock()
fondo_negro_ = visual.Rect(
    win=win, name='fondo_negro_',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
ind_lengua = visual.TextStim(win=win, name='ind_lengua',
    text='MOVER LA LENGUA \nHACIA LA DERECHA E IZQUIERDA\nCON LA BOCA CERRADA',
    font='Open Sans',
    pos=(0, 0.27), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
video_lengua = visual.MovieStim3(
    win=win, name='video_lengua', units='',
    noAudio = True,
    filename='video_lengua.mov',
    ori=0.0, pos=(0, -0.15), opacity=None,
    loop=True, anchor='center',
    size=(0.5,0.5),
    depth=-2.0,
    )

# Initialize components for Routine "DESCANSO"
DESCANSOClock = core.Clock()
fondo_negro_3 = visual.Rect(
    win=win, name='fondo_negro_3',
    width=(3, 1)[0], height=(3, 1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
ind_descanso = visual.TextStim(win=win, name='ind_descanso',
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
BienvenidoComponents = [fondo_negro, bienvenida]
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
    
    # *bienvenida* updates
    if bienvenida.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bienvenida.frameNStart = frameN  # exact frame index
        bienvenida.tStart = t  # local t and not account for scr refresh
        bienvenida.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bienvenida, 'tStartRefresh')  # time at next scr refresh
        bienvenida.setAutoDraw(True)
    if bienvenida.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bienvenida.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            bienvenida.tStop = t  # not accounting for scr refresh
            bienvenida.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bienvenida, 'tStopRefresh')  # time at next scr refresh
            bienvenida.setAutoDraw(False)
    
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
thisExp.addData('bienvenida.started', bienvenida.tStartRefresh)
thisExp.addData('bienvenida.stopped', bienvenida.tStopRefresh)

# set up handler to look after randomisation of conditions etc
repeticion_labios = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeticion_labios')
thisExp.addLoop(repeticion_labios)  # add the loop to the experiment
thisRepeticion_labio = repeticion_labios.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeticion_labio.rgb)
if thisRepeticion_labio != None:
    for paramName in thisRepeticion_labio:
        exec('{} = thisRepeticion_labio[paramName]'.format(paramName))

for thisRepeticion_labio in repeticion_labios:
    currentLoop = repeticion_labios
    # abbreviate parameter names if possible (e.g. rgb = thisRepeticion_labio.rgb)
    if thisRepeticion_labio != None:
        for paramName in thisRepeticion_labio:
            exec('{} = thisRepeticion_labio[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "inicio_labios"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    inicio_labiosComponents = [fondo_negro_2, ind_fruncir, video_fruncir]
    for thisComponent in inicio_labiosComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    inicio_labiosClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "inicio_labios"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = inicio_labiosClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=inicio_labiosClock)
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
        
        # *ind_fruncir* updates
        if ind_fruncir.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ind_fruncir.frameNStart = frameN  # exact frame index
            ind_fruncir.tStart = t  # local t and not account for scr refresh
            ind_fruncir.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ind_fruncir, 'tStartRefresh')  # time at next scr refresh
            ind_fruncir.setAutoDraw(True)
        if ind_fruncir.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ind_fruncir.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ind_fruncir.tStop = t  # not accounting for scr refresh
                ind_fruncir.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ind_fruncir, 'tStopRefresh')  # time at next scr refresh
                ind_fruncir.setAutoDraw(False)
        
        # *video_fruncir* updates
        if video_fruncir.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            video_fruncir.frameNStart = frameN  # exact frame index
            video_fruncir.tStart = t  # local t and not account for scr refresh
            video_fruncir.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(video_fruncir, 'tStartRefresh')  # time at next scr refresh
            video_fruncir.setAutoDraw(True)
        if video_fruncir.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > video_fruncir.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                video_fruncir.tStop = t  # not accounting for scr refresh
                video_fruncir.frameNStop = frameN  # exact frame index
                win.timeOnFlip(video_fruncir, 'tStopRefresh')  # time at next scr refresh
                video_fruncir.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inicio_labiosComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "inicio_labios"-------
    for thisComponent in inicio_labiosComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_labios.addData('fondo_negro_2.started', fondo_negro_2.tStartRefresh)
    repeticion_labios.addData('fondo_negro_2.stopped', fondo_negro_2.tStopRefresh)
    repeticion_labios.addData('ind_fruncir.started', ind_fruncir.tStartRefresh)
    repeticion_labios.addData('ind_fruncir.stopped', ind_fruncir.tStopRefresh)
    video_fruncir.stop()
    
    # ------Prepare to start Routine "DESCANSO"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DESCANSOComponents = [fondo_negro_3, ind_descanso]
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
            if tThisFlipGlobal > fondo_negro_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_3.tStop = t  # not accounting for scr refresh
                fondo_negro_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_3, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_3.setAutoDraw(False)
        
        # *ind_descanso* updates
        if ind_descanso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ind_descanso.frameNStart = frameN  # exact frame index
            ind_descanso.tStart = t  # local t and not account for scr refresh
            ind_descanso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ind_descanso, 'tStartRefresh')  # time at next scr refresh
            ind_descanso.setAutoDraw(True)
        if ind_descanso.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ind_descanso.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                ind_descanso.tStop = t  # not accounting for scr refresh
                ind_descanso.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ind_descanso, 'tStopRefresh')  # time at next scr refresh
                ind_descanso.setAutoDraw(False)
        
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
    repeticion_labios.addData('fondo_negro_3.started', fondo_negro_3.tStartRefresh)
    repeticion_labios.addData('fondo_negro_3.stopped', fondo_negro_3.tStopRefresh)
    repeticion_labios.addData('ind_descanso.started', ind_descanso.tStartRefresh)
    repeticion_labios.addData('ind_descanso.stopped', ind_descanso.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'repeticion_labios'


# set up handler to look after randomisation of conditions etc
repeticion_lengua = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeticion_lengua')
thisExp.addLoop(repeticion_lengua)  # add the loop to the experiment
thisRepeticion_lengua = repeticion_lengua.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeticion_lengua.rgb)
if thisRepeticion_lengua != None:
    for paramName in thisRepeticion_lengua:
        exec('{} = thisRepeticion_lengua[paramName]'.format(paramName))

for thisRepeticion_lengua in repeticion_lengua:
    currentLoop = repeticion_lengua
    # abbreviate parameter names if possible (e.g. rgb = thisRepeticion_lengua.rgb)
    if thisRepeticion_lengua != None:
        for paramName in thisRepeticion_lengua:
            exec('{} = thisRepeticion_lengua[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "inicio_lengua"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    inicio_lenguaComponents = [fondo_negro_, ind_lengua, video_lengua]
    for thisComponent in inicio_lenguaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    inicio_lenguaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "inicio_lengua"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = inicio_lenguaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=inicio_lenguaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fondo_negro_* updates
        if fondo_negro_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fondo_negro_.frameNStart = frameN  # exact frame index
            fondo_negro_.tStart = t  # local t and not account for scr refresh
            fondo_negro_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fondo_negro_, 'tStartRefresh')  # time at next scr refresh
            fondo_negro_.setAutoDraw(True)
        if fondo_negro_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fondo_negro_.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_.tStop = t  # not accounting for scr refresh
                fondo_negro_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_.setAutoDraw(False)
        
        # *ind_lengua* updates
        if ind_lengua.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ind_lengua.frameNStart = frameN  # exact frame index
            ind_lengua.tStart = t  # local t and not account for scr refresh
            ind_lengua.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ind_lengua, 'tStartRefresh')  # time at next scr refresh
            ind_lengua.setAutoDraw(True)
        if ind_lengua.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ind_lengua.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ind_lengua.tStop = t  # not accounting for scr refresh
                ind_lengua.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ind_lengua, 'tStopRefresh')  # time at next scr refresh
                ind_lengua.setAutoDraw(False)
        
        # *video_lengua* updates
        if video_lengua.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            video_lengua.frameNStart = frameN  # exact frame index
            video_lengua.tStart = t  # local t and not account for scr refresh
            video_lengua.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(video_lengua, 'tStartRefresh')  # time at next scr refresh
            video_lengua.setAutoDraw(True)
        if video_lengua.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > video_lengua.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                video_lengua.tStop = t  # not accounting for scr refresh
                video_lengua.frameNStop = frameN  # exact frame index
                win.timeOnFlip(video_lengua, 'tStopRefresh')  # time at next scr refresh
                video_lengua.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inicio_lenguaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "inicio_lengua"-------
    for thisComponent in inicio_lenguaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeticion_lengua.addData('fondo_negro_.started', fondo_negro_.tStartRefresh)
    repeticion_lengua.addData('fondo_negro_.stopped', fondo_negro_.tStopRefresh)
    repeticion_lengua.addData('ind_lengua.started', ind_lengua.tStartRefresh)
    repeticion_lengua.addData('ind_lengua.stopped', ind_lengua.tStopRefresh)
    video_lengua.stop()
    
    # ------Prepare to start Routine "DESCANSO"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DESCANSOComponents = [fondo_negro_3, ind_descanso]
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
            if tThisFlipGlobal > fondo_negro_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fondo_negro_3.tStop = t  # not accounting for scr refresh
                fondo_negro_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fondo_negro_3, 'tStopRefresh')  # time at next scr refresh
                fondo_negro_3.setAutoDraw(False)
        
        # *ind_descanso* updates
        if ind_descanso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ind_descanso.frameNStart = frameN  # exact frame index
            ind_descanso.tStart = t  # local t and not account for scr refresh
            ind_descanso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ind_descanso, 'tStartRefresh')  # time at next scr refresh
            ind_descanso.setAutoDraw(True)
        if ind_descanso.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ind_descanso.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                ind_descanso.tStop = t  # not accounting for scr refresh
                ind_descanso.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ind_descanso, 'tStopRefresh')  # time at next scr refresh
                ind_descanso.setAutoDraw(False)
        
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
    repeticion_lengua.addData('fondo_negro_3.started', fondo_negro_3.tStartRefresh)
    repeticion_lengua.addData('fondo_negro_3.stopped', fondo_negro_3.tStopRefresh)
    repeticion_lengua.addData('ind_descanso.started', ind_descanso.tStartRefresh)
    repeticion_lengua.addData('ind_descanso.stopped', ind_descanso.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'repeticion_lengua'


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
