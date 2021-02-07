import mysql.connector
mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "root",database = "exam")
mycursor = mydb.cursor()
class User:
    def __init__(self,loginId):
        self.__loginId = loginId
        self.__marks = 0

    def attempt_exam(self):
        print("------EXAM HAS STARTED-------")
        mycursor.execute("SELECT * FROM qna1;")
        for row in mycursor:
            print(row[0]," ",row[1])
            opta = row[2]
            optb = row[3]
            optc = row[4]
            optd = row[5]
            ans = ""
            print("a."+row[2]+"\nb."+row[3]+"\nc."+row[4]+"\nd."+row[5])
            data = input("Enter Answer Here :")
            if data == "a":
                ans = opta
            if data == "b":
                ans = optb
            if data == "c":
                ans = optc
            if data == "d":
                ans = optd
            if ans == row[6]:
                self.__marks = self.__marks + 1
        self.display_results(self.__marks)
        self.answers()
        self.insert_user_marks(self.__loginId,self.__marks)
    
    def user_info(self):
        print("------User Details--------")
        sql = "SELECT * FROM users WHERE id = %s"
        val = (self.__loginId,)
        mycursor.execute(sql,val)
        for row in mycursor:
            print(" USERNAME :",row[0],"\n","PASSWORD :",row[1])

    def display_results(self,mks):
        print("------RESULT------")
        print("MARKS SCORED :",mks)
        print("-------------------")

    def answers(self):
        print("****CORRECT ANSWERS****")
        mycursor.execute("SELECT * FROM qna1;")
        for row in mycursor:
            print(row[0], " ", row[1])
            print("ANSWER :" + row[6])

    def insert_user_marks(self,lId,mks):
        sql = "INSERT INTO marks_scored(loginId,marks) VALUES (%s,%s);"
        val = (lId, mks)
        mycursor.execute(sql, val)
        mydb.commit()
