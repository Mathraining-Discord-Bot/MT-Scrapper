from src import User
import time as t


def test(id: int):
    MTS = User(id)
    return MTS.info()


if __name__ == "__main__":
    time = t.time()
    print("Test wrapping info for user 4574")
    print(test(4574))
    print("Total time ", (t.time()-time)*1000, "ms")
    time = t.time()
    print("Test wrapping info for user 4574")
    print(test(4574))
    print("Total time ", (t.time()-time)*1000, "ms")
    time = t.time()
    print("Test wrapping info for Administrator, user 5")
    print(test(5))
    print("Total time ", (t.time()-time)*1000, "ms")
    time = t.time()
    print("Test wrapping info for novice, user 5475")
    print(test(4575))
    print("Total time ", (t.time()-time)*1000, "ms")
    time = t.time()
    print("Test wrapping info for non existing user, user 20000")
    print(test(20000))
    print("Total time ", (t.time()-time)*1000, "ms")