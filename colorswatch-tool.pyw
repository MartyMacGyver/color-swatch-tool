#!/usr/bin/python3

#   Copyright (c) 2015-2017 Martin F. Falatic
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
if tk.TkVersion < 8.6:
    import colorswatches85 as cswatches
    COLOR_ROWS = 47
else:
    import colorswatches86 as cswatches
    COLOR_ROWS = 48


MIN_WIDTH = 16
SORT_ORDERS = ['Original', 'RGB', 'Luminance']
LUMINANCE_STDS = ['REC_601', 'REC_709']


class ColorChart(tk.Frame):
    def __init__(self, parent=None, colors=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.colors = colors
        self.top = self.winfo_toplevel()
        self.tcl_version = tk.Tcl().call('info', 'patchlevel')  # More precise than tk.TclVersion
        self.tk_version = self.top.tk.call('info', 'patchlevel')  # More precise than tk.TkVersion
        self.COMPACTIFY = False
        self.SHOW_NAMES = True
        self.JUSTIFY = False
        self.sort_order_idx = 0
        self.sort_order = SORT_ORDERS[self.sort_order_idx]
        self.lum_std_idx = 0
        self.lum_std = LUMINANCE_STDS[self.lum_std_idx]
        self.first_color_row = 0
        self._recalculate()
        self.set_controls()
        self.label_details = OrderedDict()
        self._redraw()

    def set_controls(self):
        row = 0
        col = 0
        self.label1 = tk.Label(self.parent, text="Tcl {}".format(self.tcl_version))
        self.label1.grid(row=row, column=col, sticky='nswe')
        col += 1
        self.label2 = tk.Label(self.parent, text="Tk {}".format(self.tk_version))
        self.label2.grid(row=row, column=col, sticky='nswe')
        col += 1
        self.button_names = tk.Button(self.parent, text="Sort", command=self._on_cycle_sort)
        self.button_names.grid(row=row, column=col, sticky='nswe')
        col += 1
        self.button_names = tk.Button(self.parent, text="Lum", command=self._on_cycle_luminance)
        self.button_names.grid(row=row, column=col, sticky='nswe')
        col += 1
        self.button_names = tk.Button(self.parent, text="Names", command=self._on_toggle_names)
        self.button_names.grid(row=row, column=col, sticky='nswe')
        col += 1
        self.button_size = tk.Button(self.parent, text="Compact", command=self._on_toggle_compact)
        self.button_size.grid(row=row, column=col, sticky='nswe')
        col += 1
        self.button_size = tk.Button(self.parent, text="Justify", command=self._on_toggle_justify)
        self.button_size.grid(row=row, column=col, sticky='nswe')
        row += 1
        col = 0
        self.button_copy = tk.Button(self.parent, text="Copy", command=self._on_copy)
        self.button_copy.grid(row=row, column=col, sticky='nswe')
        col += 1
        self.textbox = tk.Entry(self.parent, bd=2, font=settings.INPUT_FONT, justify="left")
        self.textbox_text = ''
        self.update_textbox(self.textbox, "Click a color...")
        self.textbox.grid(row=row, column=col, columnspan=6, sticky='nswe')
        col += 6
        row += 1
        self.first_color_row = row

    def calculate_luminance(self, colors, lum_std):
        colors_by_y = []
        print(lum_std)
        for color_RGB in colors:
            # Luminance calculation
            (R, G, B) = struct.unpack('BBB', base64.b16decode(color_RGB))
            if lum_std == 'REC_601':
                Y = 0.2990 * R + 0.5870 * G + 0.1140 * B  # CCIR REC_601 (digital)
            elif lum_std == 'REC_709':
                Y = 0.2126 * R + 0.7152 * G + 0.0722 * B  # ITU-R REC_709 (HDTV)
            colors_by_y.append((Y, color_RGB))
        return colors_by_y

    def sort_colors(self, colors_by_y, sort_order):
        colors_idx_rgb_y = []
        print(sort_order)
        if sort_order == 'Original':
            colors_idx_rgb_y = colors_by_y  # Original order
        elif sort_order == 'RGB':
            colors_idx_rgb_y = sorted(colors_by_y, key=lambda tup: tup[1])  # Sort RGB
        elif sort_order == 'Luminance':
            colors_idx_rgb_y = sorted(colors_by_y, key=lambda tup: tup[0])  # Sort Y
        return colors_idx_rgb_y

    def _redraw(self):
        self.set_labels()
        self.parent.winfo_toplevel().wm_geometry()

    def _recalculate(self):
        self.colors_by_y = self.calculate_luminance(colors=self.colors, lum_std=self.lum_std)
        self.colors_sorted = self.sort_colors(self.colors_by_y, sort_order=self.sort_order)

    def _on_cycle_sort(self):
        self.sort_order_idx = (self.sort_order_idx + 1) % len(SORT_ORDERS)
        self.sort_order = SORT_ORDERS[self.sort_order_idx]
        logging.debug("Sort order = {}".format(self.sort_order))
        self._recalculate()
        self._redraw()

    def _on_cycle_luminance(self):
        self.lum_std_idx = (self.lum_std_idx + 1) % len(LUMINANCE_STDS)
        self.lum_std = LUMINANCE_STDS[self.lum_std_idx]
        logging.debug("Luminance std = {}".format(self.lum_std))
        self._recalculate()
        self._redraw()

    def _on_toggle_names(self):
        self.SHOW_NAMES = not self.SHOW_NAMES
        self._redraw()

    def _on_toggle_compact(self):
        self.COMPACTIFY = not self.COMPACTIFY
        self._redraw()

    def _on_toggle_justify(self):
        self.JUSTIFY = not self.JUSTIFY
        self._redraw()

    def _on_copy(self):
        if self.textbox_text:
            self.parent.clipboard_clear()
            self.parent.clipboard_append(self.textbox_text)

    def _on_click_color(self, event):
        # x = self.winfo_pointerx()
        # y = self.winfo_pointery()
        t = self.label_details[event.widget]
        color_RGB = t['color']
        aliases = self.colors[color_RGB]
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

        row = self.first_color_row
        col = 0
        for Y, color_RGB in self.colors_sorted:
            # logging.debug("{} {}".format(Y, color_RGB))
            foreground = 'black'
            if Y < 128.0:
                foreground = 'white'

            for i, color_tk in enumerate(self.colors[color_RGB]):
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
                label.grid(row=row, column=col, sticky='nswe')
                label.bind("<Button-1>", self._on_click_color)
                row += 1
                if (row >= COLOR_ROWS + self.first_color_row):
                    row = self.first_color_row
                    col += 1


if __name__ == "__main__":
    logging.basicConfig(filename='', level=logging.DEBUG)
    colors = cswatches.COLORS_ODICT
    root = tk.Tk()
    root.resizable(0, 0)
    root.title(settings.APP_Main_Title)
    logging.debug("Starting")
    root.geometry('+%d+%d' % (10, 10))
    APP = ColorChart(parent=root, colors=colors)
    APP.mainloop()
