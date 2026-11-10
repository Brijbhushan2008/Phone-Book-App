import time
import os
os.system('cls')

phonenumber={}

print('\n\n=====PHONE BOOK=====\n')

while True:
    print('\n1.[ADD]\n2.[SEARCH]\n3.[VIEW ALL]\n4.[DELETE]\n5.[EXIT]')
    op=int(input("Enter you want to do(1,2,3,4,5):"))
    if op==1:           #ADD
        name=input('Enter the name:')
        number=input("Enter the number:")
        phonenumber[name]=number
        print(f"\n[{name}] has been added with number [{number}]")
        time.sleep(2)

    elif op==2:          #SEARCH
        search=input("\nEnter the full name to search:")
        if search in phonenumber:
            print('Found..')
            print(f'\n{search} -> [{phonenumber[search]}]')
        else:
            print(f'\n[{search}] is not in the phonebook') 
        time.sleep(2)

    elif op==3:              #VIEW ALL 
        if phonenumber:
            print(f'Here are all the contacts {phonenumber}')
            for i, name in enumerate(name, start=1):
                                print(f'{i}.{name}')
        else:
            print('\nPhone book is empty..')
        time.sleep(2)
    
    elif op==4:                  #DELETE
        del_val=input('Enter the contact name to delete:')
        if del_val in phonenumber:
            del phonenumber[del_val]
            print(f'\n[{del_val}] has been deleted..')
        else:
            print('\nThis contact is not in the phone book..')
        time.sleep(2)
    
    elif op==5:                 #EXIT
        print('Thanks for using the app')
        break

    else:
        print('❗Invalid input❗\n')

