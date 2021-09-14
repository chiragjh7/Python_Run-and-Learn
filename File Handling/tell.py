f=open("sample.txt","r")
print(f.read()) # reads the file
print(f.tell()) # the file is read thus the file pointer
                # is now at the end of the contents
                # in the file
f.close()