class BuildPlan:
    """"""

    def __init__(self):
        """"""
        pass

    def test(self):
        """
        Tests that my class is working.
        """
        print("This is working.")

    def name(self):
        """
        1. Receives the data.
            - plan_duration
            - training_frequency
            - training_days
        2. Functions that create the different plans.
        These functions will handle, what date the 
        plans start on, and what exercises are given.
            - There are 9 different schedules.
            - Based on the number of schedules, I will
            most likely create a plan class, and each 
            method of it builds a different schedule.
        """


bp = BuildPlan()
bp.test()
