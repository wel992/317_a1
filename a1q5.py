# CMPT 317: Basic Solver script for solving Search Problems

# Copyright (c) 2016-2019 Michael C Horsch,
# Department of Computer Science, University of Saskatchewan

# This file is provided solely for the use of CMPT 317 students.  Students are permitted
# to use this file for their own studies, and to make copies for their own personal use.

# This file should not be posted on any public server, or made available to any party not
# enrolled in CMPT 317.

# This implementation is provided on an as-is basis, suitable for educational purposes only.
#
# Note: this script doesn't run!  It's a template.  If you want to use it, you'll
# have to fill in some blanks, and complete the Problem-specific class module

#Wenyi Li
#11233166
import InformedSearch as InformedSearch
import Problem as P
filelist = ['Data sets for Assignment 1-20190923/a_easy.txt','Data sets for Assignment 1-20190923/b_moderate.txt',
            'Data sets for Assignment 1-20190923/c_hard.txt','Data sets for Assignment 1-20190923/d_veryhard.txt',
            'Data sets for Assignment 1-20190923/e_puremadness.txt']
dls_list = [3,4,10,10,10]

for j in range(len(filelist)):
    outputList = []
    tempStoreList = []
    original = []
    goal = []
    for line in open(filelist[j], "r"):
        line = line.strip('\n')

        line = [int(line) for line in line.split()]
        tempStoreList.append(line)

    for i in tempStoreList:
        storeIn = []

        original = i[3:i[1] * i[2] +3]
        goal = i[i[1] * i[2] +3:2*i[1] * i[2] + 4]

        storeIn.append(i[0])
        storeIn.append(i[1:3])
        storeIn.append(original)
        storeIn.append(goal)

        outputList.append(storeIn)


# the following doesn't run yet, since no methods do anything useful
# but here's how you work with the different classes provided:

# # create a problem instance
# problem = P.Problem([2,10,1,6,22,7,16,14,17,21,12,18,24,23,11,20,15,0,4,9,5,13,19,8,3])
#
# # create a search object, and set the time limit
# searcher = BlindSearch.Search(problem,timelimit=1000)
#
# # establish the initial state
# s = P.State([2,10,1,6,21,7,16,14,17,23,11,12,18,24,20,15,0,4,9,3,5,13,19,8,22],5,5)
#
# # do the searching; here we're calling BFS
# answer = searcher.BreadthFirstSearch(s)
#
# # very basic output: use the __str__() method in SearchTerminationRecord
# print(str(answer))

# end of file

    time_BFS = 0
    time_ASS = 0
    time_UCS = 0

    depth_BFS = 0
    depth_ASS = 0
    depth_UCS = 0

    space_BFS = 0
    space_ASS = 0
    space_IDS = 0

    counter_BFS = 0
    counter_ASS = 0
    counter_UCS = 0

    for k in outputList:
    # create a problem instance
        problem = P.InformedProblem(k[3])

    # create a search object, and set the time limit
        searcher = InformedSearch.InformedSearch(problem, timelimit=10)

    # establish the initial state
        s = P.State(k[2], k[1][0], k[1][1])

    # do the searching; here we're calling BFS
        answer_BFS = searcher.BestFirstSearch(s)
        answer_ASS = searcher.AStarSearch(s)
        answer_UCS = searcher.UCSSearch(s)

        # answer_IDS = searcher.IDS(s)






    # very basic output: use the __str__() method in SearchTerminationRecord
        if(answer_BFS.success):
            time_BFS += answer_BFS.time
            space_BFS += answer_BFS.space
            depth_BFS += answer_BFS.result.depth
            counter_BFS+=1
            print(k[0],"BFS"+str(answer_BFS)+"( depth is "+str(answer_BFS.result.depth)+")",
                  "( space is "+str(answer_BFS.space)+")")
        else:
            print(k[0], "BFS" + str(answer_BFS) + "( depth is not found!Sorry!)",
                  "( space is " + str(answer_BFS.space) + ")")

        if (answer_ASS.success):
            time_ASS += answer_ASS.time
            space_ASS += answer_ASS.space
            depth_ASS += answer_ASS.result.depth
            counter_ASS += 1
            print(k[0],"ASS" + str(answer_ASS), "( depth is " + str(answer_ASS.result.depth) + ")",
                  "( space is " + str(answer_ASS.space) + ")")
        else:
            print(k[0], "ASS" + str(answer_ASS), "( depth is not found! sorry!) ",
                  "( space is " + str(answer_ASS.space) + ")")

        if(answer_UCS.success):
            time_UCS += answer_UCS.time
            space_IDS += answer_UCS.space
            depth_UCS += answer_UCS.result.depth
            counter_UCS += 1
            print(k[0],"UCS" + str(answer_UCS), "( depth is " + str(answer_UCS.result.depth) + ")",
                  "( space is " + str(answer_UCS.space) + ")")
        else:
            print(k[0], "UCS" + str(answer_UCS), "( depth is not found ! sorry!）",
                  "( space is " + str(answer_UCS.space) + ")")
        print("=======================next one=======================")
    try:
        print("avg time and space: "+str(time_BFS/counter_BFS)+"   "+str(   space_BFS/counter_BFS)+" instance number  "+str(   counter_BFS)
              + " AVG DEPTH  " + str(depth_BFS/counter_BFS))

    except ZeroDivisionError:
        print("o succeed")


    try:
        print("avg time and space: " + str(time_ASS / counter_ASS) + "  " + str(space_ASS / counter_ASS) + " instance number  " + str(counter_ASS)
              + " AVG DEPTH  " + str(depth_ASS / counter_ASS))
    except:
        print("o succeed")

    try:
        print("avg time and space: " + str(time_UCS / counter_UCS) + "   " + str(space_IDS / counter_UCS) + " instance number  "
              + str(counter_UCS)
              + " AVG DEPTH  " + str(depth_UCS / counter_UCS)
              )
    except:
        print("o succeed")

    print("======================= finished the "+filelist[j]+"=======================")
