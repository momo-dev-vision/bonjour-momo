from datetime import date

def main():
    aujourdhui = date.today()
    print(f"Bonjour Momo, voici la date d'aujourd'hui : {aujourdhui.strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    main()
