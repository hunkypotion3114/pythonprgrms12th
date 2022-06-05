# FLIGHT_LOGS = { FLIGHT_NO : [FLIGHT_NO, PILOT_NAME , DEP_TIME , DEP_DATE]}
# QUERY USING FLIGHT_NO... CAN BE MADE TO QUERY USING OTHER ATTRIUBTES...
# USE WHILE

def insert_flight_details(flight_log):
    prompts = {
        1:  "Enter flight no: ",
        2:  "Enter pilot name: ",
        3:  "Enter departure time: ",
        4:  "Enter departure date: "
    }
    flight_details = []
    for a in range(1,5):
        value = input(prompts[a])
        if(a == 1):
            if(value in flight_log.keys()):
                print("Looks like this flight already exists!")
                print("Flights currently in logs: ")
                for num in flight_log.keys():
                    print(num, end = " ")
                print()
                value = input("Enter flight no apart from above else enter -1: ")
                if(value == "-1"):
                    return 0
        flight_details.append(value)
    flight_log[flight_details[0]] = flight_details


def display_flights(flight_log,single=0,flight=[]):
    attrtibutes = { 
        1: "flight no: ",
        2: "pilot_name: ",
        3: "departure time: ",
        4: "departure date: "
    }
    if(single==0):
        for flight in flight_log.values():
            for a in range(0,4):
                print(f"{attrtibutes[a+1]}{flight[a]}",end = " ")
            print()
    else:
        for a in range(0,4):
            print(f"{attrtibutes[a+1]}{flight[a]}",end = " ")
        print()


def get_flight_detail(flight_log):
    flight_no = input("Enter flight no: ")
    flight_details = flight_log.get(flight_no , 0)
    if(flight_details):
        display_flights(flight_log,single=1,flight=flight_details)
    else:
        print("Looks like that flight does not exist!")


flow_control = "Y"
prompts = {
    1: "Input flight details --> 1",
    2: "Display all flights  --> 2",
    3: "Get flight detail    --> 3",
    4: "Continue [Y/N]       --> 4",
    5: "Enter choice: "
}

functions_dictionary = {
    1:insert_flight_details,
    2:display_flights,
    3:get_flight_detail
}

flight_log = {}

while(flow_control == "Y"):
    print("-------MENU-------")
    for a in range(1,5):
        print(prompts[a])
    value_entered = input(prompts[5])
    if(value_entered in ["1","2","3","4"]):
        option_selected = int(value_entered)
        if(option_selected in range(1,4)):
            functions_dictionary[option_selected](flight_log)
        else:
            verdict = input("Enter Y to continue , N to exit: ").upper()
            if(verdict in ["Y","N"]):
                flow_control = verdict
            else:
                print("Try again!")
    else:
        print("Not a valid option choice!")
        