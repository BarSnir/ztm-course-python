condition_a = True
condition_b = True

# Short circuting
print(condition_a and condition_b)
print("is 4 more than 5->",4 > 5)
print("is 4 less than 5->",4 < 5)
print("is 3 equal to 3->",3 == 3)

# == <= >= > < 
# and or not not(condition)

print("True == 1->",True == 1)
print("'' == 1->",'' == 1)
print("[] == 1->",[] == 1)
print("10 == 10.0->",10 == 10.0)
print("[] == []-> ",[] == [])
print("[] == []-> Allocation memory check",[] is [])
print("[1, 2, 3] == [1, 2, 3]->",[1, 2, 3] == [1, 2, 3])
print("[1, 2] == [1, 2, 3]->",[1, 2] == [1, 2, 3])
print("[1, 2, 3] == [1, 2, 3]-> Allocation memory check",[1, 2, 3] is [1, 2, 3])
print("{a:1} == {a:1}->",{'a':1} == {'a':1})
print("0j", True == 0j)