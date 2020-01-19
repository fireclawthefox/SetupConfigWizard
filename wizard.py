#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, time
import configparser
import importlib

from panda3d.core import loadPrcFileData
loadPrcFileData("", """
win-size 500 478
#win-fixed-size #t
""")

# We need showbase to make this script directly runnable
from direct.showbase.ShowBase import ShowBase

from panda3d.core import TextNode
from direct.gui import DirectGuiGlobals as DGG
from direct.gui.DirectCheckButton import DirectCheckButton

from wizardMainGUI import GUI as MainGUI
from wizardPatternElement import GUI as PatternElement
from wizardApplicationElement import GUI as ApplicationElement
from wizardProcessingScreen import GUI as ProcessingScreen
from wizardFileBrowser import WizardFileBrowser
from wizardTooltip import Tooltip

PLUGIN_LIBS = [
    "p3vision",
    "p3vrpn",
    "p3windisplay",
    "panda",
    "pandaai",
    "pandabullet",
    "pandaegg",
    "pandaexpress",
    "pandafx",
    "pandagl",
    "pandaode",
    "pandaphysics",
    "pandaskel",
    "p3assimp",
    "p3direct",
    "p3dtool",
    "p3dtoolconfig",
    "p3ffmpeg",
    "p3fmod_audio",
    "p3interrogatedb",
    "p3openal_audio",
    "p3ptloader",
    "p3tinydisplay"]

DEFAULT_PLUGINS = [
    "pandagl",
    "p3openal_audio"
]

