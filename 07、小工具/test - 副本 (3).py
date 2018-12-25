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

	def lbFirstClick(self,event):
		index = self.lbFirst.curselection()
		self.url1 = u"" + WORKSPACE_PATH + "\\" + self.lbFirst.get(index) 
		self.lbSecond.delete(0, END)
		for d in os.listdir(self.url1):
			self.lbSecond.insert(END,d)

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


	def datasSelect(self):
		fw = open(self.url2, "w") 
		fw.write(self.content.get("0.0", "end").strip().encode('utf-8'))
		fw.close()

	def datasInto(self):

		fw = open(self.url2, "w") 
		fw.write(self.content.get("0.0", "end").strip().encode('utf-8'))
		fw.close()

	def createWidgets(self):
		self.lbFirst = Listbox(self,width = 20,height = 50)
		self.lbFirst.grid(row = 1, column = 1, sticky="w")
		self.lbFirst.bind('<Double-Button-1>',self.lbFirstClick)
		
		for d in os.listdir(WORKSPACE_PATH):
			if os.path.isdir(WORKSPACE_PATH + "\\" + d):
				self.lbFirst.insert(END,d.decode('gbk'))

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

		self.datasSelect = Button(self.frm, width = 24,text="数据查询", command=self.datasSelect)
		self.datasSelect.grid(row = 1, column = 1)
		self.datasInto = Button(self.frm,width = 24, text="数据添加", command=self.datasInto)
		self.datasInto.grid(row = 1, column = 2)

if __name__ == '__main__':
	tools = Tools()
	tools.mainloop()
		

