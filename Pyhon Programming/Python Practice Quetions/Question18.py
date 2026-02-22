
#You Are Given a list of subjects for students. Assume One Classroom is required for 1 subject. How many classrooms are needed by all students? 
#"python", "java", "python", "c++", "java", "python","c++", "javascript", "java", "c"

subjects = ["python", "java", "python", "c++", "java", "python","c++", "javascript", "java", "c"]
classrooms_needed = len(set(subjects))
print("Number of classrooms needed:", classrooms_needed)
