"""
Password Manager 
Database Python file
By Ulysse Valdenaire
11/08/2021
"""

def createBook2(connection, name, book, cle, securite):
    """
    insert a fake password to the database
    """
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO t_book(name,  book, cle ,securite)"\
            + "values(%s, %s, %s,  %s)"

        cursor.execute(sql, (name, book, cle, securite))
        connection.commit()

    finally:
        connection.close()
        print("----------INSERT INTO DATABASE WAS A SUCCESS----------")


def getBook(connection, name):
    """
    Get the fake password and the level security in order to decrypt the password
    """
    try: 
        cursor = connection.cursor()
        sql = "SELECT book, securite FROM t_book WHERE name = %s"
        r = cursor.execute(sql, (name))
        new_list = []
        for row in cursor:
             print(row)
        for element in row:
            new_list.append(element)
        return new_list[0] ,new_list[1]
        
    finally:
        print("----------INSERT INTO DATABASE WAS A SUCCESS----------")

