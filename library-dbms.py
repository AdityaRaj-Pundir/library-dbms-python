import mysql.connector as connector
from prettytable import from_db_cursor as rec
import csv
import os
from time import sleep
from datetime import date

def clear():
    if os.name == 'nt':
        os.system('cls')
        print()
    else:
        os.system('clear')
        print()

adminkey = 'Admin_123'
pwd = input('Enter password for root user: ')

try:
    connection = connector.connect(
        host = 'localhost',
        user = 'root',
        password = pwd
    )
except:
    print('Error in connecting to MySQL Server. Please check your password!')
    print()
    exit()
clear()

def exiting():
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[95m
    ████████ ██   ██  █████  ███    ██ ██   ██     ██    ██  ██████  ██    ██        
       ██    ██   ██ ██   ██ ████   ██ ██  ██       ██  ██  ██    ██ ██    ██        
       ██    ███████ ███████ ██ ██  ██ █████         ████   ██    ██ ██    ██        
       ██    ██   ██ ██   ██ ██  ██ ██ ██  ██         ██    ██    ██ ██    ██        
       ██    ██   ██ ██   ██ ██   ████ ██   ██        ██     ██████   ██████         
                                                                                     
                                                                                     
    ███████  ██████  ██████      ██    ██ ██ ███████ ██ ████████ ██ ███    ██  ██████    
    ██      ██    ██ ██   ██     ██    ██ ██ ██      ██    ██    ██ ████   ██ ██         
    █████   ██    ██ ██████      ██    ██ ██ ███████ ██    ██    ██ ██ ██  ██ ██   ███   
    ██      ██    ██ ██   ██      ██  ██  ██      ██ ██    ██    ██ ██  ██ ██ ██    ██   
    ██       ██████  ██   ██       ████   ██ ███████ ██    ██    ██ ██   ████  ██████    
                                                                                        
                                                                                     
    ████████ ██   ██ ███████     ██      ██ ██████  ██████   █████  ██████  ██    ██ 
       ██    ██   ██ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██  ██  ██  
       ██    ███████ █████       ██      ██ ██████  ██████  ███████ ██████    ████   
       ██    ██   ██ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██    ██    
       ██    ██   ██ ███████     ███████ ██ ██████  ██   ██ ██   ██ ██   ██    ██ 
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m''')
    print()
    exit()

print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[98m  
             ██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     
             ██     ██ ██      ██      ██      ██    ██ ████  ████ ██          
             ██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████       
             ██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██          
              ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████     
                                                                            
                                                                            
                 ████████  ██████      ████████ ██   ██ ███████                
                    ██    ██    ██        ██    ██   ██ ██                     
                    ██    ██    ██        ██    ███████ █████                  
                    ██    ██    ██        ██    ██   ██ ██                     
                    ██     ██████         ██    ██   ██ ███████                
                                                                            
                                                                            
                 ██      ██ ██████  ██████   █████  ██████  ██    ██           
                 ██      ██ ██   ██ ██   ██ ██   ██ ██   ██  ██  ██            
                 ██      ██ ██████  ██████  ███████ ██████    ████             
                 ██      ██ ██   ██ ██   ██ ██   ██ ██   ██    ██              
                 ███████ ██ ██████  ██   ██ ██   ██ ██   ██    ██              
\033[00m''')                                 

# Database Setup
sqlcursor = connection.cursor()
sqlcursor.execute('create database if not exists library')
sqlcursor.execute('use library')

def search_books(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[96m
                ███████ ███████  █████  ██████   ██████ ██   ██ 
                ██      ██      ██   ██ ██   ██ ██      ██   ██ 
                ███████ █████   ███████ ██████  ██      ███████ 
                     ██ ██      ██   ██ ██   ██ ██      ██   ██
                ███████ ███████ ██   ██ ██   ██  ██████ ██   ██ 
                                                                
                                                                
                    ██████   ██████   ██████  ██   ██ ███████   
                    ██   ██ ██    ██ ██    ██ ██  ██  ██        
                    ██████  ██    ██ ██    ██ █████   ███████   
                    ██   ██ ██    ██ ██    ██ ██  ██       ██   
                    ██████   ██████   ██████  ██   ██ ███████   
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
''')
    print('''How would you like to search books?
1) By Keyword
2) By Book ID
3) By Published Year
4) By Author
5) Cancel''')
    ch = input('Enter Choice: ')
    if ch == '1':
        print('\nSearching by Keywords.')
        keyword = input('Enter keyword: ')
        sqlcursor.execute(f'select books.bookid \'Book ID\', books.bookname \'Name\', authors.authorname \'Author\', books.status \'Issue Status\', books.userid \'Issued By\' from books natural join authors where books.bookname like \'%{keyword}%\'')
        print()
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    elif ch == '2':
        print('\nSearching by Book ID.')
        input_bookid = input('Enter Book ID: ').upper()
        if len(input_bookid) != 6 or input_bookid[0] != 'B':
            print('Invalid Book ID.')
            sleep(2)
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname) 
        sqlcursor.execute('select bookid from books')
        existingBooks = []
        for i in sqlcursor:
            existingBooks.append(i[0])
        if input_bookid not in existingBooks:
            print('Book does not exist!')
            sleep(2)
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname) 
        sqlcursor.execute(f'select books.bookid \'Book ID\', books.bookname \'Name\', authors.authorname \'Author\', books.status \'Issue Status\', books.userid \'Issued By\' from books natural join authors where books.bookid = \'{input_bookid}\'')
        print()
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    elif ch == '3':
        print('\nSearching by Year of Publication.')
        input_year = input('Enter Year: ')
        if len(input_year) != 4:
            print('Invalid Year.')
            sleep(2)
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname)    
        sqlcursor.execute(f'select books.bookid \'Book ID\', books.bookname \'Name\', authors.authorname \'Author\', books.status \'Issue Status\', books.userid \'Issued By\' from books natural join authors where year(books.published) = \'{input_year}\'')
        print()
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    elif ch == '4':
        print('\nSearching by Author.')
        print('''1) By Author ID
