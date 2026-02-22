# Use map to return the list of the square of each numbers.
#Use filter to return the list with only the names that are less than or equal to seven letters.
#Use reduce to return the product of these numbers.
#Input: ints = [4, 6, 3, 9, 2, 8, 12]
# names = ["scaler", "interviewbit", "rishabh", "student", "course"]
#numbers = [4, 6, 9, 23, 5]
# Output: [16, 36, 9, 81, 4, 64, 144]
#['scaler', 'rishabh', 'student', 'course']
#24840 


from functools import reduce 
def func(ints, names, numbers):
    
    # Use map to print the square of each numbers
    # Use filter to print only the names that are less than or equal to seven letters
    # Use reduce to print the product of these numbers
    
    # Complete all the three codes.
    map_result = list(map(lambda x:x*x,ints))
    filter_result = list(filter(lambda x: len(x)<=7,names))
    reduce_result = reduce(lambda x,y: x*y,numbers)
    
    return map_result, filter_result, reduce_result
    