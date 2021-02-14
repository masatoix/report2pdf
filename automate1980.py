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
    pg.hotkey('command', 'p', interval=0.25)
    time.sleep(1)

    # Document mergin change to narrow
    pg.click(1192, 522, 1)
    pg.click(1189, 497, 1)
    time.sleep(1)


    # Open custom settings
    pg.click(1192, 522, 1)
    pg.click(1138, 560, 1)
    time.sleep(1)

    # Select "Mergin setting"
    pg.click(915, 211, 1)
    time.sleep(0.5)

    # Check vertical, holizontal
    pg.click(786, 554)
    pg.click(786, 576)
    pg.hotkey('return')
    time.sleep(0.5)

    # Change document layout to landscape
    pg.click(1157, 554, 1)
    pg.click(1157, 578, 1)
    time.sleep(0.5)

    # Change document exp and shrink setting
    pg.click(1081, 581)
    time.sleep(0.5)

    # Export to PDF
    pg.click(944, 684, 1)
    pg.click(944, 732, 1)
    time.sleep(2)


    # Save PDF to same folder
    pg.click(675, 505, 1)
    time.sleep(1)
    pg.hotkey('return')
    time.sleep(1)

    # Close xlsx file
    pg.hotkey('command', 'w')
    pg.hotkey('command', 'd', interval=0.25)
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
    ALL REPORTS have been GERATED as PDF!
    """
)
#%%
# pg.position()

#%%
# pg.size()
# %%
