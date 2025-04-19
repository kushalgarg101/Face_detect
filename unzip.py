import zipfile

zip_file = "C:/Users/Kusha/OneDrive/Desktop/Faces/archive (2).zip"
extract_path = "C:/Users/Kusha/OneDrive/Desktop/Faces/data"

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("File unzipped successfully!") 