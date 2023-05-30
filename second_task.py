casino_blacklist = ['John Dow', 'Aleks Smith', 'Penelopa Cruz']
poker_blacklist = ['John Dow', 'Daniel Welbeck', 'Jogan Girera']
alcohol_blacklist = ['John Dow', 'Jenifer Black', 'Axel Sniffer']
new_list = set(casino_blacklist).intersection(poker_blacklist).intersection(alcohol_blacklist)
