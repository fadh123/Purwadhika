def main():
    Nomor_HP= input('Masukan Nomor HP: ')
    validNumber(Nomor_HP)
    translateNumber(Nomor_HP)

def validNumber(Nomor_HP):
    for i,c in enumerate(Nomor_HP):
        if i in [3,7]:
            if c != '-':
                Nomor_HP=input('Please enter a valid phone number: ')
            return False
        elif not c.isalnum():
            Nomor_HP=input('Please enter a valid phone number: ')
        return False
    return True

def translateNumber(Nomor_HP):
    s=""
    for char in Nomor_HP:
        if char is '1':
            x1='1'
            s= s + x1
       elif char is '-':
            x2='-'
            s= s + x2
       elif char in 'ABCabc':
           x3='2'
           s= s + x3