import math
import numpy as np

a, b = map(int, input().split())

def f(x) :
    return b*x + a/math.sqrt(1+x)

def df(x) :
    return b - a/(2*(1+x)*math.sqrt(1+x))

def golden(f, x0, d, s):
    '''
    黄金分割法求最小值
    返回下降步长
    f: 需要求最小值的函数
    x0: x_0
    d: 方向 
    s: 步长上限
    '''
    t,e=0.618,1e-5
    a,b=0,s
    a1=a+(1-t)*(b-a)
    a2=a+t*(b-a)
    f1,f2=f(x0+a1*d),f(x0+a2*d)
    while abs(a-b)>=e:
        if f1<f2:
            a2,f2,b=a1,f1,a2
            a1=a+(1-t)*(b-a)
            f1=f(x0+a1*d)
        else:
            a,a1,f1=a1,a2,f2
            a2=a+t*(b-a)
            f2=f(x0+a2*d)
    a=(a1+a2)/2
    return a



def steepest_descent(f,df, x):
    '''
    最速下降法求最小值
    其中利用黄金分割法求步长
    f: 需要求最小值的函数
    df: 函数的导数
    x: 初始点
    '''
    k = 1
    while np.linalg.norm(df(x))>1e-12 :
        d = -df(x)
    # 以下三种方法都是求一维线搜索的步长，根据需要任选一种，注释掉其余两行即可。
        alpha = golden(f, x , d, 10000000000)                # 黄金分割法求步长
        # alpha = armijo(f, df, x, d, sigma=0.1)    # armijo非精确搜索求步长
        # alpha = wolfe_powell(f,df,x,d,sigma1=0.1,sigma2=0.9) # wolfe-powell非精确搜索求步长
        x = x + alpha*d
        k += 1
        # print(f(x))
    return x

if f(1) > f(0) : print('%.7f'%f(0))
else:
    x = steepest_descent(f,df,0)
    x = math.floor(x)
    print('%.10f'%min(f(x),f(x+1),f(x-1)))





