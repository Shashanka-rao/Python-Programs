usn = '4SF20CS124'
if usn[:4] == "4SF2" and usn[5:7] == "CS":
    rollnum = usn[-2:]
    submitAssignmentTo = usn[:-3] + "0"
    submitAssignmentTo += "01" if not int(rollnum[0]) else str(int(rollnum) // 10) + "0"
    print(usn, " - Submit Assignment to : ", submitAssignmentTo)
else:
    print("Submit to Vikas. M")