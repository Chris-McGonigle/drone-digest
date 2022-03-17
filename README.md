# Drone Digest

Drone Digest is a public chat forum style website aimed at both individuals and commercial enterprises with interests in Unmanned Aerial Vehicles (UAVs), more commonly known as drones.



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
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)


## Site Design Considerations



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

![Desktop](/images/readme-images/wireframes/home-page.png)

* Opened thread

![Desktop](/images/readme-images/wireframes/opened-thread.png)


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


#### Navigation Search Bar


#### Logged In Status


#### Subject Filtering


#### Post Thread Window


#### Recent Activity Thread


#### View Thread Window


#### Thread Participants




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

<br>

[Back to top](#table-of-contents)

<br>

## Bugs

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

<br>

[Back to top](#table-of-contents)

<br>
