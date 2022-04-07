martix = "7i3\nTsi\nh%x\ni #\nsM \n$a \n#t%\n^r!"
print(martix)
mat_list = martix.split('\n')
result_string = ""
space = True
for column in range(len(mat_list[0])):
    for row in mat_list:
        if row[column].isalpha():
            result_string += row[column]
            space = False
        elif not space:
            result_string += ' '
            space = True

print(result_string)