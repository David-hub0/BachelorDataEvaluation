class PlayerWithGuide:
    """This is the Object where player data with guides is saved into"""
    def __init__(self, assessmentandknowledge, postgamequestion, guidequestions,events):
        self.assessmentandknowledge = assessmentandknowledge
        self.postgamequestion = postgamequestion
        self.guidequestions = guidequestions
        #self.events = events

class PlayerWithoutGuide:
    """This is the Object where player data without guides is saved into"""
    def __init__(self,assessmentandknowledge, postgamequestion, events):
        self.assessmentandknowledge = assessmentandknowledge
        self.postgamequestion = postgamequestion
        #self.events = events

class AssessmentAndKnowledge:
    """This is the part where all previous data is collected: age, gender, climate_priority, renew_energy, deforestation, ozone_layer, video_games,
                 environmental_issues """
    def __init__(self, age, gender, climate_priority, renew_energy, deforestation, ozone_layer, video_games,
                 environmental_issues):
        self.age = age
        self.gender = gender
        self.climate_priority = climate_priority
        self.renew_energy = renew_energy
        self.deforestation = deforestation
        self.ozone_layer = ozone_layer
        self.video_games = video_games
        self.environmental_issues = environmental_issues

class PostGameQuestion:
    """This is the part where all data after the test is collected: game_goal, prev_knowledge, expectations, building_burning, invasive_species,
                 beccs"""
    def __init__(self, game_goal, prev_knowledge, expectations, building_burning, invasive_species,
                 beccs):
        self.game_goal = game_goal
        self.prev_knowledge = prev_knowledge
        self.expectations = expectations
        self.building_burning = building_burning
        self.invasive_species = invasive_species
        self.beccs = beccs

class GuideQuestions:
    """This is the part where questions specific to the guide are collected: guides_greeting, guide_repulsed, dunkelflaute, preference_guide"""
    def __init__(self, guides_greeting, guide_repulsed, dunkelflaute, preference_guide):
        self.guides_greeting = guides_greeting
        self.guide_repulsed = guide_repulsed
        self.dunkelflaute = dunkelflaute
        self.preference_guide = preference_guide

class Events:
    """This is where the event data is saved. Each Event is an Array[Event-decision, Valence, Arousal]"""
    def __init__(self, event0, event1, event2, event3,event4, event5, event6, event7, event8, event9):
        self.event0 = event0
        self.event1 = event1
        self.event2 = event2
        self.event3 = event3
        self.event4 = event4
        self.event5 = event5
        self.event6 = event6
        self.event7 = event7
        self.event8 = event8
        self.event9 = event9