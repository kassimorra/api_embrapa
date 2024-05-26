import csv
import os

# def verify_path(filename: str):
#     if not os.path.exists(filename):
#         os.makedirs(filename)
#         print(f"Folder '{filename}' created successfully.")
#     else:
#         print(f"Folder '{filename}' already exists.")

def write_csv(file_name: str, list_output: list[list[str]]) -> bool:
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')        
        writer.writerows(list_output)
    print(f"Data has been written to {file_name}")
    return True