firstSeg = float(input('First Segment: '))
secondSeg = float(input('Second Segment: '))
thirdSeg = float(input('Third Segment: '))
if(firstSeg < (secondSeg+ thirdSeg) and secondSeg < (firstSeg + thirdSeg) and thirdSeg < (firstSeg + secondSeg)):
    if(firstSeg == secondSeg == thirdSeg):
        print('Forms an equilateral triangle')
    elif(firstSeg == secondSeg and firstSeg != thirdSeg or firstSeg == thirdSeg and firstSeg != secondSeg or secondSeg == thirdSeg and secondSeg != firstSeg):
        print('Forms a isosceles triangle')
    elif(firstSeg != secondSeg != thirdSeg):
        print('Forms scalene triangle')
    else:
        print('[Error]')
else:
    print('Cannot form a triangle')