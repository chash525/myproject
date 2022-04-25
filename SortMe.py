# Method for sorting the list
def Sorting(list):
    NewList = list
    # Sort the list ascending alphabetically 
    NewList.sort()
    #NewList = sorted(list, key=len, reverse=False)
    # Sort the list by length
    NewList.sort(key=lambda item: (len(item), item))

    # Output to a new text file
    newTextFile = open('output.txt', 'r+')
    # Add new lines after each element in the list
    for x in NewList:
        newTextFile.writelines(str(x) + "\n")
    newTextFile.close()

    # Return our new sorted list
    return NewList

# Open the text file to be sorted
text_file = open('Sort Me.txt', 'r')
temp = text_file.read().splitlines()
# Strip away any whitespaces
readList = [x.strip(' ') for x in temp]
text_file.close()

# Print the old list to compare to the sorted list
# Add new lines for clarity   
print('\n'+"Old List"+'\n')
print(readList) 
print('\n')
print('\n'+"New Sorted List"+'\n')
print(Sorting(readList))
# Erase output in output.txt so we can use it again
open('output.txt', 'w').close()