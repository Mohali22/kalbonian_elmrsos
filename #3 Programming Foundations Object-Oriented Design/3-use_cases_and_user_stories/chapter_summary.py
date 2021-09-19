##### Chapter Summary ( use cases and user stories ) #####
# ------------------------------------------------------ #


# Use cases #
# --------- #

# what is Use cases?
# A use case is a methodology used in system analysis to identify, clarify and organize system requirements. The use case is made up of a set of possible sequences of interactions between systems and users in a particular environment and related to a particular goal. The method creates a document that describes all the steps taken by a user to complete an activity.

# Use cases are typically written by business analysts and can be employed during several stages of software development, such as planning system requirements, validating design, testing software and creating an outline for online help and user manuals. A use case document can help the development team identify and understand where errors may occur during a transaction so they can resolve them.

# Every use case contains three essential elements:

# The actor. The system user -- this can be a single person or a group of people interacting with the process.
# The goal. The final successful outcome that completes the process.
# The system. The process and steps taken to reach the end goal, including the necessary functional requirements and their anticipated behaviors.
# Characteristics of use case
# Use cases describe the functional requirements of a system from the end user's perspective, creating a goal-focused sequence of events that is easy for users and developers to follow. A complete use case will include one main or basic flow and various alternate flows. The alternate flow, also known as an extending use case, describes normal variations to the basic flow as well as unusual situations.

# A use case should display the following characteristics:

# Organizes functional requirements.
# Models the goals of system/actor interactions.
# Records paths -- called scenarios -- from trigger events to goals.
# Describes one main flow of events and various alternate flows.
# Multi-level, so that one use case can use the functionality of another one.
# How to write a use case
# There are two different types of use cases: business use cases and system use cases.

# A business use case is a more abstract description that's written in a technology-agnostic way, referring only to the business process being described and the actors that are involved in the activity. A business use case identifies the sequence of actions that need to be performed by the business to provide a meaningful, observable result to the end user.

# On the other hand, a system use case is written with more detail than a business use case, referring to the specific processes that must happen in various parts of the system to reach the final user goal. A system use case diagram will detail functional specifications, including dependencies, necessary internal supporting features and optional internal features.

# When writing a use case, the design scope should be considered to identify all elements that lie within and outside the boundaries of the processes. Anything essential to the use case that lies outside its boundaries should be indicated with a supporting actor or by another use case. The design scope can be a specific system, a subsystem or the entire enterprise. Use cases that describe business processes are typically of the enterprise scope.

# As mentioned, the three basic elements that make up a use case are actors, the system and the goal. Other additional elements to consider when writing a use case include:

# Stakeholders, or anybody with an interest or investment in how the system performs.
# Preconditions, or the elements that must be true before a use case can occur.
# Triggers, or the events that cause the use case to begin.
# Post-conditions, or what the system should have completed by the end of the steps.
# The use case is written using narrative language, describing the functional requirements of a system from the end user's perspective. A use case diagram is created using a unified modeling language, with each step represented by its name in an oval; each actor represented by a stick figure with their name written below; each action indicated by a line between the actor and step; and the system boundaries indicated by a rectangle around the use case.


# Identifying the actors #
# ---------------------- #

# what is Identifying the actors?
# Identifying actors is one of the first steps in use case analysis. Each type of external entities with which the system must interact is represented by an actor. For example, the operating environment of a software system consists of the users, devices, and programs that the system interacts with. These are called actors which has the following characteristics:

# An actor in use case modeling specifies a role played by a user or any other system that interacts with the subject.
# An Actor models a type of role played by an entity that interacts with the subject (e.g., by exchanging signals and data), but which is external to the subject.
# Actors may represent roles played by human users, external hardware, or other subjects.
# Actors do not necessarily represent specific physical entities but merely particular facets (i.e., “roles”) of some entities that are relevant to the specification of its associated use cases.
# A single physical instance may play the role of several different actors and a given actor may be played by multiple different instances.

# ----> identifying scenarios


# diagramming use cases #
# --------------------- #

# what is diagramming use cases
# A use case diagram is a graphical depiction of a user's possible interactions with a system.
# A use case diagram shows various use cases and different types of users the system has and will often be accompanied by other types of diagrams as well.
# The use cases are represented by either circles or ellipses. The actors are often shown as stick figures.


# the four main characteristics of Use Case Diagrams:
# 1- systems
# 2- actors
# 3- use cases
# 4- relationships

# 1- A system is whatever you’re developing.
# It could be a website, a software component, a business process, an app, or any number of other things.
# You represent a system with a rectangle.

# 2- The next aspect of Use Case Diagrams are actors.
# An actor is going to be someone or something that uses our system to achieve a goal,
# and they're represented by a stick figure.

# 3- Use Cases are elements that really start to describe what the system does.
# They're depicted with an oval shape and they represent an action that accomplishes some sort of task within the system.

# 4- The final element in Use Case Diagrams are relationships, which show how actors and use cases interact with each other.
# There are different types of relationships (like association, include, extend,
# and generalization) that are represented by varying types of lines and arrows.


# user stories #
# ------------ #

# What is a user stories?
# User stories define the who, the what and the why of a product feature.
# They’re usually aimed at developers but are intended to be easily understood by everyone on the team, including clients.
# They outline what a user needs to get done, from that user’s point of view.

# User story structure
# They often comprise just one sentence or a couple of lines written in the following structure:

# As a (user)
# I want to (goal)
# So that (reason)

# An example of this could be:
# “As a user, I want to have a barcode ticket for my train pass on my phone so that I don’t need to print it off and carry a paper around with me.”


# User stories vs use cases: differences #
# ====================================== #

# 1- User stories
# User stories are normally, and purposely, more vague.
# The user story provides a simplified, abridged description in layman’s terms of what a feature should help the user do.
# This leaves it more open to interpretation and encourages more creativity and discussion on the part of the design and development teams.

# 2- Use cases
# Use cases cover more ground by showing how the user should interact with the system and how the system should reciprocate.
# They go into further detail about how the individual steps in a feature’s process.
