# user stories
stories = [
    {'story': 'As a member of the family, I want to see the historical spending.',
    'plan': 'Moving average (n=30, days in month)',
    'priority': 'MVP'},
    {'story': 'As a member of the family, I want to see expenses coming up',
    'plan': 'List of well-defined expenses to be covered, list of averages for undefined expenses',
    'priority': 'MVP'},
    {'story': 'As a member of the family, I want to see the expected cash flow for next 30 days',
    'plan': 'Identify regular income, average other income, use expenses module',
    'priority': 'MVP'}
]

if __name__ == '__main__':
    print('\n\n'.join(['\n'.join([v for v in story.values()]) for story in stories]))