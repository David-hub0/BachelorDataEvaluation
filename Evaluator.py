import matplotlib.pyplot as plt
import numpy
import numpy as np
import seaborn as sns
import pandas as pd
from fontTools.merge import layoutPreMerge
from fontTools.t1Lib import font_dictionary_keys
from matplotlib.pyplot import minorticks_off, boxplot
from scipy.stats import shapiro, stats, ttest_ind, pearsonr

from MyMath import datawithguide, datawithoutguide, extractEvents, extractEventArousal, extractEventValance, \
    extractEventDecisions, evaluateKnowledgeQuestions, evaluateDecision, extractKnowledgeQuestions, \
    environmentPriorities, getGamingExperties, getAssessment, envPrio, envKnowledgeInfluence, gameGoalData, \
    getAttentionData, pgqattention, getGuideQuestions, guideQuestionEval, getCertainArousal, getCertainValance, \
    getGuidePoularity, evaluateDecisionLeftRight, getAge, getGender

arousalWithGuide = extractEventArousal(extractEvents(datawithguide))
arousalWithoutGuide = extractEventArousal(extractEvents(datawithoutguide))

valenceWithGuide = extractEventValance(extractEvents(datawithguide))
valenceWithoutGuide = extractEventValance(extractEvents(datawithoutguide))

decisionsWithGuide = extractEventDecisions(extractEvents(datawithguide))
decisionsWithoutGuide = extractEventDecisions(extractEvents(datawithoutguide))

knowledgeWithGuide = extractKnowledgeQuestions(datawithguide)
knowledgeWithoutGuide = extractKnowledgeQuestions(datawithoutguide)

envPrioWithGuide = environmentPriorities(datawithguide)
envPrioWithoutGuide = environmentPriorities(datawithoutguide)

def prevKnowledgeSupport(decisionsWithGuide, decisionsWithoutGuide, knowledgeWithGuide, knowledgeWithoutGuide):
    """Does guides help players with previous knowledge more?\n
    Assessment 4-6 -> EventDecisions\n
    Punkte des Vorwissen(Individuum) ->Punkte der Event Decision (Individuum)
    """
    pointCounterWithGuide = []
    for each in decisionsWithGuide:
        pointCounterWithGuide.append(evaluateDecision(each))
    pointCounterWithoutGuide = []
    for each in decisionsWithoutGuide:
        pointCounterWithoutGuide.append(evaluateDecision(each))
    knowledgePointsWithGuide = []
    for each in knowledgeWithGuide:
        knowledgePointsWithGuide.append(evaluateKnowledgeQuestions(each))
    knowledgePointsWithoutGuide = []
    for each in knowledgeWithoutGuide:
        knowledgePointsWithoutGuide.append(evaluateKnowledgeQuestions(each))
    knowledgeDecisionArrayWithGuides = [0 for _ in range(4)], [0 for _ in range(4)]
    i=0
    averageWithGuide = []
    for each in knowledgePointsWithGuide:
        knowledgeDecisionArrayWithGuides[0][each] +=1
        knowledgeDecisionArrayWithGuides[1][each] += pointCounterWithGuide[i]
        i +=1
    counter = 0
    for each in range(len(knowledgeDecisionArrayWithGuides[0])):
        if not knowledgeDecisionArrayWithGuides[0][each] == 0:
            knowledgeDecisionArrayWithGuides[1][each] = knowledgeDecisionArrayWithGuides[1][each] / \
                                                        knowledgeDecisionArrayWithGuides[0][each]
        else:
            knowledgeDecisionArrayWithGuides[1][each] = 0
        averageWithGuide.append(knowledgeDecisionArrayWithGuides[1][each])
        print(f"There are {knowledgeDecisionArrayWithGuides[0][counter]} players with guides with {counter} points in previous environmental knowledge who gained on average {knowledgeDecisionArrayWithGuides[1][counter]} points in the decision of the game.")
        counter += 1

    """a = pearsonr([0, 1, 2, 3], [0,5,6.66666,8.666666])
    print(a)"""
    """
    fig, ax = plt.subplots()
    ax.set_ylabel("Correct\nevent\ndecisions")
    ax.set_xlabel("Correct knowledge questions")
    ax.set_ylim(0, 10)
    ax.bar(x=["0","1","2","3"],height=knowledgeDecisionArrayWithGuides[1])
    plt.show()"""

    knowledgeDecisionArrayWithoutGuides = [0 for _ in range(4)], [0 for _ in range(4)]
    i=0
    averageWithoutGuide=[]
    for each in knowledgePointsWithoutGuide:
        knowledgeDecisionArrayWithoutGuides[0][each] +=1
        knowledgeDecisionArrayWithoutGuides[1][each] += pointCounterWithoutGuide[i]
        i +=1
    counter = 0
    for each in range(len(knowledgeDecisionArrayWithoutGuides[0])):
        if not knowledgeDecisionArrayWithoutGuides[0][each] == 0:
            knowledgeDecisionArrayWithoutGuides[1][each] = knowledgeDecisionArrayWithoutGuides[1][each] / \
                                                        knowledgeDecisionArrayWithoutGuides[0][each]
        else:
            knowledgeDecisionArrayWithoutGuides[1][each] = 0
        averageWithoutGuide.append(knowledgeDecisionArrayWithoutGuides[1][each])
        print(f"There are {knowledgeDecisionArrayWithoutGuides[0][counter]} players without guides with {counter} points in previous environmental knowledge who gained on average {knowledgeDecisionArrayWithoutGuides[1][counter]} points in the decision of the game.")
        counter += 1

    # Your arrays
    knowledgeDecisionArrayWithGuides = [0, 5.0, 6.666666666666667, 8.666666666666666]
    knowledgeDecisionArrayWithoutGuides = [0, 6.0, 6.0, 6.5]

    # Set the positions and width for the bars
    pos = list(range(len(knowledgeDecisionArrayWithGuides)))
    width = 0.35

    # Plotting the bars
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a bar with pre-score data in position pos
    bars1 = ax.bar(pos, knowledgeDecisionArrayWithGuides, width,  label='With Guides')

    # Create a bar with mid-score data in position pos + some width buffer
    bars2 = ax.bar([p + width for p in pos], knowledgeDecisionArrayWithoutGuides, width,
                   label='Without Guides')

    # Set the y axis label
    ax.set_ylabel("Average correct\nevent decisions",fontdict={"fontsize": 14})

    # Set the x axis label
    ax.set_xlabel("Correct knowledge questions",fontdict={"fontsize": 14})

    # Set the position of the x ticks
    ax.set_xticks([p + width / 2 for p in pos])

    # Set the labels for the x ticks
    ax.set_xticklabels([f'{i}' for i in pos])

    # Setting the x-axis and y-axis limits
    ax.set_xlim(left=0, right=len(pos) + width)
    ax.set_ylim(bottom=0, top=10)

    # Adding the legend
    ax.legend(loc='upper left')

    # Function to add value labels on top of each bar
    def add_value_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom')

    # Add value labels for both sets of bars
    add_value_labels(bars1)
    add_value_labels(bars2)

    plt.show()
    """
    #print(pearsonr([0,1,2,3],[0,6,6,6.5]))
    fig, ax = plt.subplots()
    ax.set_ylabel("Correct\nevent\ndecisions")
    ax.set_xlabel("Correct knowledge questions")
    ax.set_ylim(0,10)
    ax.bar(x=["0","1","2","3"],height=knowledgeDecisionArrayWithoutGuides[1])"""

    """
    withGuide= knowledgePointsWithGuide
    withoutGuide = knowledgePointsWithoutGuide
    
    print(withGuide,withoutGuide)
    print(shapiro(withGuide))
    print(shapiro(withoutGuide))


    # Perform a t-test
    t_stat, p_value = stats.ttest_ind(withGuide, withoutGuide, equal_var=False)
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
    """

