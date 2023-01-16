from array import *

vals= array('i',[3,5,6,2])
print(vals)
print(vals.buffer_info())

# for j in range(len(vals)):
#     print(vals[j])
for e in vals:
    print(e)

New_vals= array(vals.typecode,(a*a for a in vals))
print("New Array:")
for g in New_vals:
    print(g)













