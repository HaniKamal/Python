import sys
import os
from pathlib import Path

from PIL import Image


folder_name = sys.argv[1]  # input('Please enter image file name --->')
new_folder = sys.argv[2]   # input('Please enter new file to save name --->')


MYDIR = (new_folder)
CHECK_FOLDER = os.path.isdir(MYDIR)

if not CHECK_FOLDER:
    os.makedirs(MYDIR)
    print("created folder : ", MYDIR)

else:
    print(MYDIR, "folder already exists.")

n = 0
for filename in os.listdir(folder_name):
    f = os.path.join(folder_name, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if f.endswith(".jpg"):
            n += 1
            new_name = (Path(f).stem)
            img = Image.open(f)
            new_img = img.save(f'{new_folder}{new_name}.png', 'png')

        else:
            continue

    else:
        continue
print(f'End of Proces, Total of {n} JPG files have converted')
