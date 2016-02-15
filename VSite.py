from Site import Site

class VSite (Site):

    def __init__(self, point, center):
        Site.__init__(self, point)
        self.center = center


    def __str__(self):
        if len(self.sites) == 3:
            return str(self.sites[0]) + ", " + str(self.sites[1]) + ", " + str(self.sites[2])
        else:
            return "vSite ??"

