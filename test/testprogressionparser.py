from src import User
import time as t


def test_parser(i: int):
    u = User(i)
    return u.progressions()


if __name__ == "__main__":
    time = t.time()
    print("Testing parse progression for user 4574")
    print(test_parser(4574))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse progression for Administrator, user 5")
    print(test_parser(5))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse progression for novice, user 4575")
    print(test_parser(4575))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse progression for unexisting user, user 20000")
    print(test_parser(20000))
    print("Total time", (t.time() - time) * 1000, "ms")
