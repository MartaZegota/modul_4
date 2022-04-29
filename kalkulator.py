import logging
logging.basicConfig(level=logging.DEBUG, format='%(name)s %(levelname)s %(asctime)s %(message)s', filename="logkalku.log")

def kalkulator(x,y):
    x = int(x)
    y = int(y)
    result = ""
    result = result + ""
    result = result + ""
    if choice == '1':
      return x+y
    elif choice == '2':
      return x-y
    elif choice == '3':
      return x*y
    elif choice == '4':
      return x/y
    else:
      print("Niepoprawna wartośc")


if __name__ == "__main__":
    choice = input("Podaj nr działania: \n1 dla dodawanie lub \n2 dla odejmowanie lub \n3 dla mnozenie lub \n4 dla dzielenie\n")
    liczba_pierw = input("Podaj pierwsza liczbę: ")
    logging.info("First parameter is %s" % liczba_pierw)
    liczba_drug = input("Podaj druga liczba: ")
    logging.info("Second parameter is %s" % liczba_drug)
    print(f"Wprowadzone liczby to: {liczba_pierw} i {liczba_drug}")
    logging.info(f"Wprowadzone liczby to: {liczba_pierw} i {liczba_drug}")
    r_result = kalkulator(liczba_pierw, liczba_drug)
    print("Wynik to:", r_result)