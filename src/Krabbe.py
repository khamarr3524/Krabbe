#########################################################################################
# Krabbe Engine                                                                         #
#########################################################################################
# Author: tagon35                                                                       #
#########################################################################################
# Current Version: 1.0                                                                  #
# Read changelog.txt for more information                                               #
#########################################################################################
# Krabbe Engine is a simple python engine that facilitates the creation of shell games. #
# Shell games run from the command line / terminal. The engine is focused on text-based #
# adventure games (games that only print text to the screen).                           #
# The core of the engine is written in Python 3.10 and users can extend the engine by   #
# writing lua plugins.                                                                  #
#########################################################################################

import os
import sys
import time
import json
import random
import threading
import traceback
import importlib.util
import platform
import textwrap
import re
import datetime
import copy
import math
import argparse
import logging
import logging.handlers
import subprocess
import shlex
import signal
import locale
import gettext
import codecs
import hashlib
import base64
import zlib
import io
import urllib.parse
import urllib.request
import urllib.error

# Constants
VERSION = "1.0"
AUTHOR = "tagon35"
ENGINE_NAME = "Krabbe Engine"
DEBUG_LEVEL = logging.DEBUG
TEXT_WIDTH = 100

# Global variables
game = None
game_path = None
game_data = None

# Logging
logger = logging.getLogger("Krabbe")
logger.setLevel(DEBUG_LEVEL)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Lua
lua = None
lua_thread = None
lua_thread_stop = False
lua_thread_lock = threading.Lock()

# Localization
locale.setlocale(locale.LC_ALL, "")
gettext.bindtextdomain("krabbe", "locale")
gettext.textdomain("krabbe")

# The Krabbe class

class Krabbe:
    logo = [
        "    __ __            __    __            ______            _          ",
        "   / //_/_________ _/ /_  / /_  ___     / ____/___  ____ _(_)___  ___ ",
        "  / ,<  / ___/ __ `/ __ \/ __ \/ _ \   / __/ / __ \/ __ `/ / __ \/ _ \\",
        " / /| |/ /  / /_/ / /_/ / /_/ /  __/  / /___/ / / / /_/ / / / / /  __/",
        "/_/ |_/_/   \__,_/_.___/_.___/\___/  /_____/_/ /_/\__, /_/_/ /_/\___/ ",
        "                                                 /____/               "
    ]

    def get_input(self, prompt):
        return input(prompt)
    
    def get_input_int(self, prompt):
        while True:
            try:
                return int(self.get_input(prompt))
            except ValueError:
                pass
    
    def get_input_float(self, prompt):
        while True:
            try:
                return float(self.get_input(prompt))
            except ValueError:
                pass
    
    def get_input_bool(self, prompt):
        while True:
            value = self.get_input(prompt).lower()
            if value == "yes" or value == "y" or value == "true" or value == "t":
                return True
            if value == "no" or value == "n" or value == "false" or value == "f":
                return False
    
    def get_input_list(self, prompt, options):
        print("Options: " + ", ".join(options))
        while True:
            value = self.get_input(prompt).lower()
            if value in options:
                return value
            
    def print_text(self, text):
        print(textwrap.fill(text, TEXT_WIDTH))
    
    def print_text_centered(self, text):
        print(textwrap.fill(text, TEXT_WIDTH).center(TEXT_WIDTH))

    def print_text_wrapped(self, text):
        print(textwrap.fill(text, TEXT_WIDTH))

    def print_text_wrapped_centered(self, text):
        print(textwrap.fill(text, TEXT_WIDTH).center(TEXT_WIDTH))

    def print_text_wrapped_centered_with_border(self, text):
        print("+" + "-" * (TEXT_WIDTH - 2) + "+")
        for line in textwrap.wrap(text, TEXT_WIDTH - 4):
            print("| " + line.center(TEXT_WIDTH - 4) + " |")
        print("+" + "-" * (TEXT_WIDTH - 2) + "+")

    def print_text_wrapped_with_border(self, text):
        print("+" + "-" * (TEXT_WIDTH - 2) + "+")
        for line in textwrap.wrap(text, TEXT_WIDTH - 4):
            print("| " + line.ljust(TEXT_WIDTH - 4) + " |")
        print("+" + "-" * (TEXT_WIDTH - 2) + "+")

    def print_logo(self):
        for line in self.logo:
            self.print_text(line)

    def print_version(self):
        print(ENGINE_NAME + " v" + VERSION + " by " + AUTHOR)
    
    def print_help(self):
        print("Currently under construction...")

    def __init__(self) -> None:
        self.print_logo()
        self.print_version()
        self.print_help()
        self.print_text("Press Enter to continue...")