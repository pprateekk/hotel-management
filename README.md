# hotel-management-system

## Description

The purpose of this project is to develop the Management Information System (MIS) and to operate hotel operations by automating them.
The project aimed to enhance the current record keeping system, which will help managers to retrieve the up-to-date information at the right time in the right shape.
The system should maintain all the records and transactions, and should generate the required reports and information when required.
In its current scope, the software enables users to retrieve and update the information from a centralized database designed with MySQL.

## Executing program 
To run the program
```
python3 hotelManagement.py
```
<pre>
Sample Output  
python3 hotelManagement.py

1. TO ENTER CUSTOMER DATA
2. TO VIEW ROOM TYPE
3. TO VIEW RESTAURANT MENU
4. FOR ROOM BILL
5. FOR RESTAURANT BILL
6. FOR LAUNDRY BILL
7. SHOW CUSTOMER DATA
8. TO EXIT

ENTER YOUR CHOICE:1 
ENTER YOUR NAME:John 
ENTER YOUR ADDRESS:432 W. Acres 
ENTER CHECKIN DATE:Jun14,2021 
ENTER CHECKOUT DATE:Jun15,2021 
WANT TO RUN AGAIN?(Y/N):y 

1. TO ENTER CUSTOMER DATA 
2. TO VIEW ROOM TYPE 
3. TO VIEW RESTAURANT MENU
4. FOR ROOM BILL
5. FOR RESTAURANT BILL
6. FOR LAUNDRY BILL
7. SHOW CUSTOMER DATA
8. TO EXIT

ENTER YOUR CHOICE:2
(1, 'Type-A', 2500)
(2, 'Type-B', 3500)
(3, 'Type-C', 3500)
(4, 'Type-D', 5000)
WANT TO RUN AGAIN?(Y/N):y

1. TO ENTER CUSTOMER DATA
2. TO VIEW ROOM TYPE
3. TO VIEW RESTAURANT MENU
4. FOR ROOM BILL
5. FOR RESTAURANT BILL
6. FOR LAUNDRY BILL
7. SHOW CUSTOMER DATA
8. TO EXIT

ENTER YOUR CHOICE:3
(1, 'Lasagne', 20)
(2, 'Pizza', 20)
(3, 'Pasta', 15)
(4, 'Sandwich', 10)  
(5, 'Noodles', 17)  
(6, 'Softdrink', 5)  
(7, 'Coffee', 7)  
(8, 'Tea', 7)  
(9, 'Burrito', 15)  
(10, 'Bowl', 12)  
WANT TO RUN AGAIN?(Y/N):y

1. TO ENTER CUSTOMER DATA
2. TO VIEW ROOM TYPE
3. TO VIEW RESTAURANT MENU
4. FOR ROOM BILL
5. FOR RESTAURANT BILL
6. FOR LAUNDRY BILL
7. SHOW CUSTOMER DATA
8. TO EXIT

ENTER YOUR CHOICE:4

WE HAVE THE FOLLOWING ROOMS FOR YOU:

1. TYPE-A FOR RS.2500 PER NIGHT  
2. TYPE-B FOR RS.3500 PER NIGHT  
3. TYPE-C FOR RS.3500 PER NIGHT  
4. TYPE-D FOR RS.5000 PER NIGHT  

ENTER YOUR CHOICE:2

HOW MANY NIGHTS DID YOU STAY WITH US?:1
YOU CHOSE ROOM TYPE-B

YOUR ROOM RENT FOR 1 NIGHTS IS: 3500 

WANT TO RUN AGAIN?(Y/N):y

1. TO ENTER CUSTOMER DATA
2. TO VIEW ROOM TYPE
3. TO VIEW RESTAURANT MENU
4. FOR ROOM BILL
5. FOR RESTAURANT BILL
6. FOR LAUNDRY BILL
7. SHOW CUSTOMER DATA
8. TO EXIT

ENTER YOUR CHOICE:5

('S.NO.','FOOD ITEMS','PRICE')  
(1, 'Lasagne', 20)  
(2, 'Pizza', 20)  
(3, 'Pasta', 15)  
(4, 'Sandwich', 10)  
(5, 'Noodles', 17)  
(6, 'Softdrink', 5)  
(7, 'Coffee', 7)  
(8, 'Tea', 7)  
(9, 'Burrito', 15)  
(10, 'Bowl', 12)  

