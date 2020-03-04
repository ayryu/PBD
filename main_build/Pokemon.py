class Pokemon:

    def __init__(self, url, usage_percent, monthly_rank, type1, type2, stats):

        self.url = url
        self.usage_percent = usage_percent
        self.monthly_rank = monthly_rank
        self.type1 = type1
        self.type2 = None
        self.stats = stats
        self.moves = []
        self.teammates = []
        self.items = []
        self.abilities = []
        self.nature = []
        self.ev = []

