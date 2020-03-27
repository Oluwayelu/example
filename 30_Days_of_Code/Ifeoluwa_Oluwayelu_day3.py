

def bin_search(list_of_nums, num):
  a = 0
  b = len(list_of_nums) -1
  while a <= b:
    mid = (a-b)//2
    
    if list_of_nums[mid] == num:
      return True
      
    else:
    	if list_of_nums[mid] > num:
    		b = mid - 1
    	else:
    		a = mid + 1
  return False

#test
print(bin_search([1,3,5,6], 4))
