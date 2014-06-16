import plistlib
filename = "/Applications/Safari.app/Contents/Info.plist"
info = plistlib.readPlist(filename)
info["CFBundleGetInfoString"]

version =  info["CFBundleShortVersionString"]
print version

print info["CFBundleURLTypes"]

print info["CFBundleURLTypes"][0]

print info["CFBundleURLTypes"][0]["CFBundleURLSchemes"]

print info["CFBundleURLTypes"][0]["CFBundleURLSchemes"][0]


filename = "/Library/Preferences/com.apple.loginwindow.plist"
plistinfo = plistlib.readPlist(filename)
