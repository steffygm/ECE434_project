import sys, os

print('Turning on LCD')
os.system('sudo ./on_180.sh')
os.system('sleep 5')
print('30 seconds countdown')
filename = '.jpg'
scriptcall = './image 0.jpg'
for t in range(1,31):
    filename = str(31-t)+'.jpg'
    print(filename)
    scriptcall = './image.sh '+ '../countdown_pictures/filename'
    os.system(scriptcall)
    os.system('sleep 1')
print('Turning off LCD')
os.system('./off.sh')
