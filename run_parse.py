import json
import pandas
import os
import glob


if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

## new data frame
dataset = pandas.DataFrame()

for json_file_name in glob.glob("json_files/*.json"):

	#json_file_name = "json_files/dAAAb.json"



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
	followers_url = json_data['followers_url']

	print(gh_id)
	print(gh_number_id)
	#print(plan_name)
	print(updated_at)
	print(followers_url)


	row =pandas.DataFrame.from_records(
		[
		{
			'gh_id': gh_id,
			'gh_number_id' : gh_number_id,
			'updated_at': updated_at,
			'followers_url': followers_url
		}
		]

		)

	print(row)
	dataset = pandas.concat([dataset,row])

dataset.to_csv("parsed_files/github_user_data.csv", 
	            index=False)

