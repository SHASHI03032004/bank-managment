import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='',database='bank')
#if conn.is_connected():
     #print('connected succesfully')
cur = conn.cursor()
cur.execute('create table customer_details(acct_no int primary key,acct_name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(25),cr_amt float )')
      
