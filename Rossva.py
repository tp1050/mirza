import dis
import inspect
from dill.source import getsource

def rossva(func):
    def inner(*args, **kwargs):
        print("")
        print(func.__name__)
        print(inspect.getsource(func))
        print(inspect.getsourcelines(func))
        print(dis.dis(func))
        print( getsource(func))
        return func(*args, **kwargs)
    return inner

def show(func):
    def inner(*args,**kwargs):
        print('This is the two separate args as inja hast',*args,*kwargs,'zortom')
        print('This is kwargs',', '.join('%s=%s' % kv for kv in kwargs.items()))
        return func(*args,**kwargs)
    return inner


