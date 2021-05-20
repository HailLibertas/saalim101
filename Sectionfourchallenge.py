list_option = ["1. Learn English",
               "2. Learn French",
               "3. Learn Turkish",
               "4. Learn Chinese",
               "5. Learn Spanish",
               "6. Learn Kiswahili",
               "7. Learn Swedish",
               "8. Learn Arabic",
               "0. Exit"]
for word in list_option:
    print(word)

for i in range(1, 9):
    choice = int(input("input you choice here: "))
    if choice == 0:
        print("Thank you, come again")
        break
    elif choice not in range(1, 9):
        print("please chose a valid option")
        for word in list_option:
            print(word)
        continue
    else:
        separator = ", "
        print("you chose wisely to " + separator.join(list_option[choice-1::8]))
        break
