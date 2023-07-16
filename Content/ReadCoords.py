#Mode selection
print('Select mode:')
modestr = input()

mode = 0

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
    
    if inputobj[1] == ':':
        objstr = inputobj
    else:
        objstr = __file__[0:__file__.rfind('\\')+1] + inputobj

    try:
        objname = open(objstr, 'r')
        obj = objname.readlines()
        return(obj)
    except:
        print ('Failed to open file')
        return(None)

obj = tryopen()

while obj == None:
    obj = tryopen()
    
print(obj)

"""
#Parsing
#World Mode
if mode == 1:
    print('world')
"""