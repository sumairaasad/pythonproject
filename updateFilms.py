from connect import *
 
# create a subroutine
def update_tblFilms():
    #use filmID is a primary and a unique field to update a record
       #  the id of the record to be updated
    idField = input("Enter the filmID to update a record: ")
 
    # the field selected for update
    fieldName = input("Enter the field (text or yearReleased or genre) to update: ").title()
 
    # the value to be entered in the field
    fieldValue = input(f"Enter the value for the {fieldName}: ")
 
    # add quotes to field value
    fieldValue = "'"+fieldValue+"'"
   
    try: 
        dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField} ")
        dbCon.commit()
        print(f"{idField} Updated in the tblFilms ")
    except sql.OperationalError as e:
        print(f"Update failed: {e}")
 
if __name__ == "__main__":
    update_tblFilms()