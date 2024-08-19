# Django Checklist Project
Hackathon 3 Group A (Berks)

## A Django Setup Guide for users
Django Checklist is an app to enable tracking of installing a Django server

[enter link description here](hero%20linkgage)

# Table of Contents  
 1. [ UX ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)  
 4. [ Features Left to Implement ](#features-left-to-implement)  
 5. [ Technology used ](#technology-used) 
 6. [ Bugs ](#known-bugs)  
 7. [ Deployment](#deployment)
 8. [ Resources ](#resources)  
 

# UX

## Database Planning
Database planning was designed to '*borrow*' from Craig's Capstone project to allow a swifter start-up.  Signed in users should have CRUD access to their own notes, Read access to the checklist and Update access to their own checklist status.

## UX Design

### Overview
Django Checklist's core concept is to allow users to follow, check off stages, and review progress through the various steps of setting up a Django server.  The intention is to include a notes section for each user so that they can make their own notes on the setup to facilitate custom builds.  The initial checklist items will **not** be editable by standard users.

### Site User
The primary users of Django Checklist is likely to be those new to Django installations or those that may need a helpful reminder.  The addition of the notes system will allow users to make notes on the installation steps and would allow more advanced users to build their own 'custom' installation documentation.

### Goal
The goal behind Django Checklist is to create an easy and intuitive method of both reviewing and recording the progress through the installation and setup of a Django instance with the additional enhancement of allowing bespoke notes for users at each step.

## Wireframes
Balsamiq was used to create the wireframes with the base layout showing the initial design ideas that would allow our project to display the required information. 

![Landing Page](https://photos.google.com/photo/AF1QipMvVmgZxnUOZJjLEkQIVEcGU06cqamIHT9JGRWh)
![About Page](https://photos.google.com/photo/AF1QipMvVmgZxnUOZJjLEkQIVEcGU06cqamIHT9JGRWh)
![List Page](https://photos.google.com/photo/AF1QipO_5VV1H1V4Kb7WsAI6W3h17aiOjiKBgrvMbffs)
![Personal Checklist Page](https://photos.google.com/photo/AF1QipO02uTLvNUXKKQKmLEp8K-RGv3QOXJt1SW6mEGO)
![Mobile Pages](https://photos.google.com/photo/AF1QipOxHQOElJk24sW9dmU8QJCFlYXwCNXqKLnnJOi1)


##### [ Back to Top ](#table-of-contents)

# Agile Development

Agile methodologies were used to plan and prioritise tasks according to MoSCoW and to aid with the assigning of tasks.

## Kanban Board Overview
As per [Kanban Board](https://github.com/users/craigallendev/projects/5/views/1)
Tasks that had a relationship were linked to heighten task tracking visualisation.

- **No Status:** This section contained all the tasks prior to being assigned to the workflow.
- **Backlog:** This section contained all the tasks and user stories that were yet to be prioritized for implementation.
- **In Progress:** Work in progress was tracked here, indicating tasks actively being worked on.
- **Done:** Tasks that were completed successfully were moved to this column.
- **Future Features:** Ideas and tasks earmarked for future development were kept in this section for consideration in subsequent iterations.

### User Stories Integration

As user stories are a core of Agile Methodology they were used to define the tasks on the KanBan board.  This is to ensure that the project can match with user requirements.

### Task Management

The Kanban board has been used to both track user stories and to ensure that there was a list of tasks that could be monitored and velocity measured against.  This enabled us to break down larger tasks in to more manageable objectives.

## User Stories Overview

### {EPIC} Setup Django to a standard
As a  **registered user**  I can  **follow a checklist**  so that **all Django Instances are to a defined standard **

-   **Acceptance criteria 1:**  Create signup ability:  [User Registration & Authentication #2](https://github.com/craigallendev/django-checklist/issues/2)  [User Login #3](https://github.com/craigallendev/django-checklist/issues/3)
    
-   **Acceptance criteria 2:**  Create Django Setup Checklist:  [View Essential Steps #6](https://github.com/craigallendev/django-checklist/issues/6)
    
-   **Acceptance criteria 3:**  Allow progress monitoring through checklist:  [Progress Tracker #9](https://github.com/craigallendev/django-checklist/issues/9)  [Mark Checklist Items Completed #5](https://github.com/craigallendev/django-checklist/issues/5)
    
-   **Acceptance criteria 4:**  Allow notes to be added to steps  [Create own notes #8](https://github.com/craigallendev/django-checklist/issues/8)  [Add a Custom Step #11](https://github.com/craigallendev/django-checklist/issues/11)  [Delete a Custom Step #12](https://github.com/craigallendev/django-checklist/issues/12)

##### [ Back to Top ](#table-of-contents)

# Features Implemented

## Home Page:


## Footer/Nav Bar:

  
## Django Task List


## User Specific Task list
  

## Additional Security Features:

- Prevention of users editing others lists



# Future Features

##### [ Back to Top ](#table-of-contents)

# Technology Stack

- HTML - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for (an) event listener on (a) buttons
- Django - framework used to build this project
- Bootstrap 5 - front end framework used for styling
- PostgreSQL - used as the database
- Balsamiq - for wireframes
- GitHub - for storing the code and for the Kanban board
- Heroku - for hosting and deployement of this project
- Git - for version control


# Known Bugs


##### [ Back to Top ](#table-of-contents)

# Resources

##### [ Back to Top ](#table-of-contents)
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NjMyNzg2MDgsMTczMTc3NjkzMF19
-->