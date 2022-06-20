import re

regex = r"[0-9]{16}|(([0-9]{4}\S){3}[0-9]{4})|(-([0-9]{4}\S){3}[0-9]{4})(.)\1{4}"

tarjetasPrueba = ['4123456789123456',
            '5123-4567-8912-3456',
            '61234-567-8912-3456',
            '4123356789123456',
            '5133-3367-8912-3456',
            '5123 - 3567 - 8912 - 3456']


def testTarjetas(tarjetasPrueba):
    for test in tarjetasPrueba:
        if re.match(regex, test):
            print("Valid \t\t{}". format(test))
        else:
            print("Invalid   \t{}". format(test))
            
testTarjetas(tarjetasPrueba)