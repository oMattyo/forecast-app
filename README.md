# Forecast App
- Python weather forecast app created in a venv using Python version 3.12.0.
- The app, on startup, will present the user with a ui based on tkinter.
- The user will enter the city and country/state they are interested in finding out the weather forecast for.
    - If the user inputs valid entries for the city and country/state, the app will use the [geopy](https://pypi.org/project/geopy/) package to get the latitude and longitude values for that location.
    - The app will then call the [Open Weather API](https://openweathermap.org/) using those previously acquired lat & lon values to get the weather conditions over the next 12 hours - in 3 hour intervals.
        - Each forecast over that period will include: the condition \(cloudy, light rain, fog, etc\) as well as the cloud coverage, as a percentage, and the date and time for that forecast.

# Important Notes
- In order for this to work you will need to register at [Open Weather API](https://openweathermap.org/) and sign up for a free account.
    - You will then need to add you own API key to the project.
        - I am using the [python-dotenv](https://pypi.org/project/python-dotenv/) package to pull my API key from a folder outside of the project directory.
            - You can create your own .env file somewhere on your machine and point to it like I have done inside api.py file.

- I have included a requirements.txt file so you can quickly set up your environment to run this application.
    - After you have pulled down the github code to a file of your choosing you can run: `pip install -r requirements.txt`
        - This will install all of the pip packages you will need for the project.
