

# Big O of n
# O(n)
# write an algorithm for making a p and j sandwich be specific
'''
get bread from store
get peanut butter from store
get jelly from store
get knife from drawer
get a plate from cupboard
take two slices out of the bread bag
open jelly
open peanut butter
take knife and scoop a nice scoop of peanut butter
smear on the bread 
take knife and scoop a nice scoop of jelly
set of steps to be followed during problem solving in software or hardware routines


'''
# n = len(array)
   # return the element in the given array at the given index
 #get_element_at_index([1,2,3,4,5],3):
 def  get_index_at_element(array, goal_element):
     for i in range(len(array)):
         if array[i] == goal_element:
         return i # 0(1)
 # If we are looping through n times, its Time Complexity is Big O of n
 def get_products(array):
    products = []
    for x in array:

        for y in array:
            products.append(x * y)

    return products   
