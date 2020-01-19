#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectWaitBar import DirectWaitBar
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):
        
        self.frmProcessing = DirectFrame(
            borderWidth=(2, 2),
            frameColor=(1, 1, 1, 1),
            frameSize=(0.0, 500.0, -478.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )

        self.lblProcessing = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -210),
            scale=LVecBase3f(1, 1, 1),
            text='Processing...',
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmProcessing,
        )

        self.waitbar = DirectWaitBar(
            barColor=(0.35, 0.35, 0.5, 1.0),
            frameColor=(0.0, 0.0, 0.0, 1.0),
            frameSize=(-150.0, 150.0, -10.0, 10.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -250),
            scale=LVecBase3f(1, 1, 1),
            state='normal',
            text='50%',
            value=50.0,
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0.0, -2.5),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmProcessing,
        )

