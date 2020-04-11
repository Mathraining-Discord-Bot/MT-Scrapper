from mathraining.scrapper.mathuser import User
import time as t


def test(id: int):
    MT = User(id)
    return MT.solved(10021)


if __name__ == "__main__":
    time = t.time()
    print(test(4574))
    print(t.time() - time)
