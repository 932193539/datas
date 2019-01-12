
new 一般用于创建对象
1.new操作符从自由存储区为对象动态分配内存空间，而malloc函数从堆上动态分配内存
2.new操作符内存分配成功时，返回的是对象类型。malloc内存分配成功则是返回void * ，需要通过强制类型转换将void*指针转换成我们需要的类型
3.使用new操作符申请内存分配时无须指定内存块的大小，而malloc则需要显式地指出所需内存的尺寸。




C语言使用malloc从堆上分配内存，使用free释放
C++ 用new分配内存，用delete释放


delete会调用对象的析构函数,和new对应free只会释放内存，new调用构造函数。malloc与free是C++/C语言的标准库函数，new/delete是C++的运算符

