һ��Э����ʲô��
������1���߳�
�������ȸ�ϰһ�¶��̡߳����Ƕ�֪���̡߳���Thread��ÿһ���̶߳�����һ��ִ�����С�
�����������ڳ����д������̵߳�ʱ�򣬿�������ͬһʱ�̶���߳���ͬʱִ�еģ�����ʵ���϶���߳��ǲ����ģ���Ϊֻ��һ��CPU������ʵ����ͬһ��ʱ��ֻ��һ���߳���ִ�С�
������һ��ʱ��Ƭ��ִ���ĸ��߳��ǲ�ȷ���ģ����ǿ��Կ����̵߳����ȼ��������������̵߳�����CPU�ĵ��Ⱦ�����
������2��Э��
������ʲô��Э���أ�Э�̸��̶߳�����һ��ִ�����С���ͬ���ǣ�Э�̰��߳��в�ȷ���ĵط������ܵ�ȥ����ִ�����м���л�������CPU���صĽ��У������ɳ�����ʽ�Ľ��С�
�������ԣ�ʹ��Э��ʵ�ֲ�������Ҫ���Э�̱˴�Э����
����resume��yeild��Э����
����resume��yeild��Э����LuaЭ�̵ĺ��ġ������һ��ͼ����һ�£���һ�������ӡ�󡣶��������coroutine�����ϸ���ͺ����Ĵ��룬Ӧ�ÿ��Ը����Э�̵ĸ����ˡ�
����ע�������ڷ��״�resumeЭ�̵�����£�resume��yield�Ļ�����õ������������״�resumeЭ�̣���ôresume�Ĳ�����ֱ�Ӵ��ݸ�Э�̺�����
����coroutine�����
(1)coroutine.create (f)
������һ��������������������Э�̡�����һ����thread������
(2)coroutine.isyieldable ()
��������������е�Э�̿����ó����򷵻��档ֵ��ע����ǣ�ֻ����Э�̣��̣߳���C���������޷��ó��ġ�
(3)coroutine.resume (co [, val1, ������])
��������һ���ǳ���Ҫ�ĺ����������������ٴ�����һ��Э�̣�ʹ���ɹ���״̬�������״̬��
����������ô˵��resume�����൱����ִ��Э���еķ���������Val1...��ִ��Э��coʱ���ݸ�Э�̵ķ�����
�����״�ִ��Э��coʱ������Val1...�ᴫ�ݸ�Э��co�ĺ�����
�����ٴ�ִ��Э��coʱ������Val1...����Ϊ��Э��co����һ��yeild�ķ���ֵ��
������֪����仰��������û������Э�̵ĺ��ġ����û���Ҳ���ü����������¿����Ժ��һ���ϸ���͡�
����resume��������ʲô�أ���3�������
����1�������Э��co�ĺ���ִ����ϣ�Э��������ֹ��resume ���� true�ͺ����ķ���ֵ��
����2�������Э��co�ĺ���ִ�й����У�Э���ó��ˣ�������yeild()����������ôresume����true��Э���е���yeild����Ĳ�����
����3�������Э��co�ĺ���ִ�й����з�������resume����false�������Ϣ��
�������Կ���resume������ζ����ᵼ�³�������������ڱ���ģʽ��ִ�еġ�
(4)coroutine.running ()
���������жϵ�ǰִ�е�Э���ǲ������̣߳�����ǣ��ͷ���true��
(5)coroutine.status (co)
��������һ���ַ�������ʾЭ�̵�״̬����4��״̬��
����1����running�������Э�̵ĺ����е���status������Э������ľ������ôִ�е������ʱ��Ż᷵��running״̬��
����2����suspended�����Э�̻�δ�����������������yeild��û��ʼ���У���ô����suspended״̬��
����3����normal�����Э��AresumeЭ��Bʱ��Э��A���ڵ�״̬Ϊnormal����Э��B��ִ�й����У�Э��A��һֱ����normal״̬����Ϊ����ʱ��Ȳ��ǹ���״̬��Ҳ��������״̬��
����4����dead�����һ��Э�̷��������������������ֹ����ô�ʹ���dead״̬�������ʱ���������resume��������false�ʹ�����Ϣ��
(6)coroutine.wrap (f)
����wrap()Ҳ����������Э�̵ġ�ֻ�������Э�̵ľ�������صġ���create()���������ڣ�
����1����wrap()���ص���һ��������ÿ�ε�����������൱�ڵ���coroutine.resume()��
����2����������������൱����ִ��resume()������
����3���������������ʱ����Ĳ��������൱���ڵ���resumeʱ����ĳ�Э�̵ľ���������������
����4���������������ʱ����resume��ͬ���ǣ����������ڱ���ģʽ��ִ�еģ���ִ�б�����ֱ�������׳���
(7)coroutine.yield (������)
����ʹ����ִ�еĺ�������
�������ݸ�yeild�Ĳ�������Ϊresume�Ķ��ⷵ��ֵ��
 ����ͬʱ������Ը�Э�̲��ǵ�һ��ִ��resume��resume��������Ĳ���������Ϊyield�ķ���ֵ��
