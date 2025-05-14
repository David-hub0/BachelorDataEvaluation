import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import shapiro

import DataConverter
from DataImporter import questionsWithGuide, questionsWithoutGuide, eventsWithGuide, eventsWithoutGuide
import MyMath
from MyMath import extractEvents, extractEventDecisions, datawithguide, datawithoutguide, extractEventValance , extractEventArousal

a_1 = extractEventArousal(extractEvents(datawithguide))
a_2 = extractEventArousal(extractEvents(datawithoutguide))
v_1 = extractEventValance(extractEvents(datawithguide))
v_2 = extractEventValance(extractEvents(datawithoutguide))
d_1 = extractEventDecisions(extractEvents(datawithguide))
d_2 = extractEventDecisions(extractEvents(datawithoutguide))

d = a_2

def boxplotEvents(d):
    ab = []
    temp = []
    for iterator in range(len(d[0])):
        ab = []
        for each in d:
            ab.append(each[iterator])
        temp.append(ab)

    plt.boxplot(temp)
    plt.show()

"""fig = plt.figure(figsize =(10, 7))
ax = fig.add_axes([0, 0, 1, 1])
bp = ax.boxplot(d)"""




