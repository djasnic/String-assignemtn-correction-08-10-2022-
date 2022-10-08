# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# First part
scorer_0 = "Gullit"
scorer_1 = "Van Basten"
goal_0 = "32"
goal_1 = "54"
scorers = (scorer_0+" "+goal_0)+", "+(scorer_1+" "+goal_1)
print(scorers)
report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"
print(report)
#
# Second part
player="Marco Van Basten"
x = player.find(" ")
first_name = player[:x]
last_name_len = len(player[x+1:])
name_short = player[x+1:]
chant = (first_name+"! ")*len(first_name)
chant[0:(len(chant)-1)]
good_chant = chant != " "
print(chant)
print(good_chant)