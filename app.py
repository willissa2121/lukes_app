import requests

Get the user's LinkedIn profile URL
user_url = "https://www.linkedin.com/in/lukecherry/"

Get the user's LinkedIn activity
activity_url = user_url + "recent-activity/"
headers = {
        }

Make a request to the LinkedIn API
response = requests.get(activity_url)

Check the response status code
if response.status_code == 200:

        # Get the activity data
            activity_data = response.text

                print (activity_data)

            else:

                print("Error:", response.status_code)
