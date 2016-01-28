from Site import Site

class VSite (Site):

    def __init__(self, point, center):
        Site.__init__(self, point)
        self.center = center
