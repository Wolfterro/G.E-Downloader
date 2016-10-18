#!/usr/bin/env python2
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
# Versão: 1.0.0 - Python 2.x
# Data: 17/10/2016
#========================================

from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlparse

import os
import re
import sys
import urllib2

# Alterando a codificação padrão
# ==============================
reload(sys)
sys.setdefaultencoding('utf-8')

# Versão
# ======
VERSION = "1.0.0"

# Criando um diretório para as imagens do álbum
# =============================================
def createAlbumDir(albumTitle):
	albumTitle = albumTitle.replace("/", "").replace("\\", "")
	if os.path.exists(albumTitle):
		os.chdir(albumTitle)
	else:
		print("[G.E-Downloader] Criando pasta '%s' ..." % (albumTitle))
		os.makedirs(albumTitle)
		os.chdir(albumTitle)

# Imprimindo barra de processo no terminal
# ========================================
def printProgressBar(now, total, width=50):
	progress = float(now) / float(total)
	bar = ('#' * int(width * progress)).ljust(width)
	percent = progress * 100.0
	to_print = 'Downloading: [%s] %.2f%%\r' % (bar, percent)
	print(to_print, end='')
	if round(percent) >= 100:
		print('%s\r' % (' ' * len(to_print)), end='')

# Iniciando o download das imagens do álbum
# =========================================
def downloadAlbumImages(albumURLImages, albumSize):
	print("\n[G.E-Downloader] Iniciando o download de %s imagens: " % (albumSize))
	print("-------------------------------------------------------")
	count = 1
	for images in albumURLImages:
		try:
			request = urllib2.Request(images, headers={'Cookie' : 'nw=1'})
			response = urllib2.urlopen(request)
			total = response.headers['content-length']
		except Exception as ee:
			print("[G.E-Downloader] Erro! Não foi possível baixar a imagem!")
			print("[G.E-Downloader] Erro: %s" % (ee))
			sys.exit(1)
		
		downloaded = 0
		
		filename = os.path.basename(images)
		print("[G.E-Downloader] Baixando imagem '%s' - %s/%s ..." % (filename, count, albumSize))
		with open(filename, 'wb') as file:
			while True:
				data = response.read(4096)
				downloaded += len(data)
				if not data:
					break
				file.write(data)
				printProgressBar(downloaded, total)
		count += 1

	print("\n[G.E-Downloader] Download concluído!")

# Resgatando o endereço URL das imagens que serão baixadas
# ========================================================
def getImagesURL(albumImages):
	imgURL = []
	for imageURL in albumImages:
		for u in imageURL:
			try:
				request = urllib2.Request(u, headers={'Cookie' : 'nw=1'})
				response = urllib2.urlopen(request)
				soup = BeautifulSoup(response, 'html.parser')
			except Exception as ee:
					print("[G.E-Downloader] Erro! Não foi possível carregar informações!")
					print("[G.E-Downloader] Erro: %s" % (ee))
					sys.exit(1)

			imgURL.append(soup.find('img', {'id' : 'img'}).get('src'))

	return imgURL

