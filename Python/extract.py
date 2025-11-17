import pyzipper

zip_path = r"C:\Users\PRINCE\Downloads\Personal Attendance Marker started from 05_11_2024.zip"
extract_to = r"C:\Users\PRINCE\Downloads\Personal Attendance Marker started from 05_11_2024"
password = b"82504"   # password must be in bytes

with pyzipper.AESZipFile(zip_path, 'r') as zf:
    zf.pwd = password
    zf.extractall(path=extract_to)

print("Extraction complete!")
