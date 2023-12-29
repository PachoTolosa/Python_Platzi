import mod

data = [
        {
            "Country": "Colombia",
            "Population": 20000
        },
        {
            "Country": "Bolivia",
            "Population": 10000
        }
    ]

def run():
    k, v = mod.getPopulation() 
    print(k, v)

    
    country = input("Ingresar el país: \n").capitalize()
    result = mod.populationByCountry(data, country)
    print(result)
    
    
# Se usa para manejar esta dualidad (Correrlo como script y tambien al importarlo desde otro)
if __name__ == "__main__":
    run()