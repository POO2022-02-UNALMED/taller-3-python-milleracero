class TV:
    numTV=0

    def __init__(self,marca,estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._precio=500
        self._volumen=1
        TV.numTV+=1 
        self._control=None
    
    def getMarca(self):
        return self._marca
    
    def setMarca(self,marca):
        self._marca=marca
    
    def getControl(self):
        return self._control 
    
    def setControl(self,control):
        self._control=control

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self,volumen):
        if volumen>=0 and volumen<=7 and self._estado==True:
            self._volumen=volumen

    def getCanal(self):
        return self._canal

    def setCanal(self,canal):
        if canal>=1 and canal<=120 and self._estado==True:
            self._canal=canal
    
    def volumenDown(self):
        if self._volumen>0 and self._estado==True:
            self._volumen-=1
    
    def volumenUp(self):
        if self._volumen<7 and self._estado==True:
            self._volumen+=1
    
    def canalUp(self):
        if self._canal<120 and self._estado==True:
            self._canal+=1

    def canalDown(self):
        if self._canal>0 and self._estado==True:
            self._canal-=1
    
    def turnOn(self):
        self._estado=True
    
    def turnOff(self):
        self._estado=False

    def getEstado(self):
        return self._estado
    
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self,precio):
        self._precio=precio
    
    def setNumTV(num):
        TV.numTV = num
    
    def getNumTV():
        return TV.numTV