import datetime as dt
import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='', database='bank')
cur = conn.cursor()


conn.autocommit = True
c = 'n'
while c not in ['y','Y','yes','Yes']:
    print('\n1.CREATE BANK ACCOUNT\n')
    print('2.TRANSACTION\n')
    print('3.CUSTOMER DETAILS\n')
    print('4.TRANSACTION DETAILS\n')
    print('5.DELETE ACCOUNT\n')
    print('6.QUIT\n')
    n = int(input('Enter your CHOICE='))

    if n == 1:

        acc_no = int(input('Enter your ACCOUNT NUMBER='))
        acc_name = input('Enter your ACCOUNT NAME=')
        ph_no = int(input('Enter your PHONE NUMBER='))
        add = (input('Enter your place='))
        cr_amt = int(input('Enter your credit amount='))
        V_SQLInsert = "INSERT  INTO customer_details values (" + str(
            acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " + add + " '," + str(cr_amt) + " ) "
        cur.execute(V_SQLInsert)
        print('Account Created Succesfully!!!!!')
        conn.commit()

    if n == 2:
        acct_no = int(input('Enter Your Account Number='))
        cur.execute(
            'select * from customer_details where acct_no='+str(acct_no))
        data = cur.fetchall()
        count = cur.rowcount
        conn.commit()
        if count == 0:
            print('Account Number Invalid Sorry Try Again Later')
        else:
            print('1.WITHDRAW AMOUNT')
            print('2.ADD AMOUNT')
            x = int(input('Enter your CHOICE='))
            if x == 1:
                amt = int(input('Enter withdrawl amount='))
                cr_amt = 0
                cur.execute('update customer_details set   cr_amt=cr_amt-' +
                            str(amt) + ' where acct_no=' + str(acct_no))
                V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(
                    acct_no, dt.datetime.today(), amt, cr_amt)
                cur.execute(V_SQLInsert)
                conn.commit()
                print('Account Updated Succesfully!!!!!')

            if x == 2:
                amt = int(input('Enter amount to be added='))
                cr_amt = 0
                cur.execute('update customer_details set  cr_amt=cr_amt+' +
                            str(amt) + ' where acct_no=' + str(acct_no))
                V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(
                    acct_no, dt.datetime.today(), cr_amt, amt)
                cur.execute(V_SQLInsert)
                conn.commit()
                print('Account Updated Succesfully!!!!!')

    if n == 3:
        acct_no = int(input('Enter your account number='))
        cur.execute(
            'select * from customer_details where acct_no='+str(acct_no))
        if cur.fetchone() is None:
            print('Invalid Account number')
        else:
            cur.execute(
                'select * from customer_details where acct_no='+str(acct_no))
            data = cur.fetchall()
            for row in data:
                print('ACCOUNT NO=', acct_no)
                print('ACCOUNT NAME=', row[1])
                print(' PHONE NUMBER=', row[2])
                print('ADDRESS=', row[3])
                print('cr_amt=', row[4])
    if n == 4:
        acct_no = int(input('Enter your account number='))
        cur.execute(
            'select * from customer_details where acct_no='+str(acct_no))
        if cur.fetchone() is None:
            print('Invalid Account number')
        else:
            cur.execute(
                'select * from transactions where acct_no='+str(acct_no))
            data = cur.fetchall()
            for row in data:
                print('ACCOUNT NO=', acct_no)
                print('DATE=', row[1])
                print(' WITHDRAWAL AMOUNT=', row[2])
                print('AMOUNT ADDED=', row[3])

    if n == 5:
        print('DELETE YOUR ACCOUNT')
        acct_no = int(input('Enter your account number='))

        cur.execute('delete from customer_details where acct_no='+str(acct_no))
        print('ACCOUNT DELETED SUCCESFULLY')

    if n == 6:
        print('DO YO WANT TO EXIT(y/n)')
        c = input('enter your choice=')


else:
    print('THANK YOU PLEASE VISIT AGAIN')
    quit()