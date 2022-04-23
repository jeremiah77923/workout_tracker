# Author: Jeremiah Hawthorne
# Started: Sat April 23rd
# Finished: Sat April 23rd


# Importing all the requried modules
import requests as r
from datetime import datetime as dt
import smtplib

# Constants:
GENDER = "male"
WEIGHT_KG = 70.7
HEIGHT_CM = 195.072
AGE = 18
APP_ID = "a53ec8f5"
APPLICATION_KEY = "4d1386c01bc692f83164da4617c7aa0d"
NUTRIONX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {"x-app-id": APP_ID,
           "x-app-key": APPLICATION_KEY,
           }
SHEETS_HEADERS = {
    "Authorization": "Bearer KEYPASS",
    "Content-Type": "application/json"
}

query = {}


def get_exercises():
    query = input("Tell me the exercises you did today?\n")
    return query


exercise = get_exercises()

query = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = r.post(NUTRIONX_ENDPOINT, json=query, headers=HEADERS)
data = response.json()
exercises = data["exercises"]
for x in exercises:
    current = x
    current_min = x["duration_min"]
    current_calories = x["nf_calories"]
    current_user_input = x["user_input"]

    dates = dt.now().strftime('%m/%d/%Y %I:%M:%S')
    dat = dates.split(" ")

    params = {
        "workout": {
            "date": dat[0].replace("'", ""),
            "time": dat[1].replace("'", ""),

            "exercise": current_user_input.title(),
            "duration": f"{current_min}" + " mins",
            "calories": f"{current_calories}" + " kj",
        }
    }
    response1 = r.post(url="https://api.sheety.co/1db9455e255ce8dff061a6f826055b40/workouts/workouts", json=params,
                       headers=SHEETS_HEADERS)

