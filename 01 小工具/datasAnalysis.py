#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 数据存取工具
import os, sys

from Tkinter import *
WORKSPACE_PATH = u'C:\workspace\datas'.encode('gbk')

class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		#存入地址名
		self.url1 = ""
		self.url2 = ""
		self.content2 = []
		self.pack()
		self.winfo_toplevel().title("数据存取工具")
		self.createWidgets()

	def clearText(self):
		#清空文本
		self.textFirst.delete(0.0, END)
		self.textSecond.delete(0.0, END)
		self.content.delete(0.0, END)

	def refreshLbFirst(self):
		#刷新列表
		self.lbFirst.delete(0, END)
		for d in os.listdir(WORKSPACE_PATH):
			if os.path.isdir(WORKSPACE_PATH + "\\" + d):
				self.lbFirst.insert(END,d.decode('gbk'))

	def refreshLbSecond(self):
		index = self.lbFirst.curselection()
		if len(index) != 0:
			self.url1 = u"" + WORKSPACE_PATH + "\\" + self.lbFirst.get(index) 
		self.lbSecond.delete(0, END)
		self.content2 = []
		for d in os.listdir(self.url1):
			self.lbSecond.insert(END,d)
			self.content2.append(d)

	def lbFirstClick(self,event):
		self.refreshLbSecond()

	def lbSecondClick(self,event):
		index = self.lbSecond.curselection()
		if len(index) != 0:
			#有值就取
			self.url2 = u"" + self.url1 + "\\" + self.lbSecond.get(index) 
			fo = open(r'' + self.url2, "r")
			self.content.delete(0.0, END)
			for line in fo.readlines():                          #依次读取每行  
				print(line)
				#line = line.strip()                          #去掉每行头尾空白  
				self.content.insert(END,line)
			self.content.see(END)

	def datasAdd(self):
		#数据添加与更新
		textFirst = self.textFirst.get("0.0", "end").strip()
		textSecond = self.textSecond.get("0.0", "end").strip()
		dirFirst = u"" + WORKSPACE_PATH + "\\" + textFirst

		if textFirst != "" and os.path.isdir(dirFirst) == False:

			fileName = str(self.lbFirst.size()) + " " + textFirst
			if self.lbFirst.size() < 10:
				fileName = "0" + fileName

				
			#填写的一级目录不为空,且不存在则创建它
			os.chdir(r'' + WORKSPACE_PATH)
			os.mkdir(fileName)
			self.refreshLbFirst()
			self.textFirst.delete(0.0, END)
			self.url1 = dirFirst

		if textSecond != "" and os.path.isfile(dirFirst) == False:
			fileName = str(self.lbSecond.size()) + " " + textSecond + ".md"
			if self.lbSecond.size() < 10:
				fileName = "0" + fileName

			self.url2 = u"" + self.url1 + "\\" + fileName
			fw = open(self.url2, "w") 
			fw.write(self.content.get("0.0", "end").encode('utf-8'))
			fw.close()
			self.refreshLbSecond()
			self.textSecond.delete(0.0, END)
			self.content.delete(0.0, END)

		if textFirst == "" and textSecond == "":
			fw = open(self.url2, "w") 
			fw.write(self.content.get("0.0", "end").encode('utf-8'))
			fw.close()			

	def datasSelect(self):
		textSecond = self.textSecond.get("0.0", "end").strip()
		self.lbSecond.delete(0, END)

		if textSecond != "":
			#文件查询
			for fileName in self.content2:        # 第二个实例
				if fileName.find(textSecond) != -1:
					self.lbSecond.insert(END,fileName)
		else:
			for fileName in self.content2: 
				self.lbSecond.insert(END,fileName)

	def datasDelete(self):
		#数据删除 doing
		index = self.lbFirst.curselection()
		index2 = self.lbSecond.curselection()
		if len(index) != 0:
			dirPath = u"" + WORKSPACE_PATH + "\\" + self.lbFirst.get(index) 
			if os.path.isdir(dirPath):
				os.rmdir(dirPath)
				self.url1 == ""
				self.url2 == ""
				self.refreshLbFirst()
		elif len(index2) != 0:
			filePath = u"" + self.url1 + "\\" + self.lbSecond.get(index2) 
			if os.path.isfile(filePath):
				os.remove(filePath)
				self.url2 == ""
				self.refreshLbSecond()

	def openFile(self):
		if os.path.isdir(self.url1):
			os.startfile(self.url1)

	def fileMove(self,paramNum):
		index = self.lbFirst.curselection()
		index2 = self.lbSecond.curselection()
		fileName = ""
		url = ""
		
		if len(index2) != 0:
			fileName = self.lbSecond.get(index2) 
			url = self.url1
		elif len(index) != 0:
			fileName = self.lbFirst.get(index) 
			url = r"" + WORKSPACE_PATH

		fileId = int(fileName[0:2])
		for d in os.listdir(url):
			if d != "README.md" and d != ".git" :
				if fileId == int(d[0:2]) - paramNum:
					#改名字
					os.rename(url + "\\" + d,url + "\\" + d.replace(str(fileId + paramNum), str(fileId), 1))
					os.rename(url + "\\" + fileName,url + "\\" + fileName.replace(str(fileId), str(fileId + paramNum), 1))
					break;

		self.refreshLbFirst()
		self.refreshLbSecond()

	def createWidgets(self):
		self.lbFirst = Listbox(self,width = 20,height = 40)
		self.lbFirst.grid(row = 1, column = 1, sticky="w")
		self.lbFirst.bind('<Double-Button-1>',self.lbFirstClick)
		self.refreshLbFirst()
		
		self.lbSecond = Listbox(self,width = 40,height = 40)
		self.lbSecond.grid(row = 1, column = 2, sticky="w")
		self.lbSecond.bind('<Double-Button-1>',self.lbSecondClick)		

		self.content = Text(self,width = 100, height = 45,font = '32')
		self.content.grid(row = 1, column = 3, sticky="w")

		self.textFirst = Text(self,width = 20, height = 1)
		self.textFirst.grid(row = 2, column = 1)

		self.textSecond = Text(self,width = 40, height = 1)
		self.textSecond.grid(row = 2, column = 2)


		self.frm = Frame(self,width = 100, height = 1)
		self.frm.grid(row = 2, column = 3)

		self.datasAdd = Button(self.frm,width = 18, text="添加修改", command=self.datasAdd)
		self.datasAdd.grid(row = 1, column = 1)
		self.datasSelect = Button(self.frm, width = 18,text="数据查询", command=self.datasSelect)
		self.datasSelect.grid(row = 1, column = 2)
		self.datasDelete = Button(self.frm,width = 18, text="数据删除", command=self.datasDelete)
		self.datasDelete.grid(row = 1, column = 3)
		self.clearText = Button(self.frm,width = 18, text="清空文本", command=self.clearText)
		self.clearText.grid(row = 1, column = 4)
		self.clearText = Button(self.frm,width = 18, text="打开文件", command=self.openFile)
		self.clearText.grid(row = 1, column = 5)

		self.clearText = Button(self.frm,width = 5, text="上移", command=lambda : self.fileMove(-1))
		self.clearText.grid(row = 1, column = 6)
		self.clearText = Button(self.frm,width = 5, text="下移", command=lambda : self.fileMove(1))
		self.clearText.grid(row = 1, column = 7)

if __name__ == '__main__':
	tools = Tools()
	tools.mainloop()
		