def interrestAffectionRatio(arousalWithGuide, arousalWithoutGuide, valenceWithGuide, valenceWithoutGuide, envPrioWithGuide, envPrioWithoutGuide):
    """
    Assessment 3 -> Events Arousal/Valence\n
    Individual(mit/ohne Guide): Ranking Klimawandel -> Durchschnitt Arousal & Distanz von 5 Valance\n
    “Wie weit bestimmt das Interesse der Spieler den emotionalen Affekt der Guides?”\n
    TODO Ass 8
    """
    i=0
    for each in envPrioWithGuide:
       print(f"For the player with guides envPrio is {each} there is an average Arousal of {avgArousal(arousalWithGuide[i])} and average Valance of{avgValance(valenceWithGuide[i])}")
       i+=1
    i=0
    for each in envPrioWithoutGuide:
       print(f"For the player without guides envPrio is {each} there is an average Arousal of {avgArousal(arousalWithoutGuide[i])} and average Valance of {avgValance(valenceWithoutGuide[i])}")
       i+=1
    """Array mit [Anzahl der Spieler mit #environmental Priorty],[average arousal], [averqage valance]"""
    envPrioValArousalWithGuides = [0 for _ in range(6)], [0 for _ in range(6)], [0 for _ in range(6)]
    i=0
    for each in envPrioWithGuide:
        envPrioValArousalWithGuides[0][int(each-1)] += 1
        envPrioValArousalWithGuides[1][int(each-1)] += avgArousal(arousalWithGuide[i])
        envPrioValArousalWithGuides[2][int(each-1)] += avgValance(valenceWithGuide[i])
        i +=1
    for i in range(6):
        if envPrioValArousalWithGuides[0][i] != 0:
            envPrioValArousalWithGuides[1][i] = envPrioValArousalWithGuides[1][i]/envPrioValArousalWithGuides[0][i]
            envPrioValArousalWithGuides[2][i] = envPrioValArousalWithGuides[2][i]/envPrioValArousalWithGuides[0][i]
    print(envPrioValArousalWithGuides)

    envPrioValArousalWithoutGuides = [0 for _ in range(6)], [0 for _ in range(6)], [0 for _ in range(6)]
    i=0
    for each in envPrioWithoutGuide:
        envPrioValArousalWithoutGuides[0][int(each-1)] += 1
        envPrioValArousalWithoutGuides[1][int(each-1)] += avgArousal(arousalWithoutGuide[i])
        envPrioValArousalWithoutGuides[2][int(each-1)] += avgValance(valenceWithoutGuide[i])
        i +=1
    for i in range(6):
        if envPrioValArousalWithoutGuides[0][i] != 0:
            envPrioValArousalWithoutGuides[1][i] = envPrioValArousalWithoutGuides[1][i]/envPrioValArousalWithoutGuides[0][i]
            envPrioValArousalWithoutGuides[2][i] = envPrioValArousalWithoutGuides[2][i]/envPrioValArousalWithoutGuides[0][i]
    #print(envPrioValArousalWithoutGuides)
    arousalArray = {
        "Arousal with guides": tuple(envPrioValArousalWithGuides[1]),
        "Arousal without guides": tuple(envPrioValArousalWithoutGuides[1])
    }
    fig, ax = plt.subplots(layout='constrained')
    description = ("1", "2", "3", "4", "5", "6")
    x = np.arange(len(description))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    for name, values in arousalArray.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, values, width, label=name)
        # Round the labels to two decimal places and adjust padding
        ax.bar_label(rects, labels=[f'{val:.2f}' for val in values], padding=5)
        multiplier += 1

    ax.set_ylabel("Average arousal score")
    ax.set_xlabel("Environmental Priority")
    ax.set_xticks(x + width, description)
    ax.legend(loc='upper left', ncols=2)
    ax.set_ylim(0, 9)
    plt.show()

    envPrioValArousalWithGuides = [0 for _ in range(6)], [0 for _ in range(6)], [0 for _ in range(6)]
    i=0
    for each in envPrioWithGuide:
        envPrioValArousalWithGuides[0][int(each-1)] += 1
        envPrioValArousalWithGuides[1][int(each-1)] += avgArousal(arousalWithGuide[i])
        envPrioValArousalWithGuides[2][int(each-1)] += avgValance(valenceWithGuide[i])
        i +=1
    for i in range(6):
        if envPrioValArousalWithGuides[0][i] != 0:
            envPrioValArousalWithGuides[1][i] = envPrioValArousalWithGuides[1][i]/envPrioValArousalWithGuides[0][i]
            envPrioValArousalWithGuides[2][i] = envPrioValArousalWithGuides[2][i]/envPrioValArousalWithGuides[0][i]
    print(envPrioValArousalWithGuides)

    envPrioValArousalWithoutGuides = [0 for _ in range(6)], [0 for _ in range(6)], [0 for _ in range(6)]
    i=0
    for each in envPrioWithoutGuide:
        envPrioValArousalWithoutGuides[0][int(each-1)] += 1
        envPrioValArousalWithoutGuides[1][int(each-1)] += avgArousal(arousalWithoutGuide[i])
        envPrioValArousalWithoutGuides[2][int(each-1)] += avgValance(valenceWithoutGuide[i])
        i +=1
    for i in range(6):
        if envPrioValArousalWithoutGuides[0][i] != 0:
            envPrioValArousalWithoutGuides[1][i] = envPrioValArousalWithoutGuides[1][i]/envPrioValArousalWithoutGuides[0][i]
            envPrioValArousalWithoutGuides[2][i] = envPrioValArousalWithoutGuides[2][i]/envPrioValArousalWithoutGuides[0][i]
    print(envPrioValArousalWithoutGuides)
    valanceArray = {
        "Valence with guides": tuple(envPrioValArousalWithGuides[2]),
        "Valence without guides": tuple(envPrioValArousalWithoutGuides[2])
    }
    fig, ax = plt.subplots(layout='constrained')
    description = ("1", "2", "3", "4", "5", "6")
    x = np.arange(len(description))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    for name, values in valanceArray.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, values, width, label=name)
        # Round the labels to two decimal places
        ax.bar_label(rects, labels=[f'{val:.2f}' for val in values], padding=5)
        multiplier += 1

    ax.set_ylabel("Average valence score")
    ax.set_xlabel("Environmental Priority")
    ax.set_xticks(x + width, description)
    ax.legend(loc='upper left', ncols=2)
    ax.set_ylim(0, 9)
    plt.show()

    print("Arousal")
    print(shapiro(envPrioValArousalWithGuides[1]))
    print(shapiro(envPrioValArousalWithoutGuides[1]))
    print(shapiro(envPrioValArousalWithGuides[2]))
    print(shapiro(envPrioValArousalWithoutGuides[2]))





