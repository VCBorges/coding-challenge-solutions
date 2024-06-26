from rich import print

def luckBalance(k: int, contests: list[list[int]]) -> int:
    luck_balance = 0
    loseble_important_contests = k
    contests.sort(
        key=lambda x: (x[1], x[0]), 
        reverse=True,
    )
    for i in range(len(contests)):
        contest_luck = contests[i][0]
        contest_importance_rating = contests[i][1]
        if loseble_important_contests > 0 or contest_importance_rating == 0:
            luck_balance += contest_luck
            loseble_important_contests -= 1
        else:
            luck_balance -= contest_luck
    
    return luck_balance

if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()
    
    first_multiple_input = '6 3'.split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = [
        [5, 1],
        [2, 1],
        [1, 1],
        [8, 1],
        [10, 0],
        [5, 0],
    ]


    # contests = []

    # for _ in range(n):
    #     contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    
    print(f'{result = }')