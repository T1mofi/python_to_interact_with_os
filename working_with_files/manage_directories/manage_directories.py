import os

print(os.getcwd())
print(os.listdir(os.getcwd()))

dir_name = 'tima\'s novel'

os.mkdir(dir_name)
print(os.listdir(os.getcwd()))

for name in os.listdir(os.getcwd()):
    fullname = os.path.join(os.getcwd(), name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))


os.chdir(dir_name)
print(os.getcwd())

os.chdir(os.path.pardir)
print(os.getcwd())

os.rmdir(dir_name)
print(os.listdir(os.getcwd()))
