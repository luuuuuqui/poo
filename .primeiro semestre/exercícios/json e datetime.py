from datetime import datetime

dt = datetime.strptime(input("asadasdjasuidubasod: "), "%d-%m-%Y")
print(f"{dt: "%d/%m/%Y"}")