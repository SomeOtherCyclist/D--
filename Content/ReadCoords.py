#Imports
import statistics as s

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

#Find index of nth occurrence in string
def findnth(instring,insubstring,nthtofind):
    runningindex = 0
    while (instring[0:runningindex+1].count(insubstring) <= nthtofind) & (instring[0:runningindex+1].count(insubstring) < len(instring)):
        runningindex += 1
    return(runningindex)

#List appending
for objline in obj:
    try:
        #World mode coordinates
        if mode == 1:
            if objline[0:2] == 'v ':
                vertexx.append(round(float(objline[findnth(objline,' ',0):findnth(objline,' ',1)+1]),4))
                vertexy.append(round(float(objline[findnth(objline,' ',1):findnth(objline,' ',2)+1]),4))
                vertexz.append(round(float(objline[findnth(objline,' ',2):]),4))
                
        #Face vertex indices
        if objline[0:2] == 'f ':
            for objfaceindex in range(objline.count(' ')):
                facevertices.append(int(objline[findnth(objline,' ',objfaceindex)+1:(objline[findnth(objline,' ',objfaceindex):]).find('/') + findnth(objline,' ',objfaceindex)]))
    except:
        pass

#Set up face mean lists
facemeanx = []
facemeany = []
facemeanz = []

#Face mean coordinates
for facevertex in range(0,int(len(facevertices)/3)-1):
        facemeanx.append(round(s.mean([vertexx[facevertices[3 * facevertex] - 1], vertexx[facevertices[1 + 3 * facevertex] - 1], vertexx[facevertices[2 + 3 * facevertex] - 1]]),4))
        #print(s.mean([vertexx[facevertices[3 * facevertex] - 1], vertexx[facevertices[1 + 3 * facevertex] - 1], vertexx[facevertices[2 + 3 * facevertex] - 1]]))

for facevertex in range(0,int(len(facevertices)/3)-1):
        facemeany.append(round(s.mean([vertexy[facevertices[3 * facevertex] - 1], vertexy[facevertices[1 + 3 * facevertex] - 1], vertexy[facevertices[2 + 3 * facevertex] - 1]]),4))
        #print(s.mean([vertexy[facevertices[3 * facevertex] - 1], vertexy[facevertices[1 + 3 * facevertex] - 1], vertexy[facevertices[2 + 3 * facevertex] - 1]]))

for facevertex in range(0,int(len(facevertices)/3)-1):
        facemeanz.append(round(s.mean([vertexz[facevertices[3 * facevertex] - 1], vertexz[facevertices[1 + 3 * facevertex] - 1], vertexz[facevertices[2 + 3 * facevertex] - 1]]),4))
        #print(s.mean([vertexz[facevertices[3 * facevertex] - 1], vertexz[facevertices[1 + 3 * facevertex] - 1], vertexz[facevertices[2 + 3 * facevertex] - 1]]))
            
#Set out A-A lists
vertexr = []
vertext = []
vertexa = []

#for n in range (1):
#    pass

#Open cartesian file
txtcartesian = open(__file__[0:__file__.rfind('\\')+1] + 'CoordinatesCartesian.txt', 'w')

#Write to cartesian file
txtcartesian.write(str(mode) + '\n')
txtcartesian.write(str(vertexx) + '\n')
txtcartesian.write(str(vertexy) + '\n')
txtcartesian.write(str(vertexz) + '\n')
txtcartesian.write(str(facevertices) + '\n')
txtcartesian.write(str(facemeanx) + '\n')
txtcartesian.write(str(facemeany) + '\n')
txtcartesian.write(str(facemeanz) + '\n')

#print('p=p_{ren}\left(\left[\right],\left[\right],\left[\right]\right)')