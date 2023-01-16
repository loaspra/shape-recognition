import pandas as pd
import os


data_path = os.getcwd() + "/data/raw"

# Scan the directory data_path and select only the directories
dicc = {"file_path" : [], "label": []}


for path in os.scandir(data_path):
    if path.is_dir():
        # Scan the directory and select only the files
        for file in os.scandir(path):
            dicc["file_path"].append(file.path)
            dicc["label"].append(path.name)

# Create a dataframe with the dictionary
df = pd.DataFrame(dicc)

# save the dataframe as a csv file in the data/processed directory
df.to_csv(os.getcwd().replace('\\', '/') + "/data/processed/data.csv", index=False)