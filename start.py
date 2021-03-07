from anki import get_cards
from bitbucket import get_prs
from toggl import get_hours

hours = get_hours()

print('Learning: ' + str(hours[0]))
print('Job: ' + str(hours[1]))
print('Hustling: ' + str(hours[2]))
print('Self Dev: ' + str(hours[3]))
print('Cards: ' + str(get_cards()))
print('PRs: ' + str(get_prs()))
