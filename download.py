import wget, os

print('Beginning file download with wget module')
location = os.getcwd()
no = 1
name = 'test1Gb.db'
url = 'http://speedtest.ftp.otenet.gr/files/test1Gb.db'


print("\nThe file is downloading in "+location)
while no:
    print(f"\n=====>  Downloading file number {no}  <=====\n")
    wget.download(url, location)
    print(f"\ndownload number {no} completed. Now deleting \n")
    path = os.path.join(location, name)
    os.remove(path)
    print(f"\n=====>  Deleted file number {no} successfully  <=====\n")
    no+=1
