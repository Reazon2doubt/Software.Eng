# ======================
# Scenario: Define the classes of Objects
# ======================

class painting():

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.frame = False
        self.base_value = 10000

    def __str__(self):
        return str(self.title) + ", " + str(self.artist) + " ," + str(self.frame)

class sculpture():

    def __init__(self, name, era):
        self.name = name
        self.era = era
        self.base_value = 25000

    def __str__(self):
        return str(self.name) + ", " + str(self.era)

class digitalExhibit():

    def __init__(self, title, technology):
        self.title = title
        self.technology = technology
        self.base_value = 5000

    def __str__(self):
        return str(self.title )+ ", " + str(self.technology)


class romanCollection():

    def __init__(self, collection_name, item_count):
        self.collection_name = collection_name
        self.item_count = item_count
        self.base_value = 40000

    def __str__(self):
        return str(self.collection_name) + ", " + str(self.item_count)

# ======================
# Main Method
# ======================

def main():
    paintingObject = painting("The Starry Night", "Vincent van Gogh")
    print(paintingObject)

    digitalObjet = digitalExhibit("Ancient Rome Virtual Tour", "Virtual Reality")
    print(digitalObjet)

    sculptureObject = sculpture("Rosetta Stone", "Ptolemaic Period (196 BC)")
    print(sculptureObject)

    romanObject = romanCollection("Roman Britain Collection", 145)
    print(romanObject)

if __name__ == "__main__":
    main()