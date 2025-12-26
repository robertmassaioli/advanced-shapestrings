# SPDX-License-Identifier: LGPL-2.1-only
# SPDX-FileNotice: Part of the ShapeStrings addon.

import FreeCADGui as Gui
import FreeCAD as App
from draftutils.messages import _msg
from .paths import get_icon_path, get_translation_directory
from . import AdvancedShapestringTools

# Fallback-safe translate helpers and toolbox entries (inlined from gui_common)
try:
    import FreeCAD as App

    QT_TRANSLATE_NOOP = App.Qt.QT_TRANSLATE_NOOP

    def translate(context, text):
        return App.Qt.translate(context, text)
except Exception:
    def QT_TRANSLATE_NOOP(context, text):
        return text

    def translate(context, text):
        return text
    
TOOLBOX = [
    "AdvancedShapestrings_SpacedShapeString", 
    "AdvancedShapestrings_RadialShapeString",
]

# Add translations path
Gui.addLanguagePath(get_translation_directory())
Gui.updateLocale()

class AdvancedShapestrings(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("Workbench", "Shapestrings")
    ToolTip = translate("Workbench", "Many more Shapestring tools")
    Icon = get_icon_path("Workbench.svg")
    toolbox = TOOLBOX

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """

        try:
            ## Init so that we can use the draft tools
            import DraftGui
            import draftguitools.gui_snapper
            if not hasattr(Gui,"draftToolBar"):
                Gui.draftToolBar = DraftGui.DraftToolBar()    
            if not hasattr(Gui,"Snapper"):
                Gui.Snapper = draftguitools.gui_snapper.Snapper()
            App.activeDraftCommand = None

        except Exception as exc:
            App.Console.PrintError(exc)
            App.Console.PrintError("Error: Initializing one or more "
                                       "of the Draft modules failed, "
                                       "Draft will not work as expected.\n")

        _msg(translate(
            "Log",
            "Switching to advanced_shapestrings") + "\n")

        # NOTE: Context for this commands must be "Workbench"
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench", "Shapestring Tools"), self.toolbox)
        self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "Shapestring Tools"), self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        App.Console.PrintMessage(translate(
            "Log",
            "Workbench advanced_shapestrings activated.") + "\n")

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        if hasattr(Gui, "draftToolBar"):
            Gui.draftToolBar.Deactivated()
        if hasattr(Gui, "Snapper"):
            Gui.Snapper.hide()
        
        App.Console.PrintMessage(translate(
            "Log",
            "Workbench advanced_shapestrings de-activated.") + "\n")

# Register the workbench class with FreeCAD
Gui.addWorkbench(AdvancedShapestrings())

def _on_workbench_activated():
    wb = Gui.activeWorkbench()
    # Ensure we have the Python wrapper, not just the C++ instance
    if not hasattr(wb, "__Workbench__"):
        return
    # Only run when Draft is actually active
    if wb.__class__.__name__ == "DraftWorkbench":
        # Your one-time or repeatable hook here
        """Append Shapestrings toolbar and menu to the Draft workbench.

        This is designed to be safe to call at import time; it will no-op in
        headless environments and report errors via the FreeCAD console.
        """
        try:
            draft_wb = Gui.getWorkbench("DraftWorkbench")
            if draft_wb:
                draft_wb.appendToolbar(
                    QT_TRANSLATE_NOOP("Workbench", "Shapestrings"),
                    TOOLBOX,
                )
                draft_wb.appendMenu(
                    QT_TRANSLATE_NOOP("Workbench", "&Shapestrings"),
                    TOOLBOX,
                )
                _msg("Appended Shapestrings tools to Draft workbench\n")
        except Exception as exc:
            try:
                App.Console.PrintError(
                    "AdvancedShapestrings: could not append to Draft workbench: {}\n".format(exc)
                )
            except Exception:
                # If App isn't available just ignore
                pass

# Connect once (e.g. in your InitGui.py)
Gui.getMainWindow().workbenchActivated.connect(_on_workbench_activated)