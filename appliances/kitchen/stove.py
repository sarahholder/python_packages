from appliances import Appliance
class Stove(Appliance):

    def __init__(self, color, heat_method="electric"):
        super().__init__(color)

    def make_cookies(self):
        print("Fresh baked chocolate chip cookies can fix anything")
