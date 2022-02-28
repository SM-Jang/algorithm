class HelloWorld:
    def __init__(self):
        # __????__ : class라는 instance가 만들어질 때 생김
        print("Hello World! Just one more time")

    def __del__(self):
        # __????__ : class라는 instance가 없어질 때 실행
        print("Good Bye")

    def performAverage(self, val1, val2):
        avg = (val1 + val2) / 2
        print("The average of the score is {}".format(avg))


def main() -> None:
    dicTest = {1:'one',
               2:'two'}
    print(dicTest)
    dicTest[3] = 'three'
    print(dicTest)

    # world = HelloWorld()

    # score1, score2 = input('Enter two scores: ').split(' ')
    # score1 = int(score1)
    # score2 = int(score2)
    # world.performAverage(score1, score2)


main()
