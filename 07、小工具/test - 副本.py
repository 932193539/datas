#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys,pysvn,ctypes

from Tkinter import *
WORKSPACE_PATH = u'D:/datas'.encode('gbk')
WORKSPACE_PATH_NAME = 'D:/datas'
LIST_FILE = ['\Client\src\__Message.lua', '\Client\src\__ClickButton.lua' ,'\Client\src\__OpenUI.lua', '\Client\src\__DispatchEvent.lua']

class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.url1 = ""
		self.url2 = ""
		self.pack()
		self.winfo_toplevel().title("游戏数据解析工具")
		self.createWidgets()

	def openfile(self,fileID):

		index2 = self.test.curselection()

		if len(index2) == 0:
			index = self.lb.curselection()
			self.url1 = u"" + WORKSPACE_PATH + "\\" + self.lb.get(index) 
			self.test.delete(0, END)
			for d in os.listdir(self.url1):
				self.test.insert(END,d)
		else:
			#有值就取
			temp = u"" + self.url1 + "\\" + self.test.get(index2) 
			print(temp)
			fo = open(r'' + temp, "r")
			self.content.delete(0.0, END)
			for line in fo.readlines():                          #依次读取每行  
				line = line.strip()                             #去掉每行头尾空白  
				self.content.insert(END,line +"\n")
			self.content.see(END)


	def createWidgets(self):

		self.lb = Listbox(self,width = 50,height = 50)
		self.lb.grid(row = 1, column = 1, sticky="w")
		
		for d in os.listdir(WORKSPACE_PATH):
			if os.path.isdir(WORKSPACE_PATH + "\\" + d):
				print d
				test2 = "测试" + WORKSPACE_PATH_NAME + "\\"
				test = d.decode('gbk')
				self.lb.insert(END,test)

		scrl = Scrollbar(self)
		self.lb.configure(yscrollcommand=scrl.set)   # 指定Listbox的yscrollbar的回调函数为Scrollbar的set，表示滚动条在窗口变化时实时更新
		scrl['command'] = self.lb.yview  # 指定Scrollbar的command的回调函数是Listbar的yview

		self.test = Listbox(self,width = 50,height = 50)
		self.test.grid(row = 1, column = 2, sticky="w")
		

		self.content = Text(self,width = 50, height = 50)
		self.content.grid(row = 1, column = 3, sticky="w")

		self.frm = Frame(self,width = 100, height = 1)
		self.frm.grid(row = 2, column = 1, sticky="w")

		self.clickButton = Button(self.frm,width = 24, text="Message", command=lambda fileID=0 : self.openfile(fileID)).grid(row = 3, column = 1)

if __name__ == '__main__':
	tools = Tools()
	tools.mainloop()
		






