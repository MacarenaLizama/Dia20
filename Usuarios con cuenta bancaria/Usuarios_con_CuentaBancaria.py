class Usuario:
    def __init__(self, nombre,apellido,email):
        self.nombre= nombre
        self.apellido=apellido
        self.email=email
        self.cuenta = CuentaBancaria(tasa_interés=0.02,balance=0)

    def hacer_deposito(self,amount):
        self.cuenta.deposito (amount)

    def hacer_retiro (self,amount):
        self.cuenta.retiro (amount)
    
    def mostrar_balance_usuario(self):
        print()
        print(f"Sr(a) {self.nombre} {self.apellido}, el balance de su cuenta es:$ {self.cuenta.balance}")
        print()

    def transfer_dinero(self, other_user, cantidad):
        self.cantidad=cantidad
        self.other_user=other_user
        self.cuenta.balance -= cantidad
        other_user.cuenta.balance += cantidad
        print()
        print(f"Se realizó una transferencia por ${self.cantidad}")
        print()
        print("Saldo actual de Sr(a)", self.nombre +" " + self.apellido , "es: $", self.cuenta.balance)
        print("Saldo actual de Sr(a)", other_user.nombre + " " + other_user.apellido, "es: $", other_user.cuenta.balance)
        print()

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



#instancias


persona1= Usuario("Juan", "Gutierrez", "jgutierrez@mundo.com")
persona2= Usuario("Claudia", "Ramirez", "cramirez@mundo.com")
persona3=Usuario ("Carlos", "Sanchez", "csanchez@mundo.com")

#depositos
persona1.hacer_deposito(1500)
persona1.hacer_deposito(1000)
persona1.hacer_deposito(2150)
persona2.hacer_deposito(500)
persona2.hacer_deposito(1143)
persona3.hacer_deposito(5487)

#retiros
persona1.hacer_retiro(980)
persona2.hacer_retiro(100)
persona2.hacer_retiro(381)
persona3.hacer_retiro(150)
persona3.hacer_retiro(500)
persona3.hacer_retiro(333)

#Balance
persona1.mostrar_balance_usuario()
persona2.mostrar_balance_usuario()
persona3.mostrar_balance_usuario()

print("____________________________________________________________")
#transferencia

persona1.transfer_dinero(persona3, 300)

cuenta1=CuentaBancaria(0.01, 1500)
cuenta2=CuentaBancaria(0.01, 1000)

cuenta1.deposito(100).deposito(200).deposito(400).retiro(1000).generar_interés().mostrar_info_cuenta()
cuenta2.deposito(500).deposito(1000).retiro(100).retiro(500).retiro(300).retiro(200).generar_interés().mostrar_info_cuenta()

CuentaBancaria.mostrar_cuentas()

