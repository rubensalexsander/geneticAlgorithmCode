class Mouse:
    def __init__(self, areaDeclique=[2, 2]):
        self.areaDeclique = areaDeclique

    def getArea(self, posicaoMouse):
        ponto1 = [int((posicaoMouse[0] - (self.areaDeclique[0] / 2))), int((posicaoMouse[1] - (self.areaDeclique[1] / 2))),
                  self.areaDeclique[0], self.areaDeclique[1]]
        return [ponto1, [ponto1[0] + self.areaDeclique[0], ponto1[1] + self.areaDeclique[1]]]
