if __name__ == '__main__':
    def find_second_smallest_score(students):
        scores = sorted(set(student[1] for student in students))
        return scores[1]
        
    def find_student_names(second_smallest_score, students):
        return [student[0] for student in students if student[1] == second_smallest_score]
    
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # find the 2nd smallest score & store it in a var
    second_smallest_score = find_second_smallest_score(students)
    
    # search student/s with the 2nd smallest score & store their names in a list
    names = find_student_names(second_smallest_score, students)
    
    # sort the names list alphabetically & print the result
    names.sort()
    for name in names:
        print(name)
