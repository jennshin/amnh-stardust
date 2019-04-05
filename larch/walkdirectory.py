
# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from
'''
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
'''

extList = ['.xrf', '.ini', '.dat']
def getDirFiles(folderPath):
    for dirName, subdirList, fileList in os.walk(folderPath):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            fileName,fileExt =  os.path.splitext(fname)
            if fileExt in extList:
                print(fileName)
                
            #print('\t%s' % fname)
    return(fileList)

currentPath = os.getcwd()
print('current directory:' ,currentPath)
folderlist = ['/Volumes/GoogleDrive/My Drive/_jshin/_nbcu/_apXW/_XRF/FullXRF_T152_FullMap1_001']



#folderPath = print(os.path.dirname( os.getcwd()))
#print(os.path.join((folderPath)))
#print(os.path.dirname(os.path.dirname(folderPath)))

os.chdir(os.path.dirname( os.getcwd()))
folderPath = os.getcwd()

subDir = [dI for dI in os.listdir(folderPath) if os.path.isdir(dI)]

#subDir = [dI for dI in os.listdir(folderPath) if os.path.isdir(os.path.join(folderPath,dI))]

print('new directory:' , os.getcwd())


#for i in folderlist:
    #for j in subdirList
        #if i == j:
for dirName, subdirList, fileList in os.walk(folderPath):
    #print(dirName)
    if dirName in folderlist:
        print(getDirFiles(dirName))


    #return(getDirFiles(dirName))
#        print(dirName) #, subdirList)
        
            #print(getDir(i))
    

def registerLarchPlugin():
    return ('walkdirectory', {'walkdirectory': walkdirectory})

'''
inputDir = input('enter directory')
if inputDir == '':
    filepath = os.getcwd()
else:
    filepath = inputDir

g = getDir(filepath)

'''

