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


def read_movies():
    cursor.execute("SELECT * FROM Movies")
    movies = cursor.fetchall()
    for movie in movies:
        print(movie)


def create_movie(title, year, director_id):
    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
        (title, year, director_id)
    )
    conn.commit()  


def delete_movie(movie_id):
    try:
        cursor.execute("DELETE FROM MovieActors WHERE MovieId = ?", (movie_id,))
        cursor.execute("DELETE FROM Movies WHERE Id = ?", (movie_id,))
        conn.commit()
        print("Movie deleted successfully!")
    except pyodbc.IntegrityError as e:
        print("Error:", e)


def update_movie(movie_id, title, year, director_id):
    cursor.execute(
        "UPDATE Movies SET Title = ?, Year = ?, DirectorId = ? WHERE MovieId = ?",
        (title, year, director_id, movie_id)
    )
    conn.commit()
    print("Movie updated successfully!")


def menu():
    print("\nMenu:")
    print("1. Create a movie")
    print("2. Update a movie")
    print("3. Delete a movie")
    print("4. Exit")


if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter the movie title: ")
            year = input("Enter the release year: ")
            director_id = input("Enter the director ID: ")
            create_movie(title, year, director_id)
            print("Movie added successfully!")

        elif choice == "2":
            read_movies()
            movie_id_to_update = input("Enter the ID of the movie you want to update: ")
            title = input("Enter the updated movie title: ")
            year = input("Enter the updated release year: ")
            director_id = input("Enter the updated director ID: ")
            update_movie(movie_id_to_update, title, year, director_id)

        elif choice == "3":
            read_movies()
            movie_id_to_delete = input("Enter the ID of the movie you want to delete: ")
            delete_movie(movie_id_to_delete)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
