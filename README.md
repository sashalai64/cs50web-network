# CS50's Web Programming with Python and JavaScript

# Project 4 - Network
[Project Description](https://cs50.harvard.edu/web/2020/projects/4/network/)

## Overview
This project is a social network platform built using Python, JavaScript, HTML, and CSS. It allows users to interact with others by creating posts, following other users, and liking posts.

## Features
- **New Post**
  - Signed-in users can create new text-based posts by filling in a text area and clicking a submit button.

- **All Posts**
  - Users can view all posts from all users, with the most recent posts displayed first.
  - Each post displays the username of the post, the content of the post, the date and time of the post, and the number of likes the post has received.
    
- **Profile Page**
  - Clicking on a username takes the user to that user's profile page.
  - The profile page displays the number of followers the user has, the number of users the user is following, and all posts by the user in reverse chronological order.
  - For signed-in users viewing another user's profile, a “Follow” or “Unfollow” button is available to toggle the follow status.

- **Following**
  - Accessible only to signed-in users.
  - The “Following” link in the navigation bar shows posts from users that the current user follows.

- **Pagination**
  - Posts are displayed 10 per page.
  - If there are more than ten posts, a “Next” button appears to navigate to older posts, and a “Previous” button allows navigation to newer posts.
    
- **Edit Post**
  - Users can edit their own posts by clicking an “Edit” button.
  - Users can save the edited post, and the changes are updated asynchronously.
  - Security measures ensure users cannot edit posts of other users.

- **“Like” and “Unlike”**
  - Users can toggle the “like” status of any post.
  - The server is updated asynchronously, and the like count is displayed without reloading the page.
    
## Requirements
  - Python 3.x
  - Django

## How to Run
1. **Clone the Repository**
      ```
      git clone https://github.com/sashalai64/cs50web-network.git
      ```
      
2. **Apply migrations**
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
   
3. **Run the Server**
      ```
      python manage.py runserver
      ```
4. **Access the Application**
   
    Visit `http://127.0.0.1:8000/` in your browser.