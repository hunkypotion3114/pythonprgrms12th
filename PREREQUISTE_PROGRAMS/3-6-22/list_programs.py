"'Q3 + Q3 Extension'"
def exception_handler(value):
    "''"
    try :
        element = eval(value)
    except NameError :
        element = value
        print("Accepting input as string..")
    return element


def append_element(element_dict):
    "''"
    prompts = {
        1: "Enter element(In the expected format): ",
    }
    value_entered = input(prompts[1])
    element = exception_handler(value_entered)
    element_type = str(type(element))[8:-2]
    element_dict[element_type].append(element)


def print_dict(element_dict):
    "''"
    for key,value in element_dict.items():
        print(f"{key} : {value}")


def display_as_list(element_dict):
    "''"
    ele_list = []
    for element in element_dict.values():
        ele_list += element
    print(ele_list)


prompts = {
    1: "Enter [Y/N] to continue: ",
    2: "Looks like you enter the wrong value!",
    3: "Thank You!"
}

flow_control = "Y"
counter = 0

ele_dict = {
    "int" : [],
    "float" : [],
    "str" : [],
    "list" : [],
    "tuple" : [],
    "dict" : []
}

while flow_control == "Y":
    if counter:
        verdict = input(prompts[1]).upper()
        if verdict == "Y":
            append_element(ele_dict)
        elif verdict == "N":
            display_as_list(ele_dict)
            print("Bifurcation: ")
            print_dict(ele_dict)
            print(prompts[3])
            break
        else:
            print(prompts[2])
    else:
        append_element(ele_dict)
        counter += 1

"'Q5'"
