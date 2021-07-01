from morso import morseCode
morso=[]
def stringtoMorso(string):
    string=string.upper()
    for ch in string:
          if ch==" ":
            morso.append(".......")
            morso.append(" ")
          else:
            morso.append(morseCode[ch])
            morso.append(" ")
    output=""
    
    print(output.join(morso))
string=input("Enter the text you want to convert to morso: ")