def avgArousal(data):
    """
    Get an arousal array, return average value of arousal.
    """
    temp = 0
    for each in data:
        temp += each
    return temp/len(data)
def avgValance(data):
    """
    Get a valance array, return average value of valance.
    """
    temp = 0
    for each in data:
        temp += each
    return temp/len(data)

def gamingExpertise(datawithguide, datawithoutguide, decisionsWithGuide, decisionsWithoutGuide):
    """
    Assessment 7 -> PG3
    “Haben die Spieler mit Guide sich weniger auf ihr Spielerfahrung verlassen?”
    """
    """Create an array. The Collum represents the gaming experience, the first row the cumulated points from the decisions, the second row how many players contributed."""
    expertiseArraywithGuide = [0 for _ in range(6)],[0 for _ in range(6)]
    """
    At first get an Array with the gaming Experiese for all the Players (Ass7)
    Then get the get the Points of the events for each player
    The order the """
    gamingExpertiseWithGuides = getGamingExperties(getAssessment(datawithguide))
    i=0
    eventsWithGuide=[]
    for each in extractEvents(datawithguide):
        eventsWithGuide.append(each[0][0])
    for each in gamingExpertiseWithGuides:
        decision = evaluateDecision(eventsWithGuide[i])
        i +=1
        expertiseArraywithGuide[0][int(each) - 1] = expertiseArraywithGuide[0][int(each) - 1] + decision
        expertiseArraywithGuide[1][int(each) - 1] +=1
    outputWithGuide = []
    print("The players with guides have:")
    for i in range(6):
        outputWithGuide.append(expertiseArraywithGuide[0][i]/expertiseArraywithGuide[1][i])
        print(f"with {i+1} gaming experience, on average {outputWithGuide[i]} points in the events")

    expertiseArrayWithoutGuide = [0 for _ in range(6)
                               ],[0 for _ in range(6)]
    gamingExpertiseWithoutGuides = getGamingExperties(getAssessment(datawithoutguide))
    i=0
    eventsWithoutGuide=[]
    for each in extractEvents(datawithoutguide):
        eventsWithoutGuide.append(each[0][0])
    for each in gamingExpertiseWithoutGuides:
        decision = evaluateDecision(eventsWithoutGuide[i])
        i +=1
        expertiseArrayWithoutGuide[0][int(each) - 1] = expertiseArrayWithoutGuide[0][int(each) - 1] + decision
        expertiseArrayWithoutGuide[1][int(each) - 1] +=1
    outputWithoutGuide = []
    print("The players without guides have:")
    for i in range(6):
        outputWithoutGuide.append(expertiseArrayWithoutGuide[0][i]/expertiseArrayWithoutGuide[1][i])
        print(f"with {i+1} gaming experience, on average {outputWithoutGuide[i]} points in the events")


    experienceDecisionArray = {
        "Average correct event decisions\n with guides": tuple(outputWithGuide),
        "Average correct event decisions\n without guides": tuple(outputWithoutGuide)
    }
    withGuide = outputWithGuide
    withoutGuide =outputWithoutGuide
    print(withGuide)
    print(withoutGuide)
    print(shapiro(withGuide))
    print(shapiro(withoutGuide))
    print(ttest_ind(withGuide,withoutGuide,equal_var=False))


    fig, ax = plt.subplots()
    description = ("Less than 1 h", "1-3 h", "4-5 h", "6-7 h", "8-9 h", "10 or more h")
    x = np.arange(len(description))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0
    for name, values in experienceDecisionArray.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, values, width, label=name)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel("Average correct event decisions")
    ax.set_xlabel("Hours of video games per week")
    ax.set_xticks(x + width, description)

    ax.legend(loc='upper left', ncols=2)
    ax.set_ylim(0, 10)
    plt.show()


