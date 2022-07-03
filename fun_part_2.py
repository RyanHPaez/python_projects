from multiprocessing.sharedctypes import Value

def arb_args(*args):
  print(*args)
  
arb_args ("\nalpha","\nbeta","\ncharlie")


#---------------------------------------------------------------------


def integers(a, b):
  def inner_integers_1():
    return a + b
  def inner_integers_2():
    return a - b

  return inner_integers_1() + inner_integers_2()
  
print(integers(1,5))
print(integers(8,4))
print(integers(2,2))


#---------------------------------------------------------------------


def manyParams (** kwargs):
  # print(kwargs)
  lstStr=[]
  lstNum=[]
  lstNonNum=[]

  for arg in kwargs.values():
    print(arg)
    if (type(arg) ==str):
      lstStr.append(arg)
    elif (type(arg) ==int):
      lstNum.append(arg+3)
    else:
      lstNonNum.append(arg)  


  return lstStr,lstNum,lstNonNum

manyParams (a="mz", b= False, c=45)