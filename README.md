My vision for this project was to have a simple but functional website that connected families and individuals with caregivers in their area. 
My design was inspired by glossier.com's sleek and modern design that is eye-catching but not overwhelming. However, as we discussed in our OH session,
some of my CSS was influenced by the stylesheets my carousel required. Overall, I achieved most of my goals and learned a lot along the way. I've added error messages or print statements to obvious bugs and functional issues I'm aware of.

# subscribe.js 
contains an event listener that's used to disable the "subscribe to our newsletter" submission button until both a name and email have been provided; and appends the submission to the 'sub_list' before clearing the form. The button is then disabled for the next user. 

# categories.html
Displays individual links to each existing category. Unfortunately, the code that I commented out did not work, so I had to create the links manually. Additional error, the urls path to display a page with all of the existing listings within that specific category don't work. All url paths point to index in an effort to avoid additional errors. 

# category.html
Logically similar to listing.html, but was not brought into use given the issues i had with categories.html. It should have displayed an unordered list of hyperlinked elements, each being a listing in that respective category.

# create_event.html
Used to create a 'Community Event Listing' that is displayed in the events tab. Uses the NewEventForm.

# create_listing.html 
Used to create a 'Care Listing' that is displayed on the home page. Uses the NewListingForm.

# events.html
Displays an unordered list of all community events. 

# index.html
Displays a list of links to all active listings and their title, owner, location, dates, and description, underneath a carousel of six stock photos.

# layout.html
Contains an expanded nav class, a JS function sucess() which will appear throughout the project (subscribe to newsletter, apply to position, create listing, and create event.) Includes a subscribe to email list footer.

# listing_inactive.html
Is not utilized directly within listing.html but should have been a button displayed to users if they are the owner of the listing. A button was put into the if/else statement in listing.html as a backup. 

# listing.html
Displays the user's name and the details of their listing. Underneath the listing is an 'apply to this listing' form that utilizes the success() JS function. Bug: the listing.active and request.user == owner logic is not working and therefore the deactivate button does not appear.

# login.html
Standard login template that takes the user's username and password

# register.html
Standard register template that lets the user create a username and password, and input their full name to gain access to the full site. 

# admin.py
Where my models are registered, alongside the superuser information 

# forms.py
Form creation for: NewListingForm, NewInterestFrom, and NewEventForm. NewInterestForm could have replaced the manual 'apply' logic in listing.html but to be frank I forgot about it until now. 

# models.py
Contains the models: User, Listing, Apply, Category, and Event 

# urls.py
Contains paths for the entire project. I ran into issues with category and categories, so I'm assuming there's a flaw in my logic url-wise.

# views.py 
Contains the majority of my functions for this project, beginning with index and ending with the source code for login, logout, and register.  
- categories should have displayed each category within categories, but there's an error my logic. 
- category should render each respective category, but this section did not work either.
- create event was successful in is ability to create and save new events
- create listing was successful in is ability to create and save new listings
- events renders all events
- listing renders each individual listing. Bug with the owner information being passed to listing.html
- listing_inactive: has not been fully utilized as discussed above