import mysql.connector
con = mysql.connector.connect(
    host='localhost', user='root', password='mydb1234', database='hotelManagement')
cur = con.cursor()


def show_data():
    query = "SELECT*FROM CUSTOMERDATA"
    cur.execute(query)
    rows = cur.fetchall()
    for x in rows:
        print(x)
    runagain()


def customer_registration():
    name = input('ENTER YOUR NAME:')
    address = input('ENTER YOUR ADDRESS:')
    indate = input('ENTER CHECKIN DATE:')
    outdate = input('ENTER CHECKOUT DATE:')
    query = "INSERT INTO CUSTOMERDATA VALUE('{}','{}','{}','{}')".format(
        name, address, indate, outdate)
    cur.execute(query)
    con.commit()
    runagain()


def roomtype():
    query = "SELECT*FROM ROOMTYPES"
    cur.execute(query)
    rows = cur.fetchall()
    for x in rows:
        print(x)
    runagain()


def restaurant_menu():
    query = "SELECT*FROM RESTAURANT"
    cur.execute(query)
    rows = cur.fetchall()
    for x in rows:
        print(x)
    runagain()


def order_food():
    print("\n('S.NO.','FOOD ITEMS','PRICE')")
    query = "SELECT*FROM RESTAURANT"
    cur.execute(query)
    rows = cur.fetchall()
    for x in rows:
        print(x)
    print('\nTO PURCHASE THE FOOD ITEM')
    a = int(input('ENTER YOUR CHOICE:'))
    if a == 1:
        print('YOU HAVE ORDERED LASAGNE')
        q = int(input('\nENTER QUANTITY:'))
        price = 20*q
        print('\nYOUR AMOUNT FOR LASAGNE IS:', price, '\n')
    elif a == 2:
        print('YOU HAVE ORDERED PIZZA')
        q = int(input('\nENTER QUANTITY:'))
        price = 20*q
        print('\nYOUR AMOUNT FOR PIZZA IS:', price, '\n')
    elif a == 3:
        print('YOU HAVE ORDERED PASTA')
        q = int(input('\nENTER QUANTITY:'))
        price = 15*q
        print('\nYOUR AMOUNT FOR PASTA IS:', price, '\n')
    elif a == 4:
        print('YOU HAVE ORDERED SANDWICH')
        q = int(input('\nENTER QUANTITY:'))
        price = 10*q
        print('\nYOUR AMOUNT FOR SANDWICH IS:', price, '\n')
    elif a == 5:
        print('YOU HAVE ORDERED NOODLES')
        q = int(input('\nENTER QUANTITY:'))
        price = 17*q
        print('\nYOUR AMOUNT FOR NOODLES IS:', price, '\n')
    elif a == 6:
        print('YOU HAVE ORDERED SOFTDRINK')
        q = int(input('\nENTER QUANTITY:'))
        price = 5*q
        print('\nYOUR AMOUNT FOR SOFTDRINK IS:', price, '\n')
    elif a == 7:
        print('YOU HAVE ORDERED COFFEE')
        q = int(input('\nENTER QUANTITY:'))
        price = 7*q
        print('\nYOUR AMOUNT FOR COFFEE IS:', price, '\n')
    elif a == 8:
        print('YOU HAVE ORDERED TEA')
        q = int(input('\nENTER QUANTITY:'))
        price = 7*q
        print('\nYOUR AMOUNT FOR TEA IS:', price, '\n')
    elif a == 9:
        print('YOU HAVE ORDERED BURRITO')
        q = int(input('\nENTER QUANTITY:'))
        price = 15*q
        print('\nYOUR AMOUNT FOR BURRITO IS:', price, '\n')
    elif a == 10:
        print('YOU HAVE ORDERED BOWL')
        q = int(input('\nENTER QUANTITY:'))
        price = 12*q
        print('\nYOUR AMOUNT FOR BOWL IS:', price, '\n')

    else:
        print('PLEASE ENTER YOUR CHOICE FROM THE MENU!')
    runagain()


