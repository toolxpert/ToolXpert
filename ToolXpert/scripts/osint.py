import webbrowser

def osint_x():
    while True:
        print("""
   ____   _____ _____ _   _ _______    __   __
  / __ \ / ____|_   _| \ | |__   __|   \ \ / /
 | |  | | (___   | | |  \| |  | |  ____ \ V / 
 | |  | |\___ \  | | | . `|  | |  ____  > <  
 | |__| |____) |_| |_| |\  |  | |       / . \ 
  \____/|_____/|_____|_| \_|  |_|      /_/ \_\

1. Name Search
2. Phone Search
3. E-Mail Search
4. License Plate Search
5. VIN Search
6. Exit
        """)
        choice = input("OSINT-X~> ").strip()

        if choice == "1":
            name_search()
        elif choice == "2":
            phone_search()
        elif choice == "3":
            email_search()
        elif choice == "4":
            license_plate_search()
        elif choice == "5":
            vin_search()
        elif choice == "6":
            print("Exiting OSINT-X. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def name_search():
    name = input("Enter Name (ex: michael-scott): ").strip()
    state = input("Enter State Initials (ex: ny): ").strip()
    city = input("Enter City (ex: scranton): ").strip()

    urls = [
        f"https://www.fastpeoplesearch.com/name/{name}_{city}-{state}",
        f"https://www.searchpeoplefree.com/find/{name}/{state}/{city}",
        f"https://www.peoplesearchnow.com/person/{name}_{city}_{state}",
        f"https://www.truepeoplesearch.com/results?name={name}&citystatezip={city}%20{state}",
        f"https://www.spokeo.com/{name}?loaded=1"
    ]

    open_urls(urls)

def phone_search():
    phone = input("Enter Phone Number (ex: 123-456-7890): ").strip()

    urls = [
        f"https://www.fastpeoplesearch.com/{phone}",
        f"https://www.searchpeoplefree.com/phone-lookup/{phone}",
        f"https://www.peoplesearchnow.com/phone/{phone}",
        f"https://www.whitepages.com/phone/1-{phone}",
        f"https://www.thatsthem.com/phone/{phone}"
    ]

    open_urls(urls)

def email_search():
    email = input("Enter Email: ").strip()

    urls = [
        f"https://www.skymem.info/srch?q={email}&ss=home",
        f"https://www.melissa.com/v2/lookups/emailcheck/email/?email={email}&site="
    ]

    open_urls(urls)

def license_plate_search():
    plate = input("Enter License Plate: ").strip()
    state = input("Enter State Initials (ex: ny): ").strip()

    urls = [
        f"https://www.faxvin.com/license-plate-lookup/result?plate={plate}&state={state}",
        f"https://www.findbyplate.com/US/{state}/{plate}/"
    ]

    open_urls(urls)

def vin_search():
    vin = input("Enter VIN: ").strip()

    urls = [
        f"https://www.vehiclehistory.com/vin-report/{vin}",
        f"https://www.vindecoderz.com/EN/check-lookup/{vin}"
    ]

    open_urls(urls)

def open_urls(urls):
    for url in urls:
        webbrowser.open(url)

if __name__ == "__main__":
    osint_x()
