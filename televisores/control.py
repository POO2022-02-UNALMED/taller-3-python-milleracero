class Control:
    def __init__(self,TV):
        self._TV=TV

    def getTv(self):
        return self._TV
    
    def setTv(self,tv):
        self._TV=tv
    
    def turnOn(self):
        self._TV.turnOn()
        
    def turnOff(self):
        self._TV.turnOff()
    
    def canalUp(self):
        self._TV.canalUp()
    
    def canalDown(self):
        self._TV.canalDown()

    def volumenUp(self):
        self._TV.volumenUp()

    def volumenDown(self):
        self._TV.volumenDown()

    def setCanal(self,canal):
        self._TV.setCanal(canal)

    def enlazar(self,TV):
        self._TV=TV
        self._TV.setControl(self)