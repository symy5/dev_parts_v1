# [2013/07/03]
import os
import subprocess
import CommonUI


def isEnvWindows():
	if os.name == 'nt':
		return True
	else:
		return False


# リストから空データを削除します。
# ファイルパスを'/' で分割した際に、先頭に'/'が存在する場合、分割後のリストに空文字「""」が入るので予防
def deleteEmptyFromList(listData):
	nCnt = len(listData)
	for i in reversed(range(nCnt)):
		if len(listData[i]) <= 0:
			del listData[i]
	return listData


def commonButtonVisibleFunc(scrollArea, button, text):
	if scrollArea.isVisible():
		button.setText("[+] " + text);
		scrollArea.setVisible(False)
	else:
		button.setText("[-] " + text);
		scrollArea.setVisible(True)


def execSystemCommand(cmdStr, isMessage):
	# Check
	if len(cmdStr) <= 0:
		print("[ERROR] len(cmdStr) <= 0")
		return ""
	message = ""
	if isMessage:
		print("[MSG] " + cmdStr)
	# Execute
	p = subprocess.Popen(cmdStr, shell=True, stdin=subprocess.PIPE,
                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	(stdouterr, stdin) = (p.stdout, p.stdin)  # ファイルオブジェクト
	while True:
		line = stdouterr.readline()  # 改行を含んで行を読み込む
		if not line:
			break
		message = line.rstrip()  # 後ろの改行を消して出力

	ret = p.wait()  # 戻り値が入る
	return message



def getStringFromFile(filePathName):
	if os.path.isfile(filePathName) != True:
		# ファイルが存在しないことをユーザーに報告
		CommonUI.showWarningFileNotFound(None, filePathName)
		return ""
	fileR = open(filePathName)
	listStr = fileR.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
	fileR.close()
	# listStr: リスト。要素は1行の文字列データ
	if len(listStr) >= 0:
		return ""
	retStr = "".join(listStr)  # リスト => 文字列
	return retStr
