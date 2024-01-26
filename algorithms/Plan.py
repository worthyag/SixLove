class Plan:
    """
    Creates a different plan based on the given parameters.

    Methods
    -------
    1
    2
    3
    4
    5
    6
    7
    8
    9
    """

    def __init__(self, duration: str, is_daily: bool,
                 train_days: str = None):
        self.duration = duration
        self.is_daily = is_daily

        if not self.is_daily:
            self.train_days = train_days.split()

    def rapid_fire(self):
        """
        6 Weeks
        """

    def steady_waters(self):
        """
        3 Months
        """
        pass

    def deep_dive(self):
        """
        6 Months
        """
        pass


p = Plan("6W", True)
# p.rapid_fire()

print(p.duration)
print(p.is_daily)
print(p.train_days)