def enviroKnowledgeDecisionMaking(datawithguide, datawithoutguide):
    """Haben die Spieler mit Guide sich weniger auf ihr Vorwissen zur Umwelt verlassen?"""
    enviroPrioArrayWithGuide =envPrio(datawithguide)
    envKnowledgeInfluenceArrayWithGuide = envKnowledgeInfluence(datawithguide)
    enviroPrioArrayWithoutGuide = envPrio(datawithoutguide)
    envKnowledgeInfluenceArrayWithoutGuide = envKnowledgeInfluence(datawithoutguide)

    expertiseArrayWithGuide = [0 for _ in range(6)],[0 for _ in range(6)]
    """Fill the following Block by first row with amount of players with how much time they spent on environmental issues. The second row with the sum of the influence."""
    for i in range(len(enviroPrioArrayWithGuide)):
        expertiseArrayWithGuide[0][int(enviroPrioArrayWithGuide[i])-1] += 1
        expertiseArrayWithGuide[1][int(enviroPrioArrayWithGuide[i])-1] += int(envKnowledgeInfluenceArrayWithGuide[i])
    """The following block formats the array for the print."""
    avgWithGuideList= []
    for i in range(len(expertiseArrayWithGuide[0])):
        a = expertiseArrayWithGuide[0][i]
        b = expertiseArrayWithGuide[1][i]
        if expertiseArrayWithGuide[0][i] == 0:
            avgWithGuide = 0
        else:
            avgWithGuide = expertiseArrayWithGuide[1][i]/expertiseArrayWithGuide[0][i]
        avgWithGuideList.append(avgWithGuide)
        print(f"{a} players with the following value for time spent on environmental issues: {i+1} say they their decision making was influenced by the following value {b} and an average of {avgWithGuide} ")

    expertiseArrayWithoutGuide = [0 for _ in range(6)],[0 for _ in range(6)]
    """Fill the following Block by first row with amount of players with how much time they spent on environmental issues. The second row with the sum of the influence."""
    for i in range(len(enviroPrioArrayWithoutGuide)):
        expertiseArrayWithoutGuide[0][int(enviroPrioArrayWithoutGuide[i])-1] += 1
        expertiseArrayWithoutGuide[1][int(enviroPrioArrayWithoutGuide[i])-1] += int(envKnowledgeInfluenceArrayWithoutGuide[i])
    """The following block formats the array for the print."""
    avgWithoutGuideList =[]
    for i in range(len(expertiseArrayWithoutGuide[0])):
        a = expertiseArrayWithoutGuide[0][i]
        b = expertiseArrayWithoutGuide[1][i]
        if expertiseArrayWithoutGuide[0][i] == 0:
            avgWithoutGuide = 0
        else:
            avgWithoutGuide = expertiseArrayWithoutGuide[1][i]/expertiseArrayWithoutGuide[0][i]
        avgWithoutGuideList.append(float("{:.2f}".format(avgWithoutGuide)))
        print(f"{a} players with the following value for time spent on environmental issues: {i+1} say they their decision making was influenced by the following value {b} and an average of {avgWithoutGuide} ")

    experienceDecisionArray = {
        "Answers with guides": tuple(avgWithGuideList),
        "Answers without guides": tuple(avgWithoutGuideList)
    }
    fig, ax = plt.subplots()
    descriptionX = ("Less than 1 h", "1-3 h", "4-5 h", "6-7 h", "8-9 h", "10 or more h")
    descriptionY = (" ","Very\nlittle\ninfluence", "Little\ninfluence", "Some\ninfluence", "Strong\ninfluence", "Very\nstrong\ninfluence")
    x = np.arange(len(descriptionX))  # the label locations
    width = 0.4  # the width of the bars
    multiplier = 0
    for name, values in experienceDecisionArray.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, values, width, label=name)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel("Average influence of previous knowledge")
    ax.set_xlabel("Time spent with environmental issues ")
    ax.set_xticks(x + width, descriptionX)
    ax.set_yticks(x,descriptionY)

    ax.legend(loc='upper left', ncols=2)
    #ax.set_ylim(0, 6)
    plt.show()

    withGuide = expertiseArrayWithGuide[0]
    withoutGuide = expertiseArrayWithoutGuide[0]
    print(withGuide)
    print(withoutGuide)
    print(shapiro(withGuide))
    print(shapiro(withoutGuide))
    print(ttest_ind(withGuide, withoutGuide, equal_var=False))
    withGuideAvg = expertiseArrayWithGuide[1]
    withoutGuideAvg = expertiseArrayWithoutGuide[1]
    print(withGuideAvg)
    print(withoutGuideAvg)
    print(shapiro(withGuideAvg))
    print(shapiro(withoutGuideAvg))
    print(ttest_ind(withGuideAvg, withoutGuideAvg, equal_var=False))