def room_rent():
    print('\nWE HAVE THE FOLLOWING ROOMS FOR YOU:')
    print('\n1. TYPE-A FOR RS.2500 PER NIGHT')
    print('2. TYPE-B FOR RS.3500 PER NIGHT')
    print('3. TYPE-C FOR RS.3500 PER NIGHT')
    print('4. TYPE-D FOR RS.5000 PER NIGHT')
    x = int(input('\nENTER YOUR CHOICE:'))
    n = int(input('\nHOW MANY NIGHTS DID YOU STAY WITH US?:'))
    if x == 1:
        print('YOU CHOSE ROOM TYPE-A')
        price = 2500*n
    elif x == 2:
        print('YOU CHOSE ROOM TYPE-B')
        price = 3500*n
    elif x == 3:
        print('YOU CHOSE ROOM TYPE-C')
        price = 3500*n
    elif x == 4:
        print('YOU CHOSE ROOM TYPE-D')
        price = 5000*n
    else:
        print('PLEASE CHOOSE A ROOM')
    print('\nYOUR ROOM RENT FOR', n, 'NIGHTS IS:', price, '\n')
    runagain()


def laundry_bill():
    print('\nRATE FOR LAUNDRY:')
    print("\n('S.NO.','CLOTH ITEM','PRICE')")
    query = "SELECT*FROM LAUNDRY"
    cur.execute(query)
    rows = cur.fetchall()
    for x in rows:
        print(x)
    a = int(input('\nENTER THE SNO FOR THE ITEM YOU GAVE FOR LAUNDARY:'))
    if a == 1:
        print('YOUR ITEM WAS SHIRT')
        q = int(input('\nENTER QUANTITY:'))
        price = 20*q
        print('\nYOUR AMOUNT IS:', price, '\n')
    elif a == 2:
        print('YOUR ITEM WAS T-SHIRT')
        q = int(input('\nENTER QUANTITY:'))
        price = 20*q
        print('\nYOUR AMOUNT IS:', price, '\n')
    elif a == 3:
        print('YOUR ITEM WAS CARGOPANTS')
        q = int(input('\nENTER QUANTITY:'))
        price = 17*q
        print('\nYOUR AMOUNT IS:', price, '\n')
    elif a == 4:
        print('YOUR ITEM WAS COAT')
        q = int(input('\nENTER QUANTITY:'))
        price = 25*q
        print('\nYOUR AMOUNT IS:', price, '\n')
    elif a == 5:
        print('YOUR ITEM WAS JACKET')
        q = int(input('\nENTER QUANTITY:'))
        price = 25*q
        print('\nYOUR AMOUNT IS:', price, '\n')
    elif a == 6:
        print('YOUR ITEM WAS TROUSERS')
        q = int(input('\nENTER QUANTITY:'))
        price = 10*q
        print('\nYOUR AMOUNT IS:', price, '\n')
    runagain()


def menu_set():
    print('\n1. TO ENTER CUSTOMER DATA')
    print('2. TO VIEW ROOM TYPE')
    print('3. TO VIEW RESTAURANT MENU')
    print('4. FOR ROOM BILL')
    print('5. FOR RESTAURANT BILL')
    print('6. FOR LAUNDRY BILL')
    print('7. SHOW CUSTOMER DATA')
    print('8. TO EXIT')
    userinput = int(input('\nENTER YOUR CHOICE:'))
    if userinput == 1:
        customer_registration()
    elif userinput == 2:
        roomtype()
    elif userinput == 3:
        restaurant_menu()
    elif userinput == 4:
        room_rent()
    elif userinput == 5:
        order_food()
    elif userinput == 6:
        laundry_bill()
    elif userinput == 7:
        show_data()
    elif userinput == 8:
        quit()
    else:
        print('ENTER A CORRECT CHOICE:\n')


def runagain():
    run = input('WANT TO RUN AGAIN?(Y/N):')
    if run.upper() == 'Y':
        menu_set()
    elif run.upper() == 'N':
        quit()


menu_set()
