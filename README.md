# Drone Digest

Drone Digest is a public chat forum style website aimed at both individuals and commercial enterprises with interests in Unmanned Aerial Vehicles (UAVs), more commonly known as drones.

![Desktop View](/images/readme-images/images/desktop.png)

![Mobile View](/images/readme-images/images/mobile.png)


Please note the [Am I responsive](http://ami.responsivedesign.is/#) website would not render a display due to X-Frame Origins being set as advised in project walkthroughs [link](/images/readme-images/images/responsive.JPG)

The pace of change in the UAV market is extraordinary, with new regulations and equipment entering the market numerous times a year. The UAV market is predicted to be worth $63.6 billion by 2025 [*(Source)*](https://www.businessinsider.com/drone-industry-analysis-market-trends-growth-forecasts?r=US&IR=T) and will only get larger given technological advances in the use of drones for agriculture, construction and law enforcement to name but a few.

Until now, current offerings for those interested in having a discussion about UAVs are spread far and wide, but only catering to a small niche of the market, for example particular types of aircraft, or split by commercial and hobbyist lines.

The Drone Digest aims to provide a 'one stop shop' for all of these strands, bringing together experience from across the sector so seasoned and budding UAV pilots alike can share experiences, expertise and keep up to date with the latest changes in this ever evolving and growing sector.

You can view a live version of the [website](http://drone-digest.herokuapp.com/) 

## Table of Contents

1. [Site Design Considerations](#site-design-considerations)
    * [User Stories](#user-stories)
        * [EPIC 1 - User Accounts](#epic-1---user-accounts)
        * [EPIC 2 - Message Boards](#epic-2---message-boards) 
        * [EPIC 3 - Post Interactions](#epic-3---post-interactions)
    * [Wireframes](#wireframes)
    * [Project Management](#project-management)
2. [Data Models](#data-models)
3. [Features](#features)
    * [Initial Deployment Features](#initial-deployment-features)
    * [Future Features](#future-features)    
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
    * [Bugs](#bugs)
    * [User Story Testing](#user-story-testing)
        * [EPIC 1 Testing](#epic-1-testing)
        * [EPIC 2 Testing](#epic-2-testing) 
        * [EPIC 3 Testing](#epic-3-testing)
6. [Deployment](#deployment)
7. [Credits](#credits)


## Site Design Considerations

From the outset, I wanted to provide a bright enticing colour scheme, with modern fonts to try and convey a sense of excitement, and to show that that the UAV world is modern and fun. Current forums online have a very bland colour scheme, normally just white backgrounds with black text.

It was also important however to ensure that there was enough contrast between colours used for backgrounds and text. 

I decided to go wih a blue/green pallette (Cello, #364958 and Paradiso, #55828B) for backgrounds, which modern colour theory psychology states provides calming attributes. 

A shade of orange was used (International Orange, ##FF5400 for buttons and borders to help make these sections pop out, and highlight that users should direct their gaze to these areas. 

Text color selected was Granny Apple (#C9E4CA), for it's contrast against the darker background, but still in keeping with the overall blue green feel I was trying to achieve. Black was used sparsely where even more legibility was required, for example in form input fields.

Font selection was more diffcult, I was wanted something with a futuristic feel for my headings, to try and envoke how modern, fast paced and ever changing the UAV world is. To this end I chose [Orbitron](https://fonts.google.com/specimen/Orbitron). 

This would have been too much to use throughout the entire site so to ensure the thread content remained legible I chose [Source Sans Pro](https://fonts.google.com/specimen/Source+Sans+Pro) for my body text. I feel using the fonts in this way makes a good comprimise between legibility and trying to envoke an emotional response in the user.


### User Stories

#### EPIC 1 - User accounts

1. As a User, I want to create an account using my email address so that I can create threads and comment on existing posts.

2. As a User, I want to create an account using my social media log in so that I can create threads and comment on existing posts.

3. As a User, I want to be able to view posts without logging in so that I can quickly catch up on conversation I have been involved in.

4. As a User, I want to be able to reset my password  so that I can still access my account if I forget it.

5. As a User, I want to be able to create a basic profile including a profile picture so that I can tell other users a little about myself.

6. As a User, I want to be able to see a history of posts I have made in my profile so that I can easily reference old conversations.

7. As a User, I want to be abe to see who is currently online so that I can interact with friends made on the platform in real time.

8. As a User, I want to be able to message other users so that I can interact privately with individuals.

9. As a User, I want to be able to report accounts so that I can highlight behaviour that goes against the forum rules.

10. As a Site Admin, I want to be able to create and assign moderators so that I can spread the workload of approving comments.

<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 2 - Message boards

1. As a User, I want to be able to view a list of threads so that I select one to read.

2. As a User, I want to be able to filter threads by topic so that I select a topic that interests me.

3. As a User, I want to see a count of activity on a thread so that I can see the number of replies and views on a thread.

4. As a User, I want to be able to expand a thread so that I can view all of the posts made related to it.

5. As a User, I want to be able to see a list of who has participated in a thread so that I can easily see people I have interacted with before and new users.

6. As a User, I want to be able to create a new thread from the homepage so that I don’t have to go into a topic to create one.

7. As a User, I want to be able to search for topics and threads and users so that I easily find people or topics that interest me.


<br>

[Back to top](#table-of-contents)

<br>


#### EPIC 3 - Post interactions

1. As a User, I want to be able to create a new post so that I can start a conversation with other people.

2. As a User, I want to be able to comment on existing posts so that I can be involved in discussions.

3. As a User, I want to be able to edit existing posts that I have made so that I can amend any mistakes I may have made.

4. As a User, I want to be able to delete posts that I have made so that I manage my content.

5. As a User, I want to be able to see when a post was created or updated so that I can see how recent thread activity was.

6. As a User, I want to be able to add images to a post so that I so I can share examples or illustrate my point.

7. As a User, I want to be able to click on a post author so that I can find out further information about them or other posts that they have made.

8. As a User, I want to be able to 'like' a post so that I can interact with the content and see which are the most popular posts.

9. As a Site Admin, I want to be able to approve or disprove posts so that I can ensure all posts adhere to the site guidelines.

10. As a Site Admin, I want to be able to read, update and delete posts so that I can ensure all posts adhere to the site guidelines.


<br>

[Back to top](#table-of-contents)

<br>


### Wireframes

* Homepage

![Desktop & Landscape Tablet](/images/readme-images/wireframes/home-page.png)

* Opened thread

![Desktop & Landscape Tablet](/images/readme-images/wireframes/opened-thread.png)


* Mobile and Portrait Tablet view

![Mobile and Portrait Tablet](/images/readme-images/wireframes/mobile.png)


<br>

[Back to top](#table-of-contents)

<br>

### Project Management

The Kanban Boards feature of Github Projects was used as the project management tool during the production of this website. User stories were assigned two labels, one an EPIC label, and the second using the MoSCoW prioritisation technique.

EPICS were defined as User Accounts, Message Boards Overview, and Post Interactions. User Stories were then generated and designated as Must Have, Should Have, Could Have and Won't Have.

Must Have User stories were prioritised for completion first, and these were all implemented by project end. Once completed tasks were moved to the Done pile. Due to a major bug on deployment, one completed User story was moved back into the To Do catergory. This is explained in full in the [Bugs](#bugs) portion of this file. 

You can view the [Kanban Boards](https://github.com/Chris-McGonigle/drone-digest/projects/1?fullscreen=true) to see the project progress. Unfinished tasks would be aimed to be completed in future iterations.


<br>

[Back to top](#table-of-contents)

<br>

## Data Models

Three data models were used for this project as follows:

### Topic Model

| Key | Name | Type |
|---|---|---|
| pk | Subject | Charfield |

### Thread Model

| Key | Name | Type |
|---|---|---|
| fk | author | User model |
| fk | subject | Topic model |
|  | name | Charfield (max-length = 150)|
| | description | TextField |
| Many to Many | droners | User model |
| | Updated date | DateTimeField |
| | Created date | DateTimeField |


### Post Model

| Key | Name | Type |
|---|---|---|
| fk | author | User model |
| fk | thread | Thread model |
| | body | TextField |
| | Updated date | DateTimeField |
| | Created date | DateTimeField |


<br>

[Back to top](#table-of-contents)

<br>

## Features

### Initial Deployment Features

#### Navigation Bar

The nav bar holds the site logo which hyperlinks back to the homepage from all other site pages. It also holds the site serach bar and the Log in/ Out link.

![Nav Bar](/images/readme-images/images/nav.JPG)

#### Search Bar

The site search bar serach the entire site via either subject, name or description. It will return results on full or part parameters. The search bar utilises the Q queryset object imported from Django models to handle complex queries.

![Search Bar](/images/readme-images/images/search.JPG)


#### Logged In Status

Once logged in, the logged in status offers a greeting to the user to confirm that they are logged in.

![Logged In Status](/images/readme-images/images/log.JPG)

#### Subject Filtering

A User can select a thread subject of their choice from the menu on the left (or through the pop up menu on mobile). A list of relevant threads is then displayed to the user on that subject. The thread counter also updates with the number of threads in that subject. By selecting 'All' the filter is removed and shows all available threads.

![Subject filtering](/images/readme-images/images/filter.JPG)


#### Post Thread Window

The post thread window on the homepage shows the latest threads created in chronilogical order. It provides the thread title, which links to the main details of the thread, the author, the thread subject, and the thread description.

The thread author, when logged in, is also able to edit or delete the thread from this window. Threads not started by the author are not available to them to the Edit and Delete Links are hidden for them.

![Thread Window Logged In](/images/readme-images/images/thread-login.png)

If a user is not logged in, these edit and delete links are removed, but the user can still view the thread details.

![Thread Window Not Logged In](/images/readme-images/images/thread-logout.png)


#### Recent Activity Thread

The recent activity thread lists the most recent comments on thread posts. It is designed to help site engagement by showing a user active conversations. By displaying the time, as well as the room details it shows a user how active the site is. For display purposes only the first 50 characters of the comment is displayed.

This added feature is only avaiable on desktop. The decision was taken due to screen size restrictions and the thought that having this as a pop out window similar to the Browse Subject window would not add much to the mobile experience. This could be achieved in future by hosting activity om its own html page and inserting on the homepage via templating for desktop. It does however appear on larger tablets in landscape mode. 

![Recent Activity Thread](/images/readme-images/images/activity-thread.png)


#### View Thread Window

When a thread is selected on the home page, the thread view window opens. It shows a history of the current thread, with comments under it listed with most recent first, and how long ago they were added. A user can also add a comment using the text box provided.

When logged in, a user has the ability to delete their own comment. A decision was taken not to allow the editing of comments to ensure the continuity of conversation, and to be sure a proper history of the conversation is kept. 

If editing was allowed, a user could come in after the fact and change their comment to something out of context and there is currently no way to show that a coomment has been edited. 

If in future the ability to show a comment was edited, this functionality could be introduced, but at present it was deemed to be better not to have this function.

![Thread Logged On](/images/readme-images/images/view-thread-log-in.JPG)

When a user is not logged in, they are still able to view the thread details, but the option to comment is removed. This allows people to browse the site without the need for log in, for example of someone has asked a question and pops baack to see if they have had any replies, this functionality allows them to do so without logging in.

![Thread Not Logged In](/images/readme-images/images/view-thread-log-out.JPG)


#### Thread Participants

Particpants in a thread, or "droners" are shown in this window. The thread author is shown as the original poster asgain, and as different users add comments, their name is added to the list. This was added to help generate a sense of community, and that people can see prevalent posters, and people who may be able to help. In future these would also be hyperlinks to a users indiviudal profile page.

![Droners](/images/readme-images/images/participants.jpg)


#### Site Footer

The site folder holds social media links and a link to the developers Github, These could be tailored to link to whatever required in a real world situation.

![Site Footer](/images/readme-images/images/footer.JPG)

<br>

[Back to top](#table-of-contents)

<br>

### Future Features

1. The ability to host images was a feature up until deployment, when a bug negated this ability. This would be added in a future iteration. This issue is detailed in the [bugs](#bugs) section.

2. Single Sign On via social media or Google accounts, and now also Apple ID would be a feature to be included in next deployments.

3. An activty on thread, such as total views and reply count could be added in the next iteration realatively easily. Time on this iteration did not allow for this to be implemented.

4. Password reset functionality would be of benefit in the future.

5. A User profile which would include post history would add to the overall UX of the site. This would be also be a feature I would be very keen to add.

6. A private messaging facility between users would be advantageous. It would help to foster a sense of community in the forum and would help like minded people to further develop friendships. 

7. The ability to see a Users online status could help to further develop these relationships, and would allow users to interact more in real time. Again this is open to abuse and bullying so would have to be monitored very carefully. 

8. A robust reporting mechanism should be in place as well before the private messaging facility would be implemented for general site safety and to limit the chance of personal abuse would be advisable. Along with this, comment reporting would also be added to ensure all conversations ahdere to general rules of civility. 

9. The ability to 'like' comments could be added. This was a deliberate choice to however to not include at this point. Likes can sometimes be detrimental to indiviudal users and there has been countless research into how like counts impact self-esteem, the general consensus being that social comparison has an undeniable impact on it, particularly for young people. This could be added though if enough users requested this feature.

 

<br>

[Back to top](#table-of-contents)

<br>

## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the site markup.
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used to style the HTML content.
* [Javascript](https://en.wikipedia.org/wiki/JavaScript) was used for the Browse Subjects pop up.
* [Python3](https://en.wikipedia.org/wiki/Python_programming_language) and the Django Framework was the language used to produce the databases.
* [Black](https://github.com/psf/black) was used to format the Python Code
* [Balsamiq](https://balsamiq.com/) was used to produce the site wireframes.
* [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) was used to create the site icon.
* [Font Awesome](https://fontawesome.com/) was used for the site icons.
* [Google Fonts](https://fonts.google.com/) provided all of the fonts used on the site.
* [Firefox Developer tool](https://developer.mozilla.org/en-US/docs/Tools) was used to test site responsiveness and to test code.
* [Google Chrome Developer tools](https://developer.chrome.com/docs/devtools/) was used to test site responsiveness and to test code.
* [Safari Developer tools](https://support.apple.com/en-gb/guide/safari/sfri20948/mac) was used to test site responsiveness and to test code.
* [Github](https://github.com/Chris-McGonigle) was used as the repository hosting service.
* [Gitpod](https://www.gitpod.io/) was used as the Code Editor for the site.
* [W3C Markup](https://validator.w3.org/) and [Jigsaw validation](https://jigsaw.w3.org/) tools were used to validate the HTML and CSS used.
* [JSHint](https://jshint.com/) was used to validate the javascript used on site.
* [Pep8 Online](http://pep8online.com/) was used to validate the Python code.
* [Prettier](https://prettier.io/) was used to format the HTML Code
* [Heroku](https://www.heroku.com) was used to deploy the application.

<br>

[Back to top](#table-of-contents)

<br>

## Testing

A dedicated testing section covering validator and manual testing can be found in the [testing.md](/testing/testing.md) documentation

### Bugs

On final deployment, a day before deadline and prior to my final mentor meeting, a major bug was discovered with my initial choice of text editor [CKEditor](https://ckeditor.com/).

CKEditor had been chosen as it allowed the embedding of images and video within the message body. This was deemed to be beneficial as the developer would not have to take up Cloudinary storage space hosting these files, and instead users could use sites such as [Imgur](https://imgur.com/) and [YouTube](https://www.youtube.com/) and link from there.

The editor worked perfectly in development. However on deployment, the entire comment window was not rendered, making it in effect useless as a user could not create a new thread. The below errors were recevied in the console:

![CKEditor Error](/images/readme-images/images/capture-error.JPG)

I tried numerous fixes such as adding new script tags as suggested in Stack Overflow, and a complete rebuild following this tutorial by [Selmi Tech](https://youtu.be/Zuatckos9Pg) and this by [Codemy](https://youtu.be/mF5jzSXb1dc), neither of which were successful.

I then tried following again the instructions on the [CKEditor documentation](https://github.com/django-ckeditor/django-ckeditor/), double checking things like the static base path, and that all settings in settings.py were correct, and that urls.py was correctly updated.

Finally I contacted Tutor Support. Unfortunately Tutor Support could not fix this issue either, and it was suggested that there was an issue with CKEditor accessing its static files through Cloudinary. 

To this end I had to quickly rebuild this section of the site using Summernote, but as mentioned previously this meant that my inline image and video hosting capabilities were lost at this time. 

As my project deadline was less than 24 hours away, and I had to fully test the site time ran out to find other ways to reintroduce these features, but it is something I would like to look at again in the future.

<br>

[Back to top](#table-of-contents)

<br>

### User Story Testing

#### EPIC 1 Testing

1. As a User, I want to create an account using my email address so that I can create threads and comment on existing posts.
    * TEST PASSED

2. As a User, I want to create an account using my social media log in so that I can create threads and comment on existing posts.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

3. As a User, I want to be able to view posts without logging in so that I can quickly catch up on conversation I have been involved in.
    * TEST PASSED

4. As a User, I want to be able to reset my password  so that I can still access my account if I forget it.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

5. As a User, I want to be able to create a basic profile including a profile picture so that I can tell other users a little about myself.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

6. As a User, I want to be able to see a history of posts I have made in my profile so that I can easily reference old conversations.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

7. As a User, I want to be abe to see who is currently online so that I can interact with friends made on the platform in real time.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

8. As a User, I want to be able to message other users so that I can interact privately with individuals.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

9. As a User, I want to be able to report accounts so that I can highlight behaviour that goes against the forum rules.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

10. As a Site Admin, I want to be able to create and assign moderators so that I can spread the workload of approving comments.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 2 Testing

1. As a User, I want to be able to view a list of threads so that I select one to read.
    * TEST PASSED

2. As a User, I want to be able to filter threads by topic so that I select a topic that interests me.
    * TEST PASSED

3. As a User, I want to see a count of activity on a thread so that I can see the number of replies and views on a thread.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

4. As a User, I want to be able to expand a thread so that I can view all of the posts made related to it.
    * TEST PASSED

5. As a User, I want to be able to see a list of who has participated in a thread so that I can easily see people I have interacted with before and new users.
    * TEST PASSED

6. As a User, I want to be able to create a new thread from the homepage so that I don’t have to go into a topic to create one.
    * TEST PASSED

7. As a User, I want to be able to search for topics and threads and users so that I easily find people or topics that interest me.
    * TEST PASSED


<br>

[Back to top](#table-of-contents)

<br>


#### EPIC 3 Testing

1. As a User, I want to be able to create a new post so that I can start a conversation with other people.
    * TEST PASSED

2. As a User, I want to be able to comment on existing posts so that I can be involved in discussions.
    * TEST PASSED

3. As a User, I want to be able to edit existing posts that I have made so that I can amend any mistakes I may have made.
    * TEST PART PASSED - Users can edit original thread post but not comments to ensure continuity of conversation history

4. As a User, I want to be able to delete posts that I have made so that I manage my content.
    * TEST PASSED

5. As a User, I want to be able to see when a post was created or updated so that I can see how recent thread activity was.
    * TEST PASSED

6. As a User, I want to be able to add images to a post so that I so I can share examples or illustrate my point.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

7. As a User, I want to be able to click on a post author so that I can find out further information about them or other posts that they have made.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

8. As a User, I want to be able to 'like' a post so that I can interact with the content and see which are the most popular posts.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

9. As a Site Admin, I want to be able to approve or disprove posts so that I can ensure all posts adhere to the site guidelines.
    * TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

10. As a Site Admin, I want to be able to read, update and delete posts so that I can ensure all posts adhere to the site guidelines.
    * TEST PASSED

<br>

[Back to top](#table-of-contents)

<br>

## Deployment

Local deployment was carried out using the Command Line Interface. to enable this the following steps were carried out:

1. Create a repository on GitHub.
2. Clone the repository on your chosen source code editor (GitPod) using the clone link.
3. Open the terminal within GitPod
4. Enter "python3 manage.py runserver into the terminal.
5. Go to local host address on my web browser.
6. All locally saved changes will show up here.

For the final deployment to Heroku, the following was carried out:

1. Uncomment the PostgreSQL databse from settings.py file.
2. Set debug = False in settings.py file.
3. Commit and push all files to GitHub
4. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
5. In the deploy tab, go to the manual deploy sections and click deploy branch.

<br>

[Back to top](#table-of-contents)

<br>

## Credits

1. Dummy text for display purposes for the threads was taken from a number of existing forums such as [mavicpilots.com](https://mavicpilots.com/), [inspirepilots.com](https://inspirepilots.com/threads/remote-controller-charging-issues.24678/)

2. I used this [article](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html) on how to use Q for complex queries to power the search functionality on the site.

3. [HTMLCSSColor](https://www.htmlcsscolor.com/) and [Coolors](https://coolors.co/?home) was used to help pick colour pallettes.

4. Core functionality of the site was based on the Code Institute walkthrough, I think therefore I blog, and also tutorials by [Codemy](https://youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) and [Traversy](https://youtu.be/PtQiiknWUcI)

5. Tutorials by [StudyGyann](https://youtu.be/uJp4PaDkux0) and [Pretty Printed](https://youtu.be/VYs-u0g__1A) were used to help in the styling of form fields.

6. I also used tutorials by [Academind](https://youtu.be/t7DrJqcUviA), [Tech With Tim](https://youtu.be/sm1mokevMWk) and [Problem Solving Point](https://youtu.be/QLL4KzFMfVw) to help further my understanding of the framework.

<br>

[Back to top](#table-of-contents)

<br>
