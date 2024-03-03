import pymongo
from bson import ObjectId

client=pymongo.MongoClient("mongodb+srv://username:<password>@cluster0.qghrrwr.mongodb.net/",tlsAllowInvalidCertificates=True)
print(client)
# not a good idea to include id and password in code files
# tlsAllowInvalidCertificates=True ---> not a good way to handle ssl
db=client["ytmanager"]
video_collection=db["videos"]
# print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"Id :{video['_id']}, Name :{video['name']} and Time :{video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {'$set':{"name":new_name,"time":new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube manager App")
        print("1.List all videos")
        print("2.Add new videos")
        print("3.Update new videos")
        print("4.Delete new videos")
        print("5.Exit the app")
        choice=input("Enter your choice :- ")

        if choice =='1':
            list_videos()
        elif choice =='2':
            name=input('Enter the video name :-')
            time=input('Enter the duration of vedio :-')
            add_video(name,time)
        elif choice =='3':
            video_id=input('Enter the video id to update :-')
            name=input('Enter the updated video name :-')
            time=input('Enter the duration of updated vedio :-')
            update_video(video_id,name,time)
        elif choice =='4':
            video_id=input('Enter the video id to delete :-')
            delete_video(video_id)
        elif choice =='5':
            break
        else:
            print("Invalid syntax")

if __name__== "__main__":
    main()