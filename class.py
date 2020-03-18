class LearnersAndMentors:

    learners={}
    mentors={}
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
    def addStacks(self):
        self.techstack = raw_input('Add you stack which you like to learn/mentor:')
    def setMentorOrLearner(self):
        self.status = int(raw_input('Enter your choice\n What you wish to be:\n1.Mentor\n2.Learner'))
    def setAvailableTime(self):
        if self.status == 1:
            self.avail_time = int(raw_input('Set your available time in 24-hr format:hhmm:'))
            self.availabilty = 'free'
    def AddToDict(self):
        if self.status == 1:
            LearnersAndMentors.mentors[user_id] = self
        if self.status == 2:
            LearnersAndMentors.learners[user_id] = self
    def getMentor(self,req_time):
        for available_mentors_id,values in mentors.items():
            if values['time'] <= req_time and availabilty == 'free':
                self.availabilty = 'occupied'
                return available_mentors_id
            elif values['time']-req_time < 10:
                self.availabilty = 'assigned'
                return available_mentors_id
            
