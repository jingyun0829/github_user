import json
import pandas
import os


if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

## new data frame
dataset = pandas.DataFrame()

json_file_name = "json_files/erinata.json"


# Open the token file and read its content
#with open("json_file_name", "r") as f:
#    json_data = f.read().strip()  # strip() is used to remove any trailing newline or spaces


# Open the token file and read its content
f = open(json_file_name, "r") 
json_data = json.load(f)
f.close()


#print(json_data)

## write into csv file
gh_id = json_data['login']
gh_number_id = json_data['id']
#plan_name = json_data['plan']['name']
updated_at = json_data['updated_at']

print(gh_id)
print(gh_number_id)
#print(plan_name)
print(updated_at)