2) By Author Name''')
        ch = input('Enter Choice: ')
        if ch == '1':
            input_authorid = input('\nEnter Author ID: ').upper()
            if len(input_authorid) != 6 or input_authorid[0] != 'A':
                print('Invalid Author ID.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
            sqlcursor.execute(f'select books.bookid \'Book ID\', books.bookname \'Name\', authors.authorname \'Author\', books.status \'Issue Status\', books.userid \'Issued By\' from books natural join authors where authors.authorid = \'{input_authorid}\'')
            print()
            print(rec(sqlcursor))
            print()
            input('Press Enter to Continue: ')
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname)
        elif ch == '2':
            input_authorname = input('\nEnter Author Name: ')
            sqlcursor.execute(f'select books.bookid \'Book ID\', books.bookname \'Name\', authors.authorname \'Author\', books.status \'Issue Status\', books.userid \'Issued By\' from books natural join authors where authors.authorname = \'{input_authorname}\'')
            print()
            print(rec(sqlcursor))
            print()
            input('Press Enter to Continue: ')
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname)
        else:
            print('Invalid Input.')
            sleep(2)
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname)
    elif ch == '5':
        print('\nOk, Cancelling.')
        sleep(2)
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    else:
        print('Invalid Input.')
        sleep(2)
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    
def search_authors(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[96m
                ███████ ███████  █████  ██████   ██████ ██   ██        
                ██      ██      ██   ██ ██   ██ ██      ██   ██        
                ███████ █████   ███████ ██████  ██      ███████        
                     ██ ██      ██   ██ ██   ██ ██      ██   ██        
                ███████ ███████ ██   ██ ██   ██  ██████ ██   ██        
                                                                    
                                                                    
             █████  ██    ██ ████████ ██   ██  ██████  ██████  ███████ 
            ██   ██ ██    ██    ██    ██   ██ ██    ██ ██   ██ ██      
            ███████ ██    ██    ██    ███████ ██    ██ ██████  ███████ 
            ██   ██ ██    ██    ██    ██   ██ ██    ██ ██   ██      ██ 
            ██   ██  ██████     ██    ██   ██  ██████  ██   ██ ███████ 
                                                           
                                                           
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
''')
    print('''How would you like to search authors?
1) By Name
2) By ID''')
    ch = input('Enter Choice: ')
    if ch == '1':
        input_authorname = input('\nEnter Author Name: ')
        sqlcursor.execute(f'select authors.authorid \'Author ID\', authors.authorname \'Author\', count(books.bookid) \' Number of Books\'from books natural join authors group by authors.authorid having authors.authorname = \'{input_authorname}\'')
        print()
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    elif ch == '2':
        input_authorid = input('\nEnter Author ID: ').upper()
        if len(input_authorid) != 6 or input_authorid[0] != 'A':
            print('Invalid Author ID.')
            sleep(2)
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname)
        sqlcursor.execute(f'select authors.authorid \'Author ID\', authors.authorname \'Author\', count(books.bookid) \' Number of Books\'from books natural join authors group by authors.authorid having authors.authorid = \'{input_authorid}\'')
        print()
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    else:
        print('Invalid Input.')
        sleep(2)
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)

def delete(userid, displayname, admin_check):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[91m          
                    ██████  ███████ ██      ███████ ████████ ███████         
                    ██   ██ ██      ██      ██         ██    ██              
                    ██   ██ █████   ██      █████      ██    █████           
                    ██   ██ ██      ██      ██         ██    ██              
                    ██████  ███████ ███████ ███████    ██    ███████         
                                                                            
                                                                            
                 █████   ██████  ██████  ██████  ██    ██ ███    ██ ████████ 
                ██   ██ ██      ██      ██    ██ ██    ██ ████   ██    ██    
                ███████ ██      ██      ██    ██ ██    ██ ██ ██  ██    ██    
                ██   ██ ██      ██      ██    ██ ██    ██ ██  ██ ██    ██    
                ██   ██  ██████  ██████  ██████   ██████  ██   ████    ██   
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m''')
    if admin_check:
        print(f'''
Hello, {displayname}. Are you sure you want to delete an account?''')
        ch = input('(Y/N): ').upper()
        if ch == 'Y':
            pass
        elif ch == 'N':
            print('Ok, cancelled.')
            sleep(2)
            clear()
            admin(userid, displayname)
        else:
            print('Invalid Input.')
            sleep(2)
            clear()
            admin(userid, displayname)
        print('''
Continuing deletion process:
Delete a user's account by entering their UserID below:''')
        input_userid = input('Enter UserID: ').lower()
        existingUsers = []
        sqlcursor.execute('select userid from users')
        for i in sqlcursor:
            existingUsers.append(i[0])
        if input_userid not in existingUsers:
            print('User does not exist! Try again.')
            sleep(2)
            clear()
            delete(userid, displayname, admin_check)
        if input_userid == userid:
            clear()
            delete(userid, displayname, False)
        sqlcursor.execute(f'select displayname from users where userid = \'{input_userid}\'')
        for i in sqlcursor:
            acc_displayname = i[0]
        sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\' from users where userid = \'{input_userid}\'')
        print('This account will be deleted. Proceed?\n')
        print(rec(sqlcursor))
        ch = input('\n(Y/N): ').upper()
        if ch == 'Y':
            input_key = input('Enter Admin Key to Authenticate: ')
            if input_key == adminkey:
                sqlcursor.execute(f'delete from users where userid = \'{input_userid}\'')
                connection.commit()
                print(f'Deleted {acc_displayname} successfully.')
                sleep(2)
                clear()
                admin(userid, displayname)
            else:
                print('Incorrect Admin Key. Try again.')
                sleep(2)
                clear()
                delete(userid, displayname, admin_check)
        elif ch == 'N':
            print('Ok, cancelled.')
            sleep(2)
            clear()
            admin(userid, displayname)
        else:
            print('Invalid Input.')
            sleep(2)
            clear()
            admin(userid, displayname)
    else:
        print(f'\n{displayname}, are you sure you want to delete your account?\n')
        sqlcursor.execute(f'select password from users where userid = \'{userid}\'')
        for i in sqlcursor:
            auth = i[0]
        sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\' from users where userid = \'{userid}\'')
        print(rec(sqlcursor))
        ch = input('\n(Y/N): ').upper()
        if ch == 'Y':
            input_password = input('Enter password to authenticate: ')
            if input_password == auth:
                sqlcursor.execute(f'delete from users where userid = \'{userid}\'')
                connection.commit()
                print(f'Deleted {displayname} successfully.')
                sleep(2)
                clear()
                login()
            else:
                print('Incorrect Password. Try Again.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
        elif ch == 'N':
            print('Ok, cancelled.')
            sleep(2)
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname)
        else:
            print('Invalid Input.')
            sleep(2)
            clear()
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                admin(userid, displayname)
            else:
                standard(userid, displayname)

