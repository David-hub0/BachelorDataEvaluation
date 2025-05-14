import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, shapiro

import DataConverter
from DataImporter import questionsWithGuide, questionsWithoutGuide, eventsWithGuide, eventsWithoutGuide

datawithguide =DataConverter.playerset(questionsWithGuide, eventsWithGuide)
datawithoutguide = DataConverter.playerset(questionsWithoutGuide, eventsWithoutGuide)


def extractKnowledgeQuestions(data):
    """Takes the player data, returns the environment knowledge questions."""
    assessmentAndKnowledge = []
    knowledge = []
    for each in data:
         assessmentAndKnowledge.append(each[0])
    for each in assessmentAndKnowledge:
        knowledge.append(each[8:11])
    return knowledge

def evaluateKnowledgeQuestions(data):
    """Takes environment knowledge questions, evaluates them, gives 1 point for each correct answer. Returns sum of correct answers."""
    counter = 0
    if data[0] ==3:
        counter = counter + 1
    if data[1] == 2:
        counter = counter + 1
    if data[2] == 2:
        counter = counter + 1
    return counter

def pregameknowledge(datawithguide, datawithoutguide):
    """Gives the average value of the players environment knowledge.
    Nicht mehr aktuell!!!"""

    print(f"Mit Guide haben die Spieler{evaluateKnowledgeQuestions(extractKnowledgeQuestions(datawithguide)[0])} Punkte erreicht, bei 14 Spielern")
    print(f"Ohne Guide haben die Spieler{evaluateKnowledgeQuestions(extractKnowledgeQuestions(datawithoutguide))} Punkte erreicht, bei 9 Spielern")

def environmentPriorities(data):
    """Takes the data of players with/without guides in. Searches for their priority of the environment. Sums it up an. Returns the average of all players. Return value ranges from 1 to 7, the closer to 1 the better."""
    liste = []
    i =0
    for each in data:
        liste.append(each[0][3])
        i += 1
    return (liste)

def pgqattention(data):
    """Takes data in, searches for the questions, gives 1 Point for each correct answer. Returns the sum of all points. There are max 3 points per player, the closer the average to 3 the better."""
    counter = 0
    if data[0] == 1:
        counter =  counter +1
    if data[1] == 3:
        counter =  counter +1
    if data[2] == 2:
        counter =  counter +1
    return counter

def extractEvents(data):
    """Takes in data, returns events of players (decision, valance, arousal)."""
    eventposition = len(data[0])-1
    events = []
    for each in data:
        #print(each[eventposition])
        events.append(each[eventposition])
    return events

def evaluateAllDescisions(data):
    """All decisions of all players are evaluated, 1 point for each correct answer. Return the average Points of all players."""
    counter = 0
    decisonsContainer = []
    for each in data:
        for something in each:
            decisonsContainer.append(something[0])
    for each in decisonsContainer:
        if each[0] == 2:
            counter = counter +1
        if each[1] == 1:
            counter = counter + 1
        if each[2] == 1:
            counter = counter + 1
        if each[3] == 1:
            counter = counter + 1
        if each[4] == 1:
            counter = counter + 1
        if each[5] == 2:
            counter = counter + 1
        if each[6] == 1:
            counter = counter + 1
        if each[7] == 1:
            counter = counter + 1
        if each[8] == 2:
            counter = counter + 1
        if each[9] == 1:
            counter = counter + 1
    return counter/len(decisonsContainer)
def evaluateDecision(data):
    counter = 0
    if data[0] == 2:
        counter = counter +1
    if data[1] == 1:
        counter = counter + 1
    if data[2] == 1:
        counter = counter + 1
    if data[3] == 1:
        counter = counter + 1
    if data[4] == 1:
        counter = counter + 1
    if data[5] == 2:
        counter = counter + 1
    if data[6] == 1:
        counter = counter + 1
    if data[7] == 1:
        counter = counter + 1
    if data[8] == 2:
        counter = counter + 1
    if data[9] == 1:
        counter = counter + 1
    return counter
def extractEventDecisions(data):
    decisonsContainer = []
    for each in data:
        for something in each:
            decisonsContainer.append(something[0])
    return decisonsContainer
