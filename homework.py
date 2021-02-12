import pandas as pd


def pathfinder_scores(scores):
    try:
        score_dict= {7:-4, 8:-2, 9:-1, 10:0, 11:1, 12:2, 13:3, 14:5, 15:7, 16:10, 17:13, 18:17}
        return sum([score_dict[i] for i in scores]) <=25
    except:
        return False
    

def homework():
    dataset = pd.read_csv('football.csv')
    '''age = dataset['Age'].mean()
    n = dataset.describe(include=['object']).Nationality.top
    rich = dataset.Wage.max()
    low = dataset.Wage.min()
    total = dataset.Wage.sum()'''
    '''speedH =round(dataset[dataset.Wage > dataset.Wage.mean()].SprintSpeed.mean())
    age = dataset[(dataset.Composure > dataset.Composure.max()*0.9)&
                  (dataset.Reactions > dataset.Reactions.max()*0.9)
                 ].Age.min()
    n = dataset[dataset.Wage > dataset.Wage.mean()].Nationality.describe().top'''
    #player = round(dataset[dataset.Nationality == 'Spain']['Wage'].value_counts(normalize='True', bins=4).iloc[0]*100)
    #position = dataset.groupby(['Position'])['Wage'].sum()
    #position = position[position>2000000]
    #clubs_wages = dataset[dataset.Club == "Chelsea"].groupby(['Club'])['Wage'].sum()

    club_mean= dataset.groupby(['Club']).Wage.mean()
    club_median = dataset.groupby(['Club']).Wage.median()
    c = club_mean[club_mean==club_median]
    #player = dataset.groupby(['Club']).Wage.median()
    #c = len(club_mean[player==club_mean])
    #n = dataset[dataset.Club == 'Manchester United'].Nationality.nunique()
    print(c)

homework()

def pd_read_csv2():
    data = pd.read_csv('football.csv')
    gr = data.groupby(['Club'])['Wage'].sum()
    print(gr)

def pd_read_csv1():
    data = pd.read_csv('football.csv')
    s = data['Wage'].value_counts(bins=4)
    d = data.loc[(data.Wage>s.index[3].left)&(data.Wage<=s.index[3].right)]
    print(d)


def pd_read_csv():
    data = pd.read_csv('football.csv')
    s = data['Nationality'].value_counts(normalize=True)
    print(s.head(15))


def pd_read_csv_and_somfntgdo():
    data = pd.read_csv('football.csv')
    Barsa = data[data.Club == 'FC Barcelona'].Age
    MU = data[data.Club == 'Manchester United'].Age
    new_df = pd.DataFrame([Barsa.mean(), MU.mean()], columns= ["Age"],
                            index= ['FC Barcelona', 'Manchester United'])
    print(new_df)





def datafra():
    #df = pd.DataFrame({'col': [1,2,3,4], 'col2' : [5,6,7,8]})
    df = pd.DataFrame([ [1,2], [5,6] ],
                    columns=["foo", "bar"],
                    index=['in1', 'in2']

                    )
    print(df)


def panda():
    data = pd.Series(["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
                      index = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"])
    print(data.loc[["Среда", "Суббота"]])


def while1():
    time = 0
    current_health = 500
    attack = 80
    while current_health > 0:
        current_health -= attack
        time +=1
    print(time)
    return 'Done'

def while2():
    tank = 1000
    robot_add = 5
    count = 0
    while tank > 0:
        tank -= robot_add
        robot_add += 5
        count += 1
    print(count)
    return 'Done'

def for1():
    for i in range(1, 11):
        print('{0} {1} {2}'.format(i, i**2, i**3))
    return 'Done'

def print_all_visokos(start, stop):
    for year in range(start, stop):
        if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
            print(year)
    return 'Done'

def smile(str):
    for letter in str:
        if letter in '.,:-!?':
            str = str.replace(letter, ':)')
    return str

def glas(word):
    for letter in word:
        if letter.lower() in 'ауоыиэяюёе':
            print(letter)

def dop1():
    stavk = 10
    depos = 170000
    year = 0
    while depos <= 1000000:
        depos += depos * (stavk/100)
        year += 1
    print(year)
#mylist = [x//10 + x%10 for x in range(90, 100)]
#print_all_visokos(1000, 1040)
