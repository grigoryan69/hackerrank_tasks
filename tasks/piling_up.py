def piling_up():
    for _ in (range(int(input()))):
        no_of_cubes = int(input())
        side_lengths = list(map(int, input().strip().split()))
        result = "Yes"
        if max(side_lengths) not in (side_lengths[0], side_lengths[-1]):
            result = "No"
        print(result)


def main():
    piling_up()
    
if __name__ == '__main__':
    main()
