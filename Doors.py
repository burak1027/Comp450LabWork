import random


class RandomRiskTaker:
    def __init__(self, numberOfChanges, successesInChanging, succeesesInKeeping, firstDecision,
                 successesInFirstDecision, turns):
        self.numberOfChanges = numberOfChanges
        self.successesInChanging = successesInChanging
        self.successesInKeeping = succeesesInKeeping
        self.firstDecision = firstDecision
        self.successesInFirstDecision = successesInFirstDecision
        self.turns = turns

    def failures(self):
        return eval(self.turns - (self.succesesInChanging + self.succesesInChanging))


class RiskTaker:
    def __init__(self, successes, firstDecision, successesInFirstDecision, turns):
        self.successes = successes
        self.firstDecision = firstDecision
        self.successesInFirstDecision = successesInFirstDecision
        self.turns = turns

    def failures(self):
        return eval(self.turns - self.succeses)


class NoRiskTaker:
    def __init__(self, successes, turns, firstDecision):
        self.successes = successes
        self.turns = turns
        self.firstDecision = firstDecision

    def failures(self):
        return eval(self.turns - self.successes)



class Doors:
    list = []
    prize = 0

    def __init__(self):
        self.list = [False, False, False]
        self.prize = random.randint(0, 2)
        self.list[self.prize] = True

def eliminate(list, pick, prize):
    rnd = random.randint(0, 2)
    list2 = []
    list2.append(rnd)
    list2.append((rnd + 1) % 3)
    list2.append((rnd + 2) % 3)
    for i in list2:
        if i!=prize and i!= pick:
            return i


risk_taker = RiskTaker(0, 0, 0, 0)
non_risk_taker = NoRiskTaker(0, 0, 0)
random_risk_taker = RandomRiskTaker(0, 0, 0, 0, 0, 0)



for i in range(0, 10000):

    doors1 = Doors()  # non-risk-taker
    doors2 = Doors()  # risk-taker
    doors3 = Doors()  # random-risk-taker

    risk_taker.firstDecision = random.randint(0, 2)
    random_risk_taker.firstDecision = random.randint(0, 2)
    non_risk_taker.firstDecision = random.randint(0, 2)

    eliminated_door = eliminate(doors2.list, risk_taker.firstDecision, doors2.prize)
    eliminated_door2 = eliminate(doors3.list, random_risk_taker.firstDecision, doors3.prize)

    # value for random risk taking
    random_number = random.randint(0, 1)

    if non_risk_taker.firstDecision == doors1.prize:
        non_risk_taker.successes = non_risk_taker.successes + 1
    if risk_taker.firstDecision == doors2.prize:
        risk_taker.successesInFirstDecision = risk_taker.successesInFirstDecision + 1
    if random_risk_taker.firstDecision == doors3.prize:
        random_risk_taker.successesInFirstDecision = random_risk_taker.successesInFirstDecision + 1
        if random_number != 1:
            random_risk_taker.successesInKeeping = random_risk_taker.successesInKeeping + 1

    # secondpick

    numList = [0, 1, 2]
    numList.remove(eliminated_door)
    numList.remove(risk_taker.firstDecision)
    picked = numList[0]

    if picked == doors2.prize:
        risk_taker.successes = risk_taker.successes + 1

    if random_number == 1:
        numList = [0, 1, 2]
        numList.remove(eliminated_door2)
        numList.remove(random_risk_taker.firstDecision)
        picked = numList[0]
        if picked == doors3.prize:
            random_risk_taker.successesInChanging = random_risk_taker.successesInChanging + 1

    random_risk_taker.turns = random_risk_taker.turns + 1
    risk_taker.turns = risk_taker.turns + 1
    non_risk_taker.turns = non_risk_taker.turns + 1

print()
print("No Risk Raker:")
print("\t","Total turns:",non_risk_taker.turns)
print("\t","Successes: ",non_risk_taker.successes)
print("------------------------------------------")
print("Risk-Taker")
print("\t","Total turns:",risk_taker.turns)
print("\t","Succeses",risk_taker.successes)
print("\t","Succeses In First decision",risk_taker.successesInFirstDecision)
print("------------------------------------------")
print("Random Risk Taker")
print("\t","Total turns:",random_risk_taker.turns)
print("\t","Successes if changed",random_risk_taker.successesInChanging)
print("\t","Successes if kept",random_risk_taker.successesInKeeping)
print("\t","Succeses In First decision",random_risk_taker.successesInFirstDecision)



