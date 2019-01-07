import pymysql

conn = pymysql.connect(
     host = 'localhost',
     user = 'root',
     db = 'system_tools',
)

#ADD TOOL
def add(tool_name,price):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO tools (tool_name,price) VALUES(%s,%s);""",(tool_name,price))
    print("Tools successfully added")
    conn.commit()
    
#VIEW TOOL
def display():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tools;")
    try:
       result = cursor.fetchall()
       for r in result:
           print(r)
    except:
        print("Empty")
conn.commit()
#DELETE TOOL
def delete():
    cursor = conn.cursor()
    try:
        id = input("Enter an id to be delete: ")
        cursor.execute("DELETE FROM tools WHERE id = %s;",id)
        print("Tools Deleted")
    except:
        print("ID '"+id+"' does not exist")
    conn.commit()
#UPDATE TOOL
def update(id):
    cursor = conn.cursor()
    id = input("Enter tools id to be update: ")
    cursor.execute("SELECT * FROM tools WHERE id = %s;",id)
    cursor.fetchall()
    if cursor.rowcount > 0:
        new_tool_name = input("Enter new tools name: ")
        new_tool_price = input("Enter new tools price: ")
        cursor.execute("""UPDATE tools SET tool_name = %s, price = %s WHERE id = %s""",(new_tool_name,new_tool_price,id))
        print("Tools updated successfully")
    else:
        print("ID '"+id+"' does not exist")
    conn.commit()
    
looping_1 = 1
while looping_1:
        print("\t\t\tTOOLS")
        print ("[A]Add_new")
        print ("[U]Update")
        print ("[D]Delete")
        print ("[V]View all tools")
        print ("[Q]Quit")

        choice = input("Enter your choice: ")

        if choice == 'A' or choice == 'a':
            tool_name = input("Enter tools name: ")
            price = input("Enter tools price: ")
            add(tool_name,price)
        elif choice == 'U' or choice == 'u':
           update(id)
        elif choice == 'D' or choice == 'd':
            delete()
        elif choice == 'V' or choice == 'v':
            display()
        elif choice == 'Q' or choice == 'q':
           print("Okay!")
           break
        else:
            print("Invalid ")

looping_2 = 1
while looping_2:
        select = input("Do you wish to continue? [Y/N]: ")
        if select == 'Y' or select == 'y':
            looping_1 = 1
            looping_2 = 0
        elif select == 'N' or select == 'n':
            print("Thanks and Godspeed!")
            looping_1 = 0
            looping_2 = 0
        else:
            print("Invalid choice")
            looping_2




