from Mathraining import User
import time as t

def test(id: int):
    MT = User(id)
    return MT.name()

if __name__ == "__main__":
    print(test(4574))