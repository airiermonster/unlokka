def calculate_code(imei):
    digits = str(imei)[8:14]  # Extract digits from the 9th to the 14th
    code = ''
    for i in range(0, len(digits), 2):
        num1 = int(digits[i])
        num2 = int(digits[i+1])
        code += str((num1 + num2) % 10)  # Perform the sum and take the last digit

    return code


def print_banner():
    print("""
                    \033[45m\033[3mSmartKitochi Network\033[0m
                           
\033[1;32m██╗   ██╗███╗   ██╗██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
\033[1;32m██║   ██║████╗  ██║██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
\033[1;32m██║   ██║██╔██╗ ██║██║     ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
\033[1;33m██║   ██║██║╚██╗██║██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
\033[1;33m╚██████╔╝██║ ╚████║███████╗╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
\033[1;33m ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        
\033[1;33m Tigo,Vodacom,Zantel Smart Vitochi Unlock codes Generator..!\033[0m
\033[41m# Coded by airiermonster\033[1;0m | \033[42mgithub/airiermonster\033[0m
""")

print_banner()


def get_user_choice():
    choice = input("Do you want to continue? (Y/N): ")
    return choice.lower() == 'y'


print_banner()

while True:
    imei = input("Weka IMEI za SIM1 (Zipo Namba 15): ")
    if len(imei) != 15:
        print("IMEI inapaswa kuwa na Namba 15. Tafadhali jaribu tena.")
        continue

    code = calculate_code(imei)
    final_code = "4374{}8".format(code)
    print("Code yako kwenye IMEI", imei, "Uliyoweka NI:", final_code)
    print("Weka line ya Mtandao Mwingine kwenye slot iliyo kuwa network locked ambayo ni SIM1 kisha itakuomba uweke PIN weka:", final_code)

    if not get_user_choice():
        print("Ahsante Kwa kutumia Hii Software Karibu Tena. Kwaheri!")
        break
