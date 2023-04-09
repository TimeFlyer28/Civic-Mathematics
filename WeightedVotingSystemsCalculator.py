'''Anish Reddy - Weighted Voting Systems Calculator'''

import itertools


class player:

    totalVotes = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        player.totalVotes+=self.weight

    def BPIIndex(self):
        if hasattr(self, 'timesCritical'):
            return self.timesCritical/player.totalCritical
        else:
            return None

    def BPIIndexDetails(self):
        if hasattr(self, 'timesCritical'):
            return f'{self.timesCritical}/{player.totalCritical}', round(self.timesCritical/player.totalCritical,5)
        else:
            return 'n/a', 0
    
    def SSPIIndexDetails(self):
        if hasattr(self, 'timesPivotal'):
            return f'{self.timesPivotal}/{player.totalPivotal}', round(self.timesPivotal/player.totalPivotal,5)
        else:
            return 'n/a', 0

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return f'{self.name};   Weight: {self.weight};   PercentVote: {round(self.weight*100/player.totalVotes,2)}%;   BPI: {self.BPIIndexDetails()};   SSPI: {self.SSPIIndexDetails()};'



def findAllCoalitions(playerList):
    allCoalitions = []
    for i in range(len(playerList) + 1):
        for subset in itertools.combinations(playerList, i):
            votes = 0
            for voter in subset:
                votes += voter.weight
            allCoalitions.append([list(subset),votes])
    return allCoalitions



# i = index of each list within wC --> [coalition, total votes]
# j = index of each player object within i
def BanzhafPowerIndex(playerList, quota):
    
    player.totalCritical = 0
    for voter in playerList:
        voter.timesCritical = 0
    
    wCoalitions = []
    for i in range(len(playerList) + 1):
        for subset in itertools.combinations(playerList, i):
            votes = 0
            for voter in subset:
                votes += voter.weight
            if votes>=quota:
                wCoalitions.append([list(subset),votes])
    
    bpiList = wCoalitions.copy()
    for i in range(len(bpiList)):
        for j in range(len(bpiList[i][0])):
            if bpiList[i][1] - bpiList[i][0][j].weight < quota:
                
                # Updates objects first
                bpiList[i][0][j].timesCritical +=1
                player.totalCritical+=1

                # Replaces object with string indicating criticality
                bpiList[i][0][j] = bpiList[i][0][j].name + "*"

    return wCoalitions, bpiList



def ShapleyShubikPowerIndex(playerList, quota):
    
    player.totalPivotal = 0
    for voter in playerList:
        voter.timesPivotal = 0
    
    coalitionPermutations = []
    for subset in itertools.permutations(playerList):
        coalitionPermutations.append(list(subset))
    
    sspiList = coalitionPermutations.copy()
    for permutationIndex in range(len(sspiList)):
        votes = 0
        index = 0
        while votes<quota and index<len(playerList):
            votes+=sspiList[permutationIndex][index].weight
            index+=1
        index-=1
        
        sspiList[permutationIndex][index].timesPivotal+=1
        player.totalPivotal+=1
        
        sspiList[permutationIndex][index] = sspiList[permutationIndex][index].name+'*'
    
    return coalitionPermutations, sspiList
    


def printList(list):
    for i in list:
        print(i)
    print(f'Total: {len(list)}')






def getBPI(weightsList):
    names = ["a","b","c","d","e","f"]
    player.totalVotes = 0
    pList = []
    bpiList = []
    for i in range(len(weightsList)):
        pList.append(player(names[i],weightsList[i]))
    BanzhafPowerIndex(pList,int(player.totalVotes/2)+1)
    for i in pList:
        bpiList.append(round(i.BPIIndex(),4))
    return bpiList







def runProgram():
    '''Voting System (Edit these)'''

    quota = 133

    playerList = [
        player("R", 91),
        player("D", 118),
        player("I", 55),
        # player("D", 15),
        # player("E", 7),
        # player("F", 6),
    ]



    '''Running Stuff'''

    # Returns all winning coalitions (as objects --> usable)
    allCoalitions = findAllCoalitions(playerList)


    # Returns winning coalitions with and without critical players starred respectively (2 outputs)
    # Adds BPI to objects
    allWinningCoalitions, BPIMarkedList = BanzhafPowerIndex(playerList, quota)


    # Returns all permutations with and without pivotal players starred respectively (2 outputs)
    # Adds SSPI to objects
    allPermutations, SSPIMarkedList = ShapleyShubikPowerIndex(playerList, quota)


    #Prints one of the lists above
    print('---------------------------------------\nBPI List:\n---------------------------------------')
    printList(BPIMarkedList)
    print('\n---------------------------------------\nSSPI List:\n---------------------------------------')
    printList(SSPIMarkedList)
    print('\n---------------------------------------\nPlayer Details:\n---------------------------------------')
    printList(playerList)
    print('\n------------------------------------------------------------------------------\n\n')


# Enable this during use
# runProgram()