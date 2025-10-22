frontend ={"bibin" ,"sreekuttan", "anu","gokul"}
backend = {"joyal", "gokul", "abin","sreekuttan"}

backend.add("arun")
frontend.remove("anu")

print(frontend)
print(backend)

both_courses = frontend.intersection(backend)
print("students entrolled in both courses:",both_courses)

only_backend = backend.difference(frontend)
print("Students only in Backend:", only_backend)


unique_students = frontend.union(backend)
print("Total number of unique students:", len(unique_students))
print("Unique students list:", unique_students)


courses = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

print("\nNumber of students in each course:")
for course, count in courses.items():
    print(f"{course}: {count}")
