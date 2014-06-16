# https://developer.apple.com/library/mac/documentation/CoreFoundation/Reference/CFPreferencesUtils/Reference/reference.html

import CoreFoundation
print CoreFoundation.CFPreferencesCopyAppValue("HomePage", "com.apple.Safari")

new_home = "http://disneyanimation.com"
CoreFoundation.CFPreferencesSetAppValue("HomePage", new_home, "com.apple.Safari")

print CoreFoundation.CFPreferencesCopyAppValue("HomePage", "com.apple.Safari")


my_policy = {
    "com.macromedia.Flash Player.plugin": {
        "PlugInDisallowPromptBeforeUseDialog": True,
        "PlugInFirstVisitPolicy": "PlugInPolicyAllowWithSecurityRestrictions",
    },
}

CoreFoundation.CFPreferencesSetAppValue("ManagedPlugInPolicies", my_policy,  "com.apple.Safari")