#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import py_trees.behaviour
import py_trees.decorators
import py_trees.display
from py_trees.common import ParallelPolicy


# Event planner is a demo of a complex interaction between a chatbot and
# multiple chat participants.
# The orchestrator sits in between the LLM chatbot and the discussion
# participants herding them towards conclusion.

# The general outline of this demonstration interaction is as follows:
# - People join a channel to plan for an event.
# - They say what times are convenient for them.
# - The bot converts these in a standard form.
# - Once everyone has told their availability, there will be a conclusion
#   of times suitable to all, or no such time.

# So, the orchestrator will track the participants, and tell them
# how the system works when they first join.
# It will pass peoples messages to a chatbot as appropriate to transform them
# into a standard form.
# Once all participants have told of their availability, the orchestrator will compile
# together the summary.
# The orchestrator can utilize the chatbot for various purposes during this process.

class HaveAllUsersSignaledTheirAvailability(py_trees.behaviour.Behaviour):
    """
    Check the blackboard whether we have availability information for all users.
    """

    def __init__(self, name="HaveAllUsersSignaledTheirAvailability"):
        super(HaveAllUsersSignaledTheirAvailability, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

class NewMessageIsUserJoining(py_trees.behaviour.Behaviour):
    """
    Asks the chatbot whether the new message is about user joining.
    If yes, write the user name leaving to blackboard.
    If yes, succeed, if no, fail.
    """

    def __init__(self, name="NewMessageIsUserJoining"):
        super(NewMessageIsUserJoining, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

class NewMessageIsUserLeaving(py_trees.behaviour.Behaviour):
    """
    Asks the chatbot whether the new message is about user leaving.
    If yes, write the user name leaving to blackboard.
    If yes, succeed, if no, fail.
    """

    def __init__(self, name="NewMessageIsUserLeaving"):
        super(NewMessageIsUserLeaving, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

class IntroduceTheSystemToNewUser(py_trees.behaviour.Behaviour):
    """
    Introduces the system to the new user.
    """

    def __init__(self, name="IntroduceTheSystemToNewUser"):
        super(IntroduceTheSystemToNewUser, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

class AddUserToEvent(py_trees.behaviour.Behaviour):
    """
    Adds the user to the event.
    """

    def __init__(self, name="AddUserToEvent"):
        super(AddUserToEvent, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

class RemoveUserFromEvent(py_trees.behaviour.Behaviour):
    """
    Removes the user to the event.
    """

    def __init__(self, name="RemoveUserFromEvent"):
        super(RemoveUserFromEvent, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

class NewMessageIsUserAvailability(py_trees.behaviour.Behaviour):
    """
    Asks the chatbot whether the new message is about availability.
    If yes, succeed, if no, fail.
    """

    def __init__(self, name="NewMessageIsUserAvailability"):
        super(NewMessageIsUserAvailability, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

class UpdateUserAvailability(py_trees.behaviour.Behaviour):
    """
    Asks the chatbot what the new user availability is in a standard
    form given the previous user availability and the new message.
    Stores this availability info.
    """

    def __init__(self, name="UpdateUserAvailability"):
        super(UpdateUserAvailability, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

class SummarizeSuitableEventTime(py_trees.behaviour.Behaviour):
    """
    Sends a message to the chatbot which summarizes the suitable times for all users.
    The chatbot needs to transform this to a textual description of the conclusion.
    """

    def __init__(self, name="SummarizeSuitableEventTime"):
        super(SummarizeSuitableEventTime, self).__init__(name)

    def setup(self):
        pass

    def initialise(self):
        pass

    def update(self):
        pass

if __name__ == '__main__':

    root = py_trees.composites.Parallel(name="EventPlanner", policy=ParallelPolicy.SuccessOnOne)

    maintain_roster = py_trees.composites.Parallel(name="MaintainRoster", policy=ParallelPolicy.SuccessOnOne)
    plan_event = py_trees.composites.Sequence(name="PlanEvent", memory=True)
    maintain_availabilities = py_trees.composites.Sequence(name="MaintainAvailabilities", memory=True)

    new_user = py_trees.composites.Sequence(name="NewUser", memory=True)
    leaving_user = py_trees.composites.Sequence(name="LeavingUser", memory=True)

    root.add_children([maintain_roster, plan_event, maintain_availabilities])

    new_user.add_children([NewMessageIsUserJoining(), IntroduceTheSystemToNewUser(), AddUserToEvent()])

    leaving_user.add_children([NewMessageIsUserLeaving(), RemoveUserFromEvent()])

    maintain_roster.add_children([new_user, leaving_user])

    plan_event.add_children([HaveAllUsersSignaledTheirAvailability(), SummarizeSuitableEventTime()])

    maintain_availabilities.add_children([NewMessageIsUserAvailability(), UpdateUserAvailability()])

    py_trees.display.render_dot_tree(root)
