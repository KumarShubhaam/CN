def Print(maze):
    print('----------------------------')
    for row in maze:
        for i in range(len(row)):
            print(row[i], end=" ")
        print()    
    print('----------------------------')