def return_book(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[32m          
                    ██████  ███████ ████████ ██    ██ ██████  ███    ██ 
                    ██   ██ ██         ██    ██    ██ ██   ██ ████   ██ 
                    ██████  █████      ██    ██    ██ ██████  ██ ██  ██ 
                    ██   ██ ██         ██    ██    ██ ██   ██ ██  ██ ██ 
                    ██   ██ ███████    ██     ██████  ██   ██ ██   ████ 
                                                                        
                                                                        
                        ██████   ██████   ██████  ██   ██ ███████       
                        ██   ██ ██    ██ ██    ██ ██  ██  ██            
                        ██████  ██    ██ ██    ██ █████   ███████       
                        ██   ██ ██    ██ ██    ██ ██  ██       ██       
                        ██████   ██████   ██████  ██   ██ ███████       
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
''')
    print(f'''Hello, {displayname}! Return your previously issued books here.
Your currently issued books:''')
    sqlcursor.execute(f'select issues.bookid \'Book ID\', books.bookname \'Book Name\', issues.issuedate \'Issued On\', issues.issuetime \'Time Issued\', issues.returndate \'Returned On\', if(datediff((current_date), issues.issuedate) > 14, (datediff((current_date), issues.issuedate) - 14)*5, fine) \'Fines Applicable\' from issues natural join books where userid = \'{userid}\' and books.status = \'issued\'')
    print(rec(sqlcursor))
    sqlcursor.execute(f'select issues.bookid \'Book ID\', books.bookname \'Book Name\', issues.issuedate \'Issued On\', issues.issuetime \'Time Issued\', issues.returndate \'Returned On\', if(datediff((current_date), issues.issuedate) > 14, (datediff((current_date), issues.issuedate) - 14)*5, fine) \'Fines Applicable\' from issues natural join books where userid = \'{userid}\' and books.status = \'issued\'')
    issuedBooks = []
    for i in sqlcursor:
        issuedBooks.append(i[0])
    sqlcursor.execute('select bookid from books')
    existingBooks = []
    for i in sqlcursor:
        existingBooks.append(i[0])
    print()
    returnbook = input('Enter Book ID of book you want to return: ').upper()
    if len(returnbook) != 6 or returnbook[0] != 'B':
        print('Invalid Book ID.')
        sleep(2)
        clear()
        return_book(userid, displayname)
    if returnbook not in issuedBooks:
        print('You have not issued this book!')
        sleep(2)
        clear()
        return_book(userid, displayname)
    if returnbook not in existingBooks:
        print('Book does not exist!')
        sleep(2)
        clear()
        return_book(userid, displayname)
    sqlcursor.execute(f'select bookname from books where bookid = \'{returnbook}\'')
    for i in sqlcursor:
        returnname = i[0]
    ch = input(f'Are you sure you want to return \'{returnname}\'? (Y/N): ').upper()
    if ch == 'Y':
        sqlcursor.execute(f'select issuedate from issues where bookid = \'{returnbook}\'')
        for i in sqlcursor:
            issuedate = i[0]
        rdate = date.today()
        days = rdate - issuedate
        if days.days > 14:
            print('You have been fined', (days.days-14)*5, f'AED for keeping the issued book for more than 2 weeks - ({days.days} days).')
            sqlcursor.execute(f'update issues set fine = {(days.days-14)*5} where userid = \'{userid}\' and bookid = \'{returnbook}\'')
        else:
            print(f'You have returned the book in {days.days} days. Thank you!')
        sqlcursor.execute(f'update issues set returndate = (current_date) where userid = \'{userid}\' and bookid = \'{returnbook}\'')
        connection.commit()
        sqlcursor.execute(f'update books set status = \'not issued\' where bookid = \'{returnbook}\'')
        connection.commit()
        sqlcursor.execute(f'update books set userid = null where bookid = \'{returnbook}\'')
        connection.commit()
        print('Successfully returned book.')
        sleep(2)
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)

def add_books(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[33m
                             █████  ██████  ██████            
                            ██   ██ ██   ██ ██   ██           
                            ███████ ██   ██ ██   ██           
                            ██   ██ ██   ██ ██   ██           
                            ██   ██ ██████  ██████            
                                                            
                                                            
                    ██████   ██████   ██████  ██   ██ ███████ 
                    ██   ██ ██    ██ ██    ██ ██  ██  ██      
                    ██████  ██    ██ ██    ██ █████   ███████ 
                    ██   ██ ██    ██ ██    ██ ██  ██       ██ 
                    ██████   ██████   ██████  ██   ██ ███████ 
\033[00m  
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
''')
    print(f'Hello, {displayname}! Add new books to the library here. Wishlist:\n')
    sqlcursor.execute('select bookname \'Book Name\', authorname \'Author\' from wishlist')
    print(rec(sqlcursor))
    print('\nAdd new book:')
    # bookid char(6) primary key not null, bookname varchar(255), authorid char(6), published date, status varchar(10) default \'not issued\', userid varchar(255)
    bookid = input('Enter Book ID (Simply Enter to Cancel): ').upper()
    if not bookid:
        print('Ok, cancelled.')
        sleep(2)
        clear()
        admin(userid, displayname)
    if len(bookid) != 6 or bookid[0] != 'B':
        print('Invalid Book ID.')
        sleep(2)
        clear()
        add_books(userid, displayname)
    sqlcursor.execute('select bookid from books')
    existingBooks = []
    for i in sqlcursor:
        existingBooks.append(i[0])
    if bookid in existingBooks:
        print('This Book ID is already used!')
        sleep(2)
        clear()
        add_books(userid, displayname)
    bookname = input('Enter Book Name: ')
    authorid = input('Enter Author ID: ')
    if len(authorid) != 6 or authorid[0] != 'A':
        print('Invalid Author ID.')
        sleep(2)
        clear()
        add_books(userid, displayname)
    authorname = input('Enter Author Name: ')
    published = input('Enter date published (YYYY-MM-DD): ')
    x = published.split('-')
    if len(x[0]) != 4 or len(x[1]) != 2 or len(x[2]) != 2:
        print('Invalid Date.')
        sleep(2)
        clear()
        add_books(userid, displayname)
    key = input('Enter Admin Key: ')
    if key == adminkey:
        sqlcursor.execute(f'insert into books(bookid, bookname, authorid, published) values(\'{bookid}\', \'{bookname}\', \'{authorid}\', \'{published}\')')
        connection.commit()
        try:
            sqlcursor.execute(f'insert into authors values (\'{authorid}\',\'{authorname}\')')
            connection.commit()
        except:
            pass
        print('Successfully added this Book.')
        sleep(2)
        clear()
        admin(userid, displayname)
    else:
        print('Incorrect Admin Key.')
        sleep(2)
        clear()
        admin(userid, displayname)

def delete_books(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[35m
                ██████  ███████ ███    ███  ██████  ██    ██ ███████ 
                ██   ██ ██      ████  ████ ██    ██ ██    ██ ██      
                ██████  █████   ██ ████ ██ ██    ██ ██    ██ █████   
                ██   ██ ██      ██  ██  ██ ██    ██  ██  ██  ██      
                ██   ██ ███████ ██      ██  ██████    ████   ███████ 
                                                                    
                                                                    
                    ██████   ██████   ██████  ██   ██ ███████        
                    ██   ██ ██    ██ ██    ██ ██  ██  ██             
                    ██████  ██    ██ ██    ██ █████   ███████        
                    ██   ██ ██    ██ ██    ██ ██  ██       ██        
                    ██████   ██████   ██████  ██   ██ ███████        
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
''')
    print(f'Hello, {displayname}. To remove a book, enter it\'s Book ID below.')
    bookid = input('Enter Book ID (Simply Press Enter to Cancel): ').upper()
    if not bookid:
        print('Ok, cancelled.')
        sleep(2)
        clear()
        admin(userid, displayname)
    if len(bookid) != 6 or bookid[0] != 'B':
        print('Invalid Book ID.')
        sleep(2)
        clear()
        delete_books(userid, displayname)
    sqlcursor.execute('select bookid from books')
    existingBooks = []
    for i in sqlcursor:
        existingBooks.append(i[0])
    if bookid not in existingBooks:
        print('Book does not exist!')
        sleep(2)
        clear()
        delete_books(userid, displayname)
    key = input('Enter Admin Key: ')
    if key == adminkey:
        sqlcursor.execute(f'delete from books where bookid = \'{bookid}\'')
        connection.commit()
        print('Successfully removed Book.')
        sleep(2)
        clear()
        admin(userid, displayname)
    else:
        print('Incorrect Admin Key.')
        sleep(2)
        clear()
        admin(userid, displayname)
    

def returnPolicy():
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[95m
                        ╦═╗╔═╗╔╦╗╦ ╦╦═╗╔╗╔  ╔═╗╔═╗╦  ╦╔═╗╦ ╦
                        ╠╦╝║╣  ║ ║ ║╠╦╝║║║  ╠═╝║ ║║  ║║  ╚╦╝
                        ╩╚═╚═╝ ╩ ╚═╝╩╚═╝╚╝  ╩  ╚═╝╩═╝╩╚═╝ ╩ 
\033[00m  
\033[96mX ==== | | ================================================================= | | ==== X\033[00m

Issued books should be returned within \033[91m14 days (2 weeks)\033[00m
If the issued book is kept for more than 14 days, a fine of \033[91m5 AED\033[00m for each extra day
the book is kept will be charged.''')

def admin(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[93m          
                         █████  ██████  ███    ███ ██ ███    ██ 
                        ██   ██ ██   ██ ████  ████ ██ ████   ██ 
                        ███████ ██   ██ ██ ████ ██ ██ ██ ██  ██ 
                        ██   ██ ██   ██ ██  ██  ██ ██ ██  ██ ██ 
                        ██   ██ ██████  ██      ██ ██ ██   ████ 
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m''')
    print(f'''\nWelome to the admin panel, {displayname}. What would you like to do?
1) Delete any user's account
2) Update account information
3) Display all UserIDs, Display Names, E-Mails and their Admin Status
4) Search users
5) Search Authors/Books
6) Issue Book
7) Return Book
8) View Issued Books
9) Add Book to Library
10) Delete Book from Library
11) Assign/Revoke Admin Privileges
12) Export a table in CSV Format
13) Logout''')
    ch = input('Enter choice: ')
    if ch == '1':
        clear()
        delete(userid, displayname, True)
    elif ch == '2':
        clear()
        update_info(userid, displayname, True)
    elif ch == '3':
        print('\nRegistered Accounts:\n')
        sqlcursor.execute('select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\', admin \'Admin Privileges\' from users')
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        admin(userid, displayname)
    elif ch == '4':
        input_userid = input('\nEnter UserID to look for: ').lower()
        existingUsers = []
        sqlcursor.execute('select userid from users')
        for i in sqlcursor:
            existingUsers.append(i[0])
        if input_userid not in existingUsers:
            print('User does not exist! Try again.')
            sleep(2)
            clear()
            admin(userid, displayname)
        sqlcursor.execute(f'select displayname from users where userid = \'{input_userid}\'')
        for i in sqlcursor:
            acc_displayname = i[0]
        sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\' from users where userid = \'{input_userid}\'')
        print()
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        admin(userid, displayname)
    elif ch == '5':
        print('''\nYou can search books or authors.
