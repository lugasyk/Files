def openFiles():
    #fhand = open('mbox.txt')
    #fhand = open('stuff.txt')  It's just opening of file
    #print(fhand)

    #fhand = open('mbox.txt') coun rt
    #count = 0
    #for line in fhand:         It's just counting numbers of line in file
        #count = count + 1
   # print('Line Count:', count)

    #hand = open('mbox.txt')
    #inp = fhand.read()       This piece of code prints everything till 20 index
    #print(len(inp))
    #print(inp[:20])

    #fhand = open('mbox.txt')  This code returns the len of txt file
    #print(len(fhand.read()))

    #fhand = open('mbox.txt')
    #count = 0                This code returns all rows which starts from "From"
    #for line in fhand:
        #if line.startswith('From:'): print(line)\

    # The same logic as the previous just cutting some rows
    #fhand = open('mbox.txt')
    #for line in fhand:
        #line = line.rstrip()
    # Skip 'uninteresting lines'
        #if not line.startswith('From:'):
            #continue
    # Process our 'interesting' line
    #   print(line)

    # The logic returns rows which contains the same domen
    #fhand = open('mbox.txt')
    #for line in fhand:
        #line = line.rstrip()
        #if line.find('@uct.ac.za') == -1:
           # continue
        #print(line)

    # Here the user is able to specify the file from which he wants to count amount of lines which start with Subject
    #fname = input('Enter the file name: ')
    #fhand = open(fname)
    #count = 0
    #for line in fhand:
        #if line.startswith('Subject:'):
           # count = count + 1
       # print('There were', count, 'subject lines in', fname)

    #this piece of code using try except functions for opening files
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()
    count = 0
    for line in fhand:
        if line.startswith('Subject:'):
            count = count + 1
    print('There were', count, 'subject lines in', fname)

if __name__ == "__main__":
    openFiles()