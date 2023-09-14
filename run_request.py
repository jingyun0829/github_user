import requests
import json
import os
import pandas
import time

if not os.path.exists("json_files"):
    os.mkdir("json_files")

access_point = "https://api.github.com"

# Open the token file and read its content
with open("token", "r") as f:
    token = f.read().strip()  # strip() is used to remove any trailing newline or spaces

id_list = pandas.read_csv("seed.csv")
id_list = id_list['ghid']   

github_session = requests.Session()
github_session.auth = ("jingyun0829", token)







response_text = github_session.get(access_point + "/rate_limit").text
print(json.loads(response_text))

for user_id in id_list: 
	file_name = f"json_files/{user_id}.json"

	if os.path.exists(file_name):

		#pass
		print("File exists: ", user_id)
	else:
		
		#user_id = "erinata"
		print(user_id)
		response_text = github_session.get(f"{access_point}/users/{user_id}").text
		json_text = json.loads(response_text)

		
		with open(file_name, "w") as f:
		    json.dump(json_text, f)

		time.sleep(1)    
