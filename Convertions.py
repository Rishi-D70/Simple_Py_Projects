
print("Welcome User!, This is a convertions program ")
#classes and def for conversions are below
class Distance():
    def kmtoyards(self, valuetoconvert):
        convertion =  valuetoconvert * 1093.6
        print(f"{valuetoconvert}km --> {convertion} yd")

    def kmtomiles(self, valuetoconvert):
        convertion = valuetoconvert * 0.621371
        print(f"{valuetoconvert}km --> {round(convertion, 2)} miles")

    def milestokm(self, valuetoconvert):
        convertion = valuetoconvert * 1.609344
        print(f"{valuetoconvert}miles --> {round(convertion, 2)} km")

class Temprature():
    def celsiustokelvin(self, valuetoconvert):
        convertion = valuetoconvert + 273.15
        print(f"{valuetoconvert}°Celsius --> {round(convertion, 2)}Kelvin")

    def kelvintof(self, valuetoconvert):
        convertion = (valuetoconvert - 273.15) * 9/5 + 32
        print(f"{valuetoconvert}kelvin --> {round(convertion, 2)}°F")

    def celsiustof(self, valuetoconvert):
        convertion = (valuetoconvert * 9/5) + 32
        print(f"{valuetoconvert}°Celsius --> {round(convertion, 2)}°F")

class Weight():
    def kgtopund(self, valuetoconvert):
        convertion = valuetoconvert * 2.20462262
        print(f"{valuetoconvert}Kg --> {round(convertion, 2)}lb")

    def kgtoounces(self, valuetoconvert):
        convertion = valuetoconvert * 35.2739619
        print(f"{valuetoconvert}Kg --> {round(convertion, 2)}oz")

    def poundtoounces(self, valuetoconvert):
        convertion = valuetoconvert * 16
        print(f"{valuetoconvert}lb --> {round(convertion, 2)}oz")

cd = Distance()
ct = Temprature()
cw = Weight()


while True:
     try :
          converstion_class = int(input("Enter your choice of conversion \n1.Distance \n2.Temperature \n3.Weight \n"))
          if converstion_class not in range(1, 4):
               converstion_class = int(input("Invalid! Please select from available options : "))
          else : break
     except :
            print("Oops! Invalid input: ")



match (converstion_class):
    case 1:
       conver_type = int(input("In Distance: 1.km - yards, 2.km - miles 3.miles - km : "))

       if conver_type not in range(1, 4):
            conver_type = int(input("Invalid! Please select from available options : "))
       else: pass

       match (conver_type):
             case 1: #km - yards
                 try:

                     valuetoconvert = int(input("Enter a value to convert: "))
                     cd.kmtoyards(valuetoconvert)
                         #use class and def here
                 except: print("Oops! Invalid input")
             case 2: #km - miles
                 try:
                     valuetoconvert = int(input("Enter a value to convert: "))
                     cd.kmtomiles(valuetoconvert)
                    # use class and def here
                 except: print("Oops! Invalid input")
             case 3: #miles - km
                 try:
                     valuetoconvert = int(input("Enter a value to convert: "))
                     cd.milestokm(valuetoconvert)
                     # use class and def here
                 except: print("Oops! Invalid input")





    case 2:
        conver_type = int(input("In temperature: 1.Celsius to kelvin, 2.kelvin to Fahrenheit, 3.Celsius to Fahrenheit "))
        if conver_type not in range(1, 4):
            conver_type = int(input("Invalid! Please select from available options"))
        else: pass
        match (conver_type):
            case 1: #c-k
             try:
                  valuetoconvert = int(input("Enter a value to convert: "))
                  ct.celsiustokelvin(valuetoconvert)
                  # use class and def here
             except:
                   print("Oops! Invalid input")
            case 2:#k-f
             try:
                 valuetoconvert = int(input("Enter a value to convert: "))
                 ct.kelvintof(valuetoconvert)

                 # use class and def here
             except:#c-f
                 print("Oops! Invalid input")
            case 3:
             try:
                  valuetoconvert = int(input("Enter a value to convert: "))
                  ct.celsiustof(valuetoconvert)

             except:
                   print("Oops! Invalid input")

    case 3:
      conver_type = int(input("In Weight: 1.kg to pounds(lb), 2.kg to ounces(oz), 3.pounds to ounces "))
      if conver_type not in range(1, 4):
          conver_type = int(input("Invalid! Please select from available options"))
      else : pass
      match (conver_type):
        case 1:  # kg-pounds
             try:
              valuetoconvert = int(input("Enter a value to convert: "))
              cw.kgtopund(valuetoconvert)

                          # use class and def here
             except: print("Oops! Invalid input")

        case 2:  #
            try:
                valuetoconvert = int(input("Enter a value to convert: "))
                cw.kgtoounces(valuetoconvert)

                    # use class and def here
            except:
                print("Oops! Invalid input")
        case 3:
            try:
                valuetoconvert = int(input("Enter a value to convert: "))
                cw.poundtoounces(valuetoconvert)

                    # use class and def here
            except:
                print("Oops! Invalid input")




