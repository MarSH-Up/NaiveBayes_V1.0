import numpy as np
import pandas as pd
from collections import Counter


class Naive_Bayes:
    def __init__(self, csv_name):
        self.csv_name = csv_name
        self.Prob_class = {}
        self.attributes_counter = 0
        self.data_base()

        self.class_true_attribute = dict()
        self.class_false_attribute = dict()


    def data_base(self):
        data = pd.read_csv(self.csv_name, header=0)
        self.data_dict = data.to_dict('series')

    def csv_description(self,cl_name):
        self.cl_name = cl_name
        for x in self.data_dict:
            if x == self.cl_name:
                break
            self.attributes_counter = self.attributes_counter + 1
            testing_true = self.Attribute_per_class_true(self.cl_name, x)
            testing_false = self.Attribute_per_class_false(self.cl_name,x)

            self.Prob_class = self.Probaiblities_ref(testing_true, testing_false)
            """
            for y in testing_false:
                print('Play false: ', testing_false[y])
            for y in testing_true:
                print('Play true: ', testing_true[y])
                """

    def Attribute_per_class_true(self, class_name, attribute_name):
        self.class_name = self.data_dict[class_name]
        self.attribute_2look = self.data_dict[attribute_name]
        self.class_trues = {}

        counter = 0
        for x in self.class_name:
            if x == 'Yes':
                self.class_true_attribute[counter] = self.attribute_2look[counter]
                self.class_trues[counter] = 'Yes'
            counter = counter + 1
        return self.class_true_attribute

    def Attribute_per_class_false(self, class_name, attribute_name):
        self.class_name = self.data_dict[class_name]
        self.attribute_2look = self.data_dict[attribute_name]
        self.class_falses = {}

        counter = 0
        for x in self.class_name:
            if x == 'No':
                self.class_false_attribute[counter] = self.attribute_2look[counter]
                self.class_falses[counter] = 'No'
            counter = counter + 1
        return self.class_false_attribute

    def Probaiblities_ref(self, class_true, class_false):
        Cuenta_trues = Counter(class_true.values())
        Cuenta_falses = Counter(class_false.values())



    def Naives_bayes(self,  attribute_2analysis, key, value):
        self.attribute_2analysis = attribute_2analysis
        print(attribute_2analysis)




Event_1 = Naive_Bayes('Golf_1.csv')
Event_1.csv_description('C1')

