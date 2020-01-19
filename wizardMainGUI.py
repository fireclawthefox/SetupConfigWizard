#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectButton import DirectButton
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectCheckButton import DirectCheckButton
from direct.gui.DirectScrolledFrame import DirectScrolledFrame
from direct.gui.DirectRadioButton import DirectRadioButton
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):
        
        self.btnDeploy = DirectButton(
            borderWidth=(2, 2),
            frameColor=(0.2, 0.9, 0.2, 1.0),
            frameSize=(-250.0, 250.0, -8.1, 19.4),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -470),
            scale=LVecBase3f(1, 1, 1),
            text='Deploy',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0.0, 3.0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["deploy"],
        )

        self.btnLoad = DirectButton(
            borderWidth=(2, 2),
            frameSize=(-125.0, 125.0, -4.7, 19.4),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(375, 0, -445),
            scale=LVecBase3f(1, 1, 1),
            text='Load',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0.0, 4.0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["load"],
        )

        self.lblHeader = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.25, 0.25, 0.25, 1.0),
            frameSize=(-250.0, 250.0, -20.0, 30.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -30),
            scale=LVecBase3f(1, 1, 1),
            text='Panda3D Setup Creation Wizard',
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0.25, 0.25, 0.25, 1),
            parent=rootParent,
        )

        self.btnSave = DirectButton(
            borderWidth=(2, 2),
            frameSize=(-125.0, 125.0, -4.7, 19.4),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(125, 0, -445),
            scale=LVecBase3f(1, 1, 1),
            text='Save',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0.0, 4.0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["save"],
        )

        self.frmMetadata = DirectFrame(
            borderWidth=(2, 2),
            frameColor=(1, 1, 1, 1),
            frameSize=(-250.0, 250.0, -180.0, 150.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -245),
            relief=3,
            parent=rootParent,
        )

        self.lblAppName = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.0, 0.0, 0.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-140, 0, 70),
            scale=LVecBase3f(1, 1, 1),
            text='Application Name',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmMetadata,
        )

        self.txtAppName = DirectEntry(
            borderWidth=(0.1666, 0.166),
            hpr=LVecBase3f(0, 0, 0),
            overflow=1,
            pos=LPoint3f(-60, 0, 70),
            scale=LVecBase3f(12, 12, 12),
            width=20.0,
            text_align=TextNode.A_left,
            text_scale=(1.0, 1.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmMetadata,
        )

        self.frmPlatforms = DirectFrame(
            borderWidth=(2, 2),
            frameColor=(1, 1, 1, 1),
            frameSize=(-250.0, 250.0, -180.0, 150.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -245),
            relief=3,
            parent=rootParent,
        )

        self.lblPlatforms = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.0, 0.0, 0.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 110),
            scale=LVecBase3f(1, 1, 1),
            text='Supported Platforms',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmPlatforms,
        )

        self.cbLinux = DirectCheckButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-250.0, 250.0, -12.25, 27.55),
            hpr=LVecBase3f(0, 0, 0),
            indicatorValue=1,
            pos=LPoint3f(0, 0, 65),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Linux',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-241.4, 0, 0.449999),
            indicator_relief='sunken',
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.2),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24.0, 24.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmPlatforms,
        )

        self.cbMacOS = DirectCheckButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-250.0, 250.0, -12.25, 27.55),
            hpr=LVecBase3f(0, 0, 0),
            indicatorValue=1,
            pos=LPoint3f(0, 0, 35),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='MacOS',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-241.4, 0, 0.449999),
            indicator_relief='sunken',
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.2),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmPlatforms,
        )

        self.cbWindows = DirectCheckButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-250.0, 250.0, -12.25, 27.55),
            hpr=LVecBase3f(0, 0, 0),
            indicatorValue=1,
            pos=LPoint3f(0, 0, 5),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Windows',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-241.4, 0, 0.449999),
            indicator_relief='sunken',
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.2),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmPlatforms,
        )

        self.cbAndroid = DirectCheckButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-250.0, 250.0, -12.25, 27.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, -70),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Android',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-241.4, 0, 0.449999),
            indicator_relief='sunken',
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.2),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmPlatforms,
        )

        self.lblDesktop = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.0, 0.0, 0.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 90),
            scale=LVecBase3f(1, 1, 1),
            text='Desktop',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmPlatforms,
        )

        self.lblMobile = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.0, 0.0, 0.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, -50),
            scale=LVecBase3f(1, 1, 1),
            text='Mobile',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmPlatforms,
        )

        self.lblMetadata = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.0, 0.0, 0.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 110),
            scale=LVecBase3f(1, 1, 1),
            text='Metadata',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmMetadata,
        )

        self.lblAuthor = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.0, 0.0, 0.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-140, 0, 40),
            scale=LVecBase3f(1, 1, 1),
            text='Author',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmMetadata,
        )

        self.txtAuthor = DirectEntry(
            borderWidth=(0.1666, 0.1666),
            hpr=LVecBase3f(0, 0, 0),
            overflow=1,
            pos=LPoint3f(-60, 0, 40),
            scale=LVecBase3f(12, 12, 12),
            width=20.0,
            text_align=TextNode.A_left,
            text_scale=(1.0, 1.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmMetadata,
        )

        self.frmPlugins = DirectFrame(
            borderWidth=(2, 2),
            frameColor=(1, 1, 1, 1),
            frameSize=(-250.0, 250.0, -180.0, 150.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -245),
            relief=3,
            parent=rootParent,
        )

        self.lblPlugins = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.0, 0.0, 0.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 110),
            scale=LVecBase3f(1, 1, 1),
            text='Plugins',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmPlugins,
        )

        self.frmApplications = DirectFrame(
            borderWidth=(2.0, 2.0),
            frameColor=(1, 1, 1, 1),
            frameSize=(-250.0, 250.0, -180.0, 150.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -245),
            relief=3,
            parent=rootParent,
        )

        self.lblApplication = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.0, 0.0, 0.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 110),
            scale=LVecBase3f(1, 1, 1),
            text='Applications',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmApplications,
        )

        self.btnAddApplication = DirectButton(
            borderWidth=(2, 2),
            frameSize=(-250.0, 250.0, -12.25, 27.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 70),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Add Application',
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmApplications,
            command=base.messenger.send,
            extraArgs=["addApplication"],
        )

        self.frmApplicationSelection = DirectScrolledFrame(
            canvasSize=(-215.0, 215.0, -300.0, 0.0),
            frameColor=(1.0, 1.0, 1.0, 1.0),
            frameSize=(-225.0, 225.0, -200.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 40),
            state='normal',
            horizontalScroll_borderWidth=(2, 2),
            horizontalScroll_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_pos=LPoint3f(0, 0, 0),
            horizontalScroll_decButton_borderWidth=(2, 2),
            horizontalScroll_decButton_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_decButton_pos=LPoint3f(0, 0, 0),
            horizontalScroll_incButton_borderWidth=(2, 2),
            horizontalScroll_incButton_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_incButton_pos=LPoint3f(0, 0, 0),
            horizontalScroll_thumb_borderWidth=(2, 2),
            horizontalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_thumb_pos=LPoint3f(0, 0, 0),
            verticalScroll_borderWidth=(2, 2),
            verticalScroll_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_pos=LPoint3f(0, 0, 0),
            verticalScroll_decButton_borderWidth=(2, 2),
            verticalScroll_decButton_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_decButton_pos=LPoint3f(215, 0, -10),
            verticalScroll_incButton_borderWidth=(2, 2),
            verticalScroll_incButton_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_incButton_pos=LPoint3f(215, 0, -190),
            verticalScroll_thumb_borderWidth=(2, 2),
            verticalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_thumb_pos=LPoint3f(215, 0, -73.3333),
            parent=self.frmApplications,
        )

        self.frmPluginSelection = DirectScrolledFrame(
            canvasSize=(-215.0, 215.0, -300.0, 0.0),
            frameColor=(1, 1, 1, 1),
            frameSize=(-225.0, 225.0, -240.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 80),
            state='normal',
            horizontalScroll_borderWidth=(2, 2),
            horizontalScroll_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_pos=LPoint3f(-11.7953, 0, -228),
            horizontalScroll_decButton_borderWidth=(2, 2),
            horizontalScroll_decButton_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_decButton_pos=LPoint3f(0, 0, 0),
            horizontalScroll_incButton_borderWidth=(2, 2),
            horizontalScroll_incButton_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_incButton_pos=LPoint3f(0, 0, 0),
            horizontalScroll_thumb_borderWidth=(2, 2),
            horizontalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_thumb_pos=LPoint3f(0, 0, 0),
            verticalScroll_borderWidth=(2, 2),
            verticalScroll_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_pos=LPoint3f(0, 0, 0),
            verticalScroll_decButton_borderWidth=(2, 2),
            verticalScroll_decButton_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_decButton_pos=LPoint3f(215, 0, -10),
            verticalScroll_incButton_borderWidth=(2, 2),
            verticalScroll_incButton_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_incButton_pos=LPoint3f(215, 0, -230),
            verticalScroll_thumb_borderWidth=(2, 2),
            verticalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_thumb_pos=LPoint3f(215, 0, -100),
            parent=self.frmPlugins,
        )

        self.rbMetadata = DirectRadioButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-86.25, 69.65, -6.25, 21.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(60, 0, -65),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Metadata',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-77.65, 0, 0.449999),
            indicator_relief=3,
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.25),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["selectTab", ["metadata"]],
            variable=[],
            value=[],
        )

        self.rbPlatforms = DirectRadioButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-86.25, 69.65, -6.25, 21.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(255, 0, -85),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Platforms',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-77.65, 0, 0.449999),
            indicator_relief=3,
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.25),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["selectTab", ["platforms"]],
            variable=[],
            value=[],
        )

        self.rbPlugins = DirectRadioButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-86.25, 69.65, -7.8, 21.55),
            hpr=LVecBase3f(0, 0, 0),
            indicatorValue=1,
            pos=LPoint3f(155, 0, -85),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Plugins',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-77.65, 0, -0.325001),
            indicator_relief=3,
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.25),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["selectTab", ["plugins"]],
            variable=[],
            value=[],
        )

        self.rbApplications = DirectRadioButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-86.25, 69.65, -8.1, 21.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(60, 0, -85),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Applications',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-77.65, 0, -0.475001),
            indicator_relief=3,
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.25),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["selectTab", ["applications"]],
            variable=[],
            value=[],
        )

        self.rbInclude = DirectRadioButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-86.25, 69.65, -8.1, 21.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(155, 0, -65),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Include',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-77.65, 0, -0.475001),
            indicator_relief=3,
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.25),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["selectTab", ["include"]],
            variable=[],
            value=[],
        )

        self.frmInclude = DirectFrame(
            borderWidth=(2, 2),
            frameColor=(1, 1, 1, 1),
            frameSize=(-250.0, 250.0, -180.0, 150.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -245),
            relief=3,
            parent=rootParent,
        )

        self.btnAddIncludePattern = DirectButton(
            borderWidth=(2, 2),
            frameSize=(-250.0, 250.0, -12.25, 27.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 70),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Add pattern',
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmInclude,
            command=base.messenger.send,
            extraArgs=["addIncludePattern"],
        )

        self.lblIncludePatterns = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 110),
            scale=LVecBase3f(1, 1, 1),
            text='Include Patterns',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmInclude,
        )

        self.frmIncludePatterns = DirectScrolledFrame(
            canvasSize=(-215.0, 215.0, -300.0, 0.0),
            frameColor=(1.0, 1.0, 1.0, 1.0),
            frameSize=(-225.0, 225.0, -200.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 40),
            state='normal',
            horizontalScroll_borderWidth=(2, 2),
            horizontalScroll_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_pos=LPoint3f(0, 0, 0),
            horizontalScroll_decButton_borderWidth=(2, 2),
            horizontalScroll_decButton_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_decButton_pos=LPoint3f(0, 0, 0),
            horizontalScroll_incButton_borderWidth=(2, 2),
            horizontalScroll_incButton_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_incButton_pos=LPoint3f(0, 0, 0),
            horizontalScroll_thumb_borderWidth=(2, 2),
            horizontalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_thumb_pos=LPoint3f(0, 0, 0),
            verticalScroll_borderWidth=(2, 2),
            verticalScroll_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_pos=LPoint3f(0, 0, 0),
            verticalScroll_decButton_borderWidth=(2, 2),
            verticalScroll_decButton_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_decButton_pos=LPoint3f(215, 0, -10),
            verticalScroll_incButton_borderWidth=(2, 2),
            verticalScroll_incButton_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_incButton_pos=LPoint3f(215, 0, -190),
            verticalScroll_thumb_borderWidth=(2, 2),
            verticalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_thumb_pos=LPoint3f(215, 0, -73.3333),
            parent=self.frmInclude,
        )

        self.lblNameCol = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-220, 0, 45),
            scale=LVecBase3f(1, 1, 1),
            text='Name',
            text_align=TextNode.A_left,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmApplications,
        )

        self.lblPathCol = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-95, 0, 45),
            scale=LVecBase3f(1, 1, 1),
            text='Path',
            text_align=TextNode.A_left,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmApplications,
        )

        self.lblTerminalCol = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(100, 0, 45),
            scale=LVecBase3f(1, 1, 1),
            text='Terminal App',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmApplications,
        )

        self.lblPatternCol = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-220, 0, 45),
            scale=LVecBase3f(1, 1, 1),
            text='Pattern',
            text_align=TextNode.A_left,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmInclude,
        )

        self.frmExclude = DirectFrame(
            borderWidth=(2, 2),
            frameColor=(1, 1, 1, 1),
            frameSize=(-250.0, 250.0, -180.0, 150.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(250, 0, -245),
            relief=3,
            parent=rootParent,
        )

        self.lblExcludePatterns = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 110),
            scale=LVecBase3f(1, 1, 1),
            text='Exclude Patterns',
            text_align=TextNode.A_center,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmExclude,
        )

        self.btnAddExcludePattern = DirectButton(
            borderWidth=(2, 2),
            frameSize=(-250.0, 250.0, -12.225, 27.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 70),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Add pattern',
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmExclude,
        )

        self.pg23054 = DirectLabel(
            borderWidth=(2, 2),
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-220, 0, 45),
            scale=LVecBase3f(1, 1, 1),
            text='Pattern',
            text_align=TextNode.A_left,
            text_scale=(12.0, 12.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=self.frmExclude,
        )

        self.frmExcludePatterns = DirectScrolledFrame(
            canvasSize=(-215.0, 215.0, -300.0, 0.0),
            frameColor=(1, 1, 1, 1),
            frameSize=(-225.0, 225.0, -200.0, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 40),
            state='normal',
            horizontalScroll_borderWidth=(2, 2),
            horizontalScroll_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_pos=LPoint3f(0, 0, 0),
            horizontalScroll_decButton_borderWidth=(2, 2),
            horizontalScroll_decButton_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_decButton_pos=LPoint3f(-215, 0, -190),
            horizontalScroll_incButton_borderWidth=(2, 2),
            horizontalScroll_incButton_frameSize=(-0.05, 0.05, -10.0, 10.0),
            horizontalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_incButton_pos=LPoint3f(195, 0, -190),
            horizontalScroll_thumb_borderWidth=(2, 2),
            horizontalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_thumb_pos=LPoint3f(-42.1845, 0, -190),
            verticalScroll_borderWidth=(2, 2),
            verticalScroll_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_pos=LPoint3f(0, 0, 0),
            verticalScroll_decButton_borderWidth=(2, 2),
            verticalScroll_decButton_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_decButton_pos=LPoint3f(215, 0, -10),
            verticalScroll_incButton_borderWidth=(2, 2),
            verticalScroll_incButton_frameSize=(-10.0, 10.0, -0.05, 0.05),
            verticalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_incButton_pos=LPoint3f(215, 0, -190),
            verticalScroll_thumb_borderWidth=(2, 2),
            verticalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_thumb_pos=LPoint3f(215, 0, -73.3333),
            parent=self.frmExclude,
        )

        self.rbExclude = DirectRadioButton(
            borderWidth=(0.0, 0.0),
            frameSize=(-86.25, 69.65, -8.1, 21.55),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(255, 0, -65),
            scale=LVecBase3f(0.5, 0.5, 0.5),
            text='Exclude',
            indicator_borderWidth=(2, 2),
            indicator_hpr=LVecBase3f(0, 0, 0),
            indicator_pos=LPoint3f(-77.65, 0, -0.475001),
            indicator_relief=3,
            indicator_text_align=TextNode.A_center,
            indicator_text_scale=(24, 24),
            indicator_text_pos=(0, -0.25),
            indicator_text_fg=LVecBase4f(0, 0, 0, 1),
            indicator_text_bg=LVecBase4f(0, 0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(24, 24),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["selectTab", ["exclude"]],
            variable=[],
            value=[],
        )

        self.rbMetadata.setOthers([self.rbMetadata,self.rbPlatforms,self.rbPlugins,self.rbApplications,self.rbInclude,self.rbExclude,])
        self.rbPlatforms.setOthers([self.rbMetadata,self.rbPlatforms,self.rbPlugins,self.rbApplications,self.rbInclude,self.rbExclude,])
        self.rbPlugins.setOthers([self.rbMetadata,self.rbPlatforms,self.rbPlugins,self.rbApplications,self.rbInclude,self.rbExclude,])
        self.rbApplications.setOthers([self.rbMetadata,self.rbPlatforms,self.rbPlugins,self.rbApplications,self.rbInclude,self.rbExclude,])
        self.rbInclude.setOthers([self.rbMetadata,self.rbPlatforms,self.rbPlugins,self.rbApplications,self.rbInclude,self.rbExclude,])
        self.rbExclude.setOthers([self.rbExclude,self.rbInclude,self.rbApplications,self.rbPlatforms,self.rbPlugins,self.rbMetadata,])
