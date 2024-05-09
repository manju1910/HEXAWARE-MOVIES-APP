import pyodbc

server_name= "DESKTOP-0EUUQEO\\SQLEXPRESS"
database_name = "HexawareMoviesDB"
 
 
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
print("Welcome to the movies app")
print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("Select 1")
print("Database connection is successful 🎊")
 
def read_movies():
    cursor.execute("Select * from Movies")
    for i in cursor:
        print(i)


# create new movie
def create_movie():
   cursor.execute( "insert into movies values('Avatr',2012,13)")
   conn.commit() #always give commit if you wantto undo then you can rollback





 #to get dta from user 
 
def create_movie():
    cursor.execute( "insert into movies values(?,?,?)",("oppenheimerr",2023,14),)
    conn.commit() 

if __name__=="__main__":
    create_movie()   
    read_movies() 


# Task 1
# Get the data from the user
# Clue: Use arguments
def create_movie(title,year,director_id):
    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",(title,year,director_id)
    )
    conn.commit()  # Permanent storing | If no commit then no data
if __name__=="__main__":
    title=input("Enter the title: ")
    year=int(input("Enter the year: "))
    director_id=int(input("Id: ")) 
    create_movie(title, year, director_id)
    read_movies()
 
# # Task 2
# # Delete a movie from the db by getting the id from user

def delete_movie(movie_id):
    cursor.execute(
        "Delete from movies where movie_id = ?",
        (movie_id)
    )
    conn.commit()
    print("Deleted Successfully")
if __name__ == "__main__":
    movie_id=int(input("enter the movie id: "))
    delete_movie(movie_id)
    read_movies() 
 
# # Task
# # Choice
# # 1. Create Movie
# # 2. Delete Movie
# if __name__=="__main__":
 
#     choice = int(input("""
# Do you want to
# 1. Create Movie
# 2. Delete Movie
# 3. Exit from the App
# """))
 
#     if(choice == 1):
#         title = input("Enter Movie Title: ")
#         year = int(input("Enter movie year: "))
#         director_id = int(input("Enter director's id: "))
#         create_movie(title,year,director_id)
#         read_movies()
#     elif choice == 2:
#         read_movies()
#         Del_movieid = int(input("Enter the Movie Id you want to Delete: "))
#         delete_movie(Del_movieid)
#         read_movies
#     elif choice == 3:
#         print("See you again Soon")

cursor.close()
conn.close()