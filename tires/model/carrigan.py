from tires.tires import Tires


class Carrigan(Tires):

    def needs_service(self):
        for tire in self.tires:
            if tire >= 0.9:
                return True
        return False
