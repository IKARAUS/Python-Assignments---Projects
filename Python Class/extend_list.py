#appened = if we want to add elements im existing list
#extend = we can add more than one element in existing list at a one time

subject_list = ["python", "java", " php"]

subject_list2 = [12, 23, 5]

marks = [101,102,104]
subject_list2.extend([marks, subject_list])

print(subject_list2)