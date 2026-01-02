#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

# Info
AUTHOR = "Kaiz Khatri"
URL = "https://github.com/ful1e5/Bibata_Cursor_Rainbow"

# XCursor
X_DELAY: int = 50


# Windows Cursor
WIN_DELAY = 2

X_CURSORS_CFG: Dict[str, Dict[str, int]] = {
    ##########
    # Static #
    ##########
    "crossed_circle.png": {"xhot": 100, "yhot": 100},
    "wayland-cursor.png": {"xhot": 100, "yhot": 100},
    "X_cursor.png": {"xhot": 100, "yhot": 100},
    ############
    # Animated #
    ############
    # Note: Animated cursors don't need an extension and frame numbers.
    "bd_double_arrow": {"xhot": 100, "yhot": 100},
    "bottom_left_corner": {"xhot": 20, "yhot": 181},
    "bottom_right_corner": {"xhot": 179, "yhot": 181},
    "bottom_side": {"xhot": 101, "yhot": 183},
    "bottom_tee": {"xhot": 100, "yhot": 180},
    "center_ptr": {"xhot": 99, "yhot": 13},
    "circle": {"xhot": 43, "yhot": 13},
    "context-menu": {"xhot": 45, "yhot": 13},
    "copy": {"xhot": 43, "yhot": 13},
    "cross": {"xhot": 100, "yhot": 100},
    # "crosshair": {"xhot": 100, "yhot": 100},
    "dnd_no_drop": {"xhot": 78, "yhot": 51},
    "dnd-ask": {"xhot": 78, "yhot": 51},
    "dnd-copy": {"xhot": 78, "yhot": 51},
    "dnd-link": {"xhot": 78, "yhot": 51},
    "dnd-move": {"xhot": 86, "yhot": 79},
    "dotbox": {"xhot": 100, "yhot": 100},
    "fd_double_arrow": {"xhot": 100, "yhot": 100},
    "grabbing": {"xhot": 100, "yhot": 52},
    "hand1": {"xhot": 112, "yhot": 62},
    "hand2": {"xhot": 89, "yhot": 14},
    "left_ptr": {"xhot": 43, "yhot": 13},
    "left_side": {"xhot": 16, "yhot": 100},
    "left_tee": {"xhot": 180, "yhot": 100},
    "link": {"xhot": 43, "yhot": 13},
    "ll_angle": {"xhot": 23, "yhot": 174},
    "lr_angle": {"xhot": 175, "yhot": 180},
    "move": {"xhot": 100, "yhot": 100},
    "pencil": {"xhot": 36, "yhot": 165},
    "plus": {"xhot": 100, "yhot": 100},
    "pointer-move": {"xhot": 43, "yhot": 13},
    "question_arrow": {"xhot": 33, "yhot": 67},
    "right_ptr": {"xhot": 159, "yhot": 13},
    "right_side": {"xhot": 182, "yhot": 100},
    "right_tee": {"xhot": 23, "yhot": 100},
    "sb_down_arrow": {"xhot": 100, "yhot": 173},
    "sb_h_double_arrow": {"xhot": 100, "yhot": 100},
    "sb_left_arrow": {"xhot": 26, "yhot": 100},
    "sb_right_arrow": {"xhot": 174, "yhot": 100},
    "sb_up_arrow": {"xhot": 100, "yhot": 26},
    "sb_v_double_arrow": {"xhot": 100, "yhot": 100},
    "tcross": {"xhot": 100, "yhot": 100},
    "top_left_corner": {"xhot": 23, "yhot": 19},
    "top_right_corner": {"xhot": 179, "yhot": 19},
    "top_side": {"xhot": 100, "yhot": 18},
    "top_tee": {"xhot": 100, "yhot": 21},
    "ul_angle": {"xhot": 26, "yhot": 26},
    "ur_angle": {"xhot": 176, "yhot": 26},
    "vertical-text": {"xhot": 100, "yhot": 100},
    "xterm": {"xhot": 100, "yhot": 100},
    "zoom-in": {"xhot": 90, "yhot": 89},
    "zoom-out": {"xhot": 93, "yhot": 90},
    # Truly animated
    "left_ptr_watch": {"xhot": 43, "yhot": 13, "delay": 25},
    "wait": {"xhot": 100, "yhot": 100, "delay": 25},
}

WIN_CURSORS_CFG: Dict[str, Dict[str, str]] = {
    "right_ptr": {"to": "Alternate", "position": "top_left"},
    "cross": {"to": "Cross"},
    "left_ptr": {"to": "Default", "position": "top_left"},
    "bd_double_arrow": {"to": "Diagonal_1"},
    "fd_double_arrow": {"to": "Diagonal_2"},
    "pencil": {"to": "Handwriting"},
    "question_arrow": {"to": "Help", "position": "top_left"},
    "sb_h_double_arrow": {"to": "Horizontal"},
    "xterm": {"to": "IBeam", "position": "top_left"},
    "hand2": {"to": "Link", "position": "top_left"},
    "hand1": {"to": "Move"},
    "circle": {"to": "Unavailiable", "position": "top_left"},
    "sb_v_double_arrow": {"to": "Vertical"},
    "left_ptr_watch": {"to": "Work", "position": "top_left"},
    "wait": {"to": "Busy"},
}