�ġ����ӽ��ס�
 ��1��������1����ʵ��resume��yield�����£�
	coco = coroutine.create(function (a,b)
		print("resume args:"..a..","..b)
		yreturn = coroutine.yield()
		print ("yreturn :"..yreturn)
	end)
	coroutine.resume(coco,0,1)
	coroutine.resume(coco,21)
	�����
	resume args:0,1
	yreturn :21
��2��������2����ʹ��wrap�����£�
	coco2 = coroutine.wrap(function (a,b)
		print("resume args:"..a..","..b)
		yreturn = coroutine.yield()
		print ("yreturn :"..yreturn)
	end)
	print(type(coco2))
	coco2(0,1)
	coco2(21)
	�����
	function
	resume args:0,1
	yreturn :21
��3��
	function status()
		print("co1's status :"..coroutine.status(co1).." ,co2's status: "..coroutine.status(co2))
	end

	co1 = coroutine.create(function ( a )
		print("arg is :"..a)
		status()
		local stat,rere = coroutine.resume(co2,"2")
		print("resume's return is "..rere)
		status()
		local stat2,rere2 = coroutine.resume(co2,"4")
		print("resume's return is "..rere2)
		local arg = coroutine.yield("6")
	end)
	co2 = coroutine.create(function ( a )
		print("arg is :"..a)
		status()
		local rey = coroutine.yield("3")
		print("yeild's return is " .. rey)
		status()
		coroutine.yield("5")
	end)
	--���߳�ִ��co1,�����ַ�����main thread arg��
	stat,mainre = coroutine.resume(co1,"1")
	status()
	print("last return is "..mainre)
	�����
	arg is :1
	co1's status :running ,co2's status: suspended
	arg is :2
	co1's status :normal ,co2's status: running
	resume's return is 3
	co1's status :running ,co2's status: suspended
	yeild's return is 4
	co1's status :normal ,co2's status: running
	resume's return is 5
	co1's status :suspended ,co2's status: suspended
	last return is 6
��4��
	function foo(a)
		print("foo", a)
		return coroutine.yield(2 * a)
	end

	co = coroutine.create(function ( a, b )
		print("co-body", a, b)
		local r = foo(a + 1)
		print("co-body", r)
		local r, s = coroutine.yield(a + b, a - b)
		print("co-body", r, s)
		return b, "end"
	end)

	print("main", coroutine.resume(co, 1, 10))
	print("main", coroutine.resume(co, "r"))
	print("main", coroutine.resume(co, "x", "y"))
	print("main", coroutine.resume(co, "x", "y"))
	������£�
	co-body    1    10
	foo    2
	main    true    4
	co-body    r
	main    true    11    -9
	co-body    x    y
	main    true    10    end
	main    false    cannot resume dead coroutine





































