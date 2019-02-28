def returnFirstLine(fileName):
    f1 = open(fileName)
    return f1.readline()
def trim_strings(string1, string2):
    string1=string1.replace("preconfigure ","")
    string2=string2.replace("preconfigure ","")
    return(string1,string2)
def check_showrun_output(string1,string2,flag):
    string1=str(string1)
    string2=str(string2)
    flag=0
    if "No such configuration item(s)" in string1:
        string2 = string2.replace("interface","interface preconfigure")
        flag=1
    if "Invalid input detected" in string1:
        string2 = string2.replace("interface preconfigure","interface")
        flag=1
    return (string2,flag)
def select_stdout(string1,string2):
    if "No such configuration item(s)" in string1 or "Invalid input detected" in string1:
        return string2
    return string1
def compare_file_by_lines(f1_name,f2_name,ToBeDeleted="preconfigure "):
    f1 = open(f1_name,'rU')
    f2 = open(f2_name,'rU')
    flag=0
    f1_content = f1.readlines()
    f1_content=str(f1_content)
    f1_content=f1_content.replace(ToBeDeleted,"")
    f1_content=eval(f1_content)
    f1_content=[x.replace(' ','') for x in f1_content]
    f1_content=[x.replace('\n','') for x in f1_content]
    #f1_content=[x.rstrip(' ') for x in f1_content]
    f2_line=f2.readline()
    f2_line=f2_line.replace(ToBeDeleted,"")
    f2_line=f2_line.replace(' ','')
    f2_line=f2_line.replace('\n','')
    f2_line_original=f2_line
    #f2_line=f2_line.rstrip(' ')
    while f2_line_original != '' :
        if f2_line not in f1_content:
            flag=1
            return (flag, f2_line,f1_content)
        f2_line=f2.readline()
        f2_line_original=f2_line
        f2_line=f2_line.replace(ToBeDeleted,"")
        f2_line=f2_line.replace(' ',"")
        f2_line=f2_line.replace('\n','')
    return flag
def compare_file_by_lines_not_contain(f1_name,f2_name):
    f1 = open(f1_name,'rU')
    f2 = open(f2_name,'rU')
    flag=0
    f1_content = f1.readlines()
    f1_content=str(f1_content)
    f1_content=f1_content.replace("preconfigure ","")
    f1_content=eval(f1_content)
    f1_content=[x.replace(' ','') for x in f1_content]
    f1_content=[x.replace('\n','') for x in f1_content]
    #f1_content=[x.rstrip(' ') for x in f1_content]
    f2_line=f2.readline()
    f2_line=f2_line.replace("preconfigure ","")
    f2_line=f2_line.replace(' ','')
    f2_line=f2_line.replace('\n','')
    f2_line_original=f2_line
    #f2_line=f2_line.rstrip(' ')
    while f2_line_original != '' :
        if f2_line in f1_content:
            flag=1
            return (flag, f2_line,f1_content)
        f2_line=f2.readline()
        f2_line_original=f2_line
        f2_line=f2_line.replace("preconfigure ","")
        f2_line=f2_line.replace(' ',"")
        f2_line=f2_line.replace('\n','')
    return flag
def compare_file_by_lines_not_contain_v2(f1_name,f2_name,ToBeDeleted=["preconfigure "]):
    f1 = open(f1_name,'rU')
    f2 = open(f2_name,'rU')
    f1_content_updated = list()
    flag=0
    f1_content = f1.readlines()
    for element1 in f1_content:
        for element2 in  ToBeDeleted:
            element1=element1.replace(element2,"")
        element1=element1.replace(' ',"")
        element1=element1.replace('\n', "")
        f1_content_updated.append(element1)
    f2_line=f2.readline()
    for element in  ToBeDeleted:
        f2_line=f2_line.replace(element,"")
    f2_line=f2_line.replace(' ','')
    f2_line=f2_line.replace('\n','')
    f2_line_original=f2_line
    while f2_line_original != '' :
        if f2_line != '' :
            if f2_line in f1_content_updated:
                flag=1
                return (flag, f2_line, f1_content_updated)
        f2_line=f2.readline()
        f2_line_original=f2_line
        for element in ToBeDeleted:
            f2_line = f2_line.replace(element, "")
        f2_line=f2_line.replace(' ',"")
        f2_line=f2_line.replace('\n','')
    return str(flag)
def delete_lines_from_file(fileName,lineNumber):
    lineNumber=int(lineNumber)
    f = open(fileName,"r+b")
    f_content = f.readlines()
    line=1
    f.seek(0)
    for i in f_content:
        if line != lineNumber:
            f.write(i)
        line=line+1
    f.truncate()
    f.close()
def setDefaultValueRobot(input,defaultValue):
    if input=='':
        input=list()
	for element in defaultValue :
          input.append(element)
    return input
def compare_file_by_lines_v2(f1_name,f2_name,ToBeDeleted=["preconfigure "]):
    f1 = open(f1_name,'rU')
    f2 = open(f2_name,'rU')
    f1_content_updated = list()
    flag=0
    f1_content = f1.readlines()
    for element1 in f1_content:
        for element2 in  ToBeDeleted:
            element1=element1.replace(element2,"")
        element1=element1.replace(' ',"")
        element1=element1.replace('\n', "")
        f1_content_updated.append(element1)
    f2_line=f2.readline()
    f2_line_original=f2_line
    for element in  ToBeDeleted:
        f2_line=f2_line.replace(element,"")
    f2_line=f2_line.replace(' ','')
    f2_line=f2_line.replace('\n','')
    while f2_line_original != '' :
        if f2_line != '':
            if f2_line not in f1_content_updated:
                flag=1
                return (flag, f2_line, f1_content_updated,ToBeDeleted)
        f2_line=f2.readline()
        f2_line_original=f2_line
        for element in ToBeDeleted:
            f2_line = f2_line.replace(element, "")
        f2_line=f2_line.replace(' ',"")
        f2_line=f2_line.replace('\n','')
    return str(flag)
def getIDRDNCore(inputFile,valueName):
    # for getting tunnel id and bundle id
    f = open(inputFile, 'rU')
    f_content = f.read()
    f_content = f_content.replace(' ','')
    index_number = f_content.index(valueName)
    l=len(valueName)
    id=str(f_content[index_number+l])
    i=1
    while f_content[index_number+l+i].isdigit():
        id=id+str(f_content[index_number+l+i])
        i=i+1
    return id
def getIDFromDryrunOutput(inputFile,valueName):
    f = open(inputFile, 'rU')
    f_content = f.read()
    f_content = f_content.replace(' ','')
    index_number = f_content.index(valueName)
    l=len(valueName)
    id=str(f_content[index_number+l])
    i=1
    while f_content[index_number+l+i].isdigit():
        id=id+str(f_content[index_number+l+i])
        i=i+1
    f.close()
    return id
def compareFile(fileName2, fileName, originalValue, replacedValue,ToBeDeleted=[]):
    if len(originalValue) != len(replacedValue):
        return False
    with open(fileName) as f_read:
        oldText=f_read.read()
    for i in range (0, len(originalValue)):
        with open(fileName) as f_read:
            newText=f_read.read().replace(str(originalValue[i]), str(replacedValue[i]))
        with open(fileName, "w") as f_write:
            f_write.write(newText)
    flag = compare_file_by_lines_v2(fileName2, fileName, ToBeDeleted)
    with open(fileName, "w") as f_write:
        f_write.write(oldText)
    f_read.close()
    f_write.close()
    return  str(flag)
def compareFile_reverse(fileName2, fileName, originalValue, replacedValue,ToBeDeleted=[]):
    if len(originalValue) != len(replacedValue):
        return False
    with open(fileName2) as f_read:
        oldText=f_read.read()
    for i in range (0, len(originalValue)):
        with open(fileName2) as f_read:
            newText=f_read.read().replace(str(originalValue[i]), str(replacedValue[i]))
        with open(fileName2, "w") as f_write:
            f_write.write(newText)
    flag = compare_file_by_lines_v2(fileName2, fileName, ToBeDeleted)
    #with open(fileName2, "w") as f_write:
    #    f_write.write(oldText)
    #f_read.close()
    #f_write.close()
    return  str(flag)
def compareFile_not_contains(fileName2, fileName, originalValue, replacedValue):
    if len(originalValue) != len(replacedValue):
        return False
    with open(fileName) as f_read:
        oldText=f_read.read()
    for i in range (0, len(originalValue)):
        with open(fileName) as f_read:
            newText=f_read.read().replace(str(originalValue[i]), str(replacedValue[i]))
        with open(fileName, "w") as f_write:
            f_write.write(newText)
    flag = compare_file_by_lines_not_contain_v2(fileName2, fileName)
    with open(fileName, "w") as f_write:
        f_write.write(oldText)
    f_read.close()
    f_write.close()
    return  str(flag)
def combineString(str1, str2, str3='',str4='',str5='',str6='',str7=''):
    if str7!='':
        return str1+str2+str3+str4+str5+str6+str7
    elif str6!='':
        return str1+str2+str3+str4+str5+str6
    elif str5!='':
        return str1+str2+str3+str4+str5
    elif str4!='':
        return str1+str2+str3+str4
    elif str3!='':
        return str1+str2+str3
    elif str2!='':
        return str1+str2
    else:
        return False
def combineFile(fileName1, fileName2, combinedFile):
    newText=''
    with open(fileName1) as f_read_1:
        text1=f_read_1.read()
    with open(fileName2) as f_read_2:
        text2=f_read_2.read()
    newText=text1+text2
    with open(combinedFile, "w") as f_write:
        f_write.write(newText)
    f_read_1.close()
    f_read_2.close()
    f_write.close()
def deleteLineContainGievenStringFromFile(f1_name, f2_name, containedString):
    f1 = open(f1_name,'r')
    f2 = open(f2_name,'w')
    f1_line=f1.readline()
    while f1_line != '' :
        if containedString  not in  f1_line :
            f2.write(f1_line)
        f1_line=f1.readline()
    f1.close()
    f2.close()
def deleteStringFromFile(f1_name, f2_name, deleteString):
    f1 = open(f1_name,'rU')
    f2 = open(f2_name,'w')
    f1_line=f1.read()
    for element in deleteString:
        f1_line=f1_line.replace(element,'')
    f2.write(f1_line)
    f1.close()
    f2.close()
