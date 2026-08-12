file_name = input("Enter file name: ")
file_name = file_name.strip().lower()

if file_name.endswith(".csv"):
    print("CSV file")
elif file_name.endswith(".json"):
    print("JSON file")
elif file_name.endswith(".parquet"):
    print("Parquet file")
else:
    print("Unsupported file type")
    