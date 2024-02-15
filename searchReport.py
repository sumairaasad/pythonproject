from connect import * 
import logging
import time


# logging.basicConfig(filename=r"pythonproject/file.log", format='[%(filename)s:%(lineno)d in function %(funcName)s] %(levelname)s: %(message)s', level=logging.DEBUG)
# filename = __file__
filename = __name__
logging.basicConfig(filename=r"pythonproject\file1.log", level=logging.DEBUG)

# create a subroutine
def search():
    try:
        field = input("Would you like to search by yearReleased or duration or title or genre? ")
        if field == "yearReleased" or field == "duration":
            searchInput = input(f"Enter search field for {field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} == {searchInput}")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with {field} exists in the table: ")
                logging.warning(f"On {time.asctime()}, file is {filename}, user entered {field} as {field}")
                
            else:
                for aRecord in rows:
                    print(aRecord)
        elif field == "rating" or field == "title" or field == "genre":
            searchInput = input(f"Enter search field for {field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms  WHERE {field} LIKE '%{searchInput}%'")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with field {field} Matching '{searchInput}' in the table ")
                logging.warning(f"On {time.asctime()}, file is {filename}, user entered {field} as {field}")

            else:
                for records in rows:
                    print(records)
        else:
            print(f"Invalid search filed {field}")
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")
if __name__ == "__main__":
    search()