def gameGoal(datawithguide, datawithoutguide):
    """“Ist das Spielziel durch das Visuelle/Story-Element des Guides klarer in Erinnerung?”"""
    gameGoalWithGuide = gameGoalData(datawithguide)
    gameGoalWithoutGuide = gameGoalData(datawithoutguide)

    goalArray = [0 for _ in range(5)], [0 for _ in range(5)]
    """Fill the following Block by first row with amount of players with how much time they spent on environmental issues. The second row with the sum of the influence."""
    for i in range(len(gameGoalWithGuide)):
        goalArray[0][int(gameGoalWithGuide[i])-1] += 1
    for i in range(len(gameGoalWithoutGuide)):
        goalArray[1][int(gameGoalWithoutGuide[i])-1] += 1
    print(f"The players with guides have the following distribution {goalArray[0]} with an average Value of {numpy.sum(gameGoalWithGuide)/len(gameGoalWithGuide)}\n"
          f"The players without guides have the following distribution {goalArray[1]} with an average Value of {numpy.sum(gameGoalWithoutGuide)/len(gameGoalWithoutGuide)}")

    # Prepare data for boxplot
    goalArray = [gameGoalWithGuide, gameGoalWithoutGuide]
    labelsX = ["Players\nwith\nguides", "Players\nwithout\nguides"]
    x = np.arange(len(labelsX))  # the label locations

    # Create the plot
    fig, ax = plt.subplots()
    ax.set_ylabel("Instructional goal")

    # Create boxplot with custom colors
    boxprops = dict(linestyle='-', linewidth=2)
    medianprops = dict(linestyle='-', linewidth=2, color='red')
    boxplot = ax.boxplot(goalArray, patch_artist=True, boxprops=boxprops, medianprops=medianprops)

    # Set colors for the boxes
    colors = ['blue', 'orange']
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)

    ax.set_ylim(0, 5)

    # Set custom y-ticks and labels
    yticks = [1, 2, 3, 4, 5]
    yticklabels = ["Very\nUnclear", "Little\nUnclear", "Neutral", "Little\nClear", "Very\nClear"]
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)

    # Set x-tick labels
    ax.set_xticklabels(labelsX)

    # Show the plot
    plt.show()

    withGuide = [3, 4, 2, 4, 4, 5, 5, 4, 1, 5, 2, 5, 4, 1]#gameGoalWithGuide
    withoutGuide = [1,4,3,5,2,5,5,5,4]#gameGoalWithoutGuide
    print(withGuide)
    print(withoutGuide)
    print(shapiro(withGuide))
    print(shapiro(withoutGuide))
    print(ttest_ind(withGuide, withoutGuide, equal_var=False))

