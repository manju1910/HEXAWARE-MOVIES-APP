from Entity import Director,Movie,Actor

# from Entity.movie import Movie
from DAO.movie_service import MovieService
from DAO.director_service import DirectorService
# cursor = conn.cursor()
# cursor.execute("Select 1")
# print("Database connection is successful 🎊")
 
 
# Service - Function that talk to DB | Layer that interacts with DB
 
 
# Encapsulation

 
 

 
class ActorService:
    pass
 
 
# Entity / Model
# Encapsulation - Movie data

 
 

 
 

 
 
# Main menu
# 1. Movie Management
# 2. Director Management
# 3. Actor Management
# 4. Exit
 
 
# Task 3
# Movie Management Menu
# 1. Add a Movie
# 2. View All Movies
# 3. Update a Movie  (Task 4)
# 4. Delete a Movie
# 5. Back
 
# C - Create
# R - Read
# U - Update
# D - Delete
 
class MainMenu:
    movie_service=MovieService()
    director_service=DirectorService()
    def movie_menu(self):
      
    
        while True:
            print(
                """      
            1. Add a Movie
            2. View all Movies
            3. Update a Movie  
            4. Delete a Movie
            5. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
    
            if choice == 1:
                title = input("Please enter movie title: ")
                year = int(input("Please enter movie year: "))
                director_id = int(input("Please enter movie director's id: "))
                new_movie = Movie(title, year, director_id)
                self.movie_service.create_movie(new_movie)
            elif choice == 2:
                self.movie_service.read_movies()
            if choice == 3:
                movie_id = int(input("Please enter movie's id: "))
                title = input("Please enter movie title: ")
                year = int(input("Please enter movie year: "))
                director_id = int(input("Please enter movie director's id: "))
                updated_movie = Movie(title, year, director_id)
                self.movie_service.update_movie(updated_movie, movie_id)
            elif choice == 4:
                movie_id = int(input("Please tell a movie id to delete: "))
                self.movie_service.delete_movie(movie_id)
            elif choice == 5:
                break
    
    
    def director_menu(self):
         while True:
            print(
                """      
            
            1. View all Movies
            2. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
    
            
            if choice == 1:
                self.director_service.read_director()
            elif choice == 2:
                break
    
    
    
    def actor_menu(self):
        pass
 
 
# Task 5 - Keep it in loop
if __name__ == "__main__":
    print("Welcome to the movies app")
    main_menu=MainMenu()
    while True:
        print(
            """      
            1. Movie Management
            2. Director Management
            3. Actor Management
            4. Exit
                """
        )
 
        choice = int(input("Please choose from above options: "))
 
        if choice == 1:
            main_menu.movie_menu()
        elif choice == 2:
            main_menu.director_menu()
        elif choice == 3:
            main_menu.actor_menu()
        elif choice == 4:
            main_menu.movie_service.close()
            break
 
    # Clean up code
    # cursor.close()
    # conn.close()