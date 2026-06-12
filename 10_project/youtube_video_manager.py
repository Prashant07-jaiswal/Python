#json is used deal with string datatypes 
import json

#this function is created for details of video in a form of list
def load_videos():

    #try/except block is used to handle exception if there is no file is found
    try:
        with open("youtube.txt", "r") as file:

            #json.load() is used to make a list/dict of strings objects from a saved file or JSON formated text
            return json.load(file) 
    except FileNotFoundError:
        return []
    
#this function is created to save the details of video after adding,updating,deleting 
def save_data(videos):
    with open("youtube.txt", "w") as file:

        #json.dump() is used to save or export data form list/dict to JSON formated text in a file
        json.dump(videos, file)
        return file 

def list_all_videos(videos):

    #enumerate() provides indexting to a elements in a list by making it a dict
    for index, value in enumerate(videos, start=1):

        #{value['name']} is written because value refer to subdict inside videos
        #we want to print Name which is key of subdict and Time which is value of subdict
        print(f"\n{index}: Name: {value["name"]} \n   Duration: {value['Time']}")

def add_video(videos):
    name = input("\nEnter name of the video: ")
    time = input("Enter duaration of the video: ")

    #.append() is used to add details in the list videos at the end
    #we used this format "{"name" : name, "Time" : time}" because append only accept 1 argument and we want to give 2
    videos.append({"name" : name, "Time" : time})
    save_data(videos)
    print("\nVIDEO IS ADDED SUCCESSFULLY!")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("\nEnter which video you wanna update: "))
    if 1<= index <=len(videos):
        new_name = input("\nEnter new name: ")
        new_time = input("Enter updated time: ")

        #used slicing to update
        #"index-1" is used because we take index acc. to enumerarte() and there indexing starts with 1 not 0
        videos[index-1] = {'name': new_name, 'Time': new_time}
        save_data(videos)
        print("\nVIDEO IS UPDATED SUCCESSFULLY!")
    else:
        print("\nInvalid option selected!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("\nEnter which video you wanna delete: "))
    if 1<= index <=len(videos):
        del videos[index-1] 
        save_data(videos)
        print("\nVIDEO IS DELETED SUCCESSFULLY!")
    else:
        print("\nInvalid option selected!")

def main():

    #we store JSON formatted text to list in videos variable 
    videos = load_videos()

    #while is used so that this script run in loop after end
    while True:
        print("\nYOUTUBE MANAGER | CHOOSE AN OPTION")
        print("1. List all the youtube videos")
        print("2. Add a youtube video")
        print("3. Update youtube video")
        print("4. Delete youtube video")
        print("5. Exit app")
        choise = input("\nEnter your choise: ")

        match choise:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("\nINVALID CHOISE SELECTED!")

#this is used because if this youtube_video_manager file imported to another file 
#the script of main function assigned to name of the file and it is easy to use in new file
if __name__ == "__main__":
    main()