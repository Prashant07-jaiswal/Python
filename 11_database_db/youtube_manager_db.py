#this is used to create Database
import sqlite3

#To stablished connection between database and sqlite3
con = sqlite3.connect("youtube.db")

#To create cursor for performing SQL queries
cursor = con.cursor()

#"cursor.execute()" used to execute queries
#triple quote (''' ''') is used to save formating  
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            ID INTEGER PRIMARY KEY,
            NAME TEXT NOT NULL,
            TIME TEXT NOT NULL
    )
''')

def list_all_videos():

    #"*" returns tuple of each columns from table 
    cursor.execute("SELECT * FROM videos")

    #"cursor.fetchall" is used to return a list of result which is stored in cursor
    for row in cursor.fetchall():
            print(row)

def add_video(name,time):

    #"(?,?)" take the actual arguments from parameters variables ", (name ,time)"
    #"(Name, Time )" indicated in this column "?" take values and insert in it
    cursor.execute("INSERT INTO videos (Name, Time ) VALUES (?,?)", (name ,time))
    con.commit()

def update_video(uid,new_name,new_time):
    cursor.execute("UPDATE videos SET Name=? , Time=? WHERE ID=?", (new_name,new_time,uid))
    con.commit()

def delete_videos(uid):
    cursor.execute("DELETE FROM videos WHERE ID=?", (uid,))
    con.commit()

def main():
    while True:
        print("\nYOUTUBE MANAGER APP ")
        print("\n1. List all the videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit App")
        choise = int(input("\nEnter your choise: "))

        if choise == 1:
            print("\n")
            print("*"*70)
            list_all_videos()
            print("*"*70)

        elif choise == 2:
            name = input("\nEnter a video name: ")
            time = input("Enter a duration of video: ")
            add_video(name,time)
            print("\nVIDEO ADDED SUCCESSFULLY!")

        elif choise == 3:
            uid = int(input("\nEnter video ID which you wanna update: "))
            new_name = input("Enter a new name: ")
            new_time = input("Enter new duration of time: ")
            update_video(uid,new_name,new_time)
            print("\nVIDEO UPDATED SUCCESSFULLY!")

        elif choise == 4:
            uid = int(input("\nEnter video ID which you wanna update: "))
            delete_videos(uid)
            print("\nVIDEO DELETED SUCCESSFULLY!")
        
        elif choise == 5:
            break
        else:
            print("\nINVALID OPTION SELECTED!")
    
    con.close()

if __name__ == "__main__":
    main()