# **Table of Contents**

- [1 The Design Problem](#1-the-design-problem)
- [2 Requirements](#2-requirements)
  - [2.1 Functional Requirements](#21-functional-requirements)
  - [2.2 Non-Functional Requirements](#22-non-functional-requirements)
  - [2.3 Restrictions](23-restrictions)
- [3 Categorising and Prioritising Requirements](#3-categorising-and-prioritising-requirements)
  - [3.1 Backend Vs Frontend](#31-backend-vs-frontend)
  - [3.2 Classes and Modules](#32-classes-and-modules)
    - [3.2.1 Backend](#321-backend)
    - [3.2.2 Frontend](#322-frontend)
- [4 The Design](#4-the-design)

# 1 The Design Problem

I am going to create a tennis training system aimed primarily at novices (beginners in tennis). The system will offer tennis training in the form of structured videos following the principles of TNLP (explained in my report). The system will track tennis training / fitness workouts across sessions. The system will provide access to resources to support learning and improved technique. The system will give advice about the exercises to perform pre training, per session, it will advice about training schedules, and expectations for future sessions. The system will provide support when warming up, and advice on what to do based on certain input values (unable to understand a certain shot or successfully hit a backhand).

The system will keep track of a users progress. The system will teach at least three basic components of tennis. The system will have login / logout functionality, which enable users to login and keep track of their progress and sessions. The system will store the users username, password, email, and date of birth. Users will be able to add friends and follow each other. If they add a friend and that friend accepts the invite, they will automatically be following each other. Users can follow those who are not their friends if their profile is not private. The idea is to create a community of tennis enthusiasts, who can motivate each other. Users can set their account to public or private when they sign up and they will have the option to change it whenever. They can share updates to their profile feed. If their account is public their posts will be available to the community stream or if private only on their profile.

 A users training program will be made out of a collection of tennis videos / workouts, explanations, tennis sessions, and quizzes. However, users will have access to the complete set of training videos on the `videos` tab / section of the system. They can then search for specific videos, or filter then based on predefined tags.

The system will set a training schedule based on the available time that the user gives them (e.g. Monday and Tuesday evenings), the users can also pick their intensity. The system will allow users to visualise their progress. The system should also allow those who are not logged in to view training (?). There is a possibility for gamification. The most important functionality is that users should be able to learn their different tennis shots and track their progress- that is fundamental. Anything else can be added and discovered after user testing and further market research.

There will be a videos tab, an infos tab, a personal profile tab, the feed / community tab, and an activity tab. Settings and other customisation will be available from their personal profile tab. Their personal profile tab will display their training schedule and past sessions and also their posts. They can toggle between the two. Users can comment on their posts and others, they can also like posts, and delete their comments.

# 2 Requirements

## 2.1 Functional Requirements

1. Keep track of workouts across sessions.
2. The ability to access resources to support learning and improving technique (and other general support).
3. Keep track of user progress.
4. Login / logout functionality.
5. Store the username, password, email, name, etc of the users (securely).
6. Update and view their profile (and also set its visibility).
7. A collection of tennis training and workout videos that are tagged and can be searched and filtered.
8. A collection of tennis info / learning resources that are tagged and can be searched and filtered.
9. Interact with posts (like, remove like, comment, delete comments, delete post, post).
10. The user will have the ability to modify their generated training schedule.
11. Tailored training schedule based on user input.
12. Recommendations based on the user and their friends.
13. Share updates to a live feed or their profile.
14. Visualise user progress.
15. The ability to follow or friend other users.
16. Possible gamification.

## 2.2 Non-Functional Requirements

1. The application should be accessible to a wide variety of users (all novices) and use-cases.
   
   - Need to consider input (e.g. multitouch, sensitivity, button sizes.)
   
   - The application should visualise information in a clear and succinct way.
   
   - The application should be capable of tracking and retrieving data from multiple sessions.

2. The application should utilise a sensible technology stack that supports data collection, retrieval and visualisation over a sustained period e.g. six weeks minimum.

## 2.3 Restrictions

- Cost
- Time-to-market

# 3 Categorising and Prioritising Requirements

## 3.1 Backend Vs Frontend

1. **Keep Track of Workouts Across Sessions:**
   
   - **Backend:** Store and manage workout data in the database (Django models).
   - **Frontend:** Display the workout history, allow users to input new workouts, and visualise workout data.

2. **Access Resources for Learning and Improving Technique:**
   
   - **Backend:** Serve resources through API endpoints.
   - **Frontend:** Display resources, allow filtering and searching, and handle user interactions.

3. **Keep Track of User Progress:**
   
   - **Backend:** Store and manage user progress data.
   - **Frontend:** Visualise progress through charts, graphs, or other UI components.

4. **Login/Logout Functionality:**
   
   - **Backend:** Handle user authentication and session management.
   - **Frontend:** Provide user interfaces for login and logout actions.

5. **User Registration and Profile Management:**
   
   - **Backend:** Manage user registration, profile updates, and data storage.
   - **Frontend:** Provide forms for user registration and profile management.

6. **Collection of Tennis Training Videos and Learning Resources:**
   
   - **Backend:** Store video and resource metadata, serve through API.
   - **Frontend:** Display and organise videos/resources, enable searching and filtering.

7. **Interact with Posts:**
   
   - **Backend:** Manage posts, comments, and interactions.
   - **Frontend:** Enable users to like, comment, and interact with posts.

8. **Modify Generated Training Schedule and Tailored Training Schedule:**
   
   - **Backend:** Handle logic for generating and modifying training schedules.
   - **Frontend:** Display schedules, allow modifications, and provide user interfaces for customisation.

9. **Recommendations Based on User and Friends:**
   
   - **Backend:** Implement recommendation algorithms.
   - **Frontend:** Display and present recommendations.

10. **Share Updates to Live Feed or Profile:**
- **Backend:** Manage user-generated content, posts, and feeds.

- **Frontend:** Allow users to create posts, update feeds, and interact with shared content.
11. **Visualise User Progress:**
    
    - **Backend:** Provide data for progress visualisation.
    - **Frontend:** Implement charts, graphs, or visual components to display progress.

12. **Follow or Friend Other Users:**
    
    - **Backend:** Manage user relationships and connections.
    - **Frontend:** Provide interfaces for following/friending users.

13. **Gamification:**
    
    - **Backend:** Implement gamification logic and rules.
    - **Frontend:** Display gamification elements and progress. 

*The priority of these requirements can be viewed in my accompanying kanban board.*

## 3.2 Classes and Modules

The goal is to come up with classes and functions, and then group them into modules / libraries. Some modules / libraries may only contain one class, the idea is to create something similar to modules in python. In python, modules / libraries group functions and classes that perform similar functions together. I may also just keep them as classes it depends on the number of classes, and what seems suitable for the project.

User

- `id`: int

- `name`: dict => `{"fname": "forename", "lname": "surname" }`

- `email`: str / email

- `dob`: date

- `credentials`: dict => `{"username": username, "password": password}`

- `loggedin`: boolean

- `friend_count`: int

- `follower_count`: int

- `following_count`: int

Authentication

- `user_id`: int 

- `username`: str 

- `password`:str

TrainingResources

Progress

ProfileManagement

LearningResources

Posts

- `user_id`: int

- `likes`: dict 

- `comments`: dict => `[{"user_id": "comment text"}]`

- `comment_count`: int => `len(comments)`

Schedule

- `user_id`: int

UserRelations

Recommendations

Gamification





### 3.2.1 Backend

1. **Workouts Management**
   
   - **Class:** `Workout` (Django model)
   - **Module:** `models.py`
   - **Functions/Methods:**
     - `create_workout`
     - `get_user_workouts`
     - `calculate_workout_statistics`

2. **Resources for Learning**
   
   - **Class:** `LearningResource` (Django model)
   - **Module:** `models.py`
   - **Functions/Methods:**
     - `get_learning_resources`
     - `filter_learning_resources`

3. **User Progress**
   
   - **Class:** `UserProgress` (Django model)
   - **Module:** `models.py`
   - **Functions/Methods:**
     - `update_user_progress`
     - `get_user_progress`

4. **Authentication and Sessions**
   
   - **Class:** `User` (Django model)
   - **Module:** `views.py`
   - **Functions/Methods:**
     - `register_user`
     - `login_user`
     - `logout_user`
     - `update_user_profile`

5. **Video and Resource Management**
   
   - **Class:** `TrainingVideo` (Django model)
   - **Module:** `models.py`
   - **Functions/Methods:**
     - `get_training_videos`
     - `filter_training_videos`

6. **Posts and Interactions**
   
   - **Class:** `Post` (Django model)
   - **Module:** `models.py`
   - **Functions/Methods:**
     - `create_post`
     - `like_post`
     - `edit_post`
     - `comment_on_post`

7. **Training Schedule**
   
   - **Class:** `TrainingSchedule` (Django model)
   - **Module:** `models.py`
   - **Functions/Methods:**
     - `generate_training_schedule`
     - `modify_training_schedule`

8. **Recommendation Engine**
   
   - **Class:** `RecommendationEngine`
   - **Module:** `recommendations.py`
   - **Functions/Methods:**
     - `generate_recommendations`

9. **User Relationships**
   
   - **Class:** `UserRelationship` (Django model)
   - **Module:** `models.py`
   - **Functions/Methods:**
     - `follow_user`
     - `unfollow_user`

10. **Gamification**
    
    - **Class:** `GamificationEngine`
    - **Module:** `gamification.py`
    - **Functions/Methods:**
      - `calculate_score`
      - `award_badge`

### 3.2.2 Frontend

1. **Workout History and Input**
   
   - **Component:** `WorkoutHistory`
   - **Module:** `WorkoutHistory.js`
   - **Functions/Methods:**
     - `renderWorkoutHistory`
     - `handleAddWorkout`

2. **Learning Resources Display**
   
   - **Component:** `LearningResources`
   - **Module:** `LearningResources.js`
   - **Functions/Methods:**
     - `fetchLearningResources`
     - `renderLearningResources`

3. **User Progress Visualisation**
   
   - **Component:** `UserProgressChart`
   - **Module:** `UserProgressChart.js`
   - **Functions/Methods:**
     - `fetchUserProgress`
     - `renderProgressChart`

4. **Authentication UI**
   
   - **Component:** `AuthForm`
   - **Module:** `AuthForm.js`
   - **Functions/Methods:**
     - `renderLoginForm`
     - `renderRegistrationForm`

5. **Video and Resource Display**
   
   - **Component:** `TrainingVideos`
   - **Module:** `TrainingVideos.js`
   - **Functions/Methods:**
     - `fetchTrainingVideos`
     - `renderTrainingVideos`

6. **Post Interaction UI**
   
   - **Component:** `PostInteraction`
   - **Module:** `PostInteraction.js`
   - **Functions/Methods:**
     - `renderPost`
     - `handleLike`
     - `handleComment`

7. **Training Schedule UI**
   
   - **Component:** `TrainingScheduleViewer`
   - **Module:** `TrainingScheduleViewer.js`
   - **Functions/Methods:**
     - `fetchTrainingSchedule`
     - `renderTrainingSchedule`

8. **Recommendations Display**
   
   - **Component:** `RecommendationsPanel`
   - **Module:** `RecommendationsPanel.js`
   - **Functions/Methods:**
     - `fetchRecommendations`
     - `renderRecommendations`

9. **User Relationship UI**
   
   - **Component:** `UserRelationshipManager`
   - **Module:** `UserRelationshipManager.js`
   - **Functions/Methods:**
     - `renderFollowButton`
     - `handleFollow`

10. **Gamification Display**
    
    - **Component:** `GamificationPanel`
    - **Module:** `GamificationPanel.js`
    - **Functions/Methods:**
      - `fetchUserScore`
      - `renderBadges`


