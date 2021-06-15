class Config:

    MIN_HEALTH = 0
    MAX_HEALTH = 100

    MIN_EXPERIENCE = 0
    MAX_EXPERIENCE = 50

    MIN_RECHARGE = 100  #ms
    MAX_RECHARGE = 2000  #ms
    MIN_RECHARGE_VEHICLE = 1000  #ms

    MAX_OPERATORS = 3
    MIN_OPERATORS = 1

    STRATEGIES = ['random', 'weakest', 'strongest']

    MIN_ARMIES = 2
    MIN_SQUADS = 2
    MAX_SQUADS = 7
    
    MIN_UNITS = 5
    MAX_UNITS = 10

    DAMAGE_BOOSTER = 1000

    DMG_TO_VEHICLE = 0.6  # 60%
    DMG_TO_ONE_OPER = 0.2  # 20%
    DMG_TO_OPER = 0.1  # 10%
