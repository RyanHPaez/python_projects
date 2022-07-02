from multiprocessing.sharedctypes import Value

def arb_args(*args):
  print(*args)
  
arb_args ("\nalpha","\nbeta","\ncharlie")


#---------------------------------------------------------------------


def integers(a, b):
  def integers_1():
    return a + b
  def integers_2():
    return a - b

  return integers_1() + integers_2()
  
print(integers(1,5))
print(integers(8,4))


#---------------------------------------------------------------------


# def manyParams (** kwargs):
#   print(kwargs)
#   lstStr=[]
#   lstNum=[]
#   lstNonNum=[]

#   for arg in kwargs.values():
#     print(arg)
#     if (type(arg) ==str):
#     elif (type(arg) ==str):

#   return lstStr,lstNum,lstNonNum

# manyParams (a="mz", b= False, c=45)