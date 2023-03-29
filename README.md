#Receive daily push notifications to your device, code created using python and pushbullet API
Install requirements using command;
pip install -r requirements.txt
Edit resolution.txt to your choice of words
Go to [pushbullet website](https://www.pushbullet.com/) in your PC - preferably - and sign in using your Google account.
Install pushbullet app in you android or iPhone and give necessary permissions during setup
In the website, go to settings, and generate an API KEY, copy it to the resolution_reminder.py python code
Go to [pythonanywhere website](https://www.pythonanywhere.com/) and register an account for hosting the python app
Choose beginner for free access, and upload the files - resolution.txt and resolution_reminder.py -
Go to console, choose bash, and type in;
pip install pushbullet.py
exit
Now go to files, click on resolution_reminder.py, and click run. You should receive a notification in your phone.
To receive daily notifications, go to tasks, type in your desired time to receive the notification, and the link for where the python code is located, for example;
>python3.10/home/your_username/resolution_reminder.py
That's it, you will receive daily notifications on your device.