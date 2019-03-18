import sys

sys.stdout.write('hello')

#sys.stdout=open('out.dat','a')
#print ('goodbye')
#exit()

textfile=open('out1.dat','a')
#print >> textfile,'hjello'

print('hello',end="",file=textfile)
print('test')
exit()
