## Example: Behaviour Trees for LLM Chatbots

This simple example shows how complex interaction can be coordinated between humans and an LLM chatbot to go through a complex goal-directed interaction while utilizing LLM chatbot capabilities.

The demonstration case is a scheme where the bot and people are in the same chat channel or group.

The bot is set up to organize an event, which it does by finding a time suitable to everyone.

People can signal their intent to attend the event, to cancel their attendance, and to tell their even availabilities.
All these are normal natural language, and the system uses LLM chatbot capabilities to update the state of the consensus.

![](eventplanner.png)

Currently none of the code interfacing to the chatroom and to the LLM chatbot are implemented, but the general structure already shows how Behavior Trees can be used to structure complex interaction processes into self-documenting goal-driven Behavior Tree patterns in a modular and extensible fashion.
