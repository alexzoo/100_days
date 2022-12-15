import os
import requests
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

APP_ID = os.getenv('NUTR_APP_ID')
APP_KEY = os.getenv('NUTRITIONIX_API')
AUTH_PASS = os.getenv('AUTH_PASS')

nutri_api_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/7fc06cccc3669df91d5a3cc4ff4cc754/myWorkouts/workouts'


def post_nutritionix_excercise(ecxercise: str) -> dict:
    headers = {
        'x-app-id': APP_ID,
        'x-app-key': APP_KEY,
    }

    body = {
        'query': ecxercise,
        'gender': 'male',
        'weight_kg': 75.5,
        'height_cm': 174.0,
        'age': 40,
    }

    resp = requests.post(url=nutri_api_endpoint, json=body, headers=headers)
    resp.raise_for_status()
    return resp.json()


result = post_nutritionix_excercise(input('Enter your activity: '))


today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')

sheety_headers = {
    'Authorization': AUTH_PASS
}


for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    resp = requests.post(url=sheety_endpoint,
                         json=sheet_inputs, headers=sheety_headers)
    resp.raise_for_status()
    print(resp.text)
