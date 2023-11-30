"""
Pettrus Konnoth
CS50
Master project main
Cmdr.Schenk Raymond
Datasbase functions
"""
import mysql.connector


class SqlFunctions:
    def __init__(self):

        self.current_user = None
        self.connection_status = False

    def validateUser(self, username, password):
        # print(username, password)
        if self.connection_status:
            query = f"SELECT * FROM user WHERE username='{username}' AND password='{password}'"
            # print(query)
            self.sql.execute(query)
            rows = self.sql.fetchone()

            #check if rows is not None

            if rows is not None:
                self.current_user = rows[0]
                self.name = rows[1]
                print(rows)
                print(self.name)
                return True
            else:
                return False
        else:
            print("Not connected to database")

    def connect(self):
        if not self.connection_status:
            try:
                #change the user and password to your own
                self.connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Irine2012",
                    database="workoutdb"
                )
                self.sql = self.connection.cursor()
                self.connection_status = True

                print("connected")
            except mysql.connector.Error as err:
                return "Failed to connect with Error: ", err
        else:
            print("Already connected")
    #
    def disconnect(self):
        # print("disconnecting")
        if self.connection_status:
            #delete the current user
            self.connection.close()
            self.connection_status = False
            print("disconnected")
        else:
            print("Not connected to database")

    def createUser(self, username, password, email, age, gender):
        if self.connection_status:
            #query to insert a new user
            query = f"INSERT INTO user(username, password, email, age, gender) VALUES('{username}', '{password}', '{email}', '{age}', '{gender}')"
            self.sql.execute(query)
            self.connection.commit()
            # print(f"User {username} created")
        else:
            print("Not connected to database")


    def GetWorkout(self):

        if self.connection_status:
            #query to get the workout for the current user
            query = f"SELECT * FROM workout WHERE user_id='{self.current_user}' "
            self.sql.execute(query)

            result = self.sql.fetchall()
            if len(result) > 0:
                #to check if the result is not empty
                #print(result)

                return result


            else:
                #if the result is empty
                print("no workout found for the user")
        else:
            #if not connected to the database
            print("Not connected to database")
        return []

#pass in the exercise name, sets and reps
    def createRecord(self,ex1,ex1sets,ex1reps,ex2,ex2sets,ex2reps,ex3,ex3sets,ex3reps,ex4,ex4sets,ex4reps,ex5,ex5sets,ex5reps):
        if self.connection_status:
            query = f"INSERT INTO workout(exercise_1, exercise_1_sets, exercise_1_reps, exercise_2, exercise_2_sets, exercise_2_reps, exercise_3, exercise_3_sets, exercise_3_reps, exercise_4, exercise_4_sets, exercise_4_reps, exercise_5, exercise_5_sets, exercise_5_reps, user_id) VALUES('{ex1}', '{ex1sets}', '{ex1reps}', '{ex2}', '{ex2sets}', '{ex2reps}', '{ex3}', '{ex3sets}', '{ex3reps}', '{ex4}', '{ex4sets}', '{ex4reps}', '{ex5}', '{ex5sets}', '{ex5reps}', '{self.current_user}')"
            self.sql.execute(query)
            self.connection.commit()
            #print(f"User {username} created")
#pass in the id of the record to be deleted
    def deleteRec(self, id):
        if self.connection_status:
            #query to delete the record
            query = f"DELETE FROM workout WHERE id='{id}' and user_id='{self.current_user}'"
            print(query)
            self.sql.execute(query)
            #print(f"User {username} created")
            self.connection.commit()
            #print(f"User {username} created")
#pass in the id of the record to be updated
    def update(self, id, ex1,ex1sets,ex1reps,ex2,ex2sets,ex2reps,ex3,ex3sets,ex3reps,ex4,ex4sets,ex4reps,ex5,ex5sets,ex5reps):
        if self.connection_status:
            query = f"UPDATE workout SET exercise_1='{ex1}', exercise_1_sets='{ex1sets}', exercise_1_reps='{ex1reps}', exercise_2='{ex2}', exercise_2_sets='{ex2sets}', exercise_2_reps='{ex2reps}', exercise_3='{ex3}', exercise_3_sets='{ex3sets}', exercise_3_reps='{ex3reps}', exercise_4='{ex4}', exercise_4_sets='{ex4sets}', exercise_4_reps='{ex4reps}', exercise_5='{ex5}', exercise_5_sets='{ex5sets}', exercise_5_reps='{ex5reps}' WHERE id='{id}' and user_id='{self.current_user}'"
            self.sql.execute(query)
            self.connection.commit()
            #print(f"User {username} created")
#pass in the id of the record to be updated
