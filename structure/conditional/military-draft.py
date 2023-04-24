import datetime
yearBirth = int(input('Year of birth: '))
date = datetime.date.today()
currentYear = int(date.strftime("%Y"))
age = currentYear - yearBirth
enlistmentYear = yearBirth + 18
print('Anyone born in {} is {} years old in {}'.format(yearBirth, age, currentYear))
if(age > 18):
    print('''You should have enlisted {} years ago
Your enlistment was in {}
    '''.format((currentYear - enlistmentYear), enlistmentYear))
elif(age == 18):
    print('Your enlistment is this year {}'.format(currentYear))
else:
    print('''There are {} years left for enlistment
Your enlistment will be in {}
    '''.format(enlistmentYear - currentYear, enlistmentYear))