# Resgatando as imagens e o número de imagens do álbum
# ====================================================
def getAlbumImages(albumURL, albumID):
	links = []
	imgs = []
	pages = []
	
	try:
		request = urllib2.Request(albumURL, headers={'Cookie' : 'nw=1'})
		response = urllib2.urlopen(request)
		soup = BeautifulSoup(response, 'html.parser')
	except Exception as ee:
		print("[G.E-Downloader] Erro! Não foi possível carregar informações!")
		print("[G.E-Downloader] Erro: %s" % (ee))
		sys.exit(1)

	toMatchImages = r'http://g.e-hentai.org/.*/.*/' + albumID + r'-.*'
	toMatchPages = r'http://g.e-hentai.org/.*/' + albumID + r'/.*/\?p=.*'
	
	for img in soup.findAll('a', href=True):
		links.append(img['href'])
	
	for img in links:
		matchImg = re.findall(toMatchImages, img)
		if matchImg == []:
			continue
		else:
			imgs.append(matchImg)

	for page in links:
		matchPage = re.findall(toMatchPages, page)
		if matchPage == []:
			continue
		elif matchPage in pages:
			continue
		else:
			pages.append(matchPage)

	if len(pages) >= 1:
		for pg in pages:
			linksPg = []

			for l in pg:
				try:
					requestPg = urllib2.Request(str(l), headers={'Cookie' : 'nw=1'})
					responsePg = urllib2.urlopen(requestPg)
					soupPg = BeautifulSoup(responsePg, 'html.parser')
				except Exception as ee:
					print("[G.E-Downloader] Erro! Não foi possível carregar informações!")
					print("[G.E-Downloader] Erro: %s" % (ee))
					sys.exit(1)

				for imgPg in soupPg.findAll('a', href=True):
					linksPg.append(imgPg['href'])
		
				for imgPg in linksPg:
					matchImgPg = re.findall(toMatchImages, imgPg)
					if matchImgPg == []:
						continue
					else:
						imgs.append(matchImgPg)

	numberOfImages = len(imgs)
	return imgs, numberOfImages

# Resgatando a ID do álbum
# ========================
def getAlbumID(albumURL):
	urlSplit = urlparse.urlsplit(albumURL)
	urlID = str(urlSplit[2]).split("/", 3)[2]
	return urlID

# Resgatando o título do álbum
# ============================
def getAlbumTitle(albumURL):
	try:
		request = urllib2.Request(albumURL, headers={'Cookie' : 'nw=1'})
		response = urllib2.urlopen(request)
		soup = BeautifulSoup(response, 'html.parser')
	except Exception as ee:
		print("[G.E-Downloader] Erro! Não foi possível carregar informações!")
		print("[G.E-Downloader] Erro: %s" % (ee))
		sys.exit(1)
	
	return soup.title.string.replace(" - E-Hentai Galleries", "")

# Verificando se a URL inserida pertence ao domínio g.e-hentai.org
# ================================================================
def checkURLDomain(albumURL):
	urlSplit = urlparse.urlsplit(albumURL)
	if str(urlSplit[1]) != "g.e-hentai.org":
		print("[G.E-Downloader] Erro! URL inválida! Saindo ...")
		sys.exit(1)

# Iniciando processo de resgate de informações e download de imagens
# ==================================================================
def beginProcess(albumURL):
	if albumURL == None:
		albumURL = raw_input("Insira a URL do álbum desejado: ")
	
	checkURLDomain(albumURL)
	print("[G.E-Downloader] Carregando informações do álbum (isto pode levar um tempo) ...")
	
	albumTitle = getAlbumTitle(albumURL)
	albumID = getAlbumID(albumURL)
	albumImages, albumSize = getAlbumImages(albumURL, albumID)
	albumURLImages = getImagesURL(albumImages)
	
	createAlbumDir(albumTitle)
	downloadAlbumImages(albumURLImages, albumSize)

# Menu de ajuda
# =============
def helpMenu():
	print("Uso: ./GEDownloader.py [URL / OPÇÕES]\n")

	print("Opções")
	print("------")
	print(" -h || --help\t\tMostra este menu de ajuda.\n")

	print("----------------------------------------------------------------\n")

	print(" *** Este programa é licenciado sob a licença MIT ***\n")
	
	print("Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>")
	print("Repositório no GitHub: https://github.com/Wolfterro/G.E-Downloader\n")

# Método principal
# ================
def main():
	argc = len(sys.argv)

	print("=======================")
	print("G.E-Downloader - v%s" % (VERSION))
	print("=======================\n")

	if argc >= 2:
		if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
			helpMenu()
		else:
			beginProcess(str(sys.argv[1]))
	else:
		beginProcess(None)

# Inicializando
# =============
if __name__ == "__main__":
	main()