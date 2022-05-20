class Controller:
    def __init__(self, Color, AmountOfButtons, JoyOrRemote):
        self.Color = Color
        self.AmountOfButtons = AmountOfButtons
        self.JoyOrRemote = JoyOrRemote

ControllerNbrOne = Controller('Black', '12', 'Remote')
ControllerNbrTwo = Controller('White', '8', 'Joy')
