1.弱引用:在计算机程序设计中，弱引用与强引用相对，是指不能确保其引用的对象不会被垃圾回收器回收的引用。一个对象若只被弱引用所引用，则被认为是不可访问（或弱可访问）的，并因此可能在任何时刻被回收。一些配有垃圾回收机制的语言

 
local testa = {}
tbl_key = {}
testa[tbl_key] = 1
tbl_key = {}
testa[tbl_key] = 2
 
--垃圾回收
collectgarbage()
 
local function PrintInfo()
 
	for k, v in pairs(testa) do
		print(k, "===", v)
	end
 
end
 
PrintInfo()

--结果如下
table: 004FB890	===	1
table: 004FB8E0	===	2


--lua弱表，主要是删除key或者value是table的一种元方法
--元表里的__mode字段包含k或者v；k表示key为弱引用；v表示value为弱引用

local testa = {}
local mt = {__mode = 'k'}
setmetatable(testa,mt)
 
tbl_key = {}
testa[tbl_key] = 1
tbl_key = {}
testa[tbl_key] = 2
 
--垃圾回收
collectgarbage()
 
local function PrintInfo()
 
	for k, v in pairs(testa) do
		print(k, "===", v)
	end
 
end
 
PrintInfo()

--结果如下
table: 006EB930	===	2




通过key的弱引用，覆盖了key为key_table的值；没有其他地方在引用，所以被回收掉了
(个人理解:全局变量tbl_key第一次定义时如果有人强引用它,那它不会被回收,但是如果是弱引用且它被第二次重新定义了,那在回收时就会回收第一次定义的)


local test = {1}
local test = {2}
注意:这里两次定义的test是开辟了两个内存空间的，通过强引用是可以得到value = 1、2 这两个值的


