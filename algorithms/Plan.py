class Plan:
    """
    Creates a different plan based on the given parameters.

    Methods
    -------
    """

    def __init__(self, duration: str, is_daily: bool,
                 train_days: str = None):
        """"""
        self.duration = duration
        self.is_daily = is_daily
        # If the sessions are daily, then train_days doesn't need to be set.
        self.train_days = train_days.split(
            ",") if not self.is_daily else train_days

        match self.duration:
            case "6W":
                self.rapid_fire
            case "3M":
                self.steady_waters
            case "6M":
                self.deep_dive
            case _:
                self.plan_error

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

    def plan_error(self):
        """
        Error handling method
        """
        print("Something went wrong.")


p = Plan("6W", True)
# p = Plan("6W", False, "Mon,Wed,Fri")
# p.rapid_fire()

print(p.duration)
print(p.is_daily)
print(p.train_days)
