# CMPT 317: Search Problem definition

# Copyright (c) 2016-2019 Michael C Horsch,
# Department of Computer Science, University of Saskatchewan

# This file is provided solely for the use of CMPT 317 students.  Students are permitted
# to use this file for their own studies, and to make copies for their own personal use.

# This file should not be posted on any public server, or made available to any party not
# enrolled in CMPT 317.

# This skeleton is provided on an as-is basis, suitable for educational purposes only.
#

#########################################################################################
import numpy as np
import copy as copy
#Wenyi Li
#11233166
class State(object):
    """The Problem State objects record data needed to solve the search problem.
    """
    def __init__(self,new_list,r,c):
        """
        Initialize the State object.  
        Your definition can add constructor arguments as necessary.
        """
        self.new = 'Initial state'
        # other attributes as needed by your problem
        self.hval = 0
        self.new = new_list
        self.column = c
        self.row = r


    def __str__(self):
        """ A string representation of the State """
        return '<{}>'.format('you decide how your state objects should display')

    def __eq__(self, other):
        """ Allows states to be compared by comparing their data """
        return False

    # add more methods if necessary; these could support the Problem class methods


#########################################################################################

class InformedState(State):
    """We add an attribute to the state, namely a place to
       store the estimated path cost to the goal state.  
    """
    def __init__(self, puzzle, hval=0):
        """Initialize the State.
           The hval attribute estimates the path cost to the goal state from the current state
           It should be calculated by the InformedProblem class, and stored here for use.
        """
        super().__init__()
        self.hval = hval

    # add more methods if necessary; these could support the Problem class methods


#########################################################################################
class Problem(object):
    """The Problem class defines aspects of the problem.
       One of the important definitions is the transition model for states.
       To interact with search classes, the transition model is defined by:
            is_goal(s): returns true if the state is the goal state.
            actions(s): returns a list of all legal actions in state s
            result(s,a): returns a new state, the result of doing action a in state s
       Other methods here are not part of the interface, but support debugging or the 
       transition model.

    """

    def __init__(self,goal):
        """ Initialize the problem object.
            Your definition can add constructor arguments as necessary.
        """

        self._goal = goal



    def is_goal(self, a_state:State):
        """Returns true if the given state is a goal state"""
        if self._goal==a_state.new:
            return True
        else:
            return False


    def actions(self, a_state:State):
        """ Returns a list of all the actions that are legal in the given state.
            You decide what an action looks like.  Put 'em in a list.
        """
        # all actions
        all_actions = []

        for r in range(a_state.row):
            all_actions.append(['right', r])  #r means the row number that the a_state want to move
            all_actions.append(['left', r])

        # find remove column index number


        for c in range(a_state.column):
            all_actions.append(['up', c])  # c means the column number that the a_state want to move
            all_actions.append(['down', c])
        return all_actions


    def result(self, a_state:State, an_action):
        """Given a state and an action, return the resulting state.
           The action is one of the things you created in actions() above.
           You're only getting one action here, so only give the one resulting state.
        """
        # initialize a new state and the row , col number of
        new = list(a_state.new)
        row = a_state.row
        col = a_state.column

        # begin to get the right direction
        if an_action[0] == 'right':
            for i in range(an_action[1]*col,(an_action[1]+1)*col):
                # the range use index to picked all of number in this row
                    if (i + 1) % col == 0:
                        new[(i-col) + 1] = a_state.new[i]
                    else:
                        new[i + 1] = a_state.new[i]

            all_state = State(new, a_state.row, a_state.column)
            return all_state
#go left
        elif an_action[0] == 'left':

            for i in range(an_action[1]*col,(an_action[1]+1)*col):
                # the same,the range use index to picked all of number in this row
                if i % col == 0:
                        new[(i+col) - 1 ] = a_state.new[i]
                else:
                        new[i - 1] = a_state.new[i]

            all_state = State(new, a_state.row, a_state.column)
            return all_state
# go up
        elif an_action[0] == 'up':

            c = np.linspace(an_action[1], an_action[1]+(row-1)*col, row, endpoint=True)
            # use numpy and index to pick all numbers in a same column out
            list1 = [int(i) for i in c]
            # place the numbers into a seperate list and int it for later use

            for i in list1:
                    if (i - col) < 0:
                        new[i-col+col*row] = a_state.new[i]
                        # assign its value to the corresponding index
                    else:
                        new[i-col] = a_state.new[i]
            all_state = State(new, a_state.row, a_state.column)
            return all_state
#go down
        elif an_action[0] == 'down':

            c = np.linspace(an_action[1], an_action[1] + (row - 1) * col, row, endpoint=True)
            # use numpy and index to pick all numbers in a same column out

            list2 = [int(i) for i in c]
            # place the numbers into a seperate list and int it for later use



            for i in list2:
                    if (i + col) >= len(a_state.new):
                        new[i+col-row*col] = a_state.new[i]
                    else:
                        new[i+col] = a_state.new[i]

            all_state = State(new, a_state.row,a_state.column)
            return all_state
        elif an_action == 'NA':
            return None


            # add more methods if necessary


#########################################################################################
class InformedProblem(Problem):
    """We add the ability to calculate an estimate to the goal state.
    """
    def __init__(self, goal):
        """ Initialize the problem object.
            Your definition can add constructor arguments as necessary.
        """
        super().__init__(goal)




    def calc_h(self, a_state):
        """This function computes the heuristic function h(n)
        """
        # this trivial version returns 0, a trivial estimate, but consistent and admissible
        count = 0
        for i in range(len(a_state.new)):
            if a_state.new[i] != self._goal[i]:
                count+=1
        return count


    def result(self, a_state, an_action):
        """Given a state and an action, return the resulting state.
           The superclass does most of the work.
           We add the heuristic value to the informed state here, using calc_h()
        """
        astate = super().result(a_state, an_action)
        astate.hval = self.calc_h(astate)
        return astate

    # add more methods if necessary


# end of file