TO PURCHASE THE FOOD ITEM
ENTER YOUR CHOICE:2
YOU HAVE ORDERED PIZZA

ENTER QUANTITY:1

YOUR AMOUNT FOR PIZZA IS: 20 

WANT TO RUN AGAIN?(Y/N):y

1. TO ENTER CUSTOMER DATA
2. TO VIEW ROOM TYPE
3. TO VIEW RESTAURANT MENU
4. FOR ROOM BILL
5. FOR RESTAURANT BILL
6. FOR LAUNDRY BILL
7. SHOW CUSTOMER DATA
8. TO EXIT

ENTER YOUR CHOICE:6

RATE FOR LAUNDRY:

('S.NO.','CLOTH ITEM','PRICE')  
(1, 'Shirt', 20)  
(2, 'T-Shirt', 20)  
(3, 'CargoPants', 17)  
(4, 'Coat', 25)  
(5, 'Jacket', 25)  
(6, 'Trousers', 10)  

ENTER THE SNO FOR THE ITEM YOU GAVE FOR LAUNDARY:5  
YOUR ITEM WAS JACKET

ENTER QUANTITY:1

YOUR AMOUNT IS: 25 

WANT TO RUN AGAIN?(Y/N):y  

1. TO ENTER CUSTOMER DATA
2. TO VIEW ROOM TYPE
3. TO VIEW RESTAURANT MENU
4. FOR ROOM BILL
5. FOR RESTAURANT BILL
6. FOR LAUNDRY BILL
7. SHOW CUSTOMER DATA
8. TO EXIT

ENTER YOUR CHOICE:7  
('Mac', '908 K. Ave', 'Jan21,2021', 'Jan23,2021')  
('Joshua', '787 Kingstreet', 'Feb01,2021', 'Feb05,2021')  
('Robert', '345 Janefield', 'Mar18,2021', 'Mar19,2021')  
('John', '432 W. Acres', 'Jun14,2021', 'Jun15,2021')  
WANT TO RUN AGAIN?(Y/N):y

1. TO ENTER CUSTOMER DATA
2. TO VIEW ROOM TYPE
3. TO VIEW RESTAURANT MENU
4. FOR ROOM BILL
5. FOR RESTAURANT BILL
6. FOR LAUNDRY BILL
7. SHOW CUSTOMER DATA
8. TO EXIT

ENTER YOUR CHOICE:8
</pre>

## Structure of the Database

<pre>
mysql> show databases;  
+--------------------+  
| Database           |  
+--------------------+  
| hotelManagement    |  
| information_schema |  
| mysql              |  
| performance_schema |  
| sys                |  
+--------------------+  
5 rows in set (0.06 sec)

mysql> show tables;
+---------------------------+  
| Tables_in_hotelmanagement |  
+---------------------------+  
| customerData              |  
| laundry                   |  
| restaurant                |  
| roomTypes                 |  
+---------------------------+  
4 rows in set (0.02 sec)

mysql> desc customerdata;  
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| Name    | varchar(10) | YES  |     | NULL    |       |
| Address | varchar(20) | YES  |     | NULL    |       |
| Indate  | varchar(10) | YES  |     | NULL    |       |
| Outdate | varchar(10) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
4 rows in set (0.06 sec)

mysql> desc laundry;  
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| SNo      | int         | YES  |     | NULL    |       |
| Itemname | varchar(10) | YES  |     | NULL    |       |
| Price    | int         | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.01 sec)

mysql> desc restaurant;  
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| SNo      | int         | YES  |     | NULL    |       |
| Itemname | varchar(10) | YES  |     | NULL    |       |
| Price    | int         | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> desc roomtypes;  
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| SNo      | int         | YES  |     | NULL    |       |
| Roomtype | varchar(10) | YES  |     | NULL    |       |
| Rent     | int         | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.01 sec)
</pre>

## Limitations
1. This program can store records and produce reports in pre-designed format.
2. There is no provision to calculate penalty or loss etc. for the customer; however it can be developed easily with the help of adding modules.

The program can be easily modified independently and is open to a number of modules and functions that can let it execute additional hotel MIS functions.
