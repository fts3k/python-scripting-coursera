# Video Example 1L

for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")  # end param to ensure string writes a distinct character.
    print()    



## Vid Example 2: Output all possible team pairing:
## Avoid teams playing against themselves - use if conditions

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


# Be careful on how & where to use nested loops:


