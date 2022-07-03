# count up
def natural_numbers(x,i=1):
	#base case
  if i > x:
    return
  #recursive case
  else:
    print(i)
    natural_numbers(x,i+1)
natural_numbers(8)
#output: 1 2 3