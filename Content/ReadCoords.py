print('abc'[0])
#Mode selection
print('Select mode:')
modestr = input()

#Set int mode
if modestr == 'world':
    mode = 1
if modestr == 'static':
    mode = 2

#Print selected mode
print('Selected Mode: ' + modestr + ' (' + str(mode) + ')')

#MAKE SURE I HANDLE MODE 0 ISSUE



#Input model selection
def tryopen():
    print('Select File:')
    inputobj = input()
    
    if inputobj[0:1] == __file__[0:1]:
        objstr = inputobj
    else:
        objstr = __file__[0:__file__.rfind('\\')+1] + inputobj

    try:
        obj = open(objstr, 'r')
        return(obj)
    except:
        print ('Failed to open file')
        return(None)

obj = tryopen()

while obj == None:
    obj = tryopen()



#Set out lists
vertexx = None
vertexy = None
vertexz  = None
facevertices = None
facemean = None

#
def findnth(instring,insubstring,index):
    
    
    return()

#
if mode == 1:
    for objline in obj:
        try:
            if (objline[0] == 'v') & (objline[1] == ' '):
                print()
        except:
            pass
        
    






"""
#Parsing
#World Mode
if mode == 1:
    print('world')
"""

#use find() method for the first occurrence of something