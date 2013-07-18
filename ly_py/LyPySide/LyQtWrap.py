from PySide.QtCore import *
from PySide.QtGui import *


def toggledShowHide(widget, isShow):
	if isShow:
		widget.show()
	else:
		widget.hide()
