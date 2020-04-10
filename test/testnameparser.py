from src import User
import time as t

def test(id: int):
    MT = User(id)
    return MT.name()

if __name__ == "__main__":
    time = t.time()
    print(test(38))
    print(t.time()-time)