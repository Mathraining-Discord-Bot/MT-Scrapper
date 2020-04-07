import Mathraining as MT
import time as t


def test_parser(i: int, new=False):
    MTS = MT.User(i)
    if (new == True):
        return MTS.score_new()
    else:
        return MTS.score()


def compare(i: int):
    MTS = MT.User(i)
    time = t.time()
    print(MTS.score(), "tested old in", (t.time() - time) * 1000, "ms")
    time = t.time()
    print(MTS.score_new(), "tested new in", (t.time() - time) * 1000, "ms")


def alltest(new=False):
    time = t.time()
    print("Testing parse score for user 4574")
    print(test_parser(4574, new))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse score for user 4574")
    print(test_parser(4574, new))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse score for Administrator, user 5")
    print(test_parser(5, new))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse score for novice, user 4575")
    print(test_parser(4575, new))
    print("Total time", (t.time() - time) * 1000, "ms")
    time = t.time()
    print("Testing parse score for unexisting user, user 20000")
    print(test_parser(20000, new))
    print("Total time", (t.time() - time) * 1000, "ms")


if __name__ == "__main__":
    print("old all test")
    alltest()
    print("new all test")
    alltest(True)
