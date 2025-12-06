# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import matplotlib.pyplot as plt
import threading

class Visual:
    def __init__(self):
        self.lock = threading.Lock() # Use to make sure shared resources are accessed only once, not sure how yet

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
        plt.bar(counts.index, counts.values)
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
        labels = ["<18.5", ">18.5-22", ">22-25", ">25-30", "30-32", "32+"]
        bmiCounts = [countBar1, countBar2, countBar3, countBar4, countBar5, countBar6]
        plt.bar(labels, bmiCounts)
        plt.title("BMI Demographics")
        plt.xlabel("BMI")
        plt.ylabel("Count")
        plt.show()

    def smokersBarGraph(self, data):
        smoker = data['smoker']
        counts = smoker.value_counts()
        plt.bar(counts.index, counts.values)
        plt.title("Smoker vs Non-smoker Demographics")
        plt.ylabel("Count")
        plt.show()

    def regionBarGraph(self, data):
        regions = data['region']
        counts = regions.value_counts()
        plt.bar(counts.index, counts.values)
        plt.title("Region Demographics")
        plt.ylabel("Count")
        plt.show()

    def numOfChildrenBarGraph(self, data):
        children = data['children']
        counts = children.value_counts()
        plt.bar(counts.index, counts.values)
        plt.title("Number of Children Demographics")
        plt.ylabel("Count")
        plt.show()

    def medInsurBarGraph(self, data):
        charges = data['charges']
        bounds = [0, 1200, 1200.01, 10000, 10000.01, 20000, 20000.01, 30000, 30000.01, 40000, 40000.01, 50000, 50000.01, 60000, 60000.01, 100000]
        countBar1 = charges.between(bounds[0], bounds[1]).sum()
        countBar2 = charges.between(bounds[2], bounds[3]).sum()
        countBar3 = charges.between(bounds[4], bounds[5]).sum()
        countBar4 = charges.between(bounds[6], bounds[7]).sum()
        countBar5 = charges.between(bounds[8], bounds[9]).sum()
        countBar6 = charges.between(bounds[10], bounds[11]).sum()
        countBar7 = charges.between(bounds[12], bounds[13]).sum()
        countBar8 = charges.between(bounds[14], bounds[15]).sum()
        labels = ["<1200.00", ">1200.00 - 10000.00", ">10000.00 - 20000.00", ">20000.00 - 30000.00", ">30000.00 - 40000.00", ">40000.00 - 50000.00", ">50000.00 - 60000.00", "60000.00+"]
        medCounts = [countBar1, countBar2, countBar3, countBar4, countBar5, countBar6, countBar7, countBar8]
        plt.bar(labels, medCounts)
        plt.title("Medical Insurance Cost Demographics")
        plt.xlabel("Cost ($)")
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

    def ageLineGraph(self, data):
        dataSample = data[['age', 'charges']].sample(n=100)
        age = dataSample['age']
        cost = dataSample['charges']
        data = sorted(zip(age, cost)) # Unsure if we should change this to using one of the algorithms, may make it easier to track time complexity?
        ages, costs = zip(*data)
        plt.plot(ages, costs)
        plt.title("Age vs Medical Insurance Cost")
        plt.xlabel("Age")
        plt.ylabel("Medical Insurance Cost")
        plt.show()


    def bmiLineGraph(self, data):
        dataSample = data[['bmi', 'charges']].sample(n=100)
        bmi = dataSample['bmi']
        cost = dataSample['charges']
        data = sorted(zip(bmi, cost)) # Unsure if we should change this to using one of the algorithms, may make it easier to track time complexity?
        bmis, costs = zip(*data)
        plt.plot(bmis, costs)
        plt.title("BMI vs Medical Insurance Cost")
        plt.xlabel("BMI")
        plt.ylabel("Medical Insurance Cost")
        plt.show()

    def numOfChildrenLineGraph(self, data):
        dataSample = data[['children', 'charges']].sample(n=100)
        numOfChildren = dataSample['children']
        cost = dataSample['charges']
        data = sorted(zip(numOfChildren, cost)) # Unsure if we should change this to using one of the algorithms, may make it easier to track time complexity?
        numOfChildren, costs = zip(*data)
        plt.plot(numOfChildren, costs)
        plt.title("Number of Children vs Medical Insurance Cost")
        plt.xlabel("Number of Children")
        plt.ylabel("Medical Insurance Cost")
        plt.show()

    def drawAllLineGraphs(self, data):
        # The line graphs compare how medical insurance cost increases based on a specific attribute (how insurance cost is affected with age, bmi, and number of children)
        self.ageLineGraph(data)
        self.bmiLineGraph(data)
        self.numOfChildrenLineGraph(data)

    def agePieGraph(self, data):
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
        plt.pie(ageCounts, labels=labels, autopct=lambda val: f'{val*sum(ageCounts)/100:.0f} ({val:.2f}%)', startangle=90) # Reference: google search AI overview, how to get values in pie chart with percentages
        plt.title("Age Demographics")
        plt.show()

    def maleVsFemalePieGraph(self, data):
        people = data['sex']
        counts = people.value_counts()
        plt.pie(counts.values, labels=counts.index, autopct=lambda val: f'{val * sum(counts.values) / 100:.0f} ({val:.2f}%)', startangle=90)  # Reference: google search AI overview, how to get values in pie chart with percentages
        plt.title("Male vs Female")
        plt.show()

    def bmiPieGraph(self, data):
        bmi = data['bmi']
        bounds = [0, 18.5, 18.51, 22, 22.01, 25, 25.01, 30, 30.01, 32, 32.01, 50]
        countBar1 = bmi.between(bounds[0], bounds[1]).sum()
        countBar2 = bmi.between(bounds[2], bounds[3]).sum()
        countBar3 = bmi.between(bounds[4], bounds[5]).sum()
        countBar4 = bmi.between(bounds[6], bounds[7]).sum()
        countBar5 = bmi.between(bounds[8], bounds[9]).sum()
        countBar6 = bmi.between(bounds[10], bounds[10]).sum()
        labels = ["<18.5", ">18.5-22", ">22-25", ">25-30", "30-32", "32+"]
        bmiCounts = [countBar1, countBar2, countBar3, countBar4, countBar5, countBar6]
        plt.pie(bmiCounts, labels=labels, autopct=lambda val: f'{val * sum(bmiCounts) / 100:.0f} ({val:.2f}%)', startangle=90)  # Reference: google search AI overview, how to get values in pie chart with percentages
        plt.title("BMI Demographics")
        plt.show()

    def smokersPieGraph(self, data):
        smoker = data['smoker']
        counts = smoker.value_counts()
        plt.pie(counts.values, labels=counts.index, autopct=lambda val: f'{val * sum(counts.values) / 100:.0f} ({val:.2f}%)', startangle=90)  # Reference: google search AI overview, how to get values in pie chart with percentages
        plt.title("Smoker vs Non-smoker Demographics")
        plt.show()

    def regionPieGraph(self, data):
        regions = data['region']
        counts = regions.value_counts()
        plt.pie(counts.values, labels=counts.index, autopct=lambda val: f'{val * sum(counts.values) / 100:.0f} ({val:.2f}%)', startangle=90)  # Reference: google search AI overview, how to get values in pie chart with percentages
        plt.title("Region Demographics")
        plt.show()

    def numOfChildrenPieGraph(self, data):
        children = data['children']
        counts = children.value_counts()
        plt.pie(counts.values, labels=counts.index, autopct=lambda val: f'{val * sum(counts.values) / 100:.0f} ({val:.2f}%)', startangle=90)  # Reference: google search AI overview, how to get values in pie chart with percentages
        plt.title("Number of Children Demographics")
        plt.show()

    def medInsurPieGraph(self, data):
        charges = data['charges']
        bounds = [0, 1200, 1200.01, 10000, 10000.01, 20000, 20000.01, 30000, 30000.01, 40000, 40000.01, 50000, 50000.01, 60000, 60000.01, 100000]
        countBar1 = charges.between(bounds[0], bounds[1]).sum()
        countBar2 = charges.between(bounds[2], bounds[3]).sum()
        countBar3 = charges.between(bounds[4], bounds[5]).sum()
        countBar4 = charges.between(bounds[6], bounds[7]).sum()
        countBar5 = charges.between(bounds[8], bounds[9]).sum()
        countBar6 = charges.between(bounds[10], bounds[11]).sum()
        countBar7 = charges.between(bounds[12], bounds[13]).sum()
        countBar8 = charges.between(bounds[14], bounds[15]).sum()
        labels = ["<1200.00", ">1200.00 - 10000.00", ">10000.00 - 20000.00", ">20000.00 - 30000.00", ">30000.00 - 40000.00", ">40000.00 - 50000.00", ">50000.00 - 60000.00", "60000.00+"]
        medCounts = [countBar1, countBar2, countBar3, countBar4, countBar5, countBar6, countBar7, countBar8]
        plt.pie(medCounts, labels=labels, autopct=lambda val: f'{val * sum(medCounts) / 100:.0f} ({val:.2f}%)', startangle=90)  # Reference: google search AI overview, how to get values in pie chart with percentages
        plt.title("Medical Insurance Cost Demographics")
        plt.show()

    def drawAllPieGraphs(self, data):
        self.agePieGraph(data)
        self.maleVsFemalePieGraph(data)
        self.bmiPieGraph(data)
        self.smokersPieGraph(data)
        self.regionPieGraph(data)
        self.numOfChildrenPieGraph(data)
        self.medInsurPieGraph(data)