1) Books
2) Authors''')
        ch = input('Enter choice: ')
        if ch == '1':
            clear()
            search_books(userid, displayname)
        elif ch == '2':
            clear()
            search_authors(userid, displayname)
        else:
            print('Invalid input.')
            sleep(2)
            clear()
            admin(userid, displayname)
    elif ch == '6':
        clear()
        issue_book(userid, displayname)
    elif ch == '7':
        clear()
        return_book(userid, displayname)
    elif ch == '8':
        print('\nHere are the most recently issued books:\n')
        sqlcursor.execute(f'select userid \'User ID\', bookid \'Book ID\', issuedate \'Issued On\', issuetime \'Time Issued\', returndate \'Returned On\', fine \'Fines Applicable\' from issues')
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        admin(userid, displayname)
    elif ch == '9':
        clear()
        add_books(userid, displayname)
    elif ch == '10':
        clear()
        delete_books(userid, displayname)
    elif ch == '11':
        print(f'\nHello, {displayname}! To assign/revoke admin privileges from an account, enter their User ID below.')
        input_userid = input('Enter UserID: ').lower()
        existingUsers = []
        sqlcursor.execute('select userid from users')
        for i in sqlcursor:
            existingUsers.append(i[0])
        if input_userid not in existingUsers:
            print('User does not exist! Try again.')
            sleep(2)
            clear()
            admin(userid, displayname)
        if input_userid == userid:
            print('You cannot revoke your own privileges!')
            sleep(2)
            clear()
            admin(userid, displayname)
        sqlcursor.execute(f'select displayname from users where userid = \'{input_userid}\'')
        for i in sqlcursor:
            acc_displayname = i[0]
        input_key = input('Enter Admin Key to Authenticate: ')
        if input_key == adminkey:
            sqlcursor.execute(f'select admin from users where userid = \'{input_userid}\'')
            for i in sqlcursor:
                status = i[0]
            if status == 'Y':
                sqlcursor.execute(f'update users set admin = \'N\' where userid = \'{input_userid}\'')
                connection.commit()
                print(f'Successfully removed admin privileges from {acc_displayname}.')
                sleep(2)
                clear()
                admin(userid, displayname)
            else:
                sqlcursor.execute(f'update users set admin = \'Y\' where userid = \'{input_userid}\'')
                connection.commit()
                print(f'Successfully assigned admin privileges to {acc_displayname}.')
                sleep(2)
                clear()
                admin(userid, displayname)
        else:
            print('Incorrect Admin Key. Try again.')
            sleep(2)
            clear()
            admin(userid, displayname)
    elif ch == '12':
        print('''\nWhich table to export?
