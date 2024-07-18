#symmetric differrence
morning = ['java','c','ruby','lisp','c#']
afternoon = ['python','c#','java','c','ruby']

possible_courses = set(morning) ^ set(afternoon)
print(possible_courses)
