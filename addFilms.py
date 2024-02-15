from connect import *
 
# create a subroutine
def insert_tblFilms():
    # create an empty list
  films= []
    # ask for user input (filmID, title and yearReleased,)
    # filmID is an auto increment field and does not require input
  filmID = int(input("Enter your filmID: "))
  title = input("Enter yourtitle: ")
  yearReleased = int(input("Enter your yearReleased : "))
  rating= input("Enter your rating: ")
  duration= int(input("Enter your duration: "))
  genre= input("Enter your genre: ")
  print(f"Data: {filmID, title, yearReleased, }")
    # append data filmID, title and yearReleased)
  films.append(filmID)
  films.append(title)
  films.append(yearReleased)
  films.append(rating)
  films.append(duration)
  films.append(genre)
 

  print(f"The tblFilmslist {films}")
 
  "INSERT INTO tblFilms VALUES(NULL, 'A','B','C')"
  "INSERT INTO tblFilms(filmID, title , yearReleased,rating,duration,genre) VALUES( 'A','B','C')"
 
  try:
        dbCursor.execute("INSERT INTO tblFilms VALUES(?,?,?,?,?,?)", films) # Values from the list
        # or
        # values directly from variables
        # dbCursor.execute("INSERT INTO films VALUES(NULL, ?,?,?,?,?,?)", (filmID, title and yearReleased)
        dbCon.commit() # make the changes permanent
        print(f"{filmID} inserted in the Table")
  except sql.OperationalError as e:
        #dbCon.rollback()
        print(f"Insert failed {e}")
if __name__== "__main__":
    insert_tblFilms()