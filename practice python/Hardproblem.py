word = input()
no_part = int(input())

lenght_word = len(word)
count_table = 0


while (count_table*((2*no_part) + (no_part-2))) < lenght_word:
    count_table += 1

res_list = []
if count_table == 1:
    current_index = 0
    middle_index_count = no_part - 2
    for i in range(no_part):
        initial_list = []
        if (i == 0) or (i == (no_part-1)):
            for j in range(no_part):
                try:
                    initial_list.append(word[current_index])
                    current_index += 1
                except IndexError:
                    break
            res_list.append(initial_list[ : : -1])
        else:
            for j in range(no_part):
                if j == middle_index_count:
                    try:
                        initial_list.append(word[current_index])
                        middle_index_count -= 1
                        current_index += 1
                    except IndexError:
                        break
                else:
                    initial_list.append("x")
            res_list.append(initial_list)
else:
    count_index = 0
    current_index = 0
    middle_index_count = no_part - 2
    for i in range(count_table*no_part):
        initial_list = []
        if i == count_index:
            middle_index_count = no_part - 2
            for j in range(no_part):
                try: 
                    initial_list.append(word[current_index])
                except IndexError:
                    break
                current_index += 1
            count_index += (no_part-1)
            res_list.append(initial_list[ : :-1])
        else:
            for j in range(no_part):
                if j == middle_index_count:
                    try:
                        initial_list.append(word[current_index])
                        middle_index_count -= 1
                        current_index += 1 
                    except IndexError:
                        break
                else:
                    initial_list.append("x")
            res_list.append(initial_list) 

final_str = ""

for i in range(no_part):
    for j in res_list:
        try:
            final_str += j[i]
        except IndexError:
            break

print(final_str.replace("x", ""))