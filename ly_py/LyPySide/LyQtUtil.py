from PySide.QtCore import *
from PySide.QtGui import *
import os


def getOpenFileName(parent, caption, dirStr, filterStr):
	filePathName = QFileDialog.getOpenFileName(parent, caption, dirStr, filterStr)
	# [TODO]リストで返却されてくるので対応
	if len(filePathName) > 1:
		filePathName = unicode(filePathName[0])
		return filePathName
	return ""


def getExistingDirectory(parent, caption, dirStr):
	dirPathName = unicode(QFileDialog.getExistingDirectory(parent, caption, dirStr))
	return dirPathName


def getSaveFileName(parent, caption, filePathName):
	listValue = QFileDialog.getSaveFileName(parent, caption, filePathName, "")
	fileName = ""
	if len(listValue) > 0:
		fileName = listValue[0]
	return fileName
