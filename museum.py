from abc import ABC, abstractmethod


# ======================
# Visitor Interface
# ======================

class MuseumVisitor(ABC):

    @abstractmethod
    def visit_painting(self, painting):
        pass

    @abstractmethod
    def visit_historical_artifact(self, artifact):
        pass

    @abstractmethod
    def visit_digital_exhibit(self, exhibit):
        pass

    @abstractmethod
    def visit_roman_collection(self, collection):
        pass


# ======================
# Museum Objects
# ======================

class MuseumObject(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Painting(MuseumObject):

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.frame = False

    def accept(self, visitor):
        return visitor.visit_painting(self)


class HistoricalArtifact(MuseumObject):

    def __init__(self, name, era):
        self.name = name
        self.era = era

    def accept(self, visitor):
        return visitor.visit_historical_artifact(self)


class DigitalExhibit(MuseumObject):

    def __init__(self, title, technology):
        self.title = title
        self.technology = technology

    def accept(self, visitor):
        return visitor.visit_digital_exhibit(self)


class RomanCollection(MuseumObject):

    def __init__(self, collection_name, item_count):
        self.collection_name = collection_name
        self.item_count = item_count

    def accept(self, visitor):
        return visitor.visit_roman_collection(self)


# ======================
# Concrete Visitor
# ======================

class InsuranceValuationVisitor(MuseumVisitor):

    def visit_painting(self, painting):
        return 1000000

    def visit_historical_artifact(self, artifact):
        return 500000

    def visit_digital_exhibit(self, exhibit):
        return 100000

    def visit_roman_collection(self, collection):
        return collection.item_count * 2000

class Viewingtimeallocation(MuseumVisitor):

    def visit_painting(self, painting):
        return "20 seconds"

    def visit_historical_artifact(self, artifact):
        return "90 seconds"

    def visit_digital_exhibit(self, exhibit):
        return "120 seconds"

    def visit_roman_collection(self, collection):
        return "150 seconds"

# ======================
# MAIN
# ======================

exhibits = [
    Painting("Starry Night", "Van Gogh"),
    HistoricalArtifact("Sutton Hoo Helmet", "Anglo-Saxon"),
    DigitalExhibit("Journey Through Space", "VR"),
    RomanCollection("Roman Britain", 350),
    Painting("Test Painting", "Stuart Nicholson")
]

insurance_valuer = InsuranceValuationVisitor()
museum_customer = Viewingtimeallocation()


for exhibit in exhibits:
    value = exhibit.accept(insurance_valuer)
    print("Insurance value =", value)

for exhibit in exhibits:
    viewtime = exhibit.accept(museum_customer)
    print("Viewing time =", viewtime)