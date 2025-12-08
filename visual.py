# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading

class Visual:
    def __init__(self):
        self.lock = threading.Lock() # Use to make sure shared resources are accessed only once, not sure how yet

    def ageBarGraph(self, data, ax):
        age = data['age']
        bounds = [0, 25, 25.01, 35, 35.01, 45, 45.01, 55, 55.01, 65]
        countBar1 = age.between(bounds[0], bounds[1]).sum()
        countBar2 = age.between(bounds[2], bounds[3]).sum()
        countBar3 = age.between(bounds[4], bounds[5]).sum()
        countBar4 = age.between(bounds[6], bounds[7]).sum()
        countBar5 = age.between(bounds[8], bounds[9]).sum()
        labels = ["<25", ">25-35", ">35-45", ">45-55", ">55-65"]
        ageCounts = [countBar1, countBar2, countBar3, countBar4, countBar5]
        self.lock.acquire()
        ax.bar(labels, ageCounts)
        ax.set_title("Age Demographics")
        ax.set_xlabel("Age")
        ax.set_ylabel("Count")
        self.lock.release()

    def maleVsFemaleBarGraph(self, data, ax):
        people = data['sex']
        counts = people.value_counts()
        self.lock.acquire()
        ax.bar(counts.index, counts.values)
        ax.set_title("Male vs Female")
        ax.set_xlabel("Male vs Female")
        ax.set_ylabel("Count")
        self.lock.release()

    def bmiBarGraph(self, data, ax):
        bmi = data['bmi']
        bounds = [0, 18.5, 18.51, 22, 22.01, 25, 25.01, 30, 30.01, 32]
        countBar1 = bmi.between(bounds[0], bounds[1]).sum()
        countBar2 = bmi.between(bounds[2], bounds[3]).sum()
        countBar3 = bmi.between(bounds[4], bounds[5]).sum()
        countBar4 = bmi.between(bounds[6], bounds[7]).sum()
        countBar5 = bmi.between(bounds[8], bounds[9]).sum()
        labels = ["<18.5", ">18.5-22", ">22-25", ">25-30", "30-32"]
        bmiCounts = [countBar1, countBar2, countBar3, countBar4, countBar5]
        self.lock.acquire()
        ax.bar(labels, bmiCounts)
        ax.set_title("BMI Demographics")
        ax.set_xlabel("BMI")
        ax.set_ylabel("Count")
        self.lock.release()

    def smokersBarGraph(self, data, ax):
        smoker = data['smoker']
        counts = smoker.value_counts()
        self.lock.acquire()
        ax.bar(counts.index, counts.values)
        ax.set_title("Smoker vs Non-smoker Demographics")
        ax.set_xlabel("Smoker")
        ax.set_xlabel("Count")
        self.lock.release()

    def regionBarGraph(self, data, ax):
        regions = data['region']
        counts = regions.value_counts()
        self.lock.acquire()
        ax.bar(counts.index, counts.values)
        ax.set_title("Region Demographics")
        ax.set_xlabel("Region")
        ax.set_ylabel("Count")
        self.lock.release()

    def numOfChildrenBarGraph(self, data, ax):
        children = data['children']
        counts = children.value_counts()
        self.lock.acquire()
        ax.bar(counts.index, counts.values)
        ax.set_title("Number of Children Demographics")
        ax.set_xlabel("Number of Children")
        ax.set_ylabel("Count")
        self.lock.release()

    def medInsurBarGraph(self, data, ax):
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
        labels = ["<1200.00", ">1200.00", ">10000.00", ">20000.00", ">30000.00", ">40000.00", ">50000.00", "60000.00+"]
        medCounts = [countBar1, countBar2, countBar3, countBar4, countBar5, countBar6, countBar7, countBar8]
        self.lock.acquire()
        ax.bar(labels, medCounts)
        ax.set_title("Medical Insurance Cost Demographics")
        ax.set_xlabel("Cost ($)")
        ax.set_ylabel("Count")
        self.lock.release()

    def drawAllBarGraphs(self, data, axAge, axMF, axBMI, axSmoker, axRegion, axNumOfChildren, axMed):
        self.ageBarGraph(data, axAge)
        self.maleVsFemaleBarGraph(data, axMF)
        self.bmiBarGraph(data, axBMI)
        self.smokersBarGraph(data, axSmoker)
        self.regionBarGraph(data, axRegion)
        self.numOfChildrenBarGraph(data, axNumOfChildren)
        self.medInsurBarGraph(data, axMed)

    def ageLineGraph(self, data, ax):
        self.lock.acquire()
        data = data.sample(n=100)
        self.lock.release()
        age = list(data['age'])
        cost = list(data['charges'])
        self.lock.acquire()
        data = sorted(zip(age, cost)) # Unsure if we should change this to using one of the algorithms, may make it easier to track time complexity?
        ages, costs = zip(*data)
        ax.plot(ages, costs)
        ax.set_title("Age vs Medical Insurance Cost")
        ax.set_xlabel("Age")
        ax.set_ylabel("Medical Insurance Cost")
        self.lock.release()

    def bmiLineGraph(self, data, ax):
        self.lock.acquire()
        data = data.sample(n=100)
        self.lock.release()
        bmi = list(data['bmi'])
        cost = list(data['charges'])
        self.lock.acquire()
        data = sorted(zip(bmi, cost)) # Unsure if we should change this to using one of the algorithms, may make it easier to track time complexity?
        bmis, costs = zip(*data)
        ax.plot(bmis, costs)
        ax.set_title("BMI vs Medical Insurance Cost")
        ax.set_xlabel("BMI")
        ax.set_ylabel("Medical Insurance Cost")
        self.lock.release()

    def numOfChildrenLineGraph(self, data, ax):
        self.lock.acquire()
        data = data.sample(n=100)
        self.lock.release()
        numOfChildren = list(data['children'])
        cost = list(data['charges'])
        self.lock.acquire()
        data = sorted(zip(numOfChildren, cost)) # Unsure if we should change this to using one of the algorithms, may make it easier to track time complexity?
        numOfChildren, costs = zip(*data)
        ax.plot(numOfChildren, costs)
        ax.set_title("Number of Children vs Medical Insurance Cost")
        ax.set_xlabel("Number of Children")
        ax.set_ylabel("Medical Insurance Cost")
        self.lock.release()

    def drawAllLineGraphs(self, data, axAge_L, axBMI_L, axNumOfChildren_L):
        # The line graphs compare how medical insurance cost increases based on a specific attribute (how insurance cost is affected with age, bmi, and number of children)
        self.ageLineGraph(data, axAge_L)
        self.bmiLineGraph(data, axBMI_L)
        self.numOfChildrenLineGraph(data, axNumOfChildren_L)

    def agePieGraph(self, data, ax):
        age = data['age']
        bounds = [0, 25, 25.01, 35, 35.01, 45, 45.01, 55, 55.01, 65]
        countBar1 = age.between(bounds[0], bounds[1]).sum()
        countBar2 = age.between(bounds[2], bounds[3]).sum()
        countBar3 = age.between(bounds[4], bounds[5]).sum()
        countBar4 = age.between(bounds[6], bounds[7]).sum()
        countBar5 = age.between(bounds[8], bounds[9]).sum()
        labels = ["<25", ">25-35", ">35-45", ">45-55", ">55-65"]
        ageCounts = [countBar1, countBar2, countBar3, countBar4, countBar5]
        self.lock.acquire()
        ax.pie(ageCounts, labels=labels, autopct=lambda val: f'{val*sum(ageCounts)/100:.0f} ({val:.2f}%)', startangle=90, labeldistance=1.2, pctdistance=1) # Reference: google search AI overview, how to get values in pie chart with percentages
        ax.set_title("Age Demographics")
        self.lock.release()

    def maleVsFemalePieGraph(self, data, ax):
        people = data['sex']
        counts = people.value_counts()
        self.lock.acquire()
        ax.pie(counts.values, labels=counts.index, autopct=lambda val: f'{val * sum(counts.values) / 100:.0f} ({val:.2f}%)', startangle=90, labeldistance=1.2, pctdistance=1)  # Reference: google search AI overview, how to get values in pie chart with percentages
        ax.set_title("Male vs Female")
        self.lock.release()

    def bmiPieGraph(self, data, ax):
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
        self.lock.acquire()
        ax.pie(bmiCounts, labels=labels, autopct=lambda val: f'{val * sum(bmiCounts) / 100:.0f} ({val:.2f}%)', startangle=90, labeldistance=1.2, pctdistance=1)  # Reference: google search AI overview, how to get values in pie chart with percentages
        ax.set_title("BMI Demographics")
        self.lock.release()

    def smokersPieGraph(self, data, ax):
        smoker = data['smoker']
        counts = smoker.value_counts()
        self.lock.acquire()
        ax.pie(counts.values, labels=counts.index, autopct=lambda val: f'{val * sum(counts.values) / 100:.0f} ({val:.2f}%)', startangle=90, labeldistance=1.2, pctdistance=1)  # Reference: google search AI overview, how to get values in pie chart with percentages
        ax.set_title("Smoker vs Non-smoker Demographics")
        self.lock.release()

    def regionPieGraph(self, data, ax):
        regions = data['region']
        counts = regions.value_counts()
        self.lock.acquire()
        ax.pie(counts.values, labels=counts.index, autopct=lambda val: f'{val * sum(counts.values) / 100:.0f} ({val:.2f}%)', startangle=90, labeldistance=1.2, pctdistance=1)  # Reference: google search AI overview, how to get values in pie chart with percentages
        ax.set_title("Region Demographics")
        self.lock.release()

    def numOfChildrenPieGraph(self, data, ax):
        children = data['children']
        counts = children.value_counts()
        self.lock.acquire()
        ax.pie(counts.values, labels=counts.index, autopct=lambda val: f'{val * sum(counts.values) / 100:.0f} ({val:.2f}%)', startangle=90, labeldistance=1.2, pctdistance=1)  # Reference: google search AI overview, how to get values in pie chart with percentages
        ax.set_title("Number of Children Demographics")
        self.lock.release()

    def medInsurPieGraph(self, data, ax):
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
        self.lock.acquire()
        ax.pie(medCounts, labels=labels, autopct=lambda val: f'{val * sum(medCounts) / 100:.0f} ({val:.2f}%)', startangle=135, labeldistance=1.2, pctdistance=.8)  # Reference: google search AI overview, how to get values in pie chart with percentages
        ax.set_title("Medical Insurance Cost Demographics")
        self.lock.release()

    def drawAllPieGraphs(self, data, axAge_P, axMF_P, axBMI_P, axSmoker_P, axRegion_P, axNumOfChildren_P, axMed_P):
        self.agePieGraph(data, axAge_P)
        self.maleVsFemalePieGraph(data, axMF_P)
        self.bmiPieGraph(data, axBMI_P)
        self.smokersPieGraph(data, axSmoker_P)
        self.regionPieGraph(data, axRegion_P)
        self.numOfChildrenPieGraph(data, axNumOfChildren_P)
        self.medInsurPieGraph(data, axMed_P)