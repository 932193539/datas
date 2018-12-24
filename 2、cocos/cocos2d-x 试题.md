convertToNodeSpace

SpriteFrameCache 主要服务于多张碎图合并出来的纹理图片。这种纹理在一张大图中包含了多张小图

在游戏中需要加载大量的纹理图片，这些操作都是很耗内存和资源的。
当游戏中有个界面用到的图片非常多，第一次点进这界面时速度非常慢（因为要加载绘制很多图片）出现卡顿，我们可以使用TextureCache提前异步加载纹理，等加载结束，进入到这个界面再使用这些图片速度就会非常快。


1.autorelease和release的区别 

    release是立即释放引用计数，如果到达0，对象被销毁。 
    autorelease是延迟释放，是为了更好管理内存产生的。比如如下代码：  
CCObject *fun()   {   
   CCObject *myobj = new CCObject();   
   //myobj->release();                   //语句1      //myobj->autorelease()                //语句2      return myobj;   }   
    如果不调用语句1语句2，会导致内存泄露，根据函数定义原则，谁污染谁治理，如果要求外部调用者释放，不科学。 
    如果调用语句1，会立即被释放，外部调用者无法获取对象。 
    调用语句2，延迟被释放，可以保证外部调用者获得对象指针，而又会被释放。 
    autorelease的实现机制，是将对象加入一个pool统一管理，当pool被release时，pool里面每个对象都会被release。pool基于一个栈式结构管理，每一个mainloop会pop一次。同一个mainloop里面调用autorelease，会把引用加入栈顶pool。   

2.cocos2d-x的图形渲染机制是什么 

    只知道是每一帧调用mainloop，然后drawScene.    

3.cache机制原理是什么 

    把新加进内存的资源做一个hashmap存储，每一个资源加一个key。每次加载资源的时候，先查找资源是否存在，存在直接返回，否则加载进内存
   
4.场景切换的内存处理过程是什么 

    先构建新场景，然后显示新场景，然后释放旧场景。 
    但是在新场景onEnter，旧场景onExit的时候，会调用旧场景的cleanup，清理schedule相关部分。 

6.还有减少内存开销的方法有哪些，图片压缩方法有哪些 

    及时释放，减少泄露，重用资源，延迟加载，分部加载等。      
    一般的图片是4通道32位，即一个像素用4个字节表示，每个字节依次表示ARGB，即alpha，red，green，blue。那么图片占用的内存可以算出。 
    压缩像素即减少图片像素点多少，内存即减少。但是图片会变小。      
    压缩图片质量，即不用4个字节表示一个像素，如256色，就是用一个字节表示一个像素，每2个bit表示一个通道。但是图片表现效果变差。   
 
7.cocos2d-x 如何处理、存储、显示中文字符串,比如 玩家的名字，用户名，密码。存储在本地的文件里面，该如何处理才能防止不乱码？ 
 使用 iconv 库进行转换。或者XML 进行存储。 

9.简述cocos2d-x内存管理，图片缓存机制 

对于使用autorelease的对象，不必管它，每帧结束后会自动释放。

 CCNode节点管理 
cocos2d-x使用节点组成一棵树，渲染的时候要遍历这棵树。CCNode是所有节点类的父类，他内部使用了一个CCArray对象管理他的所有子节点，当对象被添加为子节点时，实际上是被添加到CCArray对象中，同时会调用这个对象的retain方法。同理，从CCArray中移除时，也会调用release方法。 静态工厂 
cocos2d-x中存在大量的静态工厂方法，这些方法中，全都对this指针调用了autorelease函数。 
cache机制类  
cache内部也使用了ratain和release方法，防止这些资源被释放掉。 
使用这些cache，我们可以保存预加载的一些资源，在方便的时候调用它，去绑定给一些对象。注意，这些cache在场景切换时，不会自动删除，需要手动调用purgeXXXX方法，进行清理。  

10.简述cocos2d-x 3.0与Cocos2d-x 2.X版本有哪些区别? 3.0 版本的新特性. 

以下提到即可 1 
运用了C++ 11  的新特性,例如: std::function strongly typed enums std::thread 
override  
2 
移除了所有Object-c模式，删除了CC前辍使用纯C++函数
Cocos2d-x面试题目 

3 
所有的单例都使用getInstance() and destroyInstance()   4 
创建新项目： 

9，cocos2d-x内存管理

cocos2d-x最初移植自cocos2d的objective C版本。因此，在内存管理上，使用了和NSObject类似的引用计数器方法，相关接口放置在CCObject类中。

引用计数器——手动管理内存

CCObject的及其子类的对象在创建时，引用计数自动设置为1。之后每次调用retain，引用计数+1。每次调用release，引用计数-1；若引用计数=0，则直接delete this。

retain是在指针传递和赋值时使用的，他的含义是表示拥有。这经常用在指针赋值上。

自动释放池——自动管理内存

对于使用autorelease的对象，不必管它，每帧结束后会自动释放。

CCNode节点管理

cocos2d-x使用节点组成一棵树，渲染的时候要遍历这棵树。CCNode是所有节点类的父类，他内部使用了一个CCArray对象管理他的所有子节点，当对象被添加为子节点时，实际上是被添加到CCArray对象中，同时会调用这个对象的retain方法。同理，从CCArray中移除时，也会调用release方法。

静态工厂

cocos2d-x中存在大量的静态工厂方法，这些方法中，全都对this指针调用了autorelease函数。

cache机制类

cache内部也使用了ratain和release方法，防止这些资源被释放掉。

使用这些cache，我们可以保存预加载的一些资源，在方便的时候调用它，去绑定给一些对象。注意，这些cache在场景切换时，不会自动删除，需要手动调用purgeXXXX方法，进行清理。