class main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        base.win.set_clear_color((1,1,1,1))

        self.filePath = "~/setup.cfg"

        self.setup_config = configparser.ConfigParser()
        self.include_patterns = []
        self.exclude_patterns = []
        self.applications = []
        self.plugins = []

        self.tt = Tooltip()

        # setup main gui window
        self.main_gui = MainGUI(self.pixel2d)

        self.processingScreen = ProcessingScreen(self.pixel2d)
        self.processingScreen.frmProcessing["state"] = DGG.NORMAL
        self.processingScreen.frmProcessing.hide()

        self.loadPlugins()
        for plugin in self.plugins:
            if plugin["text"] in DEFAULT_PLUGINS:
                plugin["indicatorValue"] = True

        # catch GUI events
        self.accept("selectTab", self.selectTab)
        self.accept("addApplication", self.addApplication)
        self.accept("deploy", self.deploy)
        self.accept("load", self.load)
        self.accept("save", self.save)
        self.accept("addIncludePattern", self.addIncludePattern)
        self.accept("addExcludePattern", self.addExcludePattern)

        #HACK: scrollbar size
        self.main_gui.frmApplicationSelection["scrollBarWidth"] = 20
        self.main_gui.frmPluginSelection["scrollBarWidth"] = 20
        self.main_gui.frmIncludePatterns["scrollBarWidth"] = 20

        # Add some default entries
        self.addIncludePattern()
        self.include_patterns[0].txtPattern.set("**/*.png")

        self.addApplication()
        self.applications[0].txtName.set("Name")
        self.applications[0].txtPath.set("main.py")

        # select the first tab
        self.main_gui.rbMetadata.check()

        self.loadBrowser = WizardFileBrowser(self.loadExecute, True, defaultFilename="setup.cfg", tooltip=self.tt, fileExtensions=[".cfg"])
        self.loadBrowser.hide()
        self.saveBrowser = WizardFileBrowser(self.saveExecute, True, defaultFilename="setup.cfg", tooltip=self.tt, fileExtensions=[".cfg"])
        self.saveBrowser.hide()
        self.deployBrowser = WizardFileBrowser(self.deployExecute, True, defaultFilename="setup.py", tooltip=self.tt, fileExtensions=[".py"])
        self.deployBrowser.hide()

    def selectTab(self, tab):
        # Hide all tabs
        self.main_gui.frmMetadata.hide()
        self.main_gui.frmPlatforms.hide()
        self.main_gui.frmInclude.hide()
        self.main_gui.frmExclude.hide()
        self.main_gui.frmPlugins.hide()
        self.main_gui.frmApplications.hide()

        # only show the desired one
        if tab == "metadata":
            self.main_gui.frmMetadata.show()
        elif tab == "platforms":
            self.main_gui.frmPlatforms.show()
        elif tab == "include":
            self.main_gui.frmInclude.show()
        elif tab == "exclude":
            self.main_gui.frmExclude.show()
        elif tab == "plugins":
            self.main_gui.frmPlugins.show()
        elif tab == "applications":
            self.main_gui.frmApplications.show()

    def deploy(self):
        self.deployBrowser.folderMoveIn(os.path.dirname(self.filePath))
        self.deployBrowser.show()

    def deployExecute(self, ok):
        self.deployBrowser.hide()
        if not ok:
            return

        self.processingScreen.frmProcessing.show()
        base.graphicsEngine.renderFrame()
        base.graphicsEngine.renderFrame()

        script = self.deployBrowser.get()

        #
        # Check if we have an existing python script
        # create it if we don't
        #
        if not os.path.exists(script):
            with open(script, 'w') as py_setup_script:
                py_setup_script.write("from setuptools import setup\n")
                py_setup_script.write("setup()\n")

        #
        # Run the setup python script
        #
        folder_name = os.path.realpath(os.path.dirname(script))
        old_location = os.curdir
        try:
            os.chdir(folder_name)
            preArgv = sys.argv
            sys.argv = [os.path.split(script)[1], "bdist_apps"]
            pythonFilePath = script
            spec = importlib.util.spec_from_file_location("", pythonFilePath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            sys.argv = preArgv
        finally:
            os.chdir(old_location)

        self.processingScreen.frmProcessing.hide()

    def load(self):
        self.loadBrowser.folderMoveIn(os.path.dirname(self.filePath))
        self.loadBrowser.show()

    def loadExecute(self, ok):
        if not ok:
            self.loadBrowser.hide()
            return
        self.filePath = self.loadBrowser.get()
        self.setup_config.read(self.filePath)
        self.main_gui.txtAppName.set(self.setup_config.get("metadata", "name", fallback=""))
        self.main_gui.txtAuthor.set(self.setup_config.get("metadata", "author", fallback=""))

        #
        # Clear and load include patterns
        #
        while len(self.include_patterns) > 0:
            self.removeIncludePattern(0)
        inc_pattern = self.setup_config.get("build_apps", "include_patterns", fallback="")
        idx = 0
        if inc_pattern != "":
            for pattern in inc_pattern.strip().split("\n"):
                self.addIncludePattern()
                self.include_patterns[idx].txtPattern.set(pattern)
                idx += 1

        #
        # Clear and load exclude patterns
        #
        while len(self.exclude_patterns) > 0:
            self.removeExcludePattern(0)
        exc_pattern = self.setup_config.get("build_apps", "exclude_patterns", fallback="")
        idx = 0
        if exc_pattern != "":
            for pattern in exc_pattern.strip().split("\n"):
                self.addExcludePattern()
                self.exclude_patterns[idx].txtPattern.set(pattern)
                idx += 1

        #
        # Clear and load applications
        #
        while len(self.applications) > 0:
            self.removeApplication(0)
        gui_applications = self.setup_config.get("build_apps", "gui_apps", fallback="")
        idx = 0
        if gui_applications != "":
            for application in gui_applications.strip().split("\n"):
                name, path = gui_applications.split("=")
                self.addApplication()
                self.applications[idx].txtName.set(name.strip())
                self.applications[idx].txtPath.set(path.strip())
                idx += 1

        console_applications = self.setup_config.get("build_apps", "console_apps", fallback="")
        if console_applications != "":
            for applicatin in console_applications.strip().split("\n"):
                name, path = console_applications.split("=")
                self.addApplication()
                self.applications[idx].txtName.set(name.strip())
                self.applications[idx].txtPath.set(path.strip())
                self.applications[idx].cbTerminalApp["indicatorValue"] = True
                idx += 1

        #
        # Clear and load latforms
        #
        platforms = self.setup_config.get("build_apps", "platforms", fallback="")
        self.main_gui.cbLinux["indicatorValue"] = False
        self.main_gui.cbMacOS["indicatorValue"] = False
        self.main_gui.cbWindows["indicatorValue"] = False
        self.main_gui.cbAndroid["indicatorValue"] = False
        if platforms != "":
            split_platforms = platforms.strip().split("\n")
            if "manylinux1_x86_64" in split_platforms:
                self.main_gui.cbLinux["indicatorValue"] = True
            if "macosx_10_6_x86_64" in split_platforms:
                self.main_gui.cbMacOS["indicatorValue"] = True
            if "win_amd64" in split_platforms:
                self.main_gui.cbWindows["indicatorValue"] = True
        else:
            # Default selection
            self.main_gui.cbLinux["indicatorValue"] = True
            self.main_gui.cbMacOS["indicatorValue"] = True
            self.main_gui.cbWindows["indicatorValue"] = True

        #
        # Clear and load plugins
        #
        plugins = self.setup_config.get("build_apps", "plugins", fallback="")
        for plugin in self.plugins:
            plugin["indicatorValue"] = False
        if plugins != "":
            split_plugins = plugins.strip().split("\n")
            for plugin in self.plugins:
                if plugin["text"] in split_plugins:
                    plugin["indicatorValue"] = True
        else:
            for plugin in self.plugins:
                if plugin["text"] in DEFAULT_PLUGINS:
                    plugin["indicatorValue"] = True

        self.loadBrowser.hide()

    def save(self):
        self.saveBrowser.folderMoveIn(os.path.dirname(self.filePath))
        self.saveBrowser.show()

    def saveExecute(self, ok):
        if not ok:
            self.saveBrowser.hide()
            return
        self.filePath = self.saveBrowser.get()

        #
        # METADATA
        #
        self.setup_config["metadata"] = {}
        self.setup_config["metadata"]["name"] = self.main_gui.txtAppName.get()
        self.setup_config["metadata"]["author"] = self.main_gui.txtAuthor.get()

        #
        # BUILD APPS
        #
        self.setup_config["build_apps"] = {}

        #
        # include patterns
        #
        inc_pattern = ""
        for patternElement in self.include_patterns:
            inc_pattern += patternElement.txtPattern.get() + "\n"
        if inc_pattern != "":
            self.setup_config["build_apps"]["include_patterns"] = inc_pattern.rstrip()

        #
        # exclude patterns
        #
        exc_pattern = ""
        for patternElement in self.exclude_patterns:
            exc_pattern += patternElement.txtPattern.get() + "\n"
        if exc_pattern != "":
            self.setup_config["build_apps"]["exclude_patterns"] = exc_pattern.rstrip()

        #
        # GUI and console apps
        #
        gui_applications = ""
        console_applications = ""
        for applicationElement in self.applications:
            entry = applicationElement.txtName.get() + "=" + applicationElement.txtPath.get() + "\n"
            if applicationElement.cbTerminalApp["indicatorValue"]:
                console_applications += entry
            else:
                gui_applications += entry
        self.setup_config["build_apps"]["gui_apps"] = gui_applications.rstrip()
        self.setup_config["build_apps"]["console_apps"] = console_applications.rstrip()

        #
        # plugins
        #
        plugins = ""
        for plugin in self.plugins:
            if plugin["indicatorValue"]:
                plugins += plugin["text"] + "\n"
        self.setup_config["build_apps"]["plugins"] = plugins.rstrip()

        #
        # platforms
        #
        platforms = ""
        if self.main_gui.cbLinux["indicatorValue"]:
            platforms += "manylinux1_x86_64\n"
        if self.main_gui.cbMacOS["indicatorValue"]:
            platforms += "macosx_10_6_x86_64\n"
        if self.main_gui.cbWindows["indicatorValue"]:
            platforms += "win_amd64\n"
        #if self.main_gui.cbAndroid["indicatorValue"]:
        #    platforms += "android\n"
        self.setup_config["build_apps"]["platforms"] = platforms.rstrip()

        #
        # SAVE SETUP CONFIG FILE
        #
        with open(self.filePath, 'w') as configfile:
            self.setup_config.write(configfile)

        # finally hide the browser
        self.saveBrowser.hide()

    def loadPlugins(self):
        z = 10
        for i in range(len(PLUGIN_LIBS)):
            if i%2 == 0:
                z -= 20

            x = i%2 * 200 - 125
            self.plugins.append(DirectCheckButton(
                pos=(x,0,z),
                pad=(4,4),
                text_align=TextNode.ALeft,
                text_scale=24,
                borderWidth=(0, 0),
                text=PLUGIN_LIBS[i],
                indicator_text_scale=24,
                indicator_borderWidth=(2, 2),
                parent=self.main_gui.frmPluginSelection.getCanvas(),
                scale=0.5))
            self.plugins[-1].indicator["text"] = (" ", "X")
        cs = self.main_gui.frmPluginSelection["canvasSize"]
        self.main_gui.frmPluginSelection["canvasSize"] = (
            cs[0], cs[1], z, cs[3])

    def addApplication(self):
        element_id = len(self.applications)

        element = ApplicationElement(self.main_gui.frmApplicationSelection.getCanvas())
        element.txtName.setZ(element.txtName.getZ() - element_id * 24)
        element.txtPath.setZ(element.txtPath.getZ() - element_id * 24)
        element.cbTerminalApp.setZ(element.cbTerminalApp.getZ() - element_id * 24)
        element.btnRemove.setZ(element.btnRemove.getZ() - element_id * 24)
        element.btnRemove["command"] = self.removeApplication
        element.btnRemove["extraArgs"] = [element_id]

        self.applications.append(element)

        # recalculate the canvas of the Include Pattern frame
        cs = self.main_gui.frmApplicationSelection["canvasSize"]
        self.main_gui.frmApplicationSelection["canvasSize"] = (
            cs[0], cs[1], element_id * -27, cs[3])
        self.main_gui.frmApplicationSelection.setCanvasSize()

    def removeApplication(self, application_index):
        self.applications[application_index]

        for i in range(len(self.applications)):
            if i == application_index:
                element = self.applications[i]
                element.txtName.destroy()
                element.txtPath.destroy()
                element.cbTerminalApp.destroy()
                element.btnRemove.destroy()
            elif i > application_index:
                newIndex = i-1
                element = self.applications[i]
                element.txtName.setZ(element.txtName.getZ() + 24)
                element.txtPath.setZ(element.txtPath.getZ() + 24)
                element.cbTerminalApp.setZ(element.cbTerminalApp.getZ() + 24)
                element.btnRemove.setZ(element.btnRemove.getZ() + 24)
                element.btnRemove["extraArgs"] = [newIndex]
                self.applications[newIndex] = self.applications[i]

        # rmove the last, now empty index
        del self.applications[-1]

        # recalculate the canvas of the Include Pattern frame
        cs = self.main_gui.frmApplicationSelection["canvasSize"]
        self.main_gui.frmApplicationSelection["canvasSize"] = (
            cs[0], cs[1], len(self.applications) * 24, cs[3])
        self.main_gui.frmApplicationSelection.setCanvasSize()

    def addIncludePattern(self):
        element_id = len(self.include_patterns)

        element = PatternElement(self.main_gui.frmIncludePatterns.getCanvas())
        element.txtPattern.setZ(element.txtPattern.getZ() - element_id * 24)
        element.btnRemove.setZ(element.btnRemove.getZ() - element_id * 24)
        element.btnRemove["command"] = self.removeIncludePattern
        element.btnRemove["extraArgs"] = [element_id]

        self.include_patterns.append(element)

        # recalculate the canvas of the Include Pattern frame
        cs = self.main_gui.frmIncludePatterns["canvasSize"]
        self.main_gui.frmIncludePatterns["canvasSize"] = (
            cs[0], cs[1], element_id * -27, cs[3])
        self.main_gui.frmIncludePatterns.setCanvasSize()

    def removeIncludePattern(self, pattern_index):
        self.include_patterns[pattern_index]

        for i in range(len(self.include_patterns)):
            if i == pattern_index:
                element = self.include_patterns[i]
                element.txtPattern.destroy()
                element.btnRemove.destroy()
            elif i > pattern_index:
                newIndex = i-1
                element = self.include_patterns[i]
                element.txtPattern.setZ(element.txtPattern.getZ() + 24)
                element.btnRemove.setZ(element.btnRemove.getZ() + 24)
                element.btnRemove["extraArgs"] = [newIndex]
                self.include_patterns[newIndex] = self.include_patterns[i]

        # rmove the last, now empty index
        del self.include_patterns[-1]

        # recalculate the canvas of the Include Pattern frame
        cs = self.main_gui.frmIncludePatterns["canvasSize"]
        self.main_gui.frmIncludePatterns["canvasSize"] = (
            cs[0], cs[1], len(self.include_patterns) * 24, cs[3])
        self.main_gui.frmIncludePatterns.setCanvasSize()

    def addExcludePattern(self):
        element_id = len(self.exclude_patterns)

        element = PatternElement(self.main_gui.frmExcludePatterns.getCanvas())
        element.txtPattern.setZ(element.txtPattern.getZ() - element_id * 24)
        element.btnRemove.setZ(element.btnRemove.getZ() - element_id * 24)
        element.btnRemove["command"] = self.removeExcludePattern
        element.btnRemove["extraArgs"] = [element_id]

        self.exclude_patterns.append(element)

        # recalculate the canvas of the Exclude Pattern frame
        cs = self.main_gui.frmExcludePatterns["canvasSize"]
        self.main_gui.frmExcludePatterns["canvasSize"] = (
            cs[0], cs[1], element_id * -27, cs[3])
        self.main_gui.frmExcludePatterns.setCanvasSize()

    def removeExcludePattern(self, pattern_index):
        self.exclude_patterns[pattern_index]

        for i in range(len(self.exclude_patterns)):
            if i == pattern_index:
                element = self.exclude_patterns[i]
                element.txtPattern.destroy()
                element.btnRemove.destroy()
            elif i > pattern_index:
                newIndex = i-1
                element = self.exclude_patterns[i]
                element.txtPattern.setZ(element.txtPattern.getZ() + 24)
                element.btnRemove.setZ(element.btnRemove.getZ() + 24)
                element.btnRemove["extraArgs"] = [newIndex]
                self.exclude_patterns[newIndex] = self.exclude_patterns[i]

        # rmove the last, now empty index
        del self.exclude_patterns[-1]

        # recalculate the canvas of the Exclude Pattern frame
        cs = self.main_gui.frmExcludePatterns["canvasSize"]
        self.main_gui.frmExcludePatterns["canvasSize"] = (
            cs[0], cs[1], len(self.exclude_patterns) * 24, cs[3])
        self.main_gui.frmExcludePatterns.setCanvasSize()

# Create a ShowBase instance to make this gui directly runnable
app = main()
app.run()
