#Connect to DataBase

from cv2 import _InputArray_FIXED_SIZE
import mysql.connector as a
password = str(input("DATABASE PASSWORD : "))
con = a.connect(host="localhost", user = "root", password = password)

# SELECT PR CREATE DATABASE

c = con.cursor()
c.execute("show databases")
dl = c.fetchall()
dl2 = []
for i in dl:
    dl2.append(i[0])
if "rest1" in dl2:
    sql = "use rest1"
    c.execute(sql)
else:
    sql1 = "create database rest1"
    c.execute(sql1)
    sql2 = "use rest1"
    c.execute(sql2)
    sql3 = """create table dish (Dish varchar(20", Cost intiger, Cookvarchar(50), DishID varchar(20))"""
    c.execute(sql3)
    sql4 = """create table orders (DishIDs varchar(100), Cost integer, Date varchar(20), Customer varcha(50), Aadhar Varchar(20))"""
    c.execute(sql4)
    sql5 = """create table cook(Name Varchar(100), Aadhar varchar(20), Dishes varchar(100), Salary integer, DOJ varchar(20))"""
    c.execute(sql5)
    sql6 = """create table salary (Name varchar(100), Aadhar varchar(20), Bank varchar(20), Month varchar(20), Salary integer, Days integer, Net integer)"""
    c.execute(sql6)
    sql7 = """create table bill (Type varchar(100), Cost integer, Date varchar(20))"""
    c.execute(sql7)
    con.commit()


# SYSTEM PASSWORD LOGIN

def signin():
    print("\n")
    print("  -------->>>>>>>> Welcome APNA CAFE <<<<<<<<--------")
    print("\n")
    p = input("System Password : ")
    if p=="mySQL@3007":
        options()
    else:
        print("Something went wrong! try again.")
        signin()

def options():
    print("""
                1.      DISHES
                2.      COOKS
                3.      SALARY
                4.      ORDER
                5.      INCOME
                6.      BILLS
    """)
    choice = input("Select Option : ")
    while True:
        if(choice == '1'):
            Dish()
        elif(choice == '2'):
            Cook()
        elif(choice == '3'):
            Salary()
        elif(choice == '4'):
            Order()
        elif(choice == '5'):
            Income()
        elif(choice == '6'):
            Bills()
        else:
            print(" Wrong choice.....")
            choice = input("Select Option : ")


def Dish():
    choice = input("1.Add 2.Remove 3.Display 4. Main Menu: ")
    if choice == '1':
        dn = input("Dish Name")
        dc = input("Dish Cost")
        Cname()
        cb = input("Cooked By: ")
        did = str(DishID())
        data = (dn,dc,cb,did)
        sql = 'insert into Dish values(%s,%s,%s,%s)'
        c = con.cursor() 
        c.execute(sql,data)
        con.commit()
        print("Data Entered Successfully")
    elif (choice == '2'):
        did = input("Dish ID: ")
        data = (did,)
        sql = 'delete from Dish where DishID = %s'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Updated successsfully")
    elif(choice == '3'):
        print("\n")
        sql = "select * from Dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        for i in d:
            print(f"{i[0]}-{i[1]}-{i[2]}-{i[3]}")
        print("\n")
    else:
        options()

def DishID():
    sql = 'select count(*), max(DishID) from Dish'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        if i[0] == 0:
            return(1)
        else:
            return(int(i[1])+1)
def Cname():
    sql = 'select Name, Dishes from Cook'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print("<---- Available Cooks ---->")
    for i in d:
        print(i[0],"---",i[1])
    return

def Cook():
    choice = input("1.Add 2.Remove 3.Display 4.Main Menu:")
    if choice == '1':
        cn = input("Cook Name:")
        ca = input("Aadhar:")
        d = input("Dishes:")
        s = int(input("Salary:"))
        doj = input("Data of Joining : Y/M/D:")
        data = (cn,ca,d,s,doj)
        sql = 'insert into Cook values(%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Entered Successfully")
    elif choice == '2':
        cn = input("Cook Name:")
        ca = input("Aadhar:")
        data = (cn,ca)
        sql = 'delete from Cook where Name = %s and Aadhar = %s'
        c = con.cursor()
        c.execute(sql,data)
        print("Data Update Successfully")
    elif choice == '3':
        sql = "select * from Cook"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        for i in d:
            print(f"{i[0]}-{i[1]}-{i[2]}-{i[3]}-{i[4]}")
            print("\n")
    else:
        options()
