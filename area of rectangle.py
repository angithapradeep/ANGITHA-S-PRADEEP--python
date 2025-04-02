

 #Write a Python GUI program that takes user input for the length and width of a rectangle and calculates the area when a button is pressed.
from breezypythongui import EasyFrame

class RectangleAreaCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Rectangle Area Calculator")

        # Input fields for length and breadth
        self.addLabel(text="Enter Length:", row=0, column=0)
        self.lengthField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Enter Breadth:", row=1, column=0)
        self.breadthField = self.addFloatField(value=0.0, row=1, column=1)

        # Button to calculate area
        self.calcButton = self.addButton(text="Calculate Area", row=2, column=0, columnspan=2, command=self.calculateArea)

        # Label to display the result
        self.resultLabel = self.addLabel(text="Area: ", row=3, column=0, columnspan=2)

    def calculateArea(self):
        # Get input values
        length = self.lengthField.getNumber()
        breadth = self.breadthField.getNumber()

        # Compute area
        area = length * breadth

        # Display result
        self.resultLabel["text"] = f"Area: {area} square units"

if __name__ == "__main__":
    RectangleAreaCalculator().mainloop()
