#THIS CODE IS A SOLUTION OF ONE OF THE LABS IN THE PCAP STUDY RESOURCES.
#The problem goes as follows:
#Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name,
#the student's last name, and the number of point the student received during certain classes.

#The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

#The file may look as follows:

#John	Smith	5
#Anna	Boleyn	4.5
#John	Smith	2
#Anna	Boleyn	11
#Andrew	Cox	1.5

#Your task is to write a program which:

#·asks the user for Prof. Jekyll's file name.
#·reads the file contents and counts the sum of the received points for each student.
#·prints a simple (but sorted) report.


import os#We are importing the os module.
def grades(file_name: str):#Here we have our main function.
    diccionario = {}#We are going to make use of this dictionary to store the name of students and their points.
    #We are using the try, except statement to handle some errors. 
    try:
        archive = open(file_name, "r")#Wer open the archive in read mode.
        for line in archive:#We iterate through each line of the file.
            line = line.split()#We make use of the split method to make a list of the line content.
            if len(line) != 3:#If the lenght of the line is different than three we print something descriptive an we exit the code.
                print(f"Bad line in archive {file_name}")
                exit()
            alumno = " ".join(line[:2])#We join the first element(name) and the second element(last name) with a space in between.
            if alumno not in diccionario:#If the student is not in the dictionary we need to create the key with the name and last name and set the value points 
#to zero. Otherwie if we try to update the value of a non existing key we will get an error.
                diccionario[alumno] = 0
            diccionario[alumno] += float(line[2])#We update the value.
        for students in sorted(diccionario.keys()):#To print the students full name and points sorted by the full name.
            print(f"\n\033[1;32;40m{students} {diccionario[students]}\033[0m")#We use the ANSI color code to make our output more fun.
        archive.close()#We close the stream that make the interaction with the file possible.
    except IOError as e:
        print(f"\033[1;31;40mI/O Error occurred: {os.strerror(e.errno)}\033[0m")#errno is a property of the class exception IOError. Is a number, so we can get
#the string description making use of the strerror function that comes with the os module.
        exit()

if __name__ == '__main__':
    file_name = "path_to_file_here"
#Here we can use ba$h/powershell/cmd to locate the path of the file. Maybe we will have some
#problems if there exists differents files with the same name.
#On the other hand we can use the os module to find the path.
    grades(file_name)
