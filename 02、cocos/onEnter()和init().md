这俩个方法都是CCNode的方法。其区别如下：

1.其被调用的顺序是先init()，后onEnter()。

2.init()在类的初始化时只会调用一次。

3.onEnter在该类被载入场景的时候被调用，可能会发生多次。

4.CCLayer* cclayer = new MyLayer();
这种情况下，只会触发onEnter。

5.CCLayer* cclayer = MyLayer::create();
这样情况下，既会触发init()方法，也会触发onEnter()方法。


如果你重写了onEnter或onEnterTransitionDidFinish方法 你应该在方法中调用它的父类
onEnter只能被定义一次。先发现多次定义会报错。