1) Books
2) Authors
3) Issues
4) Wishlist
''')
        ch = input('Enter choice: ')
        if ch == '1':
            sqlcursor.execute('select bookid, bookname, authorid, published, status from books')
            headers = ['Book ID', 'Book Name', 'Author ID', 'Published', 'Status']
            records = []
            for i in sqlcursor:
                records.append(i)
            with open('books.csv', 'w+') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow(headers)
                csvwriter.writerows(records)
            print('Table exported successfully!')
            sleep(2)
            clear()
            admin(userid, displayname)
        elif ch == '2':
            sqlcursor.execute('select * from authors')
            headers = ['Author ID', 'Author Name']
            records = []
            for i in sqlcursor:
                records.append(i)
            with open('authors.csv', 'w+') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerows(records)
            print('Table exported successfully!')
            sleep(2)
            clear()
            admin(userid, displayname)
        elif ch == '3':
            sqlcursor.execute('select * from issues')
            headers = ['User ID', 'Book ID', 'Issue Date', 'Issue Time' 'Return Date', 'Fine Applicable']
            records = []
            for i in sqlcursor:
                records.append(i)
            with open('issues.csv', 'w+') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerows(records)
            print('Table exported successfully!')
            sleep(2)
            clear()
            admin(userid, displayname)
        elif ch == '4':
            sqlcursor.execute('select * from wishlist')
            headers = ['Book Name', 'Author Name']
            records = []
            for i in sqlcursor:
                records.append(i)
            with open('wishlist.csv', 'w+') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerows(records)
            print('Table exported successfully!')
            sleep(2)
            clear()
            admin(userid, displayname)
        else:
            print('Invalid Input.')
            sleep(2)
            clear()
            admin(userid, displayname)
    elif ch == '13':
        clear()
        home()
    else:
        print('Invalid Input.')
        sleep(2)
        clear()
        admin(userid, displayname)

def update_info(userid, displayname, admin_check):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[95m
                ██    ██ ██████  ██████   █████  ████████ ███████                       
                ██    ██ ██   ██ ██   ██ ██   ██    ██    ██                            
                ██    ██ ██████  ██   ██ ███████    ██    █████                         
                ██    ██ ██      ██   ██ ██   ██    ██    ██                            
                 ██████  ██      ██████  ██   ██    ██    ███████                       
                                                                                        
                                                                                        
             █████   ██████  ██████  ██████  ██    ██ ███    ██ ████████                
            ██   ██ ██      ██      ██    ██ ██    ██ ████   ██    ██                   
            ███████ ██      ██      ██    ██ ██    ██ ██ ██  ██    ██                   
            ██   ██ ██      ██      ██    ██ ██    ██ ██  ██ ██    ██                   
            ██   ██  ██████  ██████  ██████   ██████  ██   ████    ██                   
                                                                                        
                                                                                        
██ ███    ██ ███████  ██████  ██████  ███    ███  █████  ████████ ██  ██████  ███    ██ 
██ ████   ██ ██      ██    ██ ██   ██ ████  ████ ██   ██    ██    ██ ██    ██ ████   ██ 
██ ██ ██  ██ █████   ██    ██ ██████  ██ ████ ██ ███████    ██    ██ ██    ██ ██ ██  ██ 
██ ██  ██ ██ ██      ██    ██ ██   ██ ██  ██  ██ ██   ██    ██    ██ ██    ██ ██  ██ ██ 
██ ██   ████ ██       ██████  ██   ██ ██      ██ ██   ██    ██    ██  ██████  ██   ████ 
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
''')
    if admin_check:
        print(f'Hello, {displayname}. Enter the User ID of the account you want to update below.')
        input_userid = input('Enter UserID: ').lower()
        existingUsers = []
        sqlcursor.execute('select userid from users')
        for i in sqlcursor:
            existingUsers.append(i[0])
        if input_userid not in existingUsers:
            print('User does not exist! Try again.')
            sleep(2)
            clear()
            update_info(userid, displayname, admin_check)
        if input_userid == userid:
            clear()
            update_info(userid, displayname, False)
        sqlcursor.execute(f'select displayname from users where userid = \'{input_userid}\'')
        for i in sqlcursor:
            acc_displayname = i[0]
        print(f'''What account information in {acc_displayname} would you like to update?
1) E-mail
2) Phone Number
3) Display Name''')
        ch = input('Enter Choice: ')
        if ch == '1':
            sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\', phone \'Phone Number\' from users where userid = \'{input_userid}\'')
            print()
            print(rec(sqlcursor))
            print()
            em = input('Enter new E-Mail: ')
            if ' ' not in em:
                if '@' in em:
                    ems=em.split('@')
                    ems2=ems[1]
                    if '.' in ems[1]:
                        ems3=ems2.split('.')
                        if ems3[1].lower() in ['com', 'ae', 'in', 'gov', 'ru', 'stu']:
                            pass
                        else:
                            print()
                            print('''We're sorry, but this domain is not currently supported.
Supported domains: ['com', 'ae', 'in', 'gov', 'ru', 'stu']
Please try again.''')
                            sleep(2)
                            clear()
                            update_info(userid, displayname, admin_check)
                    else:
                        print()
                        print('''Invalid e-mail. Try again.''')
                        sleep(2)
                        clear()
                        update_info(userid, displayname, admin_check)
                else:
                    print()
                    print('''Invalid e-mail. Please try again and include a domain. Eg: ''' + em + '''@gmail.com''')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            else:
                print()
                print('''Please make sure there are no spaces in the entered E-mail. Try again.''')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            sqlcursor.execute(f'select email from users where userid = \'{input_userid}\'')
            for i in sqlcursor:
                existingEmail = i[0]
            if existingEmail == em:
                print(f'You can\'t change {acc_displayname}\'s E-Mail to what it already is! Try again.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            ch = input(f'Are you sure you want to change {acc_displayname}\'s email to {em}? (Y/N): ').upper()
            if ch == 'Y':
                input_password = input('\nEnter Admin Key to authenticate: ')
                if input_password == adminkey:
                    sqlcursor.execute(f'update users set email = \'{em}\' where userid = \'{input_userid}\'')
                    connection.commit()
                    print(f'Changed {acc_displayname}\'s E-Mail to {em} successfully.')
                    sleep(2)
                    clear()
                    sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                    for i in sqlcursor:
                        status = i[0]
                    if status == 'Y':
                        admin(userid, displayname)
                    else:
                        standard(userid, displayname)
                else:
                    print('Incorrect Admin Key. Try Again.')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            elif ch == 'N':
                print('Ok, cancelled.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
            else:
                print('Invalid Input.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
        elif ch == '2':
            sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\', phone \'Phone Number\' from users where userid = \'{input_userid}\'')
            print()
            print(rec(sqlcursor))
            print()
            newphone = input('Enter New Phone Number: ')
            sqlcursor.execute(f'select phone from users where userid = \'{input_userid}\'')
            for i in sqlcursor:
                existingPhone = i[0]
            if existingPhone == newphone:
                print(f'You can\'t change {acc_displayname}\'s Phone Number to what it already is! Try again.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            ch = input(f'Are you sure you want to change {acc_displayname}\'s Phone Number to {newphone}? (Y/N): ').upper()
            if ch == 'Y':
                input_password = input('\nEnter password to authenticate: ')
                if input_password == auth:
                    sqlcursor.execute(f'update users set phone = \'{newphone}\' where userid = \'{input_userid}\'')
                    connection.commit()
                    print(f'Changed {acc_displayname}\'s Phone Number to {newphone} successfully.')
                    sleep(2)
                    clear()
                    sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                    for i in sqlcursor:
                        status = i[0]
                    if status == 'Y':
                        admin(userid, displayname)
                    else:
                        standard(userid, displayname)
                else:
                    print('Incorrect Password. Try Again.')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            elif ch == 'N':
                print('Ok, cancelled.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
            else:
                print('Invalid Input.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
        elif ch == '3':
            sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\', phone \'Phone Number\' from users where userid = \'{input_userid }\'')
            print()
            print(rec(sqlcursor))
            print()
            newdisplay = input('Enter New Display Name: ')
            if acc_displayname == newdisplay:
                print(f'You can\'t change {acc_displayname}\'s Display Name to what it already is! Try again.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            ch = input(f'Are you sure you want to change {acc_displayname}\'s Display Name to {newdisplay}? (Y/N): ').upper()
            if ch == 'Y':
                input_password = input('\nEnter Admin Key to authenticate: ')
                if input_password == adminkey:
                    sqlcursor.execute(f'update users set displayname = \'{newdisplay}\' where userid = \'{input_userid}\'')
                    connection.commit()
                    print(f'Changed {acc_displayname}\'s Display Name to {newdisplay} successfully.')
                    sleep(2)
                    clear()
                    sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                    for i in sqlcursor:
                        status = i[0]
                    if status == 'Y':
                        admin(userid, newdisplay)
                    else:
                        standard(userid, newdisplay)
                else:
                    print('Incorrect Password. Try Again.')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            elif ch == 'N':
                print('Ok, cancelled.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
            else:
                print('Invalid Input.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
        else:
            print('Invalid Input.')
            sleep(2)
            clear()
            update_info(userid, displayname, admin_check)
    else:
        print(f'''{displayname}, What account information would you like to update?
1) E-mail
2) Phone Number
3) Password
4) Display Name''')
        ch = input('Enter Choice: ')
        if ch == '1':
            sqlcursor.execute(f'select password from users where userid = \'{userid}\'')
            for i in sqlcursor:
                auth = i[0]
            sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\', phone \'Phone Number\' from users where userid = \'{userid}\'')
            print()
            print(rec(sqlcursor))
            print()
            em = input('Enter new E-Mail: ')
            if ' ' not in em:
                if '@' in em:
                    ems=em.split('@')
                    ems2=ems[1]
                    if '.' in ems[1]:
                        ems3=ems2.split('.')
                        if ems3[1].lower() in ['com', 'ae', 'in', 'gov', 'ru', 'stu']:
                            pass
                        else:
                            print()
                            print('''We're sorry, but this domain is not currently supported.
Supported domains: ['com', 'ae', 'in', 'gov', 'ru', 'stu']
Please try again.''')
                            sleep(2)
                            clear()
                            update_info(userid, displayname, admin_check)
                    else:
                        print()
                        print('''Invalid e-mail. Try again.''')
                        sleep(2)
                        clear()
                        update_info(userid, displayname, admin_check)
                else:
                    print()
                    print('''Invalid e-mail. Please try again and include a domain. Eg: ''' + em + '''@gmail.com''')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            else:
                print()
                print('''Please make sure there are no spaces in the entered E-mail. Try again.''')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            sqlcursor.execute(f'select email from users where userid = \'{userid}\'')
            for i in sqlcursor:
                existingEmail = i[0]
            if existingEmail == em:
                print('You can\'t change your E-Mail to what it already is! Try again.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            ch = input(f'Are you sure you want to change your email to {em}?(Y/N): ').upper()
            if ch == 'Y':
                input_password = input('\nEnter password to authenticate: ')
                if input_password == auth:
                    sqlcursor.execute(f'update users set email = \'{em}\' where userid = \'{userid}\'')
                    connection.commit()
                    print(f'Changed E-Mail to {em} successfully.')
                    sleep(2)
                    clear()
                    sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                    for i in sqlcursor:
                        status = i[0]
                    if status == 'Y':
                        admin(userid, displayname)
                    else:
                        standard(userid, displayname)
                else:
                    print('Incorrect Password. Try Again.')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            elif ch == 'N':
                print('Ok, cancelled.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
            else:
                print('Invalid Input.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
        elif ch == '2':
            sqlcursor.execute(f'select password from users where userid = \'{userid}\'')
            for i in sqlcursor:
                auth = i[0]
            sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\', phone \'Phone Number\' from users where userid = \'{userid}\'')
            print()
            print(rec(sqlcursor))
            print()
            newphone = input('Enter New Phone Number: ')
            sqlcursor.execute(f'select phone from users where userid = \'{userid}\'')
            for i in sqlcursor:
                existingPhone = i[0]
            if existingPhone == newphone:
                print('You can\'t change your Phone Number to what it already is! Try again.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            ch = input(f'Are you sure you want to change your Phone Number to {newphone}? (Y/N): ').upper()
            if ch == 'Y':
                input_password = input('\nEnter password to authenticate: ')
                if input_password == auth:
                    sqlcursor.execute(f'update users set phone = \'{newphone}\' where userid = \'{userid}\'')
                    connection.commit()
                    print(f'Changed Phone Number to {newphone} successfully.')
                    sleep(2)
                    clear()
                    sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                    for i in sqlcursor:
                        status = i[0]
                    if status == 'Y':
                        admin(userid, displayname)
                    else:
                        standard(userid, displayname)
                else:
                    print('Incorrect Password. Try Again.')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            elif ch == 'N':
                print('Ok, cancelled.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
            else:
                print('Invalid Input.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
        elif ch == '3':
            sqlcursor.execute(f'select password from users where userid = \'{userid}\'')
            for i in sqlcursor:
                auth = i[0]
            sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\', phone \'Phone Number\' from users where userid = \'{userid}\'')
            print()
            print(rec(sqlcursor))
            print()
            newpass = input('Enter New Password: ')
            temp = input('Repeat Password: ')
            if temp != newpass:
                print('Both passwords should match! Try again.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            if auth == newpass:
                print('You can\'t change your Password to what it already is! Try again.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            ch = input(f'Are you sure you want to change your Password? (Y/N): ').upper()
            if ch == 'Y':
                input_password = input('\nEnter current password to authenticate: ')
                if input_password == auth:
                    sqlcursor.execute(f'update users set password = \'{newpass}\' where userid = \'{userid}\'')
                    connection.commit()
                    print(f'Changed Password Successfully.')
                    sleep(2)
                    clear()
                    sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                    for i in sqlcursor:
                        status = i[0]
                    if status == 'Y':
                        admin(userid, displayname)
                    else:
                        standard(userid, displayname)
                else:
                    print('Incorrect Password. Try Again.')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            elif ch == 'N':
                print('Ok, cancelled.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
            else:
                print('Invalid Input.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
        elif ch == '4':
            sqlcursor.execute(f'select password from users where userid = \'{userid}\'')
            for i in sqlcursor:
                auth = i[0]
            sqlcursor.execute(f'select userid \'User ID\', displayname \'Display Name\', email \'E-Mail\', phone \'Phone Number\' from users where userid = \'{userid}\'')
            print()
            print(rec(sqlcursor))
            print()
            newdisplay = input('Enter New Display Name: ')
            if displayname == newdisplay:
                print('You can\'t change your Display Name to what it already is! Try again.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
            ch = input(f'Are you sure you want to change your Display Name to {newdisplay}? (Y/N): ').upper()
            if ch == 'Y':
                input_password = input('\nEnter password to authenticate: ')
                if input_password == auth:
                    sqlcursor.execute(f'update users set displayname = \'{newdisplay}\' where userid = \'{userid}\'')
                    connection.commit()
                    print(f'Changed Display Name to {newdisplay} successfully.')
                    sleep(2)
                    clear()
                    sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                    for i in sqlcursor:
                        status = i[0]
                    if status == 'Y':
                        admin(userid, newdisplay)
                    else:
                        standard(userid, newdisplay)
                else:
                    print('Incorrect Password. Try Again.')
                    sleep(2)
                    clear()
                    update_info(userid, displayname, admin_check)
            elif ch == 'N':
                print('Ok, cancelled.')
                sleep(2)
                clear()
                sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
                for i in sqlcursor:
                    status = i[0]
                if status == 'Y':
                    admin(userid, displayname)
                else:
                    standard(userid, displayname)
            else:
                print('Invalid Input.')
                sleep(2)
                clear()
                update_info(userid, displayname, admin_check)
        else:
            print('Invalid Input.')
            sleep(2)
            clear()
            update_info(userid, displayname, admin_check)

def issue_book(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[31m
                        ██ ███████ ███████ ██    ██ ███████   
                        ██ ██      ██      ██    ██ ██        
                        ██ ███████ ███████ ██    ██ █████     
                        ██      ██      ██ ██    ██ ██        
                        ██ ███████ ███████  ██████  ███████   
                                                            
                                                            
                    ██████   ██████   ██████  ██   ██ ███████ 
                    ██   ██ ██    ██ ██    ██ ██  ██  ██      
                    ██████  ██    ██ ██    ██ █████   ███████ 
                    ██   ██ ██    ██ ██    ██ ██  ██       ██ 
                    ██████   ██████   ██████  ██   ██ ███████ 
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
''')
    keyword = input('Enter keyword (Enter to see all books): ')
    sqlcursor.execute(f'select books.bookid \'Book ID\', books.bookname \'Name\', authors.authorname \'Author\', books.status \'Issue Status\', books.userid \'Issued By\' from books natural join authors where books.bookname like \'%{keyword}%\'')
    print()
    print(rec(sqlcursor))
    print()
    issue_id = input('Enter Book ID of the book you want to issue: ').upper()
    if len(issue_id) != 6 or issue_id[0] != 'B':
        print('Invalid Book ID.')
        sleep(2)
        clear()
        issue_book(userid, displayname)
    sqlcursor.execute('select bookid from books')
    existingBooks = []
    for i in sqlcursor:
        existingBooks.append(i[0])
    if issue_id not in existingBooks:
        print('Book does not exist! Try again.')
        sleep(2)
        clear()
        issue_book(userid, displayname)
    sqlcursor.execute(f'select bookname from books where bookid = \'{issue_id}\'')
    for i in sqlcursor:
        book_name = i[0]
    sqlcursor.execute(f'select status from books where bookid = \'{issue_id}\'')
    for i in sqlcursor:
        issued = i[0]
    if issued == 'issued':
        print('Sorry, this book has already been issued. Look for another?')
        sleep(2)
        clear()
        issue_book(userid, displayname)
    ch = input(f'Are you sure you want to issue \'{book_name}\'? (Y/N): ').upper()
    if ch == 'Y':
        sqlcursor.execute(f'update books set status = \'issued\' where bookid = \'{issue_id}\'')
        connection.commit()
        sqlcursor.execute(f'update books set userid = \'{userid}\' where bookid = \'{issue_id}\'')
        connection.commit()
        sqlcursor.execute(f'insert into issues(userid, bookid) values (\'{userid}\', \'{issue_id}\')')
        connection.commit()
        print(f'Successfully issued \'{book_name}\'.')
        sleep(2)
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    elif ch == 'N':
        print('Ok, cancelled.')
        sleep(2)
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)
    else:
        print('Invalid Input.')
        sleep(2)
        clear()
        sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
        for i in sqlcursor:
            status = i[0]
        if status == 'Y':
            admin(userid, displayname)
        else:
            standard(userid, displayname)

def wishlist(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[34m          
              ██     ██ ██ ███████ ██   ██ ██      ██ ███████ ████████ 
              ██     ██ ██ ██      ██   ██ ██      ██ ██         ██    
              ██  █  ██ ██ ███████ ███████ ██      ██ ███████    ██    
              ██ ███ ██ ██      ██ ██   ██ ██      ██      ██    ██    
               ███ ███  ██ ███████ ██   ██ ███████ ██ ███████    ██ 
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
''')
    print(f'''Hey, {displayname}. Know any good reads we missed? Let us know!''')
    suggestedbookname = input('Enter name of Suggested Book: ')
    suggestedauthorname = input('Enter author of Suggested Book: ')
    sqlcursor.execute(f'insert into wishlist values(\'{suggestedbookname}\', \'{suggestedauthorname}\')')
    connection.commit()
    print('\nSuggestion Submitted!')
    sleep(2)
    clear()
    standard(userid, displayname)

def standard(userid, displayname):
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[93m          
    ██    ██ ███████ ███████ ██████      ██████   █████  ███    ██ ███████ ██      
    ██    ██ ██      ██      ██   ██     ██   ██ ██   ██ ████   ██ ██      ██      
    ██    ██ ███████ █████   ██████      ██████  ███████ ██ ██  ██ █████   ██      
    ██    ██      ██ ██      ██   ██     ██      ██   ██ ██  ██ ██ ██      ██      
     ██████  ███████ ███████ ██   ██     ██      ██   ██ ██   ████ ███████ ███████ 
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m''')
    print(f'''\nWelcome to the user panel, {displayname}. What would you like to do?
1) Delete your account
2) Update account information
3) Search Authors/Books
4) Issue Book
5) Return Book
6) View Issued Books
7) Add Books to Wishlist
8) Logout''')
    ch = input('Enter Choice: ')
    if ch == '1':
        clear()
        delete(userid, displayname, False)
    elif ch == '2':
        clear()
        update_info(userid, displayname, False)
    elif ch == '3':
        print('''\nYou can search books or authors.
1) Books
2) Authors''')
        ch = input('Enter choice: ')
        if ch == '1':
            clear()
            search_books(userid, displayname)
        elif ch == '2':
            clear()
            search_authors(userid, displayname)
        else:
            print('Invalid input.')
            sleep(2)
            clear()
            standard(userid, displayname)
    elif ch == '4':
        clear()
        issue_book(userid, displayname)
    elif ch == '5':
        clear()
        return_book(userid, displayname)
    elif ch == '6':
        print(f'''\n Hey there, {displayname}! Here are all the books you have issued:
''')
        sqlcursor.execute(f'select issues.bookid \'Book ID\', books.bookname \'Book Name\', issues.issuedate \'Issued On\', issues.issuetime \'Time Issued\', issues.returndate \'Returned On\', issues.fine \'Fines Applicable\' from issues natural join books where userid = \'{userid}\'')
        print(rec(sqlcursor))
        print()
        input('Press Enter to Continue: ')
        clear()
        standard(userid, displayname)
    elif ch == '7':
        clear()
        wishlist(userid, displayname)
    elif ch == '8':
        clear()
        home()
    else:
        print('Invalid Input.')
        sleep(2)
        clear()
        standard(userid, displayname)

def login():
    print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[92m
                        ██       ██████   ██████  ██ ███    ██         
                        ██      ██    ██ ██       ██ ████   ██         
                        ██      ██    ██ ██   ███ ██ ██ ██  ██         
                        ██      ██    ██ ██    ██ ██ ██  ██ ██         
                        ███████  ██████   ██████  ██ ██   ████         
                                                                  
                                                                 
                                     ██████  ██████                    
                                    ██    ██ ██   ██                   
                                    ██    ██ ██████                    
                                    ██    ██ ██   ██                   
                                     ██████  ██   ██                   
                                                                 
                                                                
                    ███████ ██  ██████  ███    ██     ██    ██ ██████  
                    ██      ██ ██       ████   ██     ██    ██ ██   ██ 
                    ███████ ██ ██   ███ ██ ██  ██     ██    ██ ██████  
                         ██ ██ ██    ██ ██  ██ ██     ██    ██ ██      
                    ███████ ██  ██████  ██   ████      ██████  ██   
\033[00m
\033[96mX ==== | | ================================================================= | | ==== X\033[00m''')
    print('''\n1) Login
2) Sign Up
3) Home''')
    ch = input('Enter Choice: ')
    if ch == '1':
        # try:
        userid = input('Enter your userid: ').lower()
        existingUsers = []
        sqlcursor.execute('select userid from users')
        for i in sqlcursor:
            existingUsers.append(i[0])
        if userid not in existingUsers:
            print('User does not exist! Try again.')
            sleep(2)
            clear()
            login()
        sqlcursor.execute(f'select password from users where userid = \'{userid}\'')
        for i in sqlcursor:
            password = i[0]
        sqlcursor.execute(f'select displayname from users where userid = \'{userid}\'')
        for i in sqlcursor:
            displayname = i[0]
        input_password = input(f'Welcome, {displayname}! Enter your password: ')
        if input_password == password:
            sqlcursor.execute(f'select admin from users where userid = \'{userid}\'')
            for i in sqlcursor:
                if i[0].upper() == 'Y':
                    clear()
                    admin(userid, displayname)
                else:
                    clear()
                    standard(userid, displayname)
        else:
            print('Incorrect Password. Try again.')
            sleep(2)
            clear()
            login()
    elif ch == '2':
        print('''Hello and welcome to the library! We're glad to see you here.
To get signed up, you must agree to our return policy.
''')
        returnPolicy()
        print('''
\033[96mX ==== | | ================================================================= | | ==== X\033[00m
              
Now that you're familiar with the return policy, we'll need some details before we can
sign you up.
''')
        userid = input('''First, you\'ll need a UserID. It will be visible when you issue or return a book.
Enter UserID: ''').lower()
        existingUsers = []
        sqlcursor.execute('select userid from users')
        data = sqlcursor.fetchall()
        for i in data:
            existingUsers.append(i[0])
        if userid in existingUsers:
            print('Sorry, UserID already exists. Try again!\n')
            sleep(2)
            clear()
            login()
        else:
            password = input('''Choose a strong password. Try to use Uppercase, lowercase, numbers and special
characters. Enter password: ''')
            displayname = input('You\'ll need a display name. This is what we\'ll call you. Enter display name: ')
            em = input('Enter e-mail: ')
            if ' ' not in em:
                if '@' in em:
                    ems=em.split('@')
                    ems2=ems[1]
                    if '.' in ems[1]:
                        ems3=ems2.split('.')
                        if ems3[1].lower() in ['com', 'ae', 'in', 'gov', 'ru', 'stu']:
                            pass
                        else:
                            print()
                            print('''We're sorry, but this domain is not currently supported.
Supported domains: ['com', 'ae', 'in', 'gov', 'ru', 'stu']
Please try again.''')
                            sleep(2)
                            clear()
                            login()
                    else:
                        print()
                        print('''Invalid e-mail. Try again.''')
                        sleep(2)
                        clear()
                        login()
                else:
                    print()
                    print('''Invalid e-mail. Please try again and include a domain. Eg: ''' + em + '''@gmail.com''')
                    sleep(2)
                    clear()
                    login()
            else:
                print()
                print('''Please make sure there are no spaces in the entered E-mail. Try again.''')
                sleep(2)
                clear()
                login()
            phone = input('Enter your phone number (Should not exceed 10 digits): ')
            try:
                sudo = int(phone)
            except:
                print('Invalid Phone Number, Please try again.')
                sleep(2)
                clear()
                login()
            if len(phone) > 10:
                print('Invalid Phone Number, Please try again.')
                sleep(2)
                clear()
                login()
            print('''To gain admin status in your account, you will have to request an existing admin to
grant you admin privileges, or you could enter the admin key.''')
            ch = input('Enter admin key? (Y/N): ').upper()
            if ch.upper() == 'Y':
                input_adminkey = input('Enter Admin Key: ')
                if input_adminkey == adminkey:
                    admincheck = 'Y'
            elif ch.upper() == 'N':
                admincheck = 'N'
            else:
                print('Invalid Answer. (Considered as N)')
                admincheck = 'N'
            sqlcursor.execute(f'insert into users(userid, password, displayname, email, phone, admin) values (\'{userid}\',\'{password}\', \'{displayname}\', \'{em}\', \'{phone}\', \'{admincheck}\')')
            connection.commit()
            print('''Account successfully registered! Welcome to the library fam!
Now use your new account details to login and use the library!''')
            print()
            sleep(2)
            clear()
            login()
    elif ch == '3':
        clear()
        home()
    else:
        print('Invalid Input! Try again.')
        sleep(2)
        clear()
        login()

def home():
    while True:
        print('''\033[96mX ==== | | ================================================================= | | ==== X\033[00m
\033[94m  
                        ██   ██  ██████  ███    ███ ███████ 
                        ██   ██ ██    ██ ████  ████ ██      
                        ███████ ██    ██ ██ ████ ██ █████   
                        ██   ██ ██    ██ ██  ██  ██ ██      
                        ██   ██  ██████  ██      ██ ███████              \033[00m

\033[96mX ==== | | ================================================================= | | ==== X\033[00m''')
        print('''\nWhat would you like to do?
1) Login or Sign Up
2) View Return Policy
3) Exit''')
        ch = input('Enter choice: ')
        if ch == '1':
            clear()
            login()
        elif ch == '2':
            print()
            returnPolicy()
            print('''
\033[96mX ==== | | ================================================================= | | ==== X\033[00m\n''')
            input('Press Enter to Continue: ')
            clear()
        elif ch == '3':
            clear()
            exiting()
        else:
            print('Invalid choice! Try again.')
            sleep(2)
            clear()
            home()
        print()

# Creating Tables
sqlcursor.execute('create table if not exists users(userid varchar(255) primary key not null, password varchar(255), displayname varchar(255), email varchar(255), phone char(10), admin char(1), doj date default (current_date))')
sqlcursor.execute('create table if not exists books(bookid char(6) primary key not null, bookname varchar(255), authorid char(6), published date, status varchar(10) default \'not issued\', userid varchar(255))')
sqlcursor.execute('create table if not exists authors(authorid char(6) primary key not null, authorname varchar(255))')
sqlcursor.execute('create table if not exists issues(userid varchar(255), bookid char(6), issuedate date default (current_date), issuetime time default (current_time), returndate date, fine int default 0)')
sqlcursor.execute('create table if not exists wishlist(bookname varchar(255), authorname varchar(255))')

# Adding Data into Books and Authors tables
try:
    sqlcursor.execute('''insert into books(bookid, bookname, authorid, published) values
        ('B12001', 'Computer Science with Python - 12', 'A12005', '2023-11-12'),
        ('B11001', 'Computer Science with Python - 11', 'A12005', '2023-12-10'),
        ('B99007', 'Harry Potter and the Deathly Hallows', 'A99001', '2007-02-21'),
        ('B99002', 'Harry Potter and the Chamber of Secrets', 'A99001', '1998-07-02'),
        ('B99003', 'Harry Potter and the Prisoner of Azkaban', 'A99001', '1999-07-08'),
        ('B99004', 'Harry Potter and the Goblet of Fire', 'A99001', '2000-07-08'),
        ('B99005', 'Harry Potter and the Order of the Phoenix', 'A99001', '2003-07-21'),
        ('B99006', 'Harry Potter and the Half-blood Prince', 'A99001', '2005-07-16'),
        ('B99001', 'Harry Potter and the Philosopher\\'s Stone', 'A99001', '1997-07-30'),
        ('B98001', 'Percy Jackson and the Lightning Thief', 'A98001', '2005-06-28'),
        ('B98002', 'Percy Jackson and the Sea of Monsters', 'A98001', '2006-04-01'),
        ('B98003', 'Percy Jackson and the Titan\\'s Curse', 'A98001', '2007-04-25'),
        ('B98004', 'Percy Jackson and the Battle of the Labyrinth', 'A98001', '2008-05-06'),
        ('B98005', 'Percy Jackson and the Last Olympian', 'A98001', '2009-05-05'),
        ('B98008', 'Heroes of Olympus: The Mark of Athena', 'A98001', '2012-10-02'),
        ('B98007', 'Heroes of Olympus: The Son of Neptune', 'A98001', '2011-10-04'),
        ('B98006', 'Heroes of Olympus: The Lost Hero', 'A98001', '2010-10-12'),
        ('B98009', 'Heroes of Olympus: The House of Hades', 'A98001', '2013-10-08'),
        ('B98010', 'Heroes of Olympus: The Blood of Olympus', 'A98001', '2014-10-07'),
        ('B42001', 'When the Sky Falls', 'A42001', '2021-06-03'),
        ('B42002', 'While the Storm Rages', 'A42001', '2022-06-02'),
        ('B42003', 'Until the Road Ends', 'A42001', '2023-06-30'),
        ('B10001', 'Little Women', 'A11001', '1987-12-30')''')
    connection.commit()
    sqlcursor.execute('''insert into authors values
        ('A12005', 'Preeti Arora'),
        ('A99001', 'JK Rowling'),
        ('A98001', 'Rick Riordan'),
        ('A42001', 'Phil Earle'),
        ('A11001', 'Louis M. Alcott')''')
    connection.commit()
except:
    pass

home()

# End