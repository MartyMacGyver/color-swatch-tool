#!/usr/bin/python

#   Copyright (c) 2015 Martin F. Falatic
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""

"""

from __future__ import print_function

try:  # Python2
    import Tkinter as tk
except ImportError:  # Python3
    import tkinter as tk
from collections import OrderedDict
import struct
import base64
import logging
import settings
import colorswatches


COLORS = colorswatches.COLORS_ODICT_TK85_ORIG
COLORS_BY_Y = []
FIRST_COLOR_ROW = 1
COLOR_ROWS = 47
SHOW_NAMES = True
SORT_ORDERS = 3
MIN_WIDTH = 16
JUSTIFY = False
COMPACTIFY = False
ROOT = None


class ColorChart(tk.Frame):
    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.COMPACTIFY = COMPACTIFY
        self.SHOW_NAMES = SHOW_NAMES
        self.JUSTIFY = JUSTIFY
        self.SORT_ORDER = 0
        self.COLOR_IDX_RGB_Y = COLORS_BY_Y  # Original order
        # COLOR_IDX_RGB_Y = sorted(COLORS_BY_Y, key=lambda tup: tup[0])  # Sort Y
        # COLOR_IDX_RGB_Y = sorted(COLORS_BY_Y, key=lambda tup: tup[1])  # Sort RGB
        self.label_details = OrderedDict()
        self.set_controls()
        self.set_labels()

    def set_controls(self):
        self.row = 0
        self.col = 0
        self.button_names = tk.Button(self.parent, text="Names", command=self._on_toggle_names)
        self.button_names.grid(row=self.row, column=self.col, sticky='nswe')
        self.col += 1
        self.button_size = tk.Button(self.parent, text="Compact", command=self._on_toggle_compact)
        self.button_size.grid(row=self.row, column=self.col, sticky='nswe')
        self.col += 1
        self.button_size = tk.Button(self.parent, text="Justify", command=self._on_toggle_justify)
        self.button_size.grid(row=self.row, column=self.col, sticky='nswe')
        self.col += 1
        self.button_copy = tk.Button(self.parent, text="Copy ->", command=self._on_copy)
        self.button_copy.grid(row=self.row, column=self.col, sticky='nswe')
        self.col += 1
        self.textbox = tk.Entry(self.parent, bd=2, font=settings.INPUT_FONT, justify="left")
        self.textbox_text = ''
        self.update_textbox(self.textbox, "Click a color...")
        self.textbox.grid(row=self.row, column=self.col, columnspan=6, sticky='nswe')
        self.col += 6

    def _on_toggle_names(self):
        self.SHOW_NAMES = not self.SHOW_NAMES
        self.set_labels()
        ROOT.winfo_toplevel().wm_geometry()

    def _on_toggle_compact(self):
        self.COMPACTIFY = not self.COMPACTIFY
        self.set_labels()
        ROOT.winfo_toplevel().wm_geometry()

    def _on_toggle_justify(self):
        self.JUSTIFY = not self.JUSTIFY
        self.set_labels()
        ROOT.winfo_toplevel().wm_geometry()

    def _on_copy(self):
        if self.textbox_text:
            ROOT.clipboard_clear()
            ROOT.clipboard_append(self.textbox_text)

    def _on_click_color(self, event):
        # x = self.winfo_pointerx()
        # y = self.winfo_pointery()
        t = self.label_details[event.widget]
        color_RGB = t['color']
        aliases = COLORS[color_RGB]
        self.textbox_text = "#{}  {}".format(color_RGB, aliases)
        self.update_textbox(self.textbox, self.textbox_text)

    def update_textbox(self, textbox, text):
        textbox.delete(0, tk.END)
        textbox.insert(0, text)

    def set_labels(self):
        for label in self.label_details:
            label.grid_forget()
            label.destroy()
        self.label_details = OrderedDict()

        self.row = FIRST_COLOR_ROW
        self.col = 0
        for Y, color_RGB in self.COLOR_IDX_RGB_Y:
            # logging.debug("{} {}".format(Y, color_RGB))
            foreground = 'black'
            if Y < 128.0:
                foreground = 'white'

            for i, color_tk in enumerate(COLORS[color_RGB]):
                if self.COMPACTIFY and i > 0:
                    break
                if self.SHOW_NAMES:
                    color_label = color_tk
                else:
                    color_label = color_RGB
                label = tk.Label(self.parent, text=color_label, font=settings.SWATCH_FONT,
                                 foreground=foreground, background=color_tk,
                                 padx=0, pady=0)
                if self.JUSTIFY and len(color_label) < MIN_WIDTH:
                    label.configure(width=MIN_WIDTH)
                self.label_details[label] = {'text': color_label, 'color': color_RGB,
                                             'fg': foreground, 'bg': color_tk}
                label.grid(row=self.row, column=self.col, sticky='nswe')
                label.bind("<Button-1>", self._on_click_color)
                self.row += 1
                if (self.row >= COLOR_ROWS + FIRST_COLOR_ROW):
                    self.row = FIRST_COLOR_ROW
                    self.col += 1


def luminance_init():
    for color_RGB in COLORS:
        # Luminance calculation
        (R, G, B) = struct.unpack('BBB', base64.b16decode(color_RGB))
        # Y = 0.2990 * R + 0.5870 * G + 0.1140 * B  # CCIR REC_601 (digital)
        Y = 0.2126 * R + 0.7152 * G + 0.0722 * B  # ITU-R REC_709 (HDTV)
        COLORS_BY_Y.append((Y, color_RGB))

if __name__ == "__main__":
    logging.basicConfig(filename='', level=logging.DEBUG)
    ROOT = tk.Tk()
    ROOT.title(settings.APP_Main_Title)
    logging.debug("Starting")
    luminance_init()
    ROOT.geometry('+%d+%d' % (50, 50))
    APP = ColorChart(ROOT)
    APP.mainloop()
