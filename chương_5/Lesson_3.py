#* SET
#* Cac cach khai bao
#* Cach 1
set1={'a', 2, 'h', 5, True,7,7,8,False}

#* Cach 2
set2=set()
set2.add(5)
set2.add(2)
set2.add(3)

#* Cach 3: Tao tu list
my_list=['a','b',1]
set3=set(my_list)

#* Cach 4: Tao tu tuple
my_tuple=(3,4,'a',6,'c')
set4=set(my_tuple)
print(set1)
print(set2)
print(set3)
print(set4)

#* Union - hợp hai set
set1={1,2,3,3,4,3}
set2={2,5,4,6,8,4}

#* Union - hop cua 2 set
union_set=set1.union(set2)
print(union_set)

#* Difference - hiệu của hai set
diff1 = set1-set2
diff2 = set1.difference(set2)
print(diff1)
print(diff2)