def recallEventKnowledge(datawithguide, datawithoutguide):
    "Behalten Spieler mit Guides mehr Infos bei?"
    recallEventWithGuide = getAttentionData(datawithguide)
    recallEventWithoutGuide = getAttentionData(datawithoutguide)

    expertiseArraywithGuide = [0 for _ in range(4)],[0 for _ in range(4)]
    expertiseArraywithoutGuide = [0 for _ in range(4)],[0 for _ in range(4)]
    i=0
    for each in recallEventWithGuide:
        result = pgqattention(recallEventWithGuide[i])
        i +=1
        expertiseArraywithGuide[0][result ] = expertiseArraywithGuide[0][result ] + result
        expertiseArraywithGuide[1][result ] +=1
    totalWithGuide = np.sum(expertiseArraywithGuide[1])
    print(f"Spieler mit Guide erinnern sich: ")
    print(f"An 0 Events: {expertiseArraywithGuide[1][0]/totalWithGuide}\n"
          f"An 1 Events: {expertiseArraywithGuide[1][1]/totalWithGuide}\n"
          f"An 2 Events: {expertiseArraywithGuide[1][2]/totalWithGuide}\n"
          f"An 3 Events: {expertiseArraywithGuide[1][3]/totalWithGuide}")

          #f"Mit einem Durschnitt von {numpy.sum(expertiseArraywithGuide[0])/numpy.sum(expertiseArraywithGuide[1])}")

    i=0
    for each in recallEventWithoutGuide:
        result = pgqattention(recallEventWithoutGuide[i])
        i +=1
        expertiseArraywithoutGuide[0][result ] = expertiseArraywithoutGuide[0][result ] + result
        expertiseArraywithoutGuide[1][result ] +=1

    totalWithoutGuide = np.sum(expertiseArraywithoutGuide[1])
    print(f"Spieler ohne Guide erinnern sich: ")
    print(f"An 0 Events: {expertiseArraywithoutGuide[1][0]/totalWithoutGuide}\n"
          f"An 1 Events: {expertiseArraywithoutGuide[1][1]/totalWithoutGuide}\n"
          f"An 2 Events: {expertiseArraywithoutGuide[1][2]/totalWithoutGuide}\n"
          f"An 3 Events: {expertiseArraywithoutGuide[1][3]/totalWithoutGuide}\n")
     #f"Mit einem Durschnitt von {numpy.sum(expertiseArraywithoutGuide[0])/numpy.sum(expertiseArraywithoutGuide[1])}")

    # Prepare the data for plotting
    memoryArraywithGuide = expertiseArraywithGuide[1] #[0, 6, 8, 0]
    memoryArraywithoutGuide = expertiseArraywithoutGuide[1]#[1, 2, 5, 1]

    # Convert to relative values
    memoryArraywithGuide = [x / sum(memoryArraywithGuide) for x in memoryArraywithGuide]
    memoryArraywithoutGuide = [x / sum(memoryArraywithoutGuide) for x in memoryArraywithoutGuide]

    print(memoryArraywithGuide)
    print(memoryArraywithoutGuide)
    print(shapiro(memoryArraywithGuide))
    print(shapiro(memoryArraywithoutGuide))
    print(ttest_ind(memoryArraywithGuide,memoryArraywithoutGuide, equal_var=True))


    # Convert to percentage values
    memoryArraywithGuide = [x * 100 for x in memoryArraywithGuide]
    memoryArraywithoutGuide = [x * 100 for x in memoryArraywithoutGuide]

    # Labels for the x-axis
    labelsX = ["0 Events", "1 Event", "2 Events", "3 Events"]
    x = np.arange(len(labelsX))  # the label locations

    # Width of the bars
    width = 0.35

    # Create the plot
    fig, ax = plt.subplots()

    # Plot the bars for each category
    bars1 = ax.bar(x - width / 2, memoryArraywithGuide, width, label='Players with guides')
    bars2 = ax.bar(x + width / 2, memoryArraywithoutGuide, width, label='Players without guides')

    # Set the labels and title
    ax.set_xlabel('Remembered events')
    ax.set_ylabel('Percentage of players')
    # ax.set_title('Comparison of Remembered Events')
    ax.set_xticks(x)
    ax.set_xticklabels(labelsX)
    ax.legend()
    
    # Add text annotations on top of each bar
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}%', ha='center', va='bottom')

    add_labels(bars1)
    add_labels(bars2)

    # Show the plot
    plt.show()




def affectionGuideRelation(datawithguide, arousalWithGuide, valenceWithGuide):
    """Wie sehr wirkt sich der erzielte Affekt auf die Informationserinnerung aus"""
    guideQuestions = getGuideQuestions(datawithguide)
    guidePoints = guideQuestionEval(guideQuestions)
    arousalPoints = getCertainArousal(arousalWithGuide)
    valencePoints = getCertainValance(valenceWithGuide)
    guideArousalValenceArray = [0 for _ in range(4)], [0 for _ in range(4)], [0 for _ in range(4)]
    i=0
    arousalAvgList = []
    valenceAvgList = []
    arousalTotalValuesList = []
    valenceTotalValuesList = []


    print(arousalPoints)
    print(shapiro(arousalPoints))
    print(valencePoints)
    print(shapiro(valencePoints))

    for each in guidePoints:
        guideArousalValenceArray[0][each] +=1
        guideArousalValenceArray[1][each] += arousalPoints[i]
        arousalTotalValuesList.append(arousalPoints[i])
        guideArousalValenceArray[2][each] += valencePoints[i]
        valenceTotalValuesList.append(valencePoints[i])
        i +=1
    for i in range(4):
        arousal = guideArousalValenceArray[1][i]
        valence = guideArousalValenceArray[2][i]
        player = guideArousalValenceArray[0][i]

        if player == 0:
            arousalAvg = None
            valanceAvg = None
        else:
            arousalAvg = arousal/player
            valanceAvg = valence/player
        arousalAvgList.append(arousalAvg)
        valenceAvgList.append(valanceAvg)
        print(f"There are {player} players with {i} points for the Guide Questions\n"
              f"an average arousal value for the corresponding events of {arousalAvg}\n"
              f"and an average valence value for the corresponding events of {valanceAvg}")
    #print(arousalAvgList,valenceAvgList)
    x_labels = ["0 Answers", "1 Answers", "2 Answers", "3 Answers"]

    # Create the bar graph
    plt.bar(x_labels, arousalAvgList)

    # Add labels and title
    plt.xlabel('Correct Answers')
    plt.ylabel('Arousal Average')
    plt.title('Arousal Average by Points')


    # Add exact values on top of each bar
    for i, value in enumerate(arousalAvgList):
        plt.text(i, value + 0.05, f'{value:.3f}', ha='center', va='bottom')

    # Set the Y-axis to range from 0 to 9 with increments of 1
    plt.yticks(np.arange(0, 10, 1))
    # Show the plot
    plt.show()
    print('Arousal Average by Points')
    print(pearsonr([0,1,2,3],arousalAvgList))

    plt.bar(x_labels, valenceAvgList)

    # Add labels and title
    plt.xlabel('Correct Answers')
    plt.ylabel('Valance Average')
    plt.title('Valence Average by Points')

    # Add exact values on top of each bar
    for i, value in enumerate(valenceAvgList):
        plt.text(i, value + 0.05, f'{value:.3f}', ha='center', va='bottom')

    # Set the Y-axis to range from 0 to 9 with increments of 1
    plt.yticks(np.arange(0, 10, 1))

    # Show the plot
    plt.show()
    print('Arousal Valence by Points')
    print(pearsonr([0,1,2,3],valenceAvgList))

