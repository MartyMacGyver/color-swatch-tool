# Color Swatch Tool

Run: python colorswatch-tool.pyw

Features:
* Click color to show details
* Use Copy to copy details to clipboard
* Selectable luminance mode (CCIR REC_601 (digital, default), ITU-R REC_709 (HDTV))
* Sort by original order, RGB order, or luminance mode order
* Works with Python 2.7 and 3.4+
* Requires Tk (for Tkinter) - see below

More information:
* TclTk 8.6 adds / updates certain colors, currently only documented at http://www.tcl.tk/cgi-bin/tct/tip/403.html mentioned at http://wiki.tcl.tk/21276. The man page at http://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm does NOT yet reflect this change (see http://core.tcl.tk/tk/tktview/2a02881e4c23634022d0ae40a14383d9baad9eb9).
* The Python.org Python 2.7 Windows distributions contain TclTk 8.5
* The Python.org Python 3.4 Windows distributions contain TclTk 8.6 (need exact referemce for this)
* The Python.org Python 2.7 and 3.4 OS X distributions *recommend* TclTk 8.5 (see https://www.python.org/download/mac/tcltk/)
