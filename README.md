# SetupConfigWizard
A tool that will help you create setup configuration files for Panda3D applications and deploy them instantly

## Features
- Create setup config files
- Load existing config files
- Directly Deploy your apps

## Requirements
- Python 3.x
- Panda3D 1.10+

## Manual

### Startup
To start the Wizard, simply run the wizard.py script

<code>python wizard.py</code>

### Usage
1. Enter your information in the available categories.<br>Categories can be selected at the top.
2. Save your configuration as setup.cfg
3. Deploy your game by selecting a setup.py script in the same location as your setup.cfg file.<br>**NOTE:** The setup.py script doesn't have to exist, the wizard will automatically create a simple script for you.

### Custom Entries
The wizard will keep custom entries of loaded config files. They can't be edited in the wizard yet.
