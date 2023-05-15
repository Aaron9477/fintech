

class Fund:
    def __int__(self, fundId, fundName, fundIdZyyx, fundNameZyyx, fundIdSmpp, strategy, administrator, region,
                manager, establishTime, reportDataSource = '朝阳永续', reportNetWorthType = '复权净值'):
        self.fundId = fundId
        self.fundName = fundName
        self.fundIdZyyx = fundIdZyyx
        self.fundNameZyyx = fundNameZyyx
        self.fundIdSmpp = fundIdSmpp
        self.strategy = strategy
        self.administrator = administrator
        self.region = region
        self.manager = manager
        self.establishTime = establishTime
        self.reportDataSource = reportDataSource
        self.reportNetWorthType = reportNetWorthType