def Salary():
    sql = "select * from Cook"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d :
        print(f"{i[0]}-{i[1]}-{i[2]}-{i[3]}-{i[4]}")
        print("-----------------------------------------------------")
    cn = input("Cook Name: ")
    ca = input("Aadhar: ")
    ba = input("Bank Account:")
    mn = input("DATE: Y/M/D: ")
    s = int(input("Salary:"))
    d = int(input("Working days:"))
    if mn[5:7] in ['01','03','05','07','08','10','12']:
        ns = (s/31)*d
    elif mn[5:7]in ['04','06','09','11']:
        ns = (s/30)*d
    else:
        ns = (s/28)*d
    data = (cn,ca,ba,mn,s,d,ns)
    sql = 'insert into Salary values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(f"Net Salary Paid:{ns}Rs")
    print("--------------------------------------")
    xy = input("1.SAlary Menu   2.Main Menu : ")
    print("--------------------------------------")
    if xy == '1':
        Salary()
    else:
        options()
    
def Order():
    sql = "select * from Dish"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print("NAME-----COST-----COOK-----DISH ID")
    for i in d:
        print(f"{i[0]}-{i[1]}-{i[2]}-{i[3]}")
    print("\n")
    dil = []            # list of dish items ordered
    while True:
        di = input("Select Dish ID {0 When Done} :")
        if di =='0':
            break
        else:
            dil.append(di)
    sql = "select DishID, Cost from Dish"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    dicl = {}           #dicl - list of cost of dish id , dii - dish id list
    for i in d: 
        dicl[i[0]] = i[1]
    tc = 0
    for i in dil:
        dc = dicl[i]
        tc = tc + dc
    dt = input("Date : Y/M/D :")
    cn = input("Customer Name:")
    ca = input("Aadhar:")
    lis = input("Enter Dish IDs:")
    data = (lis, tc, dt, cn, ca)
    sql = 'insert into Orders values(%s,%s,%s,%s,%s)'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print(f"Tatal Amount: {tc}Rs")
    print("Data Entered Successfully")
    print("--------------------------------------------")
    xy = input("1.Order Menu    2.Main Menu :")
    print("--------------------------------------------")
    if xy == '1':
        Order()
    else:
        options()

def Income():
    c = con.cursor()
    t = input("1.All    2.Year  3.Month  4.Date  5.Main Menu: ")
    if t == '1':
        sql = 'select Cost from Orders'
        c.execute(sql)
        d = c.fetchall()
        oi = 0
        for i in d:
            oi = oi + i[0]
        print(f"Total Income from Orders: {oi}Rs")
    elif t == '2':
        y = input("Enter Year:")
        sql = 'select Cost, Date from Orders'
        c.execute(sql)
        d = c.fetchall()
        oi = 0
        for i in d:
            if y in i[1]:
                oi = oi + i[0]
        print(f"Total Income from Orders: {oi}Rs")
    elif t =='3':
        my = input("Enter Year/Month:")
        sql = 'select Cost,Date from Orders'
        c.execute(sql)
        d = c.fetchall()
        oi = 0
        for i in d:
            if my in i[0]:
                print(f"Total Income from Orders: {oi}Rs")
    elif t == '4':
        y = input("Enter Y/M/D :")
        sql = 'select Cost from Orders where Date like %s'
        data = (y,)
        c.execute(sql,data)
        d = c.fetchall()
        oi = 0          #order Income
        for i in d:
            oi = oi + i[0]
        print(f"Total Income from Orders : {oi}Rs")
    else:
        options()
def saBills():
    choice = input("1.Bill Entry    2.Show Bills    3.Main Menu ")
    if choice == '1':
        t = input("Type:")
        c = int(input("Cost:"))
        d = input("Date: Y/M/D:")
        data = (t,c,d)
        sql = 'insert into Bill values(%s,%s,%s)'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Entered Successfully")
        options()
    elif choice == '2':
        c = con.cursor()
        t = input("1.All    2.Year  3.Month  4.Date :")
        if t == '1':
            sql = 'select * from Bill'
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                print(i)
        elif t =='2':
            y = input("Enter Year:")
            sql = 'select * from Bill'
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
                else:
                    print("Nill")
        elif t == '3':
            y = input("Enter : YEAR/MONTH:")
            sql = 'select * from Bill'
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
        elif t == '4':
            y = input("Enter Date:")
            sql = 'select * from Bill'
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
    else:
        options()





if __name__ == '__main__' :
    signin()    
        

