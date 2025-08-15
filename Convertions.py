
print("Welcome User!, This is a convertions program ")
#classes and def for conversions are below

















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

                         #use class and def here
                 except: print("Oops! Invalid input")
             case 2: #km - miles
                 try:
                     valuetoconvert = int(input("Enter a value to convert: "))

                    # use class and def here
                 except: print("Oops! Invalid input")
             case 3: #miles - km
                 try:
                     valuetoconvert = int(input("Enter a value to convert: "))

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

                  # use class and def here
             except:
                   print("Oops! Invalid input")
            case 2:#k-f
             try:
                 valuetoconvert = int(input("Enter a value to convert: "))

                 # use class and def here
             except:#c-f
                 print("Oops! Invalid input")
            case 3:
             try:
                  valuetoconvert = int(input("Enter a value to convert: "))

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

                          # use class and def here
             except: print("Oops! Invalid input")

        case 2:  #
            try:
                valuetoconvert = int(input("Enter a value to convert: "))

                    # use class and def here
            except:
                print("Oops! Invalid input")
        case 3:
            try:
                valuetoconvert = int(input("Enter a value to convert: "))

                    # use class and def here
            except:
                print("Oops! Invalid input")




