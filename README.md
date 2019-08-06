# Y2 2019 Summer: Flask Login

## Setup

Before you start coding, make sure you fork and clone the repository
for this lab:
```
cd ~/Desktop
git clone https://github.com/YOUR_GITHUB_USERNAME/y2s19-flask-login.git
```

Run the following commands in your terminal to install passlib and flask_login:
```
pip3 install passlib
pip3 install flask_login
```

## Warm-up Exercises

### Part 1: User Models

Somebody started creating a User model, but they're missing an important part. Open `model.py` and replace this missing line of code.

*Hint* whenever you edit your model structure, you will need to recreate the database. To do this, find the user.db file and delete it. When you run `python app.py`, it will make a new database with the right models.

### Part 2: Just Add User

`database.py` also has problems! Look at the `add_user` function in `database.py` and figure out what else is needed to properly add a user to the database.

### Part 3: sign-up and login

After fixing both parts, run the server by running `python app.py` in the terminal. Then try signing-up a user and logging in. Make sure that when you log in the site responds with with the right username.

### Part 4: login_session

Remember that we can use `login_session` inside of our HTML templates as well. Inside of the template `home.html`, add an `if` statement that will say "Hi *username*" if the user is logged in.

*Hint* Look at `logged.html` to see how we can use `session` inside of a template to get values from `login_session`.

*Hint* To make an `if` statement in HTML, use this structure:
{% if *boolean* %}
    do something
{% endif %}


### Part 5: logout

Notice that clicking logout doesn't actually do anything. That's because in `app.py`, the logout function doesn't change the `login_session`. Figure out how to change `login_session` to logout the current user.


## Independent Lab: Using the User

### Part 1: Putting Food in the Database

In `model.py`, make new column in the user model to keep track of a user's favorite food. Name this column `fav_food` and make it a String type column.

In `databases.py` make a function that will allow a user to update their favorite food.

### Part 2: Forms to Fill

Add a form to the `logged.html` page that will allow a user to enter in a food. 

Edit the app route '/logged-in' in `app.py` so that POST and GET requests are accepted, and upon receiving a POST request, update the user's favorite food using the function you made in `databases.py`.

### Part 3: Where's the beef? - Showing fav foods

Now we will edit the `home.html` and `logged.html` to show the user's favorite food. Remember how we can feed parameters into a template? If we had the users favorite food, we could write: `render_template('home.html', food = fav_food)`.  But how do we get their favorite food from the database?

Remember, if a user is logged in, we already have the user's name stored in `login_session['name']`. With the username, what function in `databases.py` can we use to get the user object?

Once we have the user object, we can get their favorite food with the line `user_object.fav_food`, and use that as the parameter in `render_template`.


## Bonus - make it so that users can upload a picture of themselves that will be shown in the logged-in page.
