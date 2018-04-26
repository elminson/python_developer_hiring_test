#!/usr/bin/env python


def DFS(j, visited, zombies, row):
    for k in range(row):
        if zombies[j][k] == '1' and visited[j][k] == False and visited[k][j] == False:
            visited[j][k] = True
            visited[k][j] = True
            DFS(k, visited, zombies, row)


def zombieCluster(zombies):
    row = len(zombies)
    col = len(zombies[0])
    count = 0
    if row == 0 or col == 0:
        return count
    visited = [[False for j in range(col)] for i in range(row)]
    for i in range(row):
        bol = False
        for j in range(row):
            if zombies[i][j] == '1' and visited[i][j] == False and visited[j][i] == False:
                visited[i][j] = True
                visited[j][i] = True
                DFS(j, visited, zombies, row)
                if bol == 0:
                    count += 1
                    bol = True
    return count


def main():
    # array input of zombie
    zombie_array = list()
    zombie_count = int(input())
    for i in range(int(zombie_count)):
        n = raw_input()
        zombie_array.append(str(n))

    # zombie_array = ["1100" ,"1110", "0110", "0001"]
    # print out the result
    print(zombieCluster(zombie_array))


if __name__ == '__main__':
    main()
