from anki import get_cards
from bitbucket import get_prs
from toggl import get_hours

print('Hours: ' + str(get_hours()))
print('Cards: ' + str(get_cards()))
print('PRs: ' + str(get_prs()))
