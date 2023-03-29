from pushbullet import Pushbullet

#copy api key in the quotation marks
API_KEY = ""


file = "resolution.txt"

with open(file, mode='r') as f:
    text = f.read()


pb = Pushbullet(API_KEY)
push = pb.push_note('Please remember', text)