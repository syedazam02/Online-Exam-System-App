from superUser import SupUser
from user import User
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root" , password = "root", database = "exam")
mycursor = mydb.cursor()

print("1.Super User\n2.User")
choice = input("Enter Here 1 = Super user , 2 = User: ")
if choice == "1":
    loginId = input("Enter SuperUser Login ID :")
    passd = input("Enter SuperUser Password :")
    sql = "SELECT * FROM superusers WHERE user_id = %s and password = %s"
    val = (loginId,passd)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    if res:
        ch1 = "yes"
        while(ch1 == "yes"):
            print("1.Add Question\n2.Remove Question\n3.Add User\n4.Remove User\n5.Users Information\n6.Exam MCQS")
            ch2 = input("Enter Here :")
            obj = SupUser(loginId)
            if ch2 == "1":
                ques = input("Enter question here :")
                opt1 = input("Enter option1 here : ")
                opt2 = input("Enter option2 here : ")
                opt3 = input("Enter option3 here : ")
                opt4 = input("Enter option4 here : ")
                ans = input("Enter Answer here : ")
                obj.add_question(ques,opt1,opt2,opt3,opt4,ans)
            elif ch2 == "2":
                ques = input("Enter question here: ")
                obj.remove_question(ques)
            elif ch2 == "3":
                un = input("Enter username :")
                passw = input("Enter password :")
                obj.add_user(un,passw)
            elif ch2 == "4":
                un = input("Enter username :")
                obj.remove_user(un)
            elif ch2 == "5":
                obj.display_users()
            elif ch2 == "6":
                obj.display_qna()

            i = input("Type Yes more modifications and No for exit ")
            ch1 = i.lower()
    else:
        print("ERROR : INVALID USERNAME OR PASSWORD\n")

elif choice == "2":
    loginId = input("Enter User Login ID :")
    passd = input("Enter User Password :")
    sql = "SELECT * FROM users WHERE ID = %s and password = %s"
    val = (loginId,passd)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    if res:
        ch1 = "yes"
        while(ch1 == "yes"):
            print("1.Attempt Exam\n2.User Info")
            ch2 = input("Enter Here :")
            if ch2 == "1":
                obj = User(loginId)
                obj.attempt_exam()
            elif ch2 == "2":
                obj = User(loginId)
                obj.user_info()
            i = input("Type Yes to continue and No for exit ")
            ch1 = i.lower()
    else:
        print("ERROR : INVALID USERNAME OR PASSWORD\n")

