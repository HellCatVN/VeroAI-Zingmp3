# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler , intent_file_handler
from mycroft.util.log import LOG
from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
from mycroft.util.parse import match_one
from mycroft.skills.audioservice import AudioService
from mycroft.audio import wait_while_speaking


import requests
import json
import urllib
import re
import random
from os.path import dirname, join

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class TemplateSkill(MycroftSkill):
    
    # track_dict = {
    #     'Be Your EveryThing': 'https://blog.hellcatvn.com/mp3/Be%20Your%20Everything',
    #     'Yeu Duong': 'https://blog.hellcatvn.com/mp3/Yêu Đương',
    # }

    # def CPS_match_query_phrase(self, phrase):
    #     # Get match and confidence
    #     match, confidence = match_one(phrase, track_dict)
    #     # If the confidence is high enough return a match
    #     if confidence > 0.5:
    #         return (match, CPSMatchLevel.TITLE, {"track": match})
    #     # Otherwise return None
    #     else:
    #         return None

    # def CPS_start(self, phrase, data):
    #     # Retrieve the track url from the data
    #     url = data['track']
    #     print(url)
    #     self.audioservice.play(url)  # Send url to audioservice to start playback

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(TemplateSkill, self).__init__(name="TemplateSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0
        self.process = None
        self.play_list = {
            0: join(dirname(__file__), "Seasons.mp3")
        }

    def initialize(self):
        self.audioservice = AudioService(self.bus)
        self.add_event("mycroft.sing", self.sing, False)

    def sing(self, message):
        self.process = play_mp3(self.play_list[3])

    @intent_handler(IntentBuilder("").require("Play").require("Zingmp3"))
    def handle_play_zing_mp3(self, message):
        print("BBC")
        # key_word = "Yêu 5"
        # resp = requests.get('http://ac.mp3.zing.vn/complete/desktop?type=song&query='+urllib.parse.quote(key_word))
        # resultJson = json.dumps(resp.json())
        # obj = json.loads(resultJson)
        # songID = obj["data"][1]['song'][0]['id']
        # songUrl= "https://mp3.zing.vn/bai-hat/"+songID+".html"
        # resp = requests.get(songUrl)
        # key = re.findall('data-xml="\/media\/get-source\?type=audio&key=([a-zA-Z0-9]{20,35})', resp.text)
        # songApiUrl = "https://mp3.zing.vn/xhr/media/get-source?type=audio&key="+key[0]
        # resp = requests.get(songApiUrl)
        # resultJson = json.dumps(resp.json())
        # obj = json.loads(resultJson)
        # mp3Source = "https:"+obj["data"]["source"]["128"]
        # realURLdata = requests.get(mp3Source,allow_redirects=False)
        # realURL = realURLdata.headers['Location']
        # print(realURL)
        # self.audioservice.play(realURL) 
        path = random.choice(self.play_list)
        try:
            self.audioservice.play(path)
        except Exception as e:
            self.log.error("Error: {0}".format(e))


        def stop(self):
            if self.process and self.process.poll() is None:
                print("ngung hat")
                self.process.terminate()
                self.process.wait()

def create_skill():
    return TemplateSkill()
