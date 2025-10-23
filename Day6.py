attendence = [18,20,19,15,21]
total_attendance = 0
total_count = 0


for the_students in attendence:
    if the_students >= 20:
        total_count += 1
        print("full")
    else:
        print("not full") 



print("total_count:", total_count)

total_attendance = sum(attendence)
print("total_attendance:", total_attendance)
