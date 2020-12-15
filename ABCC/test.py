x = "my name is format name"

if 'format' in x:
    print("inside format")
    variableName = []
    xArray = x.split()

    for i in range(len(xArray)-1):
        print("inside FOR")
        print(i)
#        if xArray[i] == format:
#            variableName.append(xArray[1])
        if xArray[i] == "format":
            variableName.append(xArray[i+1])
            xArray[i] = "{}"
            xArray.pop(i+1)
    
    result = '"' +' '.join(map(str, xArray)) + '"' +".format("+','.join(map(str, variableName))+")"
    # if endNone == True:
    #     result = '"' +' '.join(map(str, xArray)) + '"' +".format("+','.join(map(str, variableName))+")"+f", end={y}"
    # else:
    #     result = '"' +' '.join(map(str, xArray)) + '"' +".format("+','.join(map(str, variableName))+")"

    result = "print(" + result + ')'
    print(result)