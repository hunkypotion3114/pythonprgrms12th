# "'Q3 + Q3 Extension'"
# def exception_handler(value):
#     "''"
#     try :
#         element = eval(value)
#     except NameError :
#         element = value
#         print("Accepting input as string..")
#     return element


# def append_element(element_dict):
#     "''"
#     prompts = {
#         1: "Enter element(In the expected format): ",
#     }
#     value_entered = input(prompts[1])
#     element = exception_handler(value_entered)
#     element_type = str(type(element))[8:-2]
#     element_dict[element_type].append(element)


# def print_dict(element_dict):
#     "''"
#     for key,value in element_dict.items():
#         print(f"{key} : {value}")


# def display_as_list(element_dict):
#     "''"
#     ele_list = []
#     for element in element_dict.values():
#         ele_list += element
#     print(ele_list)


# prompts = {
#     1: "Enter [Y/N] to continue: ",
#     2: "Looks like you enter the wrong value!",
#     3: "Thank You!"
# }

# flow_control = "Y"
# counter = 0

# ele_dict = {
#     "int" : [],
#     "float" : [],
#     "str" : [],
#     "list" : [],
#     "tuple" : [],
#     "dict" : []
# }

# while flow_control == "Y":
#     if counter:
#         verdict = input(prompts[1]).upper()
#         if verdict == "Y":
#             append_element(ele_dict)
#         elif verdict == "N":
#             display_as_list(ele_dict)
#             print("Bifurcation: ")
#             print_dict(ele_dict)
#             print(prompts[3])
#             break
#         else:
#             print(prompts[2])
#     else:
#         append_element(ele_dict)
#         counter += 1

# "'Q6 + Q7'"

# def key_value_swap(dictionary):
#     "'Function to swap the key and values in a dictionary'"
#     dictionary_values = list(dictionary.values())
#     duplicate_values = []
#     unique_values = list(filter(lambda x : dictionary_values.count(x) == 1 , dictionary_values))
#     swapped_dictioanry = {}
#     for value in unique_values:
#         for key in dictionary:
#             if(dictionary[key] == value):
#                 swapped_dictioanry[value] = key
#                 dictionary_values.remove(value)
#             else:
#                 if(dictionary[key] not in duplicate_values):
#                     duplicate_values.append(dictionary[key])
#     for value in duplicate_values:
#         list_of_keys = []
#         for key in dictionary:
#             if(dictionary[key] == value):
#                 list_of_keys.append(key)
#         swapped_dictioanry[value] = list_of_keys
#     return swapped_dictioanry

# prompts = {
#     1 : "Enter length of dictionary: ",
#     2 : "Enter name of student: ",
#     3: "Enter the corrosponding height(in cm): "
# }

# ht = {}
# len_dict = int(input(prompts[1]))
# for a in range(0,len_dict):
#     name = input(prompts[2])
#     height = float(input(prompts[3]))
#     ht[name] = height

# print(f"Dictionary: {ht} \n Swapped dictionary : {key_value_swap(ht)}")

"'Q5 + Q8'"

def exception_handler(value):
    "''"
    try :
        element = eval(value)
    except NameError :
        element = value
        print("Accepting input as string..")
    return element

def append_element(ele_set,dictionary=0):
    "''"
    prompts = {
        1: "Enter element to append: ",
        2: "Enter key: ",
        3: "Enter corrosponding value: ",
        4: "Wrong format for key in dictionary!"
    }
    if(dictionary):
        key = exception_handler(input(prompts[2]))
        key_type = str(type(key))[8:-2]
        if(key_type in ["int","str","float"]):
            value = exception_handler(input(prompts[3]))
            ele_set[key] = value
        else:
            print(prompts[4])
    else:
        element = exception_handler(input(prompts[1]))
        ele_set.append(element)

def modify_element_list(ele_set):
    "''"
    prompts = {
        1: "Enter 1-to modify using index\nEnter 2-to modify using value\nEnter choice: ",
        2: "Enter index of element to modify: ",
        3: "Enter element value to modify: ",
        4: "Enter modified value: ",
        5: "key/index/element does not exist",
        6: "Enter how many values to replace"
    }
    verdict = exception_handler(input(prompts[1]))
    if(verdict==1):
        max_index = len(ele_set) -1
        index = int(input(prompts[2]))
        if(index <= max_index):
            ele_set[index] = exception_handler(prompts[4])
        else:
            print(prompts[5])
    elif(verdict == 2):
        value = exception_handler(prompts[3]) 
        if(value in ele_set):
            total_count = ele_set.count(value)
            print(f"value repeated {total_count} times")
            times_to_replace = int(input(prompts[6]))
            new_value = exception_handler(input(prompts[4]))
            index_list = [a for a in range(0,len(ele_set)) if ele_set[a] == value]
            for b in range(0,times_to_replace):
                index = index_list[b]
                ele_set[index] = new_value
        else:
            print(prompts[5])
    else:
        print(prompts[5])


def modify_element_dict(ele_set):
    "''"
    prompts = {
        1: "Enter key value: ",
        2: "Enter modified value: ",
        3: "key/index/element does not exist",
    }
    key = exception_handler(input(prompts[1]))
    key_type = str(type(key))[8:-2]
    if(key_type in ["int","str","float"]):
        value = ele_set.get(key, prompts[3])
        if(value == prompts[3]):
            print(prompts[3])
        else:
            ele_set[key] = exception_handler(input(prompts[2]))
    else:
        print(prompts[3])

def display_delete_element(ele_set,delete=0):
    "'"
    prompts = {
        1: "Enter 1-print/delete range of elements\nEnter 2-print/delete single element\nEnter choice: ",
        2: "Enter index of element: ",
        3: "Enter lower index(LI) , Higher Index(HI) (as (LI,HI): ",
        
    }