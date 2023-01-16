from array import *

# vals= array('i',[3,5,6,2])
# print(vals)
# print(vals.buffer_info())
#
# # for j in range(len(vals)):
# #     print(vals[j])
# for e in vals:
#     print(e)
#
# New_vals= array(vals.typecode,(a*a for a in vals))
# print("New Array:")
# for g in New_vals:
#     print(g)

val = array('i',[])
x = int(input("Enter the number of values: "))
for e in range(x):
    x=int(input("Enter the number: "))
    val.append(x)
print(val)
n = int(input("Enter the number to find: "))
k=0
for g in val:
    if n==g:
        print(k)
        break
    k+=1
else:
    print("not in array")
print(val.index(n))










