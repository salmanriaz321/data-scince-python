import pandas as pd
scores = [21,23,22,54]
data = {
    'Player' : ['Neymar jr', 'Ronaldo', 'Messi'],
    'scores' : ['11', '7', '10'],
    'win' : [9, 8, 8]
}
fd = pd.DataFrame (data)
print(fd)
print(fd.loc[2])
full = pd.read_csv('leaderboard.csv')
print(full.info())