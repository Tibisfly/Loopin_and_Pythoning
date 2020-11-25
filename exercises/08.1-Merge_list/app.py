chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']
both_lists = []

def merge_list(list1, list2):
    #Your code go here:
    for i in list1:
        both_lists.append(i)
    for i in list2:
        both_lists.append(i)
    return both_lists
    
print(merge_list(chunk_one, chunk_two))
