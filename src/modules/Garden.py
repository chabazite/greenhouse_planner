class Garden:

    def __init__(self, name, length, width, sqft, type, 
     sunlight, beds, plant_cost, soil='soil'):
        """
        Class for visualizing and storing the user's garden data

        Args:
            name (string): nickname for the garden
            length (int): length of the garden
            width (int): width of the garden
            sqft (int): square feet of actual planting area
            type (string): raised beds, greenhouse, etc.
            sunlight (int): hours of full sunlight the garden recieves
            beds (int): how many individual beds are there. 
            plants (list): list of current plant objects in garden
            plant_cost (int): total cost of garden to buy plants
            soil (string, optional): is it soil or hydroponics. Defaults to 'soil'.

        """
        self.name = name
        self.length = length
        self.width = width
        self.sqft = sqft
        self.type = type
        self.sunlight = sunlight
        self.beds = beds
        self.plant_cost = plant_cost
        self.soil = soil
        self.plants = []

    def Addbed(self, n, length, width):
        """
        method to add more beds to your garden. These all need to be the same length and width.

        Args:
            n (int): number of beds to add to your garden
            length (int): length of individual bed
            width (int): width of individual bed
        """
        self.beds += n

        sqft_beds = n * length * width

        self.sqft += sqft_beds

    def Addplant(self, plant, number):
        """
        add a number of a defined plant class to the garden

        Args:
            plant (_type_): type of plant to add to the garden
            number (int): number of plants to add to the garden
        """
        if plant.sunlight <= self.sunlight:
            for _ in range(number):
                self.plants.append(plant)
            self.sqft -= plant.sqft * number
            self.plant_cost += plant.cost * number
        else:
            answer = input("This plant needs more sunlight than your garden has, do you still wish to plant (y/n): ")
            if answer == 'y':
                for _ in range(number):
                    self.plants.append(plant)
                self.sqft -= plant.sqft * number
                self.plant_cost += plant.cost * number
            else:
                'o well, lets try a different garden'

    def checkGarden(self):
        """
        a method that tells what you garden currently looks like
        """
        print('These are the plants in your garden:')
        for plant in self.plants:
            print(plant.name,':',plant.variety)
        print('You currently have {} sqft. remaining'.format(self.sqft))
        print('You will have to spend {} to plant the garden'.format(self.plant_cost))