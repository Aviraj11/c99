import os
import shutil
import time

path = "/PATH_TO_DELETE"
days = 30
seconds = time.time() - (days*24*60*60)

if (os.path.exists(path)):
    files = os.walk(path)
    for file in files:
        os.path.join()
else:
    print("File Not Found")

ctime = os.stat(path).st_ctime
if (ctime >= seconds):
    os.remove(path)
else:
    shutil.rmtree()