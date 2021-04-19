import wget, os

print('Beginning file download with wget module')
location = os.getcwd()
no = 1
name = '1GB.bin'
url = 'https://speed.hetzner.de/1GB.bin'


print("The file is downloading in "+location)
while no:
    print(f"Downloading file number {no}")
    wget.download(url, location)
    print(f"download number {no} completed. Now deleting")
    path = os.path.join(location, name)
    os.remove(path)
    print("Deleted successfully")
    no+=1