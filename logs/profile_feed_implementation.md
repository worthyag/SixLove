# How I will go about implementing the profile page.

---

**Fri 22nd Dec 23**

- I will create 2 div elements, one that will house the feed and one that will house the awards (they will be given corresponding classes/id).
- Based on what view is toggled (Feed/Achievements) each respective div will toggle between display and no display.
  - This means that I must add corresponding onClick functions to the buttons that will toggle the views.
- I will generate the post boxes using javascript.
  - They will be generated based on the number of post that the user has (which is stored somewhere (db)).
- The image for each corresponding post will be displayed (the id for the corresponding post will be stored).
- When a user clicks on a post, either a full screen pop up will be displayed or I'll overlay the post on top of the page.
- The post will display the image, caption, comments and likes. Users will be able to like and comment etc.
- The user can exit the post by going back or pressing the close button.