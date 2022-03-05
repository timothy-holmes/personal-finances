# user stories

stories = [
    {'story': 'As a member of the family, I want to see the historical spending.',
    'plan': 'Moving average (n=30, days in month) for spending, broken down by tags/categories/reason/account',
    'priority': '1-MVP'},
    {'story': 'As a member of the family, I want to see current balances.',
    'plan': '-List of well-defined expenses to be covered\n-List of averages for undefined expenses',
    'priority': '1-MVP'},
    {'story': 'As a member of the family, I want to see the expected cash flow for next 30 days.',
    'plan': 'Identify:\n-regular income,\n-average other income,\nUse expenses module already created',
    'priority': '2-MLP'},
    {'story': 'As a member of the family, I want to know how much money we will have in 90 days in our long-term savings account.',
    'plan': 'As above',
    'priority': '3-NTH'},
    {'story': 'As advisor to the Chief Financial Officer, I want to be able to present information in a simple, understandable way to facilitate harmony in the household',
    'plan': 'Create dashboard/report',
    'priority': '1-MVP'}
]

class InformationRequest():
    # pass data to analysis engine
    def __init__(self,config):
        self.config = config
        # open information file
        current, date, self.information = self.load_information(config['INFORMATION_PATH'])
        if not current:
            self.information = self.update_information(date)




if __name__ == '__main__':
    print('\n\n'.join(['\n'.join([v for v in story.values()]) for story in stories]))