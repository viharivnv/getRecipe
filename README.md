# getRecipe
A Web application currently running on local host to search recipes.

As of now, I was able to fetch the recipes using the Recipe names through APIs. This simple web application can be further improved by modifying the search using Ingredients, category etc. This application is available to all but sooner User Authentication will be implemented to maintain favouraites of a specific person.

I am planning to integrate the web application to a database, by choosing one from MySQL or MongoDB based on the structure requiremnets. This data base can be used for maintaining user data, favourite stocks etc.

**Steps to run the web application:**

1. Open CMD prompt and goto the file location of get-recipe. Make sure you are not in the get-recipe folder yet.
2. Activate the Virtual Environment get-recipe using the line get-recipe\Scripts\activate.bat
3. Then cd into the get-recipe folder.
4. cd into mysite.
5. Run the line py manage.py runserver.
6. Open the localhost http://127.0.0.1:8000/ on any browser.
7. Use the web application for searching the recipes.