def guidePopularityDecisionComparision(datawithguide, decisionsWithGuide):
    """Lassen sich Spieler mehr von Guides beeinflussen die sie toll finden"""
    popularityArray = getGuidePoularity(datawithguide)
    decisionArray = []
    for each in decisionsWithGuide:
        decisionArray.append(evaluateDecisionLeftRight(each))
    "An array with priority = array position [Amount of players who prefer the guide ],[decision points for left guide], [decision points for right guide]"

    guidePopularityDecisionArray = [0 for _ in range(5)], [0 for _ in range(5)], [0 for _ in range(5)]
    i=0
    for each in popularityArray:
        guidePopularityDecisionArray[0][each-1] +=1
        guidePopularityDecisionArray[1][each-1] += decisionArray[i][0]
        guidePopularityDecisionArray[2][each-1] += decisionArray[i][1]
        i +=1
    for i in range(5):
        if guidePopularityDecisionArray[0][i] != 0:
            print(f"Players {guidePopularityDecisionArray[0][i]} with priority {i} prefere on average left guide point {guidePopularityDecisionArray[1][i]/guidePopularityDecisionArray[0][i]} and right guide points {guidePopularityDecisionArray[2][i]/guidePopularityDecisionArray[0][i]}")
            guidePopularityDecisionArray[1][i] = guidePopularityDecisionArray[1][i]/guidePopularityDecisionArray[0][i]
            guidePopularityDecisionArray[2][i] = guidePopularityDecisionArray[2][i]/guidePopularityDecisionArray[0][i]
        else:
            print(
                f"Players {0} with priority {i} prefere on average left guide point {0} and right guide points {0}")
    print(guidePopularityDecisionArray)

    # Data
    player_counts = guidePopularityDecisionArray[0]
    left_guide_scores = guidePopularityDecisionArray[1]
    right_guide_scores = guidePopularityDecisionArray[2]
    preferences = ['Prefer left guide a lot', 'Prefer left guide', 'Prefer neither', 'Prefer right guide',
                   'Prefer right guide a lot']

    # Set the width of the bars
    bar_width = 0.35

    # Set the positions of the bars on the x-axis
    r1 = np.arange(len(preferences))
    r2 = [x + bar_width for x in r1]

    # Create the bar graph
    plt.figure(figsize=(12, 8))

    # Plotting the bars
    bars1 = plt.bar(r1, left_guide_scores, color='b', width=bar_width, edgecolor='grey', label='Left Guide Answers')
    bars2 = plt.bar(r2, right_guide_scores, color='r', width=bar_width, edgecolor='grey', label='Right Guide Answers')

    # Add player counts as text annotations
    for i, count in enumerate(player_counts):
        plt.text(r1[i] + bar_width / 2, max(left_guide_scores[i], right_guide_scores[i]) + 0.1, f'Amount of Players ={count}',
                 horizontalalignment='center', fontsize=10, color='black')

    # Adding labels and title
    plt.xlabel('Player Preferences', fontweight='bold')
    plt.xticks([r + bar_width / 2 for r in range(len(preferences))], preferences, rotation=45, ha='right')
    plt.ylabel('Average Correct Decisions')
    plt.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()
    print(guidePopularityDecisionArray[0])
    print(shapiro(guidePopularityDecisionArray[0]))



def decisionPointsComparision(decisionsWithGuide, decisionsWithoutGuide):
    decisionArrayWithGuide = []
    for each in decisionsWithGuide:
        decisionArrayWithGuide.append(evaluateDecision(each))
    decisionArrayWithoutGuide = []
    for each in decisionsWithoutGuide:
        decisionArrayWithoutGuide.append(evaluateDecision(each))
    decisionArray = [0 for _ in range(11)], [0 for _ in range(11)]

    for i in range(len(decisionArrayWithGuide)):
        decisionArray[0][decisionArrayWithGuide[i]] += 1
    for each in range(len(decisionArrayWithoutGuide)):
        decisionArray[1][decisionArrayWithoutGuide[each]] += 1
    for counter in range(len(decisionArray[0])):
        print(f"There are {decisionArray[0][counter]} players with guide who gained {counter} points and {decisionArray[1][counter]} players without guides who gained {counter} points.")
    avgWithGuide =numpy.average(decisionArrayWithGuide)
    avgWithoutGuide = numpy.average(decisionArrayWithoutGuide)
    print(f"\nThe players with guides gained {avgWithGuide} points on average and the players without guide gained {avgWithoutGuide} points on average.\n"
          f"The players with guides have an {(1-(avgWithoutGuide/avgWithGuide))*100}% advantage over the players without guides.")
    #print(decisionArray)


    # Convert the decisionArray into two separate lists
    with_guide = (decisionArrayWithGuide)  #[9, 6, 7, 2, 7, 4, 6, 6, 8, 9, 8, 6, 4, 9] \

    print(with_guide)
    without_guide =(decisionArrayWithoutGuide)# [7, 5, 7, 6, 5, 8, 6, 6, 5]\

    print(without_guide)
    # Create data for boxplot
    # Create data for boxplot
    data = [with_guide, without_guide]

    # Create a boxplot
    plt.figure(figsize=(10, 6))

    # Create boxplot with custom colors
    boxprops = dict(linestyle='-', linewidth=2)
    medianprops = dict(linestyle='-', linewidth=2, color='red')

    bp = plt.boxplot(data, labels=['With Guide', 'Without Guide'],
                     patch_artist=True, boxprops=boxprops, medianprops=medianprops)

    # Color the boxes
    colors = ['blue', 'orange']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    plt.ylim(0, 10)  # Set the Y-axis scale from 0 to 10
    plt.yticks(np.arange(0, 11, 1))  # Set Y-axis ticks from 0 to 10 with increments of 1
    plt.ylabel('Number of Correct Answers')
    plt.show()

    # Shapiro-Wilk test for normality
    print(shapiro(with_guide))
    print(shapiro(without_guide))

    # Perform a t-test
    t_stat, p_value = stats.ttest_ind(with_guide, without_guide, equal_var=False)
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")


