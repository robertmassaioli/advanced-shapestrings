# SPDX-License-Identifier: LGPL-2.1-only
# SPDX-FileNotice: Part of the ShapeStrings addon.

from .Commands import registerCommands
from .Toolbar import extendToolbar
from .paths import get_translation_directory

from FreeCAD import Gui


Gui.addLanguagePath(get_translation_directory())
Gui.updateLocale()

registerCommands()
extendToolbar()
