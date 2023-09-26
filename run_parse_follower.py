import pandas as pd
import os
import glob
import json

dataset = pd.DataFrame()


# Check if there are any .json files in the directory
json_files = glob.glob("follower_json_files/*.json")
if not json_files:
    print("No JSON files found in 'follower_json_files' directory.")

for json_file_name in json_files:
    try:
        # Open the JSON file and read its content
        with open(json_file_name, "r") as f:
            json_data = json.load(f)
        
        if not json_data:
            print(f"Empty or invalid data in {json_file_name}.")
            continue
        
        for user_info in json_data:
            if 'login' in user_info:
                gh_id = user_info['login']
                row = pd.DataFrame.from_records([{'gh_id': gh_id}])
                dataset = pd.concat([dataset, row])
            else:
                print(f"Login key not found in data from {json_file_name}.")
                
    except Exception as e:
        print(f"Error processing {json_file_name}: {e}")

if dataset.empty:
    print("No data to write to seed2.csv.")
else:
    dataset.to_csv("input_files/seed2.csv", index=False)
    print("Data saved to seed2.csv.")
