#%%
import pyautogui as pg
import time
import os
import glob
import subprocess
import sys

pg.FAILSAFE = True
exported_files = '/Users/masatoi/Google ドライブ/Python/FUSiON_Report/exported_files/'
generated_pdfs = '/Users/masatoi/Google ドライブ/Python/FUSiON_Report/generated_pdfs/'

#%%

def folder_open():
    # Folder open
    subprocess.Popen(['open', exported_files])
    time.sleep(4)

def generate_pdf():
    # To create PDF file, change some settings
    time.sleep(4)
    pg.hotkey('command', 'p')
    time.sleep(1)

    # Document mergin change to narrow
    pg.click(1000, 515, 1)
    pg.click(1000, 482, 1)
    time.sleep(1)


    # Open custom settings
    pg.click(1000, 515, 1)
    pg.click(1000, 550, 1)
    time.sleep(1)

    # Select "Mergin setting"
    pg.click(795, 203, 1)
    time.sleep(0.5)

    # Check vertical, holizontal
    pg.click(660, 548)
    pg.click(667, 570)
    pg.hotkey('return')
    time.sleep(0.5)

    # Change document layout to landscape
    pg.click(1000, 546, 1)
    pg.click(1000, 570, 1)
    time.sleep(0.5)

    # Change document exp and shrink setting
    pg.click(956, 572)
    time.sleep(0.5)

    # Export to PDF
    pg.click(827, 675, 1)
    pg.click(827, 726, 1)
    time.sleep(2)


    # Save PDF to same folder
    pg.click(557, 495, 1)
    time.sleep(1)
    pg.hotkey('return')
    time.sleep(1)

    # Close xlsx file
    pg.hotkey('command', 'w')
    time.sleep(1)
    pg.hotkey('command', 'd')
    time.sleep(1)

#%%
pdfs = os.listdir(generated_pdfs)
print(pdfs)
if len(pdfs) >= 2:
    sys.exit('Any file exists. Please DELETE it!')
else:
    folder_open()

    # First file and Select top of file and open the file
    # pg.hotkey('option', 'up')
    pg.hotkey('option', 'up')
    time.sleep(1)
    pg.hotkey('command', 'down')
    time.sleep(3)
    generate_pdf()
#%%
num = len(os.listdir(exported_files))
num -= 2
#%%
for i in range(num):
    folder_open()
    time.sleep(2)
    pg.hotkey('down')
    pg.hotkey('command', 'down')
    generate_pdf()
#%%
print(
    """
    Conguratulations!
    ALL REPORT has been GERATED as PDF!
    """
)
#%%
# pg.position()

#%%
# pg.size()