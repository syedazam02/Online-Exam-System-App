import mysql.connector
mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "root",database = "exam")
mycursor = mydb.cursor()
class SupUser:
    def add_question(self,question,opt1,opt2,opt3,opt4,ans):
        # mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "root",database = "exam")
        # mycursor = mydb.cursor()
        # sql = "INSERT INTO qna VALUES (%s,%s)"
        sql = "INSERT INTO qna1(question,option1,option2,option3,option4,answers) VALUES (%s,%s,%s,%s,%s,%s);"
        val = (question,opt1,opt2,opt3,opt4,ans)
        mycursor.execute(sql,val)
        mydb.commit()
        # mydb.close()
    
    def remove_question(self,delQ):
        # mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "root",database = "exam")
        # mycursor = mydb.cursor()
        sql = "DELETE FROM qna1 WHERE question = %s"
        val = (delQ,)
        mycursor.execute(sql,val)
        mydb.commit()
        # mydb.close()
    
    def add_user(self,un,passw):
        sql = "INSERT INTO users(id,password) VALUES (%s,%s);"
        val = (un,passw)
        mycursor.execute(sql,val)
        mydb.commit()
    
    def remove_user(self,un):
        sql = "DELETE FROM users WHERE id = %s"
        val = (un,)
        mycursor.execute(sql,val)
        mydb.commit()
    
    def display_users(self):
        print("-----USER DETAILS------")
        mycursor.execute("SELECT * FROM users;")
        for row in mycursor:
            print("USERNAME :",row[0],"PASSWORD :",row[1])
    
    def display_qna(self):
        mycursor.execute("SELECT * FROM qna1;")
        for row in mycursor:
            print(row[0]," ",row[1])
            print("a."+row[2]+"\nb."+row[3]+"\nc."+row[4]+"\nd."+row[5])
    
    
