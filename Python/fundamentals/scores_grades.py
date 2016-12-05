def scoresGrades():
    print "Scores and Grades"
    for num in range(10):
        score = int(raw_input())
        if (score >= 90):
            grade = "A"
        elif (score >= 80):
            grade = "B"
        elif (score >= 70):
            grade = "C"
        elif (score >= 60):
            grade = "D"
        else:
            grade = "FAIL"
        print "Score: " + str(score) + "; Your grade is a" + grade
    print "End of the program. Bye!"

scoresGrades()
