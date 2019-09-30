#Wenyi Li
#11233166
import Problem


import Problem

# four test cases
test1 = [0, [2, 2], [3, 0, 1, 2], [1, 2, 3, 0]]
pro1 = Problem.Problem(test1[3])
state1 = Problem.State(test1[2], test1[1][0], test1[1][1])

test2 = [1, [2, 2], [2, 1, 0, 3], [1, 3, 0, 2]]
pro2 = Problem.Problem(test2[3])
state2 = Problem.State(test2[2], test2[1][0], test2[1][1])

test3 = [2, [3, 2], [1, 2, 3, 4, 5, 6], [2, 5, 4, 3, 1, 0]]
pro3 = Problem.Problem(test3[3])
state3 = Problem.State(test3[2], test3[1][0], test3[1][1])

test4 = [3, [2, 3], [1, 2, 4, 6, 5, 3], [1, 2, 4, 6, 5, 3]]
test = [test1, test2, test3,test4]

actions_1 = Problem.Problem.actions(pro1, state1)
actions_2 = Problem.Problem.actions(pro2, state2)
actions_3 = Problem.Problem.actions(pro3, state3)

# test is_goal() method
##################################################################
goal_result = []

for k in range(len(test)):
    pbm = Problem.Problem(test[k][3])
    st = Problem.State(test[k][2], test[k][1][0], test[k][1][1])

    # put all result into a list after using is_goal() method
    goal_result.append(pbm.is_goal(st))

# check if is_goal() method works properly
if goal_result == [False, False, False, True]:
    print('SOME Test all finished in is_goal() method test.')
else:
    print('Test failed in is_goal() method')
##################################################################


# test actions() method
##################################################################
actions_result = []

# put all result into a list after using actions() method
if actions_1 == [['right', 0], ['left', 0], ['right', 1],['left', 1], ['up', 0], ['down', 0],
                 ['up', 1], ['down', 1]]:
    actions_result.append(True)
else:
    actions_result.append(False)

# test second case
if actions_2 == [['right', 0], ['left', 0],['right', 1],['left', 1],  ['up', 0], ['down', 0], ['up', 1], ['down', 1]]:
    actions_result.append(True)
else:
    actions_result.append(False)

# test third case
if actions_3 == [['right', 0], ['left', 0],['right', 1],['left', 1],['right', 2], ['left', 2], ['up', 0], ['down', 0],['up', 1], ['down', 1]]:
    actions_result.append(True)
else:
    actions_result.append(False)


# check if actions() method works properly
if False in actions_result:
    print('SOME Test failed in actions() method')
else:
    print('Test all finished in actions() method.')
##################################################################


# test result() method
##################################################################
resultList = []

new_a1 = pro1.result(state1, ['left', 0])
new_a2 = pro1.result(state2, ['right', 1])
new_a3 = pro1.result(state3, ['up', 0])
new_a4 = pro1.result(state3, ['down', 0])
new_a5 = pro1.result(state3, ['down', 1])

# test move right
if new_a1.new == [0, 3, 1, 2]:
    resultList.append(True)
else:
    resultList.append(False)

# test move left
if new_a2.new == [2, 1, 3, 0]:
    resultList.append(True)
else:
    resultList.append(False)

# # test go up
if new_a3.new == [3, 2, 5, 4, 1, 6]:
    resultList.append(True)
else:
    resultList.append(False)

# test go down
if new_a4.new == [5, 2, 1, 4, 3, 6]:
    resultList.append(True)
else:
    resultList.append(False)


# test go down
if new_a5.new == [1, 6, 3, 2, 5, 4]:
    resultList.append(True)
else:
    resultList.append(False)

# check if actions() method works
if False in resultList:
    print('SOME Test failed in result() method')
else:
    print('Test all finished in result() method .')























