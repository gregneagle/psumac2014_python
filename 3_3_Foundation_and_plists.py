# https://developer.apple.com/library/mac/documentation/cocoa/conceptual/PropertyLists/Introduction/Introduction.html

from Foundation import NSData
from Foundation import NSPropertyListSerialization
from Foundation import NSPropertyListMutableContainersAndLeaves

filename = "/Library/Preferences/com.apple.loginwindow.plist"
plist_data = NSData.dataWithContentsOfFile_(filename)
(dataObject, plistFormat, error) = (
    NSPropertyListSerialization.propertyListWithData_options_format_error_(
        plist_data, NSPropertyListMutableContainersAndLeaves, None, None))

print dataObject


