# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#========================================
# Criado por: Wolfterro
# Versão: 1.0.2 - Python 2.x
# Data: 14/11/2016
#========================================

from PyQt4 import QtCore, QtGui
from os.path import expanduser
from bs4 import BeautifulSoup
from urllib2 import urlparse

import os
import re
import sys
import ctypes
import urllib2
import platform
import subprocess

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Definindo Versão do Programa e determinando a pasta 'home' do usuário.
# ======================================================================
version = "1.0.2"
if platform.system() == "Windows":
	buf = ctypes.create_unicode_buffer(1024)
	ctypes.windll.kernel32.GetEnvironmentVariableW(u"USERPROFILE", buf, 1024)
	home_dir = buf.value
else:
	home_dir = expanduser("~")

# Codificação do programa.
# ========================
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

# Classe principal do Programa gerado pelo Qt Designer.
# =====================================================
class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		global cancel
		self.cancel = False

		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(500, 600)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.pushButton = QtGui.QPushButton(self.centralwidget)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		
		self.pushButton.clicked.connect(self.getUserValues)

		self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2.clicked.connect(self.cancelDownload)
		self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 3)
		
		self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 3)
		self.progressBar = QtGui.QProgressBar(self.centralwidget)
		self.progressBar.setProperty("value", 0)
		self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBar.setObjectName(_fromUtf8("progressBar"))
		self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 3)
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.lineEdit_2.setReadOnly(True)
		self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 2, 1)
		self.textEdit = QtGui.QTextEdit(self.centralwidget)
		self.textEdit.setObjectName(_fromUtf8("textEdit"))
		self.textEdit.setReadOnly(True)
		self.gridLayout.addWidget(self.textEdit, 4, 0, 1, 3)
		self.toolButton = QtGui.QToolButton(self.centralwidget)
		self.toolButton.setObjectName(_fromUtf8("toolButton"))
		
		self.toolButton.clicked.connect(self.selectOutputDir)
		
		self.gridLayout.addWidget(self.toolButton, 1, 2, 2, 1)
		self.lineEdit = QtGui.QLineEdit(self.centralwidget)
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 22))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "G.E-Downloader - v%s" % (version), None))
		self.pushButton.setText(_translate("MainWindow", "Download", None))
		self.label.setText(_translate("MainWindow", "URL do Álbum:", None))
		self.toolButton.setText(_translate("MainWindow", "...", None))
		self.label_2.setText(_translate("MainWindow", "Pasta de Destino:", None))
		self.lineEdit_2.setText(_translate("MainWindow", "%s%sHentai" % (home_dir, "\\" if platform.system() == 'Windows' else '/'), None))
		self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Insira a URL do álbum desejado</p></body></html>", None))
		self.toolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolher pasta de destino...</p></body></html>", None))
		self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Iniciar o download do álbum</p></body></html>", None))
		self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Cancelar o download das imagens</p></body></html>", None))
		self.pushButton_2.setText(_translate("MainWindow", "Cancelar", None))

	# ===================================================================
	# Métodos do programa: Resgate de informações e download das imagens.
	# ===================================================================

	# ===============================
	# Métodos de verificação de pasta
	# ===============================

	# Método para selecionar pasta de destino.
	# ========================================
	def selectOutputDir(self):
		self.chosenDir = QtGui.QFileDialog.getExistingDirectory(MainWindow, 'Selecione a pasta de destino:', home_dir, QtGui.QFileDialog.ShowDirsOnly)
		if platform.system() == "Windows":
			self.lineEdit_2.setText(self.chosenDir.replace("/", "\\"))
		else:
			self.lineEdit_2.setText(self.chosenDir)
		return

	# Método de verificação de pasta de destino, verificando se existe ou não.
	# ========================================================================
	def checkOutputDir(self, getOutputDir):
		if os.path.exists(unicode(self.getOutputDir)):
			os.chdir(unicode(self.getOutputDir))
		else:
			os.makedirs(unicode(self.getOutputDir))
			os.chdir(unicode(self.getOutputDir))
		return

	# Criando um diretório para as imagens do álbum
	# =============================================
	def createAlbumDir(self, albumTitle):
		self.invalidChars = ["\\", "/", ":", "*", "?", "<", ">", "|"]

		for self.char in self.albumTitle:
			if self.char in self.invalidChars:
				self.albumTitle = self.albumTitle.replace(self.char, "")
		
		if os.path.exists(unicode(self.albumTitle)):
			os.chdir(unicode(self.albumTitle))
			self.textEdit.append(u"[G.E-Downloader] Baixando em '%s' ..." % (unicode(self.albumTitle)))
			QtGui.QApplication.processEvents()
		else:
			self.textEdit.append(u"[G.E-Downloader] Criando pasta '%s' ..." % (unicode(self.albumTitle)))
			QtGui.QApplication.processEvents()
			os.makedirs(unicode(self.albumTitle))
			os.chdir(unicode(self.albumTitle))

	# =======================================================
	# Métodos de resgate de informações e download de imagens
	# =======================================================

	# Método para calcular o progresso do download dos arquivos.
	# O método resgata o valor da barra e incrementa com o valor de cada progresso.
	# =============================================================================
	def setProgress(self, downloaded, total):
		self.oldValue = self.progressBar.value()
		self.progress = float(self.downloaded) / float(self.total)
		self.percent = self.progress * 100.0
		self.progressBar.setProperty("value", self.percent)
		QtGui.QApplication.processEvents()

	# Iniciando o download das imagens do álbum
	# =========================================
	def downloadAlbumImages(self, albumURLImages, albumSize):
		self.textEdit.append(u"\n[G.E-Downloader] Iniciando o download de %s imagens: " % (str(self.albumSize)))
		self.textEdit.append(u"==============================================")
		QtGui.QApplication.processEvents()
		
		self.count = 1
		for self.images in self.albumURLImages:
			if self.cancel == True:
				self.textEdit.append(u"[G.E-Downloader] Cancelado!!")
				QtGui.QApplication.processEvents()
				return False
			else:
				self.filename = os.path.basename(str(self.images))
				
				if os.path.exists(str(self.filename)):
					self.textEdit.append(u"[G.E-Downloader] Imagem '%s' já existe! Pulando ..." % (str(self.filename)))
					QtGui.QApplication.processEvents()
					self.count += 1
				else:
					try:
						self.requestFour = urllib2.Request(str(self.images), headers={'Cookie' : 'nw=1'})
						self.responseFour = urllib2.urlopen(self.requestFour)
						self.total = self.responseFour.headers['content-length']
					except Exception as self.eeSix:
						self.textEdit.append(u"[G.E-Downloader] Erro! Não foi possível baixar a imagem!")
						self.textEdit.append("[G.E-Downloader] Erro: %s" % (str(self.eeSix)))
						QtGui.QApplication.processEvents()
						return
					
					self.downloaded = 0
					
					self.textEdit.append(u"[G.E-Downloader] Baixando imagem '%s' - %s/%s ..." % (str(self.filename), str(self.count), str(self.albumSize)))
					with open(str(self.filename), 'wb') as self.file:
						while True:
							self.data = self.responseFour.read(4096)
							self.downloaded += len(self.data)
							if not self.data:
								break
							self.file.write(self.data)
							self.setProgress(self.downloaded, self.total)
					self.count += 1

	# Resgatando o endereço URL das imagens que serão baixadas
	# ========================================================
	def getImagesURL(self, albumImages):
		self.imgURL = []
		for self.imageURL in self.albumImages:
			for self.u in self.imageURL:
				try:
					self.requestThree = urllib2.Request(str(self.u), headers={'Cookie' : 'nw=1'})
					self.responseThree = urllib2.urlopen(self.requestThree)
					self.soupThree = BeautifulSoup(self.responseThree, 'html.parser')
				except Exception as self.eeFour:
					self.textEdit.append(u"[G.E-Downloader] Erro! Não foi possível carregar informações!")
					self.textEdit.append("[G.E-Downloader] Erro: %s" % (str(self.eeFour)))
					QtGui.QApplication.processEvents()
					return

				self.imgURL.append(self.soupThree.find('img', {'id' : 'img'}).get('src'))

		return self.imgURL

	# Resgatando as imagens e o número de imagens do álbum
	# ====================================================
	def getAlbumImages(self, cleanedAlbumURL, albumID):
		self.links = []
		self.imgs = []
		self.pages = []
		
		try:
			self.requestTwo = urllib2.Request(str(self.cleanedAlbumURL), headers={'Cookie' : 'nw=1'})
			self.responseTwo = urllib2.urlopen(self.requestTwo)
			self.soupTwo = BeautifulSoup(self.responseTwo, 'html.parser')
		except Exception as self.eeTwo:
			self.textEdit.append(u"[G.E-Downloader] Erro! Não foi possível carregar informações!")
			self.textEdit.append("[G.E-Downloader] Erro: %s" % (str(self.eeTwo)))
			QtGui.QApplication.processEvents()
			return

		self.toMatchImages = r'http://g.e-hentai.org/.*/.*/' + str(self.albumID) + r'-.*'
		self.toMatchPages = r'http://g.e-hentai.org/.*/' + str(self.albumID) + r'/.*/\?p=.*'
		
		for self.img in self.soupTwo.findAll('a', href=True):
			self.links.append(self.img['href'])
		
		for self.img in self.links:
			self.matchImg = re.findall(self.toMatchImages, self.img)
			if self.matchImg == []:
				continue
			else:
				self.imgs.append(self.matchImg)

		for self.page in self.links:
			self.matchPage = re.findall(self.toMatchPages, self.page)
			if self.matchPage == []:
				continue
			elif self.matchPage in self.pages:
				continue
			else:
				self.pages.append(self.matchPage)

		if len(self.pages) >= 1:
			for self.pg in self.pages:
				self.linksPg = []

				for self.l in self.pg:
					try:
						self.requestPg = urllib2.Request(str(self.l), headers={'Cookie' : 'nw=1'})
						self.responsePg = urllib2.urlopen(self.requestPg)
						self.soupPg = BeautifulSoup(self.responsePg, 'html.parser')
					except Exception as self.eeThree:
						self.textEdit.append(u"[G.E-Downloader] Erro! Não foi possível carregar informações!")
						self.textEdit.append("[G.E-Downloader] Erro: %s" % (str(self.eeThree)))
						QtGui.QApplication.processEvents()
						return

					for self.imgPg in self.soupPg.findAll('a', href=True):
						self.linksPg.append(self.imgPg['href'])
			
					for self.imgPg in self.linksPg:
						self.matchImgPg = re.findall(self.toMatchImages, self.imgPg)
						if self.matchImgPg == []:
							continue
						else:
							self.imgs.append(self.matchImgPg)

		self.numberOfImages = len(self.imgs)
		return self.imgs, self.numberOfImages

	# Resgatando a ID do álbum
	# ========================
	def getAlbumID(self, cleanedAlbumURL):
		self.urlSplitID = urlparse.urlsplit(str(self.cleanedAlbumURL))
		self.urlID = str(self.urlSplitID[2]).split("/", 3)[2]
		return self.urlID

	# Resgatando o título do álbum
	# ============================
	def getAlbumTitle(self, cleanedAlbumURL):
		try:
			self.requestOne = urllib2.Request(str(self.cleanedAlbumURL), headers={'Cookie' : 'nw=1'})
			self.responseOne = urllib2.urlopen(self.requestOne)
			self.soupOne = BeautifulSoup(self.responseOne, 'html.parser')
		except Exception as self.eeOne:
			self.textEdit.append(u"[G.E-Downloader] Erro! Não foi possível carregar informações!")
			self.textEdit.append("[G.E-Downloader] Erro: %s" % (str(self.eeOne)))
			QtGui.QApplication.processEvents()
			return
		
		try:
			return self.soupOne.title.string.replace(" - E-Hentai Galleries", "")
		except Exception as self.eeFive:
			self.textEdit.append(u"[G.E-Downloader] Erro! Não foi possível carregar informações!")
			self.textEdit.append("[G.E-Downloader] Erro: %s" % (str(self.eeFive)))
			QtGui.QApplication.processEvents()
			return None
	
	# Verificando se a URL inserida pertence ao domínio g.e-hentai.org
	# ================================================================
	def checkURLDomain(self, cleanedAlbumURL):
		self.urlSplit = urlparse.urlsplit(str(self.cleanedAlbumURL))
		if str(self.urlSplit[1]) != "g.e-hentai.org":
			self.textEdit.append(u"[G.E-Downloader] Erro! URL inválida! Tente novamente.")
			return

	# Limpando a URL para que ela aponte para a primeira página
	# =========================================================
	def cleanURL(self, albumURL):
		self.cleanedAlbumURL = re.sub(r'/\?p=.*', '', str(self.albumURL))
		return self.cleanedAlbumURL

	# Iniciando processo de resgate de informações e download de imagens
	# ==================================================================
	def beginProcess(self, albumURL):
		self.cleanedAlbumURL = self.cleanURL(self.albumURL)
		self.checkURLDomain(self.cleanedAlbumURL)
		self.textEdit.append(u"[G.E-Downloader] Carregando informações do álbum (isto pode levar um tempo) ...")
		QtGui.QApplication.processEvents()
		
		self.albumTitle = self.getAlbumTitle(self.cleanedAlbumURL)
		if self.albumTitle == None:
			return

		self.albumID = self.getAlbumID(self.cleanedAlbumURL)
		self.albumImages, self.albumSize = self.getAlbumImages(self.cleanedAlbumURL, self.albumID)
		self.albumURLImages = self.getImagesURL(self.albumImages)
		self.createAlbumDir(self.albumTitle)
		self.downloadAlbumImages(self.albumURLImages, self.albumSize)

		return
	
	# Método para recuperar os valores inseridos pelo usuário.
	# URL do álbum e pasta de destino são resgatados por este método.
	# No final do processo, a pasta de destino é aberta para o usuário.
	# =================================================================
	def getUserValues(self):
		self.albumURL = self.lineEdit.text()
		self.getOutputDir = self.lineEdit_2.text()

		if self.albumURL == "":
			self.textEdit.append(u"[G.E-Downloader] Erro! Falta a URL do álbum!")
			return
		elif self.getOutputDir == "":
			self.textEdit.append(u"[G.E-Downloader] Erro! Falta o caminho para a pasta de destino!")
			return
		else:
			self.cancel = False
			self.pushButton.setEnabled(False)
			self.pushButton.setText(_translate("MainWindow", "Downloading...", None))
			self.pushButton.repaint()
			self.progressBar.setProperty("value", 0)
			QtGui.QApplication.processEvents()

			self.checkOutputDir(self.getOutputDir)

			self.textEdit.clear()
			QtGui.QApplication.processEvents()

			# Iniciando o processo...
			# ==============================
			self.beginProcess(self.albumURL)
			# ==============================

			self.pushButton.setEnabled(True)
			self.pushButton.setText(_translate("MainWindow", "Download", None))
			self.pushButton.repaint()
			QtGui.QApplication.processEvents()

			self.textEdit.append(u"\n==============================================\n")
			self.textEdit.append(u"[G.E-Downloader] Processo de Download Finalizado!")
			QtGui.QApplication.processEvents()

			if platform.system() == "Windows":
				os.startfile(self.getOutputDir)
			else:
				try:
					subprocess.Popen(["xdg-open", "%s" % (self.getOutputDir)])
				except Exception:
					pass

			return

	# Método para cancelar o processo de download.
	# ============================================
	def cancelDownload(self):
		self.cancel = True
		return

# Executando o Programa.
# ======================
if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())