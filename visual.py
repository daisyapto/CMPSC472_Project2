# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import matplotlib.pyplot as plt

class Visual:

    def ageBarGraph(self, data):
        age = data['age']
        bounds = [0, 25, 25.01, 35, 35.01, 45, 45.01, 55, 55.01, 65, 65.01, 120]

        countBar1 = age.between(bounds[0], bounds[1]).sum()
        countBar2 = age.between(bounds[2], bounds[3]).sum()
        countBar3 = age.between(bounds[4], bounds[5]).sum()
        countBar4 = age.between(bounds[6], bounds[7]).sum()
        countBar5 = age.between(bounds[8], bounds[9]).sum()
        countBar6 = age.between(bounds[10], bounds[11]).sum()

        labels = ["<25", ">25-35", ">35-45", ">45-55", ">55-65", "65+"]
        ageCounts = [countBar1, countBar2, countBar3, countBar4, countBar5, countBar6]

        plt.bar(labels, ageCounts)
        plt.title("Age Demographics")
        plt.xlabel("Age")
        plt.ylabel("Count")
        plt.show()

    def maleVsFemaleBarGraph(self, data):
        people = data['sex']
        counts = people.value_counts()
        labels = counts.index
        counts = [counts['male'], counts['female']]
        plt.bar(labels, counts)
        plt.title("Male vs Female")
        plt.ylabel("Count")
        plt.show()

    def bmiBarGraph(self, data):
        bmi = data['bmi']
        bounds = [0, 18.5, 18.51, 22, 22.01, 25, 25.01, 30, 30.01, 32, 32.01, 50]

        countBar1 = bmi.between(bounds[0], bounds[1]).sum()
        countBar2 = bmi.between(bounds[2], bounds[3]).sum()
        countBar3 = bmi.between(bounds[4], bounds[5]).sum()
        countBar4 = bmi.between(bounds[6], bounds[7]).sum()
        countBar5 = bmi.between(bounds[8], bounds[9]).sum()
        countBar6 = bmi.between(bounds[10], bounds[10]).sum()

        labels = ["<18.5", ">18.5-22", ">22-25", ">25-30", "30-32"]
        bmiCounts = [countBar1, countBar2, countBar3, countBar4, countBar5, countBar6]
        plt.bar(labels, bmiCounts)
        plt.title("BMI Demographics")
        plt.xlabel("BMI")
        plt.ylabel("Count")
        plt.show()

    def smokersBarGraph(self, data):
        smokers = data['smoker']
        counts = smokers.value_counts()
        labels = counts.index
        counts = [counts['yes'], counts['no']]
        plt.bar(labels, counts)
        plt.title("Smokers Demographics")
        plt.xlabel("Smoker")
        plt.ylabel("Count")
        plt.show()

    def drawAllBarGraphs(self, data):
        self.ageBarGraph(data)
        self.maleVsFemaleBarGraph(data)
        self.bmiBarGraph(data)
        self.smokersBarGraph(data)
        self.regionBarGraph(data)
        self.numOfChildrenBarGraph(data)
        self.medInsurBarGraph(data)

    def drawLineGraph(self, data):
        x = 1  # Placeholder

    def drawPieGraph(self, data):
        x = 1  # Placeholder