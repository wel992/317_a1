# CMPT 317: A Python implementation of Frontier interfaces for uninformed search.

# Copyright (c) 2016-2019 Michael C Horsch,
# Department of Computer Science, University of Saskatchewan

# This file is provided solely for the use of CMPT 317 students.  Students are permitted
# to use this file for their own studies, and to make copies for their own personal use.

# This file should not be posted on any public server, or made available to any party not
# enrolled in CMPT 317.

# This implementation is provided on an as-is basis, suitable for educational purposes only.

# Simple implementations of the Frontier interface.
#   Frontier: a base class
#   FrontierFIFO: implements FIFO, for use by BFS
#   FrontierLIFO: implements LIFO, for use by DFS
#
# Assumes a problem class with the methods:
#   is_goal(problem_state): returns True if the state is the goal state
#   actions(problem_state): returns a list of all valid actions in state
#                           (the actions are only passed to result())
#   result(state, action): returns a new state that is the result of doing action in state.


#########################################################################################
class Frontier(object):
    """
    A base class for Frontiers.  A Frontier is a list.
    This base class leaves the remove() method unimplemented.
    """

    def __init__(self):
        """ initialize the Frontier"""
        self._nodes = []

    def __len__(self):
        """ the length of the Frontier is the length of the list attribute"""
        return len(self._nodes)

    def is_empty(self):
        """ a Frontier is empty when there are no nodes in the list """
        return len(self._nodes) == 0

    def add(self, aNode):
        """add the new Node to the Frontier"""
        # adding to the end is fast
        self._nodes.append(aNode)



#########################################################################################
class FrontierFIFO(Frontier):
    """ This Frontier uses a typical FIFO queue.
        This class inherits the Frontier methods.
    """

    def __init__(self):
        """ initialize the Frontier"""
        Frontier.__init__(self)

    def remove(self):
        """remove a Node from the Frontier"""
        # in a FIFO queue, remove the front Node
        # this is O(N) --- ouch!
        val = self._nodes.pop(0)
        return val



#########################################################################################
class FrontierLIFO(Frontier):
    """ This Frontier uses a typical LIFO stack.
    This class inherits the Frontier methods.
    """

    def __init__(self):
        """ initialize the Frontier"""
        Frontier.__init__(self)

    def remove(self):
        """remove the state from the end"""
        val = self._nodes.pop()
        return val



#########################################################################################
class FrontierLIFO_DL(FrontierLIFO):
    """ This is a LIFO queue, but nodes that exceed a limit are discarded.
    """

    def __init__(self, dlimit):
        """ initialize the Frontier
            dlimit: an integer representing the depth limit to be used.
            Any Node whose depth is greater than dlimit is not added to the Frontier.
            This simplifies the search code!
        """
        FrontierLIFO.__init__(self)
        self.__dlimit = dlimit
        self._cutoff = False

    def add(self, aNode):
        """add the new state on the end"""
        if aNode.depth <= self.__dlimit:
            self._nodes.append(aNode)
        elif not self._cutoff:
            self._cutoff = True


# end of file

