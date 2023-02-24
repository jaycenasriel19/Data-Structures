cars={'Toyota corolla':15000,
      'Toyota camry':16500,
      'Toyota yaris':16750,
      'Toyota CH-R':20000,
      'Toyota 4-Runner':40000,
      'Honda civic':25000,
      'Honda accord':26500,
      'Honda fit':31500,
      'Honda pilot':27200,
      'Honda CR-V':28500,
      'Tesla model s':56300,
      'Tesla model y':69000,
      'Tesla model 3':43000,
      'Tesla cybertruck':70000,
      'Lucid air touring':138000,
      'Lucid air pure':87400,
      'Lucid air grand touring':138000,
      'Mercedes benz class c':47500,
      'Mercedes benz class s':43000, 
      'Mercedes benz class a':44300,
      'Mercedes benz gla coupe':65400,
      'Mercedes benz eqs':125000,
      'Range rover evoque':46000,
      'Range rover velar':42500, 
      'Range rover discovery sport':50000,
      'Range rover sport':47000,
      'Bmw x7':55000,
      'Bmw x3':48000,
      'Bmw i8':147500,
      'Bmw m5':107500,
      'Bmw x6':89000}
    
carName = input('Enter carName: ')
if carName in cars:
    print('Yes')
    carPrice=cars[carName]
    print(f'The price of {carName} is ${carPrice} ')
else:
    print(f'Apologies,{carName} is not available.')
    
    
    
    #github account  @jaycenasriel19
    