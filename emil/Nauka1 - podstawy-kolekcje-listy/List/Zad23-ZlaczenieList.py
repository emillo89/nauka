from itertools import chain

original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]

merged_list = list(chain(*original_list))
print((merged_list))