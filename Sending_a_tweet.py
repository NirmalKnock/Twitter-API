from twython import Twython
#Replace your Twitter keys
C_KEY=""
C_SECRET=""
A_TOKEN=""
A_SECRET=""
api=Twython(C_KEY,C_SECRET,A_TOKEN,A_SECRET)
api.update_status(status="Hi")
