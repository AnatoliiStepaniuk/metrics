from anki import get_cards
from bitbucket import get_prs
from toggl import get_hours

hours = get_hours()
print('Coding: ' + str(hours[0]))
print('Hustling: ' + str(hours[1]))
print('Cards: ' + str(get_cards()))
print('PRs: ' + str(get_prs()))