def presenterAge(datawithguide, datawithoutguide):
    ageWithGuide = getAge(datawithguide)
    ageWithoutGuide = getAge(datawithoutguide)
    """labels = ["Group age\n with \nguides", "Group age\n without \nguides"]
    plt.boxplot([ageWithGuide,ageWithoutGuide], orientation= "horizontal", tick_labels= labels)
    #plt.bar(ageWithGuide, height=25)
    plt.show()"""
    print(ageWithGuide)
    print(ageWithoutGuide)
    ageArray = [[item for subarray in [ageWithGuide,ageWithoutGuide] for item in subarray]][0]
    print(ageArray)
    sum_array = [0]*6
    for each in ageArray:
        sum_array[each-1] += 1
    print(sum_array)
    fig, ax = plt.subplots()
    ax.set_ylabel("Amount of playtesters")
    ax.set_xlabel("Age")
    ax.set_ylim(0, 25)
    bars= ax.bar(x=["18-24","25-34","35-44","45-54","55-64", "65+"],height=sum_array)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{int(height)}',
                ha='center', va='bottom')

    plt.show()
def presenterGender(datawithguide, datawithoutguide):
    genderWithGuide = getGender(datawithguide)
    genderWithoutGuide = getGender(datawithoutguide)
    """
    labels = ["Group age\n with \nguides", "Group age\n without \nguides"]
    plt.boxplot([genderWithGuide, genderWithoutGuide], orientation="horizontal", tick_labels=labels)
    plt.show()
    """
    print(genderWithGuide)
    print(genderWithoutGuide)
    genderArray = [[item for subarray in [genderWithGuide, genderWithoutGuide] for item in subarray]][0]
    sum_array = [0] * 4
    for each in genderArray:
        sum_array[each - 1] += 1
    print(sum_array)

    fig, ax = plt.subplots()
    ax.set_ylabel("Amount of playtesters")
    ax.set_xlabel("Gender")
    ax.set_ylim(0, 20)

    # Set y-axis ticks to increment by 1
    ax.set_yticks(range(0, 21, 1))

    # Plot bars
    bars = ax.bar(x=["Male", "Female", "Diverse", "Prefer not to say"], height=sum_array)

    # Display the value of each bar on top of it
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{int(height)}',
                ha='center', va='bottom')

    plt.show()
def affectionSliderComparison(arousalWithGuide, arousalWithoutGuide, valenceWithGuide, valenceWithoutGuide):
    print(f"arousalWithGuide= {arousalWithGuide}")
    print(f"valanceWithGuide= {valenceWithGuide}")
    print(f"arousalWithoutGuide= {arousalWithoutGuide}")
    print(f"valanceWithoutGuide= {valenceWithoutGuide}")

    # Convert lists to numpy arrays for easier manipulation
    arousalWithGuide = np.array(arousalWithGuide)
    arousalWithoutGuide = np.array(arousalWithoutGuide)
    valenceWithGuide = np.array(valenceWithGuide)
    valenceWithoutGuide = np.array(valenceWithoutGuide)

    # Function to create boxplots with custom median color
    def create_boxplot_with_median_color(data_with_guide, data_without_guide, ylabel, title, median_color_with,
                                         median_color_without):
        plt.figure(figsize=(12, 6))

        # Boxplot for data with guide
        plt.boxplot(data_with_guide, positions=np.arange(0, 20, 2), widths=0.6, showfliers=True, patch_artist=True,
                    boxprops=dict(facecolor="blue", alpha=1), medianprops=dict(color=median_color_with, linewidth=2),
                    vert=False)

        # Boxplot for data without guide
        plt.boxplot(data_without_guide, positions=np.arange(1, 20, 2), widths=0.6, showfliers=True, patch_artist=True,
                    boxprops=dict(facecolor="orange", alpha=1),
                    medianprops=dict(color=median_color_without, linewidth=2), vert=False)

        # Adding labels and title
        plt.yticks(np.arange(0, 20, 2), [f'Event {i}' for i in range(10)])
        plt.xlabel(ylabel)
        plt.title(title)
        plt.legend([plt.Line2D([0], [0], color="blue", lw=4), plt.Line2D([0], [0], color="orange", lw=4)],
                   ['With Guide', 'Without Guide'])

        # Display the plot
        plt.tight_layout()
        plt.show()

    # Create boxplots for arousal and valence
    create_boxplot_with_median_color(arousalWithGuide, arousalWithoutGuide, 'Arousal Value', 'Boxplot of Arousal Values for Each Event', 'red', 'red')
    create_boxplot_with_median_color(valenceWithGuide, valenceWithoutGuide, 'Valence Value', 'Boxplot of Valence Values for Each Event', 'red', 'red')



















