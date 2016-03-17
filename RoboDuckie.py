import tweepy, time, sys
import datetime
import re
import urllib3
urllib3.disable_warnings()

class Tweepy:
    def __init__(self):
        self.C_K = ''
        self.C_S = ''
        self.A_K = ''
        self.A_S = ''
        self.auth = ''
        self.api = ''
        self.tweets = ''

    def setKey(self, authFile):
        file = open(authFile, 'r')
        f = file.readlines()
        file.close()
        self.C_K = f[0].replace("\n", "")
        self.C_S = f[1].replace("\n", "")
        self.A_K = f[2].replace("\n", "")
        self.A_S = f[3].replace("\n", "")

    def setAuth(self):
        self.auth = tweepy.OAuthHandler(self.C_K,self.C_S)
        self.auth.set_access_token(self.A_K,self.A_S)
        self.api = tweepy.API(self.auth)

    def setTweets(self, tweetfile):
        file = open(tweetfile, 'r')
        self.tweets = file.readlines()
        file.close()

    def sleep(self, sleeptime):
        print(dateSTR() + 'Duck going to sleep...')
        time.sleep(sleeptime)
        print(dateSTR() + 'Duck waking up...')

def dateSTR():
    return str(datetime.datetime.now().strftime("|[%Y-%m-%d %H:%M]| "))

def spacer():
    return str('                     ')


print('\n______________________________WELCOME TO DUCK______________________________')
print('Created by: GR347WH173N0R7H\nUsing: Tweepy Lib\nSpecial Thanks: Jared\n')
print('Authentication:      ' + str(sys.argv[1]))
print('Tweets:              ' + str(sys.argv[2]))
print('Sleep:               ' + str(sys.argv[3])+' seconds')
print('___________________________________________________________________________\n')

print(dateSTR() + 'DUCK INITIALISING...')
authfile = str(sys.argv[1])
tweetfile = str(sys.argv[2])
sleeptime = int(sys.argv[3])

print(spacer() + 'Creating a duck...')
duck = Tweepy()
duck.setKey(authfile)
duck.setAuth()

print(spacer() + 'Duck learning to tweet...')
duck.setTweets(tweetfile)

print(dateSTR() + 'DUCK FLYING')

i = False

for l in duck.tweets:
    if i:
       duck.sleep(sleeptime)
    cmd = l[0:5]
    tweet = l[6:len(l)].replace("\n", "")
    try:
        if len(tweet) < 140:
            if cmd == '[TXT]':
                print(dateSTR() +'Tweeting Text: '+tweet)
                duck.api.update_status(tweet)
            elif cmd == '[IMG]':
                img = re.search('[^#]\w+\.+\w+', tweet)
                tweet = tweet[(2 + len(img.group(0))):len(tweet)]
                print(dateSTR() +'Tweeting Image:')
                print(spacer() + '> Image: ' + img.group(0))
                print(spacer() + '> Text: '+ tweet)
                duck.api.update_with_media('img/' + img.group(0), tweet)
            print(dateSTR() +'Tweet Complete')
            i = True
        else:
            print(dateSTR() +'***Tweet FAILED***')
            print(spacer() +'> ERROR: TEXT TO LONG')
            i = False

    except tweepy.error.TweepError:
        print(dateSTR() +'***Tweet FAILED***')
        i = False
        pass

print(dateSTR() + 'No More Tweets!')
print(dateSTR() + 'DUCK TERMINATED!')

