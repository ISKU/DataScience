import fitbit
import json
import configparser

config = configparser.RawConfigParser()
config.read('config.ini')

CLIENT_ID = config.get('ACCOUNT', 'CLIENT_ID')
CLIENT_SECRET = config.get('ACCOUNT', 'CLIENT_SECRET')
ACCESS_TOKEN = config.get('ACCOUNT', 'ACCESS_TOKEN')
REPRESH_TOKEN = config.get('ACCOUNT', 'REPRESH_TOKEN')

authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token = ACCESS_TOKEN, refresh_token = REPRESH_TOKEN)

intraday_step = authd_client.intraday_time_series('activities/steps', base_date = '2017-03-20', detail_level = '15min')
print(intraday_step)

f = open('step.json', 'w')
json.dump(intraday_step, f)
