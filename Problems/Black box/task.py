# use the function blackbox(lst) that is already defined
lst = list()
new_lst = blackbox(lst)
if all(id(lst[i]) != id(new_lst[i]) for i in range(len(lst))):
    print('new')
else:
    print('modifies')
