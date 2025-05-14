from scipy.stats import shapiro
import matplotlib.pyplot as plt

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

d = d_1


def datagatherer(d):
    ab = []
    temp = []
    for iterator in range(len(d[0])):
        ab = []
        for each in d:
            ab.append(each[iterator])
        temp.append(ab)
        print(f"Event:{iterator} with the values {ab} p-value= {shapiro(ab)[1]}")
        temp = []

datagatherer(d)


"""
print(np.var(d_1), np.var(d_2))
print(stats.ttest_ind(d_1, d_2, equal_var=True))
"""