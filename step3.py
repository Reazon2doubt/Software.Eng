# ======================
# Step 3:
# Implementation of a interface.
# We need this so we know what methods each visitor should have
# Highlight double dispatch
# Highlight polymorphism
# Highlight SE advantages
# ======================

class visitor(): #abstract visior class
    def visitPainting(self,painting):
        pass

    def visitSculpture(self,sculpture):
        pass

    def visitDigitalExhibit(self,digitalExhibit):
        pass

    def visitRomanCollection(self,romanCollection):
        pass

class insuranceVisitor(visitor): #visior class

    def visitSculpture(self, sculpture):
        return sculpture.base_value * 1.1

    def visitPainting(self, painting):
        return painting.base_value * 1.5

    def visitDigitalExhibit(self, digitalExhibit):
        return digitalExhibit.base_value + 5000

    def visitRomanCollection(self, romanCollection):
        return romanCollection.base_value * 1

class accessibilityVisitor(visitor): #visior class

    def visitSculpture(self, sculpture):
        accessibilityScore = 80
        return accessibilityScore

    def visitPainting(self, painting):
        accessibilityScore = 65
        return accessibilityScore

    def visitDigitalExhibit(self, digitalExhibit):
        accessibilityScore = 20
        return accessibilityScore

    def visitRomanCollection(self, romanCollection):
        accessibilityScore = 90
        return accessibilityScore
    
class painting():

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.frame = False
        self.base_value = 10000

    def __str__(self):
        return str(self.title) + ", " + str(self.artist) + " ," + str(self.frame)

    def accept(self,visitor):
        return visitor.visitPainting(self)

class sculpture():

    def __init__(self, name, era):
        self.name = name
        self.era = era
        self.base_value = 25000

    def __str__(self):
        return str(self.name) + ", " + str(self.era)

    def accept(self,visitor):
        return visitor.visitSculpture(self)

class digitalExhibit():

    def __init__(self, title, technology):
        self.title = title
        self.technology = technology
        self.base_value = 5000

    def __str__(self):
        return str(self.title )+ ", " + str(self.technology)

    def accept(self,visitor):
        return visitor.visitDigitalExhibit(self)

class romanCollection():

    def __init__(self, collection_name, item_count):
        self.collection_name = collection_name
        self.item_count = item_count
        self.base_value = 40000

    def __str__(self):
        return str(self.collection_name) + ", " + str(self.item_count)

    def accept(self,visitor):
        return visitor.visitRomanCollection(self)

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

    insuranceAdvisor = insuranceVisitor()

    paintingValue = paintingObject.accept(insuranceAdvisor)
    digitalValue = digitalObjet.accept(insuranceAdvisor)
    sculptureValue = (sculptureObject.accept(insuranceAdvisor))
    RomanValue =romanObject.accept(insuranceAdvisor)

    print(paintingValue, digitalValue, sculptureValue, RomanValue)

    accessibilityAdvisor = accessibilityVisitor()

    paintingAccessibility = paintingObject.accept(accessibilityAdvisor)
    digitalAccessibility = paintingObject.accept(accessibilityAdvisor)
    sculptureAccessibility = paintingObject.accept(accessibilityAdvisor)
    romanAccessibility = paintingObject.accept(accessibilityAdvisor)

    print(paintingAccessibility, digitalAccessibility, sculptureAccessibility, romanAccessibility)

if __name__ == "__main__":
    main()