"""
Redisctricting Project
Anish Reddy
"""
import DistrictArrays as DA
import WeightedVotingSystemsCalculator as WVS




'''___Classes___'''

class Squareville:

    map =  [[0 for i in range(10)] for j in range(10)]

    # census realted data
    population = 0
    RDI = [0,0,0]
    KLMN = [0,0,0,0]

    def __init__(this, cPop, cAffil, cCOI, cDistrict, cLoc):
        this.cPop = cPop
        this.cAffil = cAffil
        this.cCOI = cCOI
        this.cDistrict = cDistrict
        this.cLoc = cLoc

        # Commands to run
        Squareville.map[this.cLoc[0]][this.cLoc[1]] = this
        this.updateSquarevilleInfo()
        District.listOfDistricts[cDistrict].add(this)

    # Updates census realted data
    def updateSquarevilleInfo(this):
        Squareville.population += this.cPop
        match this.cAffil:
            case "R":
                Squareville.RDI[0]+=this.cPop
            case "D":
                Squareville.RDI[1]+=this.cPop
            case "I":
                Squareville.RDI[2]+=this.cPop
        match this.cCOI:
            case "K":
                Squareville.KLMN[0]+=this.cPop
            case "L":
                Squareville.KLMN[1]+=this.cPop
            case "M":
                Squareville.KLMN[2]+=this.cPop
            case "N":
                Squareville.KLMN[3]+=this.cPop

    def getOverallPartyPercent():
        return [round(val/Squareville.population*100,2) for val in Squareville.RDI]
    
    def getOverallCOIPercent():
        return [round(val/Squareville.population*100,2) for val in Squareville.KLMN]

    def getOverallPartyBPI():
        return WVS.getBPI(Squareville.RDI)
    
    def getOverallCOIBPI():
        return WVS.getBPI(Squareville.KLMN)


    def __repr__(this):
        return f"{this.cAffil}{this.cCOI}{this.cPop}-{this.cDistrict}"
    
    def __str__(this) -> str:
        return f"{this.cAffil}{this.cCOI}{this.cPop}-{this.cDistrict}"
    


class District:
    
    listOfDistricts = [None]

    # Assuming each district has 1 vote based on plurality (bc representative)
    RDI = None
    KLMN = None

    def __init__(this):
        District.listOfDistricts.append(this)

        this.withinDistrict = []
        this.dPop = 0
        this.dRDI = [0,0,0]
        this.dKLMN = [0,0,0,0]
        this.dAffil = None
        this.dCOI = None

        this.minR = None
        this.maxR = None
        this.minC = None
        this.maxC = None

    # Adds a Squarevill cell to the district
    def add(this, cell):
        this.withinDistrict.append(cell)
        this.updateDistrictInfo(cell)
        District.updateRepresentation()

    # Updates district realted data
    def updateDistrictInfo(this, cell):
        this.dPop += cell.cPop
        match cell.cAffil:
            case "R":
                this.dRDI[0]+=cell.cPop
            case "D":
                this.dRDI[1]+=cell.cPop
            case "I":
                this.dRDI[2]+=cell.cPop
        match cell.cCOI:
            case "K":
                this.dKLMN[0]+=cell.cPop
            case "L":
                this.dKLMN[1]+=cell.cPop
            case "M":
                this.dKLMN[2]+=cell.cPop
            case "N":
                this.dKLMN[3]+=cell.cPop
        
        # Sets affiliation of the district
        if this.dRDI[0] > this.dRDI[1] and this.dRDI[0] > this.dRDI[2]:
            this.dAffil = "R"
        elif this.dRDI[1] > this.dRDI[0] and this.dRDI[1] > this.dRDI[2]:
            this.dAffil = "D"
        elif this.dRDI[2] > this.dRDI[0] and this.dRDI[2] > this.dRDI[1]:
           this.dAffil = "I"

        # Sets COI of the district
        if this.dKLMN[0] > this.dKLMN[1] and this.dKLMN[0] > this.dKLMN[2] and this.dKLMN[0] > this.dKLMN[3]:
            this.dCOI = "K"
        elif this.dKLMN[1] > this.dKLMN[0] and this.dKLMN[1] > this.dKLMN[2] and this.dKLMN[1] > this.dKLMN[3]:
            this.dCOI = "L"
        elif this.dKLMN[2] > this.dKLMN[0] and this.dKLMN[2] > this.dKLMN[1] and this.dKLMN[2] > this.dKLMN[3]:
            this.dCOI = "M"
        elif this.dKLMN[3] > this.dKLMN[0] and this.dKLMN[3] > this.dKLMN[1] and this.dKLMN[3] > this.dKLMN[2]:
            this.dCOI = "N"

        # Update min and max R and C
        r = cell.cLoc[0]
        c = cell.cLoc[1]
        if this.minR == None:
            this.minR = r
            this.maxR = r
            this.minC = c
            this.maxC = c
        else:
            if r < this.minR:
                this.minR = r
            elif r > this.maxR:
                this.maxR = r
            if c < this.minC:
                this.minC = c
            elif c > this.maxC:
                this.maxC = c
        
    # Updates the Overall Representation
    def updateRepresentation():
        District.RDI = [0,0,0]
        District.KLMN = [0,0,0,0]
        for i in range(1,8):
            j = District.listOfDistricts[i]
            match j.dAffil:
                case "R":
                    District.RDI[0]+=1
                case "D":
                    District.RDI[1]+=1
                case "I":
                    District.RDI[2]+=1
            match j.dCOI:
                case "K":
                    District.KLMN[0]+=1
                case "L":
                    District.KLMN[1]+=1
                case "M":
                    District.KLMN[2]+=1
                case "N":
                    District.KLMN[3]+=1

    
    # Each District Check
    def checkDPop(this):
        if this.dPop>41 or this.dPop<34:
            return False
        else:
            return True

    def getReockScore(this):
        area = len(this.withinDistrict)
        if (this.maxR-this.minR) > (this.maxC-this.minC):
            minSquareSide = this.maxR-this.minR+1
        else:
            minSquareSide = this.maxC-this.minC+1
        return area/(minSquareSide*minSquareSide)
    
    # Overall Check
    def averageReockScore():
        sum=0
        for i in range(1,8):
            sum += District.listOfDistricts[i].getReockScore()
        return sum/7
    
    def getPartyPercent():
        return [round(val/7*100,2) for val in District.RDI]

    def getCOIPercent():
        return [round(val/7*100,2) for val in District.KLMN]

    def getPartyBPI():
        return WVS.getBPI(District.RDI)

    def getCOIBPI():
        return WVS.getBPI(District.KLMN)
                

    def __repr__(this):
        return this.withinDistrict

    def __str__(this):
        return f"{this.withinDistrict}"




'''___Running Stuff___'''

# Creating all the District Objects
for i in range(7):
    District()


# Creating all the Squareville objects
for row in range(10):
   for col in range(10):
        a = DA.population[row][col]
        b = DA.affiliation[row][col]
        c = DA.demographic[row][col]
        d = DA.districtAssignments[row][col]
        e = (row, col)
        Squareville(a,b,c,d,e)


# prints Squareville.map in Terminal
print("\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9")
for i in Squareville.map:
    print(Squareville.map.index(i), end="\t")
    for j in i:
        print(j, end="\t")
    print()
print("\n")


# prints the info for each district
print("The District\tPopulation\tR/D/I\t\t\tK/L/M/N\t\t\tReock Score\tAffiliation\tCOI")
print("------------------------------------------------------------------------------------------------------------------------")
for i in range(1,8):
    print(f"District {i}", end="\t")
    x = District.listOfDistricts[i]
    print(f"{x.dPop},{x.checkDPop()}\t\t{x.dRDI}\t\t{x.dKLMN}\t\t{round(x.getReockScore(),4)}\t\t{x.dAffil}\t\t{x.dCOI}")
    print()
print()


print(f"Average Reock Score of Compactness: {round(District.averageReockScore(),4)}\n")
print(f"Party Power Comparison:")
print(f"Overall:\t%R/D/I={Squareville.getOverallPartyPercent()}\tR/D/I-BPI={Squareville.getOverallPartyBPI()}")
print(f"Overall:\t%R/D/I={District.getPartyPercent()}\tR/D/I-BPI={District.getPartyBPI()}\n")
print(f"COI Power Comparison:")
print(f"Overall:\t%K/L/M/N={Squareville.getOverallCOIPercent()}\tK/L/M/N-BPI={Squareville.getOverallCOIBPI()}")
print(f"Overall:\t%K/L/M/N={District.getCOIPercent()}\tK/L/M/N-BPI={District.getCOIBPI()}\n")


    
        
