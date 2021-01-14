# Vision

GetKraken is all about crackin into events, making sure that individuals can plan series of events as bigger groups.

Most events require some sort of tickets, which can be expensive. For true fans, a great solution is the Season Tickets that allow them to participate in every game for a fraction
of the cost. But the does not work for the average person, many people don't have the time or money to commit to every game of a team for an entire season. What many people have
chosen to pursue is buying Season Tickets as a group of friends, and splitting the individual tickets among the friends. The big problem hear is that certain events will inevitably
be more popular, so to divvy the tickets up in fair and effective manner, GetKraken offers a great way to include everyone and remove the bias.

In today's Pandemic times, planning events with large groups of people has become virtually impossible. As fear and disease seperates us, technology has developed to connect us and 
create new opportunities for new experiences. Share technology has exploded, and events have only become more and more expensive to attend. GetKraken cracks up all the awkward ice that
forms around determining who goes to which event and when. 

# Scope

We are starting from making a single series for the Seattle Kraken with the ability for multiple groups to be formed. This will require a Login to Authenticate and associate users 
with specific groups and series. This will also require the ability to create groups, create series, and progress through the actual draft with tickets. The results of the draft
and the associations between users, groups, series, and events will all need to be stored in SQL based data structures.

The strech goal is to generalize the ability for drafts of different series, starting with other sports team seasons and expanding to other types of events like Dinner Parties,
Opera Tickets, or any other ticket-utilizing event.

## Minimum Viable Product

- [ ] Populate a random draft order for the members of a given series of events
- [ ] Authenticate user logins/passwords from the login page using Django authentication
- [ ] Django backend to handle databases, RESTful API calls
- [ ] React frontend building out all the different views (Login Page, Signup Page, Create Groups Page, User Homepage, Series Page)
- [ ] SQL database to store users, events, groups, and series of events (postgreSQL, ElephantSQL, other services)
- [ ] The ability for existing users to login and see the groups/series that they pertain to
- [ ] The ability to sign up new users to application and add their credentials to the user database
- [ ] Protections based on user and ticket availability (Authorization and Authentications)
- [ ] Only the person whose turn it is can select a ticket to move from "available" to their claimed column
- [ ] The ticket must be available to be selected for a person to chose it.
- [ ] It must be the selecter's turn to choose
- [ ] Only the owner of a ticket can move it back to the "available" column
- [ ] Use of Docker to facilitate structuring and layering the Django APIs
- [ ] Use of ElephantSQL or other service for postgres SQL DB

## Stretch Goals

- [ ] even numbered draft rounds are reference order
- [ ] two step verification process to avoid mistakes when claiming ticket
- [ ] Twillio text notification to inform users of drafts progression, invitations, and deletions of series
- [ ] Auto game schedule population (use API, maybe have user select league/team)
- [ ] Add a count down clock to limit time for the selection process, automatically switch to the next member at the end of the count down
- [ ] Create an autodraft option to allow groups to rank all of their choices, and automatically sort members into respective events
- [ ] Enter rank choices with weights for optimization of the drafting algorithm
- [ ] Classify the whole page to make instances for various groups to use the same class of series simulatneously without interfering with existing instances
- [ ] Custom design page:  set up to change the logo, theme, names for different uses such as board game night; opera, dinner parties
- [ ] Claim a single ticket to one person (split games) 
- [ ] Make number of total tickets available scalable
- [ ] Figure out ways to exchange and trade tickets after initial seleciton corrections for errantly chosing a ticket
- [ ] pick it, send it back to available, and then have it be your turn again (an available game to choose)

# Functional Requirements

- [ ] A user must be able to sign up for an account at GetKraken
- [ ] A user must be able to log in to their account with the proper credentials
- [ ] Any authorized user can create a series of events
- [ ] Any user can create a new group
- [ ] Group admins can add or remove a member of the group
- [ ] Groups of users must be able to participate in a draft for a series
- [ ] Series must be able to determine draft orders for instances of groups
- [ ] Groups must be able to go through drafts
- [ ] During a draft, members of the group must be able to select events they want to attend on their turn
- [ ] A specific series should be able to begin and end the draft for an individual group

## Non-functional Requirements

- [ ] User authentication information should not be accessible to admins or other users
- [ ] Login and signup need to be intuitive and accessible from the home view
- [ ] After log in, users should be taken totheir individual user pages (showing their series, their groups in those series, and the ability to create new series/groups)
- [ ] The draft page must have a clear display of the current draft situation, which events are claimed and which are available, and give an intuitive format for selecting
- [ ] Tests for creating new users
- [ ] Tests for creating new series
- [ ] Tests for creating new groups
- [ ] Tests to make sure that the groups, series, and users information are being stored correctly



