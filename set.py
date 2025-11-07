# tuples ()
# lists []
# sets {}

s1 = {2 , 4, 6, 2, 8}
print(s1)  
list(s1)
print(type(s1))



A = {1, 2, 3 }
B = {3, 4, 5 }
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

li1 = [1, 2, 3, 4, 5, 1, 2, 3]
li_set = set(li1)
print( "list set = " ,li_set)
# creating frozen set
fs = frozenset([1 , 2, 3 , 4])
print("frozen set = ", fs)
print(type(fs))

my_dict = { "name" : "Ayaan" ,
            "age" : 19 ,
              "country" : "India" }
print(my_dict)

my_lis = (1,4,2,4,2,1,3,)
unique_lis = set(my_lis)
print("unique list = ", unique_lis)


