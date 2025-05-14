import re
import Data
import DataImporter
from DataImporter import questionsWithGuide, eventsWithGuide, questionsWithoutGuide, eventsWithoutGuide


#guideData = DataImporter.withguide
#guideEvents=DataImporter.guide_events

def playerset(guideData, events):
    playerList=[]
    player = Data.PlayerWithGuide
    assessment = Data.AssessmentAndKnowledge
    postgamequestions = Data.PostGameQuestion
    guidequestions = Data.GuideQuestions
    temp0 = []
    temp1 = []
    temp2 = []

    for playerCounter in range(guideData.shape[1]):
        for attributeCounter in range(guideData.shape[0]):
            if attributeCounter <= 12:
                temp0.append(guideData[attributeCounter, playerCounter])
            elif 12 < attributeCounter < 19:
                temp1.append(guideData[attributeCounter, playerCounter])
            else:
                temp2.append(guideData[attributeCounter, playerCounter])
        tp = events[playerCounter]
        eventsValue = extract_values(tp)
        assessment = temp0
        postgamequestions = temp1
        guidequestions = temp2
        player = (assessment, postgamequestions, guidequestions, eventsValue)
        playerList.append(player)
        temp0= []
        temp1= []
        temp2 =[]

        #print(player)

    return playerList

def extract_values(text):
    """Extract the Decision, Valance and Arousal values from an array of text strings."""
    results = []

    # Regular expression patterns to match the desired values
    decision_pattern = r'\((\d+)\)'
    valance_pattern = r'Valance: (-?\d+)'
    arousal_pattern = r'Arousal: (-?\d+)'


    # Find all decision numbers
    decisions = re.findall(decision_pattern, text)

    # Find all Valance and Arousal values
    valance_matches = re.findall(valance_pattern, text)
    arousal_matches = re.findall(arousal_pattern, text)

    # Extract and format Decision, Valance and Arousal values
    decisions_values = [int(each0) for each0 in decisions]
    valance_values = [int(each1) for each1 in valance_matches]
    arousal_values = [int(each2) for each2 in arousal_matches]

    # Append the results as a tuple to the results list
    results.append((decisions_values, valance_values, arousal_values))

    return results

#print(playerset(questionsWithGuide, eventsWithGuide))
#print(playerset(questionsWithoutGuide, eventsWithoutGuide))