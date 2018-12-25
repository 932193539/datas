#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 数据存取工具
import os, sys,pysvn,ctypes

from Tkinter import *
WORKSPACE_PATH = u'D:/datas'.encode('gbk')

class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.url1 = ""
		self.url2 = ""
		self.pack()
		self.winfo_toplevel().title("数据存取工具")
		self.createWidgets()


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
		for d in os.listdir(self.url1):
			self.lbSecond.insert(END,d)

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
				line = line.strip()                          #去掉每行头尾空白  
				self.content.insert(END,line +"\n")
			self.content.see(END)

	def datasAdd(self):
		#数据添加与更新
		textFirst = self.textFirst.get("0.0", "end").strip().encode('utf-8')
		textSecond = self.textSecond.get("0.0", "end").strip().encode('utf-8')

		dirFirst = u"" + WORKSPACE_PATH + "\\" + textFirst

		if textFirst != "" and os.path.isdir(dirFirst) == False:
			#填写的一级目录不为空,且不存在则创建它
			os.chdir(r'' + WORKSPACE_PATH)
			os.mkdir(textFirst)
			self.refreshLbFirst()
			self.url1 = dirFirst

		if textSecond != "" and os.path.isfile(dirFirst) == False:
			self.url2 = u"" + self.url1 + "\\" + textSecond
			fw = open(self.url2, "w") 
			fw.write(self.content.get("0.0", "end").strip().encode('utf-8'))
			fw.close()

		if textFirst != "" and textSecond != "":
			fw = open(self.url2, "w") 
			fw.write(self.content.get("0.0", "end").strip().encode('utf-8'))
			fw.close()

	def datasSelect(self):
		#数据查询与搜索 doing(好像沒必要弄)
		fw = open(self.url2, "w") 
		fw.write(self.content.get("0.0", "end").strip().encode('utf-8'))
		fw.close()
		
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

	def clearText(self):
		#清空文本
		self.textFirst.delete(0.0, END)
		self.textSecond.delete(0.0, END)
		self.content.delete(0.0, END)

	def createWidgets(self):
		self.lbFirst = Listbox(self,width = 20,height = 50)
		self.lbFirst.grid(row = 1, column = 1, sticky="w")
		self.lbFirst.bind('<Double-Button-1>',self.lbFirstClick)
		
		self.refreshLbFirst()

		self.lbSecond = Listbox(self,width = 40,height = 50)
		self.lbSecond.grid(row = 1, column = 2, sticky="w")
		self.lbSecond.bind('<Double-Button-1>',self.lbSecondClick)		

		self.content = Text(self,width = 100, height = 69)
		self.content.grid(row = 1, column = 3, sticky="w")

		self.textFirst = Text(self,width = 20, height = 1)
		self.textFirst.grid(row = 2, column = 1)

		self.textSecond = Text(self,width = 40, height = 1)
		self.textSecond.grid(row = 2, column = 2)


		self.frm = Frame(self,width = 100, height = 1)
		self.frm.grid(row = 2, column = 3)

		self.datasAdd = Button(self.frm,width = 24, text="添加修改", command=self.datasAdd)
		self.datasAdd.grid(row = 1, column = 1)
		self.datasSelect = Button(self.frm, width = 24,text="数据查询", command=self.datasSelect)
		self.datasSelect.grid(row = 1, column = 2)
		self.datasDelete = Button(self.frm,width = 24, text="数据删除", command=self.datasDelete)
		self.datasDelete.grid(row = 1, column = 3)
		self.clearText = Button(self.frm,width = 24, text="清空文本", command=self.clearText)
		self.clearText.grid(row = 1, column = 4)

if __name__ == '__main__':
	tools = Tools()
	tools.mainloop()
		

