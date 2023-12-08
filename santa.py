from info import pwd, people
from mailsender import Mailer
import random
    
class Participant:
    def __init__(self, name, email, hasGift):
            self.name = name
            self.email = email
            self.hasGift = hasGift

participants = [] # Participant

# Initialize participants, no santa set yet
def constructParticipants():
    for name, email in people.items():
        participants.append(Participant(name, email, False))
        
# Assign each participant a unique Santa
def determineSantas():
    # for every participant
    for i in range(len(participants)):
        person = participants[i]
        r = random.randrange(len(participants))
        # if they do not have a santa - find one
        while r == i or participants[r].hasGift:
            r = random.randrange(len(participants))
        # found santa
        participants[r].hasGift = True
        # print(person.name + " is getting a gift for: " + participants[r].name)
        mailsender = Mailer("rhinosanta@gmail.com", pwd)
        mailsender.sendMessage(person.email, person.name, participants[r].name)
            
constructParticipants()
determineSantas()
    
            