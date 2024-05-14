from util.DBconn import DBConnection


class DirectorService(DBConnection):
    def read_director(self):
        try:
            self.cursor.execute("Select * from Directors")
            directors = self.cursor.fetchall()
            for i in directors: # Get all data
                print(i)
        except Exception as e:
            print(e)  
           