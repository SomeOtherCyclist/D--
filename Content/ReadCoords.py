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
vertexx = []
vertexy = []
vertexz  = []
facevertices = []
facemean = []

#Find index of nth occurrence in string
def findnth(instring,insubstring,nthtofind):
    runningindex = 0
    while (instring[0:runningindex+1].count(insubstring) <= nthtofind) & (instring[0:runningindex+1].count(insubstring) < len(instring)):
        runningindex += 1
    return(runningindex)

#world mode appending
if mode == 1:
    for objline in obj:
        try:
            if objline[0:2] == 'v ':
                vertexx.append(float(objline[findnth(objline,' ',0):findnth(objline,' ',1)+1]))
                vertexy.append(float(objline[findnth(objline,' ',1):findnth(objline,' ',2)+1]))
                vertexz.append(float(objline[findnth(objline,' ',2):]))
            if objline[0:2] == 'f ':
                for objfaceindex in range(objline.count(' ')):
                    facevertices.append(int(objline))
        except:
            pass

[findnth(objline,' ',objfaceindex):(objline[findnth(objline,' ',objfaceindex):]).find('\\')]

findnth(objline,' ',objfaceindex)




#Open cartesian file
txtcartesion = open(__file__[0:__file__.rfind('\\')+1] + 'CoordinatesCartesian.txt', 'w')

#Write to cartesian file
txtcartesion.write(str(vertexx) + '\n')
txtcartesion.write(str(vertexy) + '\n')
txtcartesion.write(str(vertexz) + '\n')
txtcartesion.write(str(facevertices))

print(facevertices)