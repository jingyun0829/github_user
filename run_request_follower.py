import requests
import json
import os
import pandas
import time

if not os.path.exists("follower_json_files"):
    os.mkdir("follower_json_files")

access_point = "https://api.github.com"

# Open the token file and read its content
with open("token", "r") as f:
    token = f.read().strip()  # strip() is used to remove any trailing newline or spaces

followers_url_list = pandas.read_csv("parsed_files/github_user_data.csv")
followers_url_list = followers_url_list['followers_url']

github_session = requests.Session()
github_session.auth = ("jingyun0829", token)

response_text = github_session.get(access_point + "/rate_limit").text
print(json.loads(response_text))

for followers_url in followers_url_list:
    user_id = followers_url.split("/")[-2]
    print(user_id)
    file_name = f"follower_json_files/{user_id}.json"


    if os.path.exists(file_name):
        print("File exists: ", user_id)
    else:
        try:
            print(user_id)
            response_text = github_session.get(followers_url).text
            json_text = json.loads(response_text)

            # some tmp file and st
            with open(file_name + ".tmp", "w") as f:
                json.dump(json_text, f)

            os.rename(file_name + ".tmp", file_name)    
        except Exception as e:  # all the exceptions, do not stop the program do whatever inside the code
            print(e)

    time.sleep(1)
