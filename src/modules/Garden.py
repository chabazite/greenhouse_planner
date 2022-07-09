from datetime import datetime

def add_plant_update(number):
    """
    this function will add the plant to a garden, update the remaining sqft and update the total plant cost. 
    """
    for _ in range(number):
        self.plants.append(plant)
    self.remaining_sqft -= plant.sqft * number
    self.plant_cost += plant.cost * number

class Garden:

    def __init__(self, name, length, width, type, 
     sunlight, soil='soil'):
        """
        Class for visualizing and storing the user's garden data

        Args:
            name (string): nickname for the garden
            length (int): length of the garden
            width (int): width of the garden
            total_sqft (int): square feet of garden (length * width)
            type (string): raised beds, greenhouse, etc.
            planted_sqft(int): total sqft of beds planted
            sunlight (int): hours of full sunlight the garden recieves
            beds (int): how many individual beds are there. 
            plants (list): list of current plant objects in garden
            plant_cost (int): total cost of garden to buy plants
            soil (string, optional): is it soil or hydroponics. Defaults to 'soil'.

        """
        self.name = name
        self.length = length
        self.width = width
        self.max_sqft = length * width
        self.type = type
        self.plantable_sqft = 0
        self.sunlight = sunlight
        self.beds = 0
        self.remaining_sqft = 0
        self.plant_cost = 0
        self.soil = soil
        self.plants = []
        self.notes = []

    def add_bed(self, n, length, width):
        """
        method to add more beds to your garden. These all need to be the same length and width.

        Args:
            n (int): number of beds to add to your garden
            length (int): length of individual bed
            width (int): width of individual bed
        """
        sqft_beds = n * length * width
        if self.max_sqft < (self.plantable_sqft + sqft_beds):
            return 'Your garden is full'
        else:
            self.beds += n
            self.plantable_sqft += sqft_beds
            self.remaining_sqft += sqft_beds

    def add_plant(self, plant, number):
        """
        add a number of a defined plant class to the garden

        Args:
            plant (_type_): type of plant to add to the garden
            number (int): number of plants to add to the garden
        """
        if (plant.sunlight <= self.sunlight) and (plant.sqft*number <= self.remaining_sqft):
            add_plant_update(number)
        # If the plant needs more sunlight than the garden can offer
        elif plant.sunlight > self.sunlight:
            answer = input("This plant needs more sunlight than your garden has, do you still wish to plant (y/n): ")
            if answer == 'y':
                add_plant_update(number)
            else:
                return 'o well, lets try a different garden'
        # If the plants need more space than the garden can offer
        elif plant.sqft*number > self.remaining_sqft:
            plant_possible = int(self.remaining_sqft/plant.sqft)
            answer = input(f"This garden doesn't have enough room to plant this many {plant.name}, would you like to plant {plant_possible}? (y/n): ")
            if answer == 'y':
                add_plant_update(plant_possible)
            else:
                return 'o well, lets try a different garden'

    def check_garden(self):
        """
        a method that tells what you garden currently looks like
        """
        print('These are the plants in your garden:')
        for plant in self.plants:
            print(plant.name,':',plant.variety)
        print('You currently have {} sqft. remaining of {} worth of beds'.format(self.remaining_sqft,self.plantable_sqft))
        print('You will have to spend ${} to plant the garden'.format(self.plant_cost))

    def add_notes(self, note):
        """
        method to add to the note string for this plant 
        Args:
            note (string): note to add about the plant
        """
        today = datetime.now()
        datetime_string = today.strftime("%d/%m/%Y %H:%M:%S")
        note = datetime_string +"--> "+ note
        self.notes.append(note)

