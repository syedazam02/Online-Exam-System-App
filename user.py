import mysql.connector
mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "root",database = "exam")
mycursor = mydb.cursor()
class User:
    def attempt_exam(self):
        marks = 0
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
                marks = marks + 1
        self.display_results(marks)      
    
    def user_info(self,loginId):
        print("-----User Info------")
        sql = "SELECT * FROM users WHERE id = %s"
        val = (loginId,)
        mycursor.execute(sql,val)
        for row in mycursor:
            print("USERNAME :",row[0],"PASSWORD :",row[1])

    def display_results(self,marks):
        print("-----RESULT-----")
        print("Marks obtained :",marks)

# obj = User()
# obj.user_info("sam")