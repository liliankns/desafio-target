def inverter_string(string):
    string_invertida = ''
    for s in string:
        string_invertida = s + string_invertida
    return string_invertida

string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
