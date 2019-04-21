def extend_list(val, list=[]):
    list.append(val)
    return list

list_one = extend_list(10)
list_two = extend_list(123, [])
list_three = extend_list('a')

print("List one : %s" % (list_one))
print("List two : %s" % (list_two))
print("List three : %s" % (list_three))
