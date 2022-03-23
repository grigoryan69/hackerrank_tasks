import sys
def piling_up(cubes):
    t_cube = 0
    
    if cubes[0] > cubes[len(cubes)-1]:
        t_cube = cubes[0]
        cubes.pop(0)
    else:
        t_cube = cubes[len(cubes)-1]
        cubes.pop(len(cubes)-1)
    
    while len(cubes) > 0:
        if t_cube == cubes[0]:
            t_cube = cubes.pop(0)
        elif t_cube == cubes[len(cubes)-1]:
            t_cube = cubes.pop(len(cubes)-1)
        elif (cubes[0] > cubes[len(cubes)-1]) and (t_cube >= cubes[0]):
            t_cube = cubes.pop(0)
        elif (cubes[0] < cubes[len(cubes)-1]) and (t_cube >= cubes[len(cubes)-1]):
            t_cube = cubes.pop(len(cubes)-1)
        elif (cubes[0] == cubes[len(cubes)-1]):
            t_cube = cubes.pop(0)
        else:
            return "No"
    return "Yes"


if __name__ == '__main__':
    num_of_tests = sys.stdin.readline().strip()
    num_of_tests = int(num_of_tests)
    
    for i in range(0, num_of_tests):
        sys.stdin.readline()
        cubes = list(map(int, sys.stdin.readline().strip().split(' ')))
        print(piling_up(cubes))