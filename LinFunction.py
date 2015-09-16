__author__ = 'benjamin_sanchez'

def main():
    aCount = 2 #int(input())
    for x in range(aCount):
        bLine =  [0, 0, 1, 1]  #[int(x) for x in input().split()]
        xShift = abs(bLine[2] - bLine[0])
        yShift = abs(bline[1] - bline[3])
        xVal = yShift / xShift



main()