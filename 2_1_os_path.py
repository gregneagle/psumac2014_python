import os
PATH = "/Library/Preferences/com.apple.SoftwareUpdate.plist"
os.path.exists(PATH)

os.path.isdir(PATH)

os.path.dirname(PATH)

os.path.basename(PATH)


home = os.path.expanduser("~")
print home

prefs_dir = os.path.join(home, "Library/Preferences")
print prefs_dir

for filename in os.listdir(prefs_dir):
    print filename
