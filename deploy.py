import os
import sys
IP = '192.168.133.38'
USERNAME = 'pi'
PORT = 1234
# Wifi - pibot: rasrobot

if '-r' in sys.argv:
    os.system(
        f'ssh -t {USERNAME}@{IP} "cd Robot ; python3 main.py {IP} {PORT}"')
elif '-s' in sys.argv:
    os.system(f'ssh {USERNAME}@{IP}')
else:
    print('Deploy')
    os.system(f'ssh -t {USERNAME}@{IP} "rm -r Robot"')
    print('Removed Old')
    os.system(f'scp -r Robot {USERNAME}@{IP}:/home/{USERNAME}')
    print('Deployed New')
