def natural_numbers(x,i=1):
	#base case
  if i > x:
    return
  #recursive case
  else:
    print(i)
    natural_numbers(x,i+1)
natural_numbers(3)
#output: 1 2 3