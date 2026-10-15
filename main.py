records = {}

while True:
    print("==== Record Keeping App ====")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")

    action = input("Select action: ")

    if action == 'a':
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        records[key] = value
        print(records)

    elif action == 'b':
        records.popitem()
        print(records)

    elif action == 'c':
        print('THANK YOU')
        break


