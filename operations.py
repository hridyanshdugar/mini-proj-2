from pymongo import MongoClient

port_number = int(input("Enter the port number: "))
client = MongoClient("mongodb://localhost:"+str(port_number)+"/")
db = client["291db"]


def search_titles():
    pass


def search_genres():
    pass


def search_cast():
    global db
    # Get the cast member
    cast_name = input("Enter a name: ")

    # Query the collection for the details
    collection_name = db["name_basics"]
    collection_title_p = db["title_principals"]
    collection_title_b = db["title_basics"]

    query = {"primaryName": {"$regex": cast_name, "$options": "i"}}
    docs = collection_name.find(query)
    for doc in docs:
        print("*"*60)
        print("Name: "+ doc["primaryName"])
        print("nconst: "+ doc["nconst"])
        professions = doc["primaryProfession"]
        print("Professions: ")
        if professions is not None:
            for profession in professions:
                print(profession)
        else:
            print(professions)


        # Find the jobs and other details
        query = {"nconst":doc["nconst"]}
        job_char = collection_title_p.find(query,{"tconst":1,"job":1,"characters":1,"_id":0})
        print("-"*60)

        for jc in job_char:
            query = {"tconst":jc["tconst"]}
            titles = collection_title_b.find(query,{"primaryTitle":1,"_id":0})
            printed_flag = False
            for title in titles:
                if jc["job"] is not None or jc["characters"] is not None:
                    print("Primary Title: " + title["primaryTitle"])
                    print("Job: " + str(jc["job"]))
                    print("Characters: ")
                    if jc["characters"] is not None:
                        for character in jc["characters"]:
                            print(character)
                    else:
                        print(jc["characters"])
                    printed_flag = True

            if not printed_flag:
                print("No Movie Appearances")

            print("-"*60)
        print("*"*60)


def add_movie():
    pass


def add_cast():
    pass


search_cast()