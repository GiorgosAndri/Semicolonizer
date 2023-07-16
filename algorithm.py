c_code = ""
decision = input("file(F) or code(C) as an input? Coose between F and C  ")
while decision.lower() not in ['c', 'f']:
    decision = input("file(F) or code(C) as an input? Coose between F and C  ")
if decision.lower() == 'f':
    file_path = input("enter file path: ")
    with open(file_path, "r") as file:
        c_code = file.read()
elif decision.lower() == "c":
    c_code = input("Insert code here: ")



lines = c_code.split('\n')
spaces = 0 #A tool that will use to find the actual position of the text after we strip it and process it
downline = -1 # A tool that will help us manage the \n values
indexes = [] # A tool that will help us manage the \n values
do = 0 #checking variable for finding the function do in order to add semicolon to the while later
symbols = ['=', '-', '+', '%', '/', '//', '*', '<' , '>', '==']
updated = []
for i in range(len(lines)):
    line = lines[i].strip()
    #Avoiding to put semicolons where they already exist and avoid curly braces and comments for enhancing performance
    if (line=='{' or line[:2]=='//' or line=='#') or (len(line)>1 and line[0]=='#') or (len(line)>1 and line[-1]) == ';':
        continue
    spaces = len(lines[i])-len(line)
    check_list = line.split(' ')
    if check_list[0] in ('switch', 'if', 'else', '//'):
        if "'''" in line:
            for j in range(len(line)):
                if line[j] == "'" and line[j+1] == "'" and line[j+2] == "'":
                    lines[i] = lines[i][:(spaces-1+(j))] + "'\\'" + lines[i][(spaces + (j+2)):]
        continue
    if len(line) > 1 and i+1<len(lines):
        if line[-1] == ')' and lines[i+1].strip() =='{' and line[:3]!='for':
            continue
    #Processing the do functions
    if line == 'do' or line == 'do{' or line == 'do {':
        do = 1
        continue
    if do == 1:
        if line[:len('while')] == 'while':
            lines[i] += ';'
            do = 0
            continue
    elif line[:len('while')] == 'while' and do == 0:
        continue


    #Processing typedef and stuct
    if i+1 < len(lines):
        next = lines[i+1].strip() #checking if the next line begins with {
    if check_list[0] in ['typedef', 'struct'] and (check_list[-1]=='{' or check_list[-1][-1]=='{' or next[0]=='{'):
        continue

#Processing tables
    if len(line)>2:
            if line[-1] != '{' and '{' in line and line[-1] == '}' and (line[line.index('{')-1] in symbols or (line[line.index('{')-1] == ' ' and line[line.index('{')-2] in symbols)):
                lines[i] += ';'

        #Fixing the for loops
    if 'for(' in line or 'for (' in line:
        #Splitting the string into a list
        lista = line.split(' ')
        listb = []
        for j in range(len(lista)):
            #fixing the first positions
            if (lista[j]=='for' and '(' in lista[j+1]) or (lista[j-1]=='for' and '(' in lista[j]) or 'for(' in lista[j]:
                listb.append(lista[j])
                continue
            #Checking after the opening of the parentheses in case there is a space between the parentheses and the first declaration
            if isinstance(lista[j], str) and lista[j-1]=='(':
                    listb.append(lista[j])
                    continue
            #Checking out the symbols in case there are spaces between them
            if j+1 < len(lista):
                if lista[j+1] in symbols:
                    listb.append(lista[j])
                    continue
            #Checking the declarations
            if lista[j][-1].isnumeric() or lista[j][-1].isalpha() or lista[j][-1] in [')', ']'] :
                lista[j] += ';'
            #Putting the semicolonized parts in another list
            listb.append(lista[j])
            #Making it a string again and putting it in it's position using the spaces
        listb[-1] = listb[-1][:-1]
        lines[i] = spaces*' ' + ' '.join(listb)
        continue
    #Checking for '\'' values
    if "'''" in line:
        for j in range(len(line)):
            if line[j] == "'" and line[j+1] == "'" and line[j+2] == "'":
                lines[i] = lines[i][:(spaces-1+(j))] + "'\\'" + lines[i][(spaces + (j+2)):]

    #Checking in which indexed ae the \n values that we don't want to keep
    if line.count('"')%2 != 0:
        if i == downline+1:
            continue
        indexes.append(i+1)
        if len(line)>1:
            if line[-1] == ';':
                print(line)
                lines[i] == lines[i][:-1]
        lines[i] = lines[i] + '\\n' + lines[i+1] + ';'
        downline = i

    #Checking if the last line is a number or a character or a symbol that requires semicolon
    if line and (line[-1].isnumeric() or line[-1].isalpha() or line[-1] in [']', ')', '"', "'"]) or line[-2:] in ['++', '--']:
        lines[i] += ';'
    #Checking for double semicolons or more
    if len(lines[i]) > 1:
        if lines[i][-1] == ';' and lines[i][-2] == ';':
            for j in range(len(lines[i]) - 1, -1, -1):
                if lines[i][j]!=';':
                    break
            lines[i] = lines[i][:j+2]




#Putting out the 'trash' lines after handling the \n values
for i in range(len(indexes)):
    lines.pop(indexes[i])
    for j in indexes[i:]:
        indexes[indexes.index(j)] -= 1

#Putting everything together
updated = '\n'.join(lines)



if decision.lower == 'c':
    with open("output.c", "w") as file:
        # Write the string to the file
        file.write(updated)
else:
    new_file = file_path[:file_path.index(".")]
    with open(f"{new_file}_semicolonized.c", "w") as file:
        # Write the string to the file
        file.write(updated)
