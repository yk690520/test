# -*- coding:utf-8 -*-

#针对昨天想法的实现

#第一种方式
def demo1(a=0,b=0):
    for i in range(a):
        #此处实现a控制的操作逻辑
        print('点击【a】%s次' % a)
    for j in range(b):
        #此处实现b控制的操作逻辑
        print('点击【b】%s次' % b)


#第二种方式
def demo2(times=0,*,func):
    '''
    *是一个分隔符，用来区分位置参数和命名关键字参数的符号
    :param times: 步骤的执行次数
    :param func: 需要执行的步骤
    :return:
    '''
    for i in range(times):
        func()

#第三种实现
def demo3(kwargs):
    '''
    :param kwargs: 执行步骤和执行次数的一个字典{步骤a:a次,步骤b:b次}
    :return:
    '''
    for func,times in kwargs.items():
        for i in range(times):
            func()


#函数的调用
if __name__=='__main__':

    print('第一种实现的调用')
    #只执行【a】2次，不执行b
    demo1(2)
    #或者 demo1(a=2)

    #只执行【b】2次，不执行a
    demo1(b=2)

    #都执行2次
    demo1(2,2)
    #或者 demo(a=2,b=2) 或者 demo(b=2,a=2)

    print('第二种实现的调用')
    #其中【2】是步骤的执行次数，func是需要执行的步骤，lambda是匿名函数的写法，也可以直接传入一个函数
    demo2(2,func=lambda :print('点击【a】2次'))
    demo2(2, func=lambda: print('点击【b】2次'))


    print("第三种实现的调用")
    #先将步骤和执行次数组装成一个字典，再将这个字典传入
    temp={lambda :print("点击【a】2次"):2,lambda :print('点击【b】2次'):2}
    demo3(temp)


    #我比较喜欢第二种包装，因为比较灵活
