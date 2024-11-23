class Team: 
    def __init__(self, id, name, school):
        self.id = f'Team{str(id).zfill(2)}'
        self.name = name
        self.school = school
    
    def __str__(self) -> str:
        return self.id + ' ' + self.name + ' ' + self.school

class Student: 
    def __init__(self, id, name, team): 
        self.id = f'C{str(id).zfill(3)}'
        self.name = name
        self.team = team
    
    def __str__(self) -> str:
        return self.id + ' ' + self.name + ' ' + self.team.name + ' ' + self.team.school

def main():
    lsTeam = [] 
    for index in range(int(input())):
        lsTeam.append(Team(index + 1, input(), input()))
    
    lsStudent = []
    for index in range(int(input())):
        lsStudent.append(Student(index + 1, input(), lsTeam[int(input()[4:]) - 1]))

    lsSS = sorted(lsStudent, key=lambda x: x.name) # List Student Sorted
    for stu in lsSS: 
        print(stu)

if __name__ == "__main__":
    main()