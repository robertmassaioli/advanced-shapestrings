# AdvancedShapestrings (FreeCAD)

## Overview
AdvancedShapestrings adds a new FreeCAD workbench with additional, or improved, Shapestring commands.
## SpacedShapeString — what it is and why use it

Icon: 

![SpacedShapeString icon](./freecad/advanced_shapestrings/resources/icons/AdvancedShapestrings_SpacedShapeString.svg)

### What the Command Does

The **SpacedShapeString** command lets you create several text strings—like numbers or labels—and place them in a line with even spacing between each one. The offset you choose always applies, either setting where each string starts relative to the last, or keeping the visible gap between strings constant.

For example, if you want to display numbers 1 through 11 across a face for a Pad, you’d usually need to create and position each number separately with the **Draft ShapeString** command. With **SpacedShapeString**, that same pattern can be done in one easy step.

The resulting shapes are standard FreeCAD objects that work seamlessly with both **Part** and **PartDesign** tools.

### Properties

- **Strings**  
  List of text entries to render, in order, as separate strings.

- **FontFile**  
  Path to the font file to use (for example, a `.ttf` or `.otf` file).

- **Size**  
  Height of the rendered text, in model units (the same meaning as the Size property of a standard Draft ShapeString).

- **Offset**  
  Horizontal spacing value applied between strings. This value is always used when positioning each subsequent string.

- **UseBoundingBox**  
  Controls how the offset is interpreted when laying out the strings:
  - **False**: Each string’s insertion point is placed at a fixed offset from the previous string’s insertion point, regardless of character widths.  
  - **True**: The visible gap between the end of one string and the start of the next is kept equal to the offset, using each string’s bounding box to measure its width.

## Using the tool (GUI)
1. Switch to the Advanced Shapestrings workbench.
2. Choose the "Spaced shape from text" tool.
3. In the task panel:
   - Add, edit or remove strings.
   - Select a font file.
   - Set Size and Offset.
   - Optionally set "Use bounding box" to space strings by their width.
4. Pick the placement point in the 3D view.
5. Click OK to create the SpacedShapeString object in the active document.

## Using from Python (inside FreeCAD)
Example (run in the FreeCAD Python console with an open document):

```python
from freecad.advanced_shapestrings.make import make_spacedshapestring

make_spacedshapestring(["String1", "String2"], "/path/to/font.ttf", Size=10, Offset=5, UseBoundingBox=False)
```

## Installation

### Via the Addon Manager

TODO

### User install (for development)
Copy the module directory into FreeCAD's Mod folder, then restart FreeCAD.

macOS example:

```bash
cd ~/Library/Application\ Support/FreeCAD/Mod
ln -s /path/to/this/repo AdvancedShapestrings
```

Restart FreeCAD. The tool appears in the Draft toolbox.