# Name: Foodie

## Project Overview

My project is going to be a social media app focused SOLELY on food. I emphazise the "solely" because there are a lot of platforms that have just a general broad description of what they are allowed to post on their platforms, but I want the only thing allowed to be posted on mine is just food and drinks. As someone
who does not want to sift through a million posts of random content when I am trying to decide on food. 

## Features

THer application will be a simple scroll down format of pictures and restaurants that the person is posting themselves onto their own timeline. It will feature the restaurant, pictures of whatever they user uploaded, a simple description of what they want to say about their retaurant(max length of characters set to about 250 characters), and a voting system based on users voting on the retaurant the voting will be simple, on a scale of 1-20, to allow for half voting. Once they cast their numerical vote, it will be converted into a 1-10 scale. Users will also be able to flag posts in case they are violating the rules of the site.  

### User Posts 

Users will be able to post what they want on the platform so long as it follows the rules of the platform

#### Restaurant/Food Venue being showcased

One of the requirements will be a basic field for the name of the restaurant. If there is no restaurant, or valid name of one, the post will be removed. Only one post will be allowed per restaurant, per user. This will ensure that there are no people self promoting their business by spamming their restaurant with a ton of fake posts or postive voting.

#### Location of Restaurant

This will be a required field in order to make it easier to sort through what posts are originating for what city. Initially, the options will only be the city and state that they retsaurant are located in. A nice-to-have will be a neighborhood location within a city so if someone is walking, they can look up just their immediate area vs. scouting the entire city. 

#### User Description

Users can write a short description of what they want to add to their post regarding the retsuarant that they are adding to the list. Descriptions will match 
what they want to convey to the world what they think of the restaurant. One of the caveats to the description is that there is no hate bashing allowed on the 
actual retsaurant. The purpose of the app is to showcase the top restaurants in the area, and overtly negative posts will be removed. If there is legitimate feedback on a restaurant, and the feedback is consistent with the restaurant being a place that our users do not want to visit, it will be removed and not allowed 
to be a part of the app. 

#### User Photos

Users will be able to upload photos to the site. I have a preset maximum of 5, but a required 1 minimum to showcase what restaurant they visited. The photos must be related to the actual restaurant and if a photo appears that is not part of the restaurant, the post will be removed, along with any of the voting that the user submitted. 

#### Flag Posts

A final feature will be allowing people to flag posts for any sort of infraction of the rules. If somone is promoting something other than the actual restaurant being showcased, the user profile will be removed. 


## Data Models

The two main things that I will be collecting are the text fields of user's posts, restaurants names. I will also be collecting the voting results of user's restaurants, and images of the restaurants. 

### Image Sets

Since user's will be posting their picutres, I will only allow jpeg format pictures to be uploaded. It will just make it easier to start with just having one standard way of holding the information needed. 


### Text Fields

I will hold the user post description and restaurants names along with their city location. One of the fields that I will have as optional will be the neighborhod that they reside in. The reason being is I want to have people be able to look up restaurants near them if they are interested in searching only for their immediate area vs the entire city they are in. 

### Voting Results

I want to have the voting results be a float represented by the users voting ranges from 1-20. It will be displayed as a number between 1-10, but the 1-20 from them will allow for a more precise vote float for a restaurant if multiple people are voting for it. A nice to have will be if a restaraunt merrits less than 5.0 for an extended period of time, it will be removed from the list so as to showcase only the best restaurants in the area. Perhaps in the future the threshhold can be moved to accomodate a higher quality. 
