
class CuentaBancaria:

    cuentas=[]

    def __init__(self, tasa_interés, balance=0): 

        self.tasa_interés=tasa_interés
        self.balance=balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance +=amount
        return self

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -=5
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: $ {self.balance}")
        return self

    def generar_interés(self):
        if self.balance >0:
            interés_generado =self.balance * self.tasa_interés
            self.balance+= interés_generado
        return self

    @classmethod
    def mostrar_cuentas(cls):
        for cuentas in cls.cuentas:
            print(f"Tasa de interés: {cuentas.tasa_interés}, Balance: {cuentas.balance}")


cuenta1=CuentaBancaria(0.01, 1500)
cuenta2=CuentaBancaria(0.01, 1000)

cuenta1.deposito(100).deposito(200).deposito(400).retiro(1000).generar_interés().mostrar_info_cuenta()
cuenta2.deposito(500).deposito(1000).retiro(100).retiro(500).retiro(300).retiro(200).generar_interés().mostrar_info_cuenta()

CuentaBancaria.mostrar_cuentas()

