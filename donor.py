import csv 
thelist = []
class donor:
    def __init__(self, name, phone, mail, group, amount):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.group = group
        self.amount = amount
class blooddb(donor):
    def __init__(self, name, phone, mail, group, amount):
        donor.__init__(self, name, phone, mail, group, amount)
    def search_donor(self, phone):
        flag = 0
        for lines in thelist:
            alpha, beta, ceta, deta, eta, feta = lines
            if beta == phone:
                print("Record Found:\n")
                print(lines)
                flag = 1
                return "Found"
        if flag != 1:
            print("Record not found.")
            return "Not Found"
    def read_data(self, thelist):
        file = open('Blooddata.csv', mode = 'r')
        csvFile = csv.reader(file)
        for lines in csvFile:
            thelist.append(lines)
    def write_data(self, thelist):
        file1 = open('Blooddata.txt', 'w')
        for lines in thelist:
            alpha, beta, ceta, deta, eta, feta = lines
            file1.write("Name:")
            file1.write(alpha)
            file1.write("\n")
            file1.write("Phone Num:")
            file1.write(beta)
            file1.write("\n")
            file1.write("Mail ID:")
            file1.write(ceta)
            file1.write("\n")
            file1.write("Blood Group:")
            file1.write(deta)
            file1.write("\n")
            file1.write("Amount:")
            file1.write(eta)
            file1.write("\n")
            file1.write("\n")
            file1.write("\n")
            print("Name:")
            print(alpha)
            print("\n")
            print("Phone Num:")
            print(beta)
            print("\n")
            print("Mail ID:")
            print(ceta)
            print("\n")
            print("Blood Group:")
            print(eta)
            print("\n")
            print("Amount:")
            print(deta)
            print("\n")
            print("\n")
            print("\n")
