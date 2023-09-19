import json
import pandas
import os


if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

## new data frame
dataset = pandas.DataFrame()

json_file_name = "json_files/dAAAb.json"


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


row =pandas.DataFrame.from_records(
	[
	{
		'gh_id': gh_id,
		'gh_number_id' : gh_number_id,
		'updated_at': updated_at
	}
	]

	)

print(row)
dataset = pandas.concat([dataset,row])

dataset.to_csv("parsed_files/github_user_data.csv", 
	            index=False)