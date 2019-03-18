#outFile = open('text.txt','w')
#outFile.write('test 1\n')
#outFile.close();

outFile= open('grades2.txt','w')
grade= 0
while (grade != 'q'):
    print("enter a grade(q to quit) :")
    grade = raw_input ()
#    outFile.write(grade + '\n')
    if (grade != 'q'):
            outFile.write(grade + '\n')
outFile.close();
