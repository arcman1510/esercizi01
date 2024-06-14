class Persona:

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: float = age
        
        if first_name and last_name is True:
                print("Benvenuto")
        else:
             print("inserisci un nome valido!")

        