def extractEventValance(data):
    valanceContainer = []
    for each in data:
        for something in each:
            valanceContainer.append(something[2])
    return valanceContainer
def extractEventArousal(data):
    arousalContainer = []
    for each in data:
        for something in each:
            arousalContainer.append(something[1])
    return arousalContainer

def getGamingExperties(data):
    temp = []
    for each in data:
        temp.append(each[11])
    return temp

def getAssessment(data):
    temp =[]
    for each in data:
        temp.append(each[0])
    return temp

def envPrio(data):
    """Returns the priority of the players for the environment (Assesment Question 8)"""
    enviroPrioArray = []
    for each in data:
        enviroPrioArray.append(each[0][12])
    return enviroPrioArray

def envKnowledgeInfluence(data):
    """Returns the self reported influence of the players previous knowledge on their decision making"""
    enviroPrioKnowledgeArray =[]
    for each in data:
        enviroPrioKnowledgeArray.append(each[1][1])
    return enviroPrioKnowledgeArray
def gameGoalData(data):
    """Returns the self reported understanding of the game goal"""
    gameGoalArray = []
    for each in data:
        gameGoalArray.append(each[1][0])
    return gameGoalArray

def getEventKnowledge(data):
    """Returns the self reported understanding of the game goal"""
    gameGoalArray = []
    for each in data:
        gameGoalArray.append(each[1][0])
    return gameGoalArray

def getAttentionData(data):
    """Get the knowledge questions of the questionnaire. PGQuestions 4-6"""
    attentionArray = []
    for each in data:
        attentionArray.append(each[1][3:6])
    return attentionArray

def getGuideQuestions(data):
    guideArray = []
    for each in data:
        guideArray.append(each[2])
    return guideArray
def guideQuestionEval(data):
    guidePoints =[]
    for each in data:
        counter = 0
        if each[0] == 1:
            counter += 1
        if each[1] == 2:
            counter += 1
        if each[2] == 2:
            counter += 1
        guidePoints.append(counter)
    return guidePoints

def getCertainArousal(data):
    """Return the average arousal of Event 0 ,3 ,5 ,9 für die Fragen zu den Guides """
    arousalArray = []
    for each in data:
        temp = [each[0], each[3], each[5], each[9]]
        arousalArray.append(numpy.average(temp))
    return arousalArray
def getCertainValance(data):
    """Return the average valance of Event 0 ,3 ,5 ,9 für die Fragen zu den Guides """
    valanceArray = []
    for each in data:
        #temp = [numpy.abs(each[0]-5), numpy.abs(each[3]-5), numpy.abs(each[5]-5),numpy.abs(each[9]-5)]
        temp = [each[0], each[3], each[5], each[9]]
        valanceArray.append(numpy.average(temp))
    return valanceArray

def getGuidePoularity(data):
    """Return the Value which guide is more popular"""
    popularityArray = []
    for each in data:
        popularityArray.append(int(each[2][3]))
    return popularityArray
def evaluateDecisionLeftRight(data):
    "Evaluates the players decisions and sorts them to the left and right guide."
    counterLeft = 0
    counterRight = 0
    if data[0] == 2:
        counterLeft = counterLeft +1
    if data[1] == 1:
        counterRight = counterRight + 1
    if data[2] == 1:
        counterLeft = counterLeft + 1
    if data[3] == 1:
        counterRight = counterRight + 1
    if data[4] == 1:
        counterLeft = counterLeft + 1
    if data[5] == 2:
        counterRight = counterRight + 1
    if data[6] == 1:
        counterLeft = counterLeft + 1
    if data[7] == 1:
        counterRight = counterRight + 1
    if data[8] == 2:
        counterLeft = counterLeft + 1
    if data[9] == 1:
        counterRight = counterRight + 1
    return counterLeft, counterRight

def getAge(data):
    ageList = []
    for each in data:
        ageList.append(int(each[0][0]))
    return ageList
def getGender(data):
    genderList = []
    for each in data:
        genderList.append(int(each[0][1]))
    return genderList







