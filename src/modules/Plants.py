
class Plants:

    def __init__(self, name, variety, difficulty, cost, season,harvest_time, sunlight, soil, plant_date, sqft):
        """
        a class for creating and detailing each plant variety that will be used in the garden 
        Args:
            name (string): plant general name
            variety (string): specific plant variety
            difficulty (string): how hard is it to grow
            cost (float): cost of the plant
            season (string): what season does this grow in
            harvest_time (string): what month is best for harvesting
            sunlight (int): how many hours of sunlight does it need
            soil (string): what type of soil
            plant_date (string): when do you need to plant a seedling
            sqft (int): how many square feet does it need for planting
            notes (list): a running notepad for the plant
        """
        self.name = name
        self.variety = variety
        self.difficulty = difficulty
        self.cost = cost
        self.season  = season
        self.harvest_time = harvest_time
        self.sunlight = sunlight
        self.soil = soil
        self.plant_date = plant_date
        self.sqft = sqft

