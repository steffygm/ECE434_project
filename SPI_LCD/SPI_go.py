import sys, os

print('Turning on LCD')
os.system('sudo ./on_180.sh')
os.system('sleep 5')
print('Placing Tux on LCD')
os.system('sudo fbi -noverbose -T 1 -a tux.png')
os.system('sleep 10')
print('Turning off LCD')
os.system('./off.sh')
