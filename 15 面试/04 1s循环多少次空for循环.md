GetTickCount是一种函数。GetTickCount返回（retrieve）从操作系统（程序）启动所经过（elapsed）的毫秒数
它经常用于测试代码算法执行效率上

如下代码表面一般的电脑差不多能执行1亿多的for空循环


    DWORD startTick = GetTickCount();

    int i = 0;
    for(;;i++)
    {   
        DWORD endTick = GetTickCount();
        if((endTick - startTick)/1000 >= 1) break;

    }
	    printf("i = %d\n", i);

    system("pause");

