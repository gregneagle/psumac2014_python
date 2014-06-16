student_ids = {"Bob": 12334546, "Sally": 23666, "Jane": 45678899}
student_ids["Jane"]

for key in student_ids:
    print student_ids[key]

for key in student_ids:
    print key, student_ids[key]


prefs = {"UseColor": False, "NumberOfCopies": 2, "HeaderText": "Property of me"}
print prefs["HeaderText"]