"""
Redisctricting Project
Anish Reddy
"""
import DistrictArrays as DA




'''___Classes___'''

class Squareville:

    map =  [[0 for i in range(10)] for j in range(10)]

    # census realted data
    census = 0
    RDI = [0,0,0]
    KLMN = [0,0,0,0]


    def __init__(this, pop, affil, coi, district, loc):
        this.pop = pop
        this.affil = affil
        this.coi = coi
        this.district = district
        this.loc = loc

        # Commands to run
        Squareville.map[this.loc[0]][this.loc[1]] = this
        this.updateCensusInfo()
        District.listOfDistricts[district].add(this)

    # Updates census realted data
    def updateCensusInfo(this):
        Squareville.census += this.pop
        if this.affil == "R":
            Squareville.RDI[0]+=this.pop
        elif this.affil == "D":
            Squareville.RDI[1]+=this.pop
        elif this.affil == "I":
            Squareville.RDI[2]+=this.pop
        if this.coi == "K":
            Squareville.KLMN[0]+=this.pop
        elif this.coi == "L":
            Squareville.KLMN[1]+=this.pop
        elif this.coi == "M":
            Squareville.KLMN[2]+=this.pop
        elif this.coi == "N":
            Squareville.KLMN[3]+=this.pop

    
    def __repr__(this):
        return f"{this.affil}{this.coi}{this.pop}-{this.district}"
    
    def __str__(this) -> str:
        return f"{this.affil}{this.coi}{this.pop}-{this.district}"
    


class District:
    
    listOfDistricts = [None]

    def __init__(this):
        District.listOfDistricts.append(this)

        this.withinDistrict = []
        this.pop = 0
        this.RDI = [0,0,0]
        this.KLMN = [0,0,0,0]

        this.minR = None
        this.maxR = None
        this.minC = None
        this.maxC = None

    # Adds a Squarevill cell to the district
    def add(this, cell):
        this.withinDistrict.append(cell)
        this.updateCensusInfo(cell)
        this.updateMixMax(cell)

    # Updates census realted data
    def updateCensusInfo(this, cell):
        this.pop += cell.pop
        if cell.affil == "R":
            this.RDI[0]+=cell.pop
        elif cell.affil == "D":
            this.RDI[1]+=cell.pop
        elif cell.affil == "I":
            this.RDI[2]+=cell.pop
        if cell.coi == "K":
            this.KLMN[0]+=cell.pop
        elif cell.coi == "L":
            this.KLMN[1]+=cell.pop
        elif cell.coi == "M":
            this.KLMN[2]+=cell.pop
        elif cell.coi == "N":
            this.KLMN[3]+=cell.pop

    # Update min and max R and C
    def updateMixMax(this, cell):
        r = cell.loc[0]
        c = cell.loc[1]
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

    def getReockScore(this):
        area = len(this.withinDistrict)
        if (this.maxR-this.minR) > (this.maxC-this.minC):
            minSquareSide = this.maxR-this.minR+1
        else:
            minSquareSide = this.maxC-this.minC+1
        return area/(minSquareSide*minSquareSide)

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
        d = DA.district[row][col]
        e = (row, col)
        Squareville(a,b,c,d,e)


# prints Squareville.map in Terminal
print("\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9")
for i in Squareville.map:
    print(Squareville.map.index(i), end="\t")
    for j in i:
        print(j, end="\t")
    print()
print()


# prints the info for each district
print("The District\tPopulation\tR/D/I\t\t\tK/L/M/N\t\t\tReock Score")
for i in range(1,8):
    print(f"District {i}", end="\t")
    x = District.listOfDistricts[i]
    print(f"{x.pop}\t\t{x.RDI}\t\t{x.KLMN}\t\t{x.getReockScore()}")
    print()

# print(Squareville.census)
# print(District.listOfDistricts[1])


    
        
