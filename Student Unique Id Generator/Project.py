studentsEnrolled = []
studentsIds = []
idCount = {}

class Student():
    def __init__(self,name):
        self.name=name
        self.netid = self.generateNetid()
        self.addStudents()
        
    def generateNetid(self):    
        separatedName = self.name.split(" ")
        nid = separatedName[0][0].lower()+separatedName[1][0].lower()
        check = False
        
        if len(studentsIds) > 0:
            for i in studentsIds:
                if nid == i:
                    check=True
                    break

        if check == False:
            studentsIds.append(nid)
            idCount[nid]=1
        else:
            idCount[nid] =idCount[nid]+1
                

        nid=nid+str(idCount[nid])+"\n"
        return nid 

    def addStudents(self):
        studentsEnrolled.append(self.name.split("\n")[0]+","+str(self.netid))

names = open("NUSH-students.txt","r").readlines()
for name in names:
    s=Student(name)

f= open("output.txt","w")
for student in studentsEnrolled:
    f.write(student)