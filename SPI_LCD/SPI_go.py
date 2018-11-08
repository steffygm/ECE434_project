import sys, os

print('Turning on LCD')
os.system('sudo ./on_180.sh')
os.system('sleep 5')
print('Placing Tux on LCD')
os.system('./text.sh')
os.system('sleep 1')
os.system('./text_2.sh')
os.system('sleep 5')
print('Turning off LCD')
os.system('./off.sh')
