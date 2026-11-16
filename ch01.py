# name = "Amnat"
# visit = 20
# mounths = 10

# def is_at_risk(visit , mounths):
#     return visit < 10 and mounths > 6 

# print(f"ชื่อ : {name} \n จำนวนครั้งที่ใช้งาน : {visit} \n อายุสมาชิก : {mounths} \n โอกาสไม่ต่ออายุ : {is_at_risk(visit,mounths)}")

class Member:
    def __init__(self,name,visit,mounths,monthly_fee):
        self.name = name
        self.visit = visit
        self.mounths = mounths
        self.monthly_fee = monthly_fee

    def is_at_risk(self):
        return self.visit < 10 and self.mounths > 6

    def total_paid(self):
        return self.monthly_fee * self.mounths


if __name__ == "__main__":
    m1 = Member("Amnat",4,10,300)
    m2 = Member("August",6,10,200)
    m3 = Member("Plaai",10,10,100)

    data = [m1,m2,m3]

    for i in data:
        print(f"\nชื่อ : {i.name} \n จำนวนครั้งที่ใช้งาน : {i.visit} \n อายุสมาชิก : {i.mounths} \n โอกาสไม่ต่ออายุ : {i.is_at_risk()} \n ยอดชำระทั้งหมด : {i.total_paid()}")
