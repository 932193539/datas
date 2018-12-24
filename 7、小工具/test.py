#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 阅读工具
import os, sys,pysvn,ctypes

from Tkinter import *
WORKSPACE_PATH = u'D:/datas'.encode('gbk')

class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.url1 = ""
		self.url2 = ""
		self.pack()
		self.winfo_toplevel().title("游戏数据解析工具")
		self.createWidgets()

	def lbSecondClick(self,event):
		index = self.lbSecond.curselection()
		if len(index) != 0:
			#有值就取
			self.url2 = u"" + self.url1 + "\\" + self.lbSecond.get(index) 
			fo = open(r'' + self.url2, "r")
			self.content.delete(0.0, END)
			for line in fo.readlines():                          #依次读取每行  
				line = line.strip()                             #去掉每行头尾空白  
				self.content.insert(END,line +"\n")
			self.content.see(END)

	def lbFirstClick(self,event):
		index = self.lbFirst.curselection()
		self.url1 = u"" + WORKSPACE_PATH + "\\" + self.lbFirst.get(index) 
		self.lbSecond.delete(0, END)
		for d in os.listdir(self.url1):
			self.lbSecond.insert(END,d)

	def createWidgets(self):
		self.lbFirst = Listbox(self,width = 50,height = 50)
		self.lbFirst.grid(row = 1, column = 1, sticky="w")
		self.lbFirst.bind('<Double-Button-1>',self.lbFirstClick)
		
		for d in os.listdir(WORKSPACE_PATH):
			if os.path.isdir(WORKSPACE_PATH + "\\" + d):
				self.lbFirst.insert(END,d.decode('gbk'))

		self.lbSecond = Listbox(self,width = 50,height = 50)
		self.lbSecond.grid(row = 1, column = 2, sticky="w")
		self.lbSecond.bind('<Double-Button-1>',self.lbSecondClick)		

		self.content = Text(self,width = 100, height = 69)
		self.content.grid(row = 1, column = 3, sticky="w")

if __name__ == '__main__':
	tools = Tools()
	tools.mainloop()
		

