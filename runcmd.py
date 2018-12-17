import os
print("This Program will delete the 2.0 folder")
cmd='rd /s /q "%localappdata%/apps/2.0"'
os.system(cmd)
print("Done!")
