
import operator
def readStudentDetails():
    print() #j adding a blank line
    print('enter number of students:')
    numberOfStudents=int(input())
    studentRecord={}
    for student in range(0,numberOfStudents):
        print('enter the name of student:')
        name=input()
        print('enter the marks of Student:')
        marks=int(input())
        studentRecord[name]=marks
    return studentRecord



def rankStudents(studentRecord):
    sortedStudentRecord= sorted(studentRecord.items(), key=operator.itemgetter(1), reverse=True) #conveting dictaionary into list of tupples
    print(sortedStudentRecord)
    print("{} has scored first place, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1])) #first zero is the first record and rhe seocnd zero is first value in that record which is the name mark
    print('{} has scored second place, scoring {} marks'.format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
    print('{} has scored third place, scoring {} marks'.format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
    print()
    return sortedStudentRecord

def rewardStudents(sortedStudentRecord, reward):
    print('{} has received ${}'.format(sortedStudentRecord[0][0], reward[0]))  #fist two zeroes is where the name is stored like in the table
    print('{} has received ${}'.format(sortedStudentRecord[1][0], reward[1]))
    print('{} has received ${}'.format(sortedStudentRecord[2][0], reward[2]))
    print()

def appreciateStudents(sortedStudentRecord):
    for record in sortedStudentRecord:
        if record[1]>=950:
            print('congrats on storing {} marks, {}'.format(record[1], record[0])) #marks of student are at index psotion one and name is at index psotion zero
        else:
            break
    print()

studentRecord=readStudentDetails()
sortedStudentRecord= rankStudents(studentRecord) # when you return4 sortedStudentRecord it needs to be stored somewhere
reward= (500,300,100) #tupple
rewardStudents(sortedStudentRecord, reward) #sortedStudentRecord is part of out rankStudents so we have to return it there
appreciateStudents(sortedStudentRecord)
