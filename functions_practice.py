def hello(name):
  print("Hello "+ name)

hello('whatever your name is.')

# ---------------------------------------------
def pack(pack1, pack2, pack3):
  # print(pack1+pack2+pack3)
  return [pack1, pack2, pack3]
  
pack ("\ta","\tb","\tc")
pack ("\nalpha","\nbeta","\ncharlie")

# ---------------------------------------------

def eat_lunch(my_list):
  
  # print (my_list)
  if len(my_list) ==0:    
     print("my lunch box is empty!")
  for i in range(len(my_list)):
    if i == 0:
      print("first I eat " + my_list [i])
    else:
      print("Next, I eat " +my_list [i])
eat_lunch(["Strawberries", "yogurt", "water"])
# eat_lunch(["apples", "sandwich", "juice"])
eat_lunch([])


