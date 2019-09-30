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

import UninformedSearch as BlindSearch
import Problem as P



filelist = ['Data sets for Assignment 1-20190923/a_easy.txt','Data sets for Assignment 1-20190923/b_moderate.txt',
            'Data sets for Assignment 1-20190923/c_hard.txt','Data sets for Assignment 1-20190923/d_veryhard.txt',
            'Data sets for Assignment 1-20190923/e_puremadness.txt']
dls_list = [3,4,10,10,10]

 # open a file
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
        # original is the initial state of the kessel
        original = i[3:i[1] * i[2] +3]
        # goal is the target kessel
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
    time_DFS = 0
    time_DLS = 0
    time_IDS = 0
    depth_BFS = 0
    depth_DFS = 0
    depth_DLS = 0
    depth_IDS = 0
    space_BFS = 0
    space_DFS = 0
    space_DLS = 0
    space_IDS = 0
    counter_BFS = 0
    counter_DFS = 0
    counter_DLS = 0
    counter_IDS = 0

    for k in outputList:
    # create a problem instance
        problem = P.Problem(k[3])

    # create a search object, and set the time limit
        searcher = BlindSearch.Search(problem, timelimit=10)

    # establish the initial state
        s = P.State(k[2], k[1][0], k[1][1])

    # do the searching; here we're calling BFS, DFS, DLS, IDS
        answer_BFS = searcher.BreadthFirstSearch(s)
        answer_DFS = searcher.DepthFirstSearch(s)
        answer_DLS = searcher.DepthLimitedSearch(s,dls_list[j])
        answer_IDS = searcher.IDS(s)



    # very basic output: use the str() method in SearchTerminationRecord
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

        if(answer_DFS.success):
            time_DFS += answer_DFS.time
            space_DFS += answer_DFS.space
            counter_DFS += 1
            print(k[0],"DFS"+str(answer_DFS),"( depth is "+str(answer_DFS.result.depth)+")",
                  "( space is " + str(answer_DFS.space) + ")")
        else:
            print(k[0], "DFS" + str(answer_DFS), "( depth is not found! sorry!) ",
                  "( space is " + str(answer_DFS.space) + ")")

        if (answer_DLS.success):
            time_DLS += answer_DLS.time
            space_DLS += answer_DLS.space
            depth_DLS += answer_DLS.result.depth
            counter_DLS += 1
            print(k[0],"DLS"+str(answer_DLS),"( depth is "+str(answer_DLS.result.depth)+")",
                  "( space is " + str(answer_DLS.space) + ")")
        else:
            print(k[0], "DLS" + str(answer_DLS), "( depth is not found! sorry!) ",
                  "( space is " + str(answer_DLS.space) + ")")

        if(answer_IDS.success):
            time_IDS += answer_IDS.time
            space_IDS += answer_IDS.space
            depth_IDS += answer_IDS.result.depth
            counter_IDS += 1
            print(k[0],"IDS"+str(answer_IDS),"( depth is "+str(answer_IDS.result.depth)+")",
                  "( space is " + str(answer_IDS.space) + ")")
        else:
            print(k[0], "IDS" + str(answer_IDS), "( depth is not found ! sorry!）",
                  "( space is " + str(answer_IDS.space) + ")")
        print("=======================next one=======================")
    try:
        print("avg time and space: "+str(time_BFS/counter_BFS)+"   "+str(   space_BFS/counter_BFS)+" instance number  "+str(   counter_BFS)
              + " AVG DEPTH  " + str(depth_BFS/counter_BFS))

    except ZeroDivisionError:
        print("o succeed")

    try:
        print("avg time and space: "+str(time_DFS / counter_DFS)+"   "+str(   space_DFS/counter_DFS)+" instance number  "+str(   counter_DFS)
              + " AVG DEPTH  " + str(depth_DFS / counter_DFS))
    except:
        print("o succeed")
    try:
        print("avg time and space: "+str(time_DLS / counter_DLS)+"  "+str(   space_DLS/counter_DLS)+" instance number  "+str(   counter_DLS)
              + " AVG DEPTH  " + str(depth_DLS / counter_DLS))
    except:
        print("o succeed")
    try:
        print("avg time and space: "+str(time_IDS / counter_IDS)+"   "+str(   space_IDS/counter_IDS)+" instance number  "
              +str(   counter_IDS)
              + " AVG DEPTH  " + str(depth_IDS / counter_IDS)
              )
    except:
        print("o succeed")

    print()
    print("======================= finished the "+filelist[j]+"=======================")
