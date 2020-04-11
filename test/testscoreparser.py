from mathraining.scrapper.mathuser import User
import time as t


def test_parser(i: int):
    MTS = User(i)
    return MTS.score()


def alltest():
    time = t.time()
    print("Testing parse score for user 4574")
    print(test_parser(4574))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse score for user 4574")
    print(test_parser(4574))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse score for Administrator, user 5")
    print(test_parser(5))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse score for novice, user 4575")
    print(test_parser(4575))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse score for unexisting user, user 20000")
    print(test_parser(20000))
    print("Total time", (t.time() - time) * 1000, "ms")


if __name__ == "__main__":
    time = t.time()
    print("old all test")
    alltest()
    print("All test executed in ", (t.time()-time)*1000, "ms")
