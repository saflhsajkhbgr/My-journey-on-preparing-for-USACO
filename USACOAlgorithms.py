
import time


# 定义不可达距离
_ = float('inf')


class BFS:
    """
    Breadth first search
    """
    def __init__(self, input, start, dest):
        self.input = input
        self.start = start
        self.dest = dest
        self.route = None

    def bfs_walk(self):
        route = {}
        S = [self.start]
        counter = 0
        unread = list(self.input.keys())
        # print('unread:', unread)
        while unread:
            counter += 1
            next_vertex = []
            for vertex in S:
                for v in self.input[str(vertex)]:
                    next_vertex.append(v)
                try:
                    unread.remove(str(vertex))
                    # print('unread:', unread)
                except ValueError:
                    pass
            S = next_vertex
            route[str(counter)] = next_vertex
        self.route = route

    def simplify(self):
        readed = []
        for r in self.route.keys():
            self.route[r] = set(self.route[r])
            cur = []
            for i in self.route[r]:
                if i not in readed:
                    cur.append(i)
                    readed.append(i)
            self.route[r] = cur

    def solve(self):
        for r in self.route.keys():
            if self.dest in self.route[r]:
                print(int(r))


def BFS_solve():
    t1 = time.time()
    graph1 = {'(0, 2)': [(1, 3), (1, 2), (1, 1)], '(1, 3)': [(2, 3), (1, 2)], '(1, 2)': [(1, 3), (2, 2), (1, 1)],
              '(1, 1)': [(4, 2)], '(2, 3)': [(4, 2)], '(4, 2)': [], '(2, 2)': []}
    graph2 = {'(3, 0)': [(1, 1), (2, 2), (3, 4)], '(1, 1)': [(5, 9)], '(2, 2)': [(6, 7), (2, 3)], '(5, 9)': [(3, 4)],
         '(3, 4)': [], '(6, 7)': [], '(2, 3)': []}

    alg = BFS(graph1, start=(0, 2), dest=(4, 2))
    alg.bfs_walk()
    alg.simplify()
    alg.solve()
    # print(alg.route)
    t2 = time.time()
    cost = t2 - t1
    print('cost:', cost)


def right(n):
    return n+1


def left(n):
    return n-1


def move(n):
    return 2*n


def catch_the_cow_BFS(s, e):
    """
    时间限制: 1 s
    空间限制: 16000 KB
    题目等级 : 黄金 Gold
    题解
    题目描述 Description
    农夫约翰被告知一头逃跑奶牛的位置，想要立即抓住它，他开始在数轴的N 点（0≤N≤100000），奶牛在同一个数轴的K 点（0≤K≤100000）。
    约翰有两种移动方式：1 分钟内从x 点移动到x+1 或x-1；1 分钟内从x 点移动到2x。假设奶牛不会移动，约翰抓住它需要多少时间？
    :param s: starting point
    :param e: destination
    :return: steps taken to get there
    """
    movement = [right, left, move]
    routes = [[s]]
    i = 0
    flag = True
    print('routes[i]:', routes[i])
    while flag:
        route = []
        print('i:', i)
        for r in routes[i]:
            if not flag:
                break
            for m in movement:
                cur = m(r)
                route.append(cur)
            if e in route:
                flag = False
        routes.append(route)
        i += 1
        print('routes[i]:', routes)
    # print(routes)
    return i


def milk_bucket(inp):
    """
    Question: three buckets, pour milk from 1 to 2, 2 to 3, 3 to 4. Stop pouring if one empty or one full,
    print the amount left in each bucket after 100 iterations.
    e.g. [[10, 3], [11, 4], [12, 5]] => 0, 10, 2
    :param inp: such that [[capacity1, milk1], [capacity2, milk2], [capacity3, milk3]]
    :return: milk amount in each bucket
    """
    counter = 0
    i = 0
    while counter != 100:
        if i == 2:
            res = inp[0][1] + inp[2][1]
            if res > inp[0][0]:
                inp[0][1] = inp[0][0]
                inp[2][1] = res - inp[0][0]
            else:
                inp[0][1] = res
                inp[2][1] = 0
            i = 0
        else:
            res = inp[i][1] + inp[i+1][1]
            if not res > inp[i+1][0]:
                inp[i+1][1] = res
                inp[i][1] = 0
            else:
                inp[i+1][1] = inp[i+1][0]
                inp[i][1] = res - inp[i+1][0]
            i += 1
        counter += 1
    for j in inp:
        print(j[1])


def right_up(i, j):
    if i - 1 >= 0 and j + 2 >= 0:
        return i - 1, j + 2
    else:
        return None, None

def up_right(i, j):
    if i - 2 >= 0 and j + 1 >= 0:
        return i - 2, j + 1
    else:
        return None, None

def up_left(i, j):
    if i - 2 >= 0 and j - 1 >= 0:
        return i - 2, j - 1
    else:
        return None, None

def left_up(i, j):
    if i - 1 >= 0 and j - 2 >= 0:
        return i - 1, j - 2
    else:
        return None, None

def left_down(i, j):
    if i + 1 >= 0 and j - 2 >= 0:
        return i + 1, j - 2
    else:
        return None, None

def down_left(i, j):
    if i + 2 >= 0 and j - 1 >= 0:
        return i + 2, j - 1
    else:
        return None, None

def down_right(i, j):
    if i + 2 >= 0 and j + 1 >= 0:
        return i + 2, j + 1
    else:
        return None, None

def right_down(i, j):
    if i + 1 >= 0 and j + 2 >= 0:
        return i + 1, j + 2
    else:
        return None, None


def lotus_pond(s, e):
    movements = [right_up, up_right, up_left, left_up, left_down, down_left, down_right, right_down]
    routes = [[s]]
    i = 0
    flag = True
    print('routes[i]:', routes[i])
    while flag:
        route = []
        print('i:', i)
        for r in routes[i]:
            if not flag:
                break
            for m in movements:
                cur = m(r[0], r[1])
                if cur != (None, None):
                    try:
                        t = mat[cur[0]][cur[1]]
                        route.append(cur)
                    except Exception:
                        pass
            if e in route:
                flag = False
        routes.append(route)
        i += 1
        print('routes[i]:', routes)
    # print(routes)
    return i


def milk_shop(n):
    drink = n
    while True:
        exchange = int(n/3)
        left = n % 3
        drink += exchange
        n = left + exchange
        if n < 3:
            break
    print(drink)


def solve_pond():
    directions = [right_up, up_right, up_left, left_up, left_down, down_left, down_right, right_down]
    mat = [[0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1],
           [0, 0, 0, 0, 0, 4, 0, 0],
           [3, 0, 0, 0, 0, 0, 1, 0]]
    solution = lotus_pond(s=(3, 0), e=(2, 5))
    return None


def calfflac(string):
    l = []
    for index_mid in range(len(string)):
        a = True
        b = True
        counter = 0
        while a == b:
            counter += 1
            try:
                a = string[index_mid-counter]
                b = string[index_mid+counter]
            except Exception:
                pass
        l.append(counter)
    return l


def generate_l():
    block = [1, 3, 5]
    n = int(input('pls input n:'))
    l = []
    for i in range(n):
        l.append(block)
        block = [block[1], block[2], block[2]+2]
    last = l[-1][-1]
    return l, last, n


def xmastree():
    l, last, n = generate_l()
    for i in l:
        for j in i:
            print(' '*int(((last-j)/2)) + '*'*j)

    if n % 2 == 0:
        for i in range(int(n/2)):
            print(' '*int(((last-(n-1))/2)) + '*'*(n-1))
    else:
        for i in range(int((n+1)/2)):
            print(' '*int(((last-n)/2)) + '*'*n)


# points点个数，edges边个数,graph路径连通图,start七点,end终点
def Dijkstra(points, edges, graph, start, end):
    # 定义不可达距离
    _ = float('inf')
    map = [[_ for i in range(points + 1)] for j in range(points + 1)]
    pre = [0] * (points + 1)  # 记录前驱
    vis = [0] * (points + 1)  # 记录节点遍历状态
    dis = [_ for i in range(points + 1)]  # 保存最短距离
    road = [0] * (points + 1)  # 保存最短路径
    roads = []
    map = graph

    for i in range(points + 1):  # 初始化起点到其他点的距离
        if i == start:
            dis[i] = 0
        else:
            dis[i] = map[start][i]
        if map[start][i] != _:
            pre[i] = start
        else:
            pre[i] = -1
    vis[start] = 1
    for i in range(points + 1):  # 每循环一次确定一条最短路
        min = _
        for j in range(points + 1):  # 寻找当前最短路
            if vis[j] == 0 and dis[j] < min:
                t = j
                min = dis[j]
        vis[t] = 1  # 找到最短的一条路径 ,标记
        for j in range(points + 1):
            if vis[j] == 0 and dis[j] > dis[t] + map[t][j]:
                dis[j] = dis[t] + map[t][j]
                pre[j] = t
    p = end
    len = 0
    while p >= 1 and len < points:
        road[len] = p
        p = pre[p]
        len += 1
    mark = 0
    len -= 1
    while len >= 0:
        roads.append(road[len])
        len -= 1
    return dis[end], roads


def generate_map(mat, num_of_nodes):
    l = []
    l = [[_ for j in range(num_of_nodes + 1)] for i in range(num_of_nodes+1)]
    for m in mat:
        l[m[0]][m[1]] = m[2]
    return l


# 固定map图
def dij_solve(map, s, e):
    # mat = [(3, 1, 10), (1, 3, 10), (1, 2, 7)]
    # import time
    # t1 = time.time()
    # mat = [(1, 2, 3), (1, 3, 4), (2, 3, 5), (3, 2, 5), (2, 4, 6), (4, 2, 6), (3, 4, 2), (4, 3, 2),
    #        (2, 5, 10), (4, 5, 7), (4, 6, 9), (6, 7, 14), (5, 7, 12), (4, 7, 16)]
    # map = generate_map(mat, 7)
    # s = 1
    # e = 7
    # solution = dij_solve(map, s, e)
    # print(solution)
    # t2 = time.time()
    # print('cost:', t2-t1)
    # map()
    dis, road = Dijkstra(7, 12, map, int(s), int(e))
    return dis, road


def binarySearch(lst, value, low, high):  # low,high是lst的查找范围
    if high < low:
        return -1
    mid = (low + high) / 2
    if lst[mid] > value:
        return binarySearch(lst, value, low, mid - 1)
    elif lst[mid] < value:
        return binarySearch(lst, value, mid + 1, high)
    else:
        return mid


def bsearch_cowvid_nineteen(N, sections, D, low, high, state):
    """
    等级：白银组
    N: 奶牛数量
    sections: [(a, b), (c, d)...]
    由于高传染性的牛传染病 COWVID-19 的爆发，Farmer John 非常担忧他的奶牛们的健康。
为了限制疾病的传播，Farmer John 的 N 头奶牛（ 2 ≤ N ≤ 1 0 5 ） （2≤N≤10^5）（2≤N≤10)
 ）决定践行“社交距离”，分散到农场的各处。农场的形状如一维数轴，上有 M 个互不相交的区间（ 1 ≤ M ≤ 1 0 5 ） （1≤M≤10^5）
 ），其中有可用来放牧的青草。奶牛们想要使她们位于不同的整数位置，每个位置上均有草，并且最大化 D 的值，其中 D 为最近的两头奶牛之间的距离。请帮助奶牛们求出 D 的最大可能值。
输入格式（文件名：socdist.in）：
输入的第一行包含 N 和 M。以下 M 行每行用两个整数 a 和 b 描述一个区间，其中 0 ≤ a ≤ b ≤ 1 0 18 0≤a≤b≤10^{18}0≤a≤b≤10
18
 。没有两个区间有重合部分或在端点处相交。位于一个区间的端点上的奶牛视为在草上。
输出格式（文件名：socdist.out）：
输出 D 的最大可能值，使得所有奶牛之间的距离均不小于 D 单位。保证存在 D>0 的解
    """
    flag = True
    l = [0 for i in range(low, high+1)]
    next = 0
    counter = 0
    while flag:
        if next in range(sections[counter][0], sections[counter][1] + 1):
            l[next] = 1
            next += D
            counter = 0
        else:
            counter += 1
            if counter == 3:
                counter = 0
                next += 1
        if next >= len(l):
            break
    if abs(state-D) > 1 and l.count(1) < N:
        print('step:', D)
        print(l)
        return bsearch_cowvid_nineteen(N, sections, int((D-low)/2), low, high, state=D)
    elif abs(state-D) > 1 and l.count(1) > N:
        print('step:', D)
        print(l)
        return bsearch_cowvid_nineteen(N, sections, int((high-D)/2), low, high, state=D)
    elif l.count(1) == N:
        return l
    else:
        return l


def solve_cowvid_nineteen():
    sections = [(0, 2), (4, 6), (9, 9)]
    low = sections[0][0]
    high = sections[-1][-1]
    D = int((low + high) / 2)
    l = bsearch_cowvid_nineteen(4, sections, D, low, high, state=0)
    print(l)


def mu_particle():
    return None


class DynamicProgramming:
    def recursive_example(self, x):
        """
        硬币问题的递归解法
        """
        if x == 0:
            return 0
        res = _
        if x >= 2:
            res = min([self.recursive_example(x - 2) + 1, res])
        if x >= 5:
            res = min([self.recursive_example(x - 5) + 1, res])
        if x >= 7:
            res = min([self.recursive_example(x - 7) + 1, res])
        return res

    def dp_least_coins(self, sum):
        """
        DP的最值问题
        硬币问题的DP解法
        状态转移方程: f[x] = min(f[x-2]+1, f[x-5]+1, f[x-7]=1)
        """
        l = [_ for i in range(sum+1)]
        for i in range(sum+1):
            if i == 0:
                l[0] = 0
            elif i >= 7:
                l[i] = min(l[i-2]+1, l[i-5]+1, l[i-7]+1)
            elif i >= 5:
                l[i] = min(l[i-2]+1, l[i-5]+1)
            elif i >= 2:
                l[i] = l[i-2]+1
        return l
        # return l[-1]

    def dp_all_paths(self, i, j):
        """
        DP的计数性问题
        从方格左上角到指定(i, j)的路径数量，每次只能走i+1 or j+1
        状态转移方程：f[i][j] = f[i-1][j] + f[i][j-1]
        """
        l = [[_ for i in range(i)] for j in range(j)]
        for a in range(i):
            for b in range(j):
                if a == 0 or b == 0:
                    l[a][b] = 1
                else:
                    l[a][b] = l[a-1][b] + l[a][b-1]
        return l
        # return l[i-1][j-1]

    def dp_frog_jump(self, lst):
        """
        DP的存在性问题
        从数组的左边出发，青蛙只能跳到当前石头显示步数以内的下一个石头，问青蛙能否跳到最后一个石头
        状态转移方程：f[i] = (True in (f[0] to f[i-1])) AND i-j <= a[j])
        """
        l = [False for i in range(len(lst))]
        for i in range(len(lst)):
            if i == 0:
                l[0] = True
            for j in range(len(l)):
                if l[j] and i-j <= lst[j]:
                    l[i] = True
                    break
        return l
        # return l[-1]


def reverse(lst):
    for i in range(int(len(lst)/2)):
        ex = lst[-i-1]
        lst[-i-1] = lst[i]
        lst[i] = ex
    return lst


def swap(N, swaplist, K):
    lst = [i+1 for i in range(N)]
    for k in range(K):
        for l in swaplist:
            lst[l[0]-1:l[1]] = reverse(lst[l[0]-1:l[1]])
    return lst


def triangle():
    lst = [[0, 0], [0, 1], [1, 0], [1, 2]]
    # with open('triangles.in') as f:
    #     while 1:
    #         line = f.readline().split()
    #         if not line:
    #             break
    #         l = [int(i) for i in line]
    #         lst.append(l)
    triangles = []
    for vertex in lst:
        # print('vertex:', vertex)
        v1 = []
        v2 = []
        for others in lst:
            if others != vertex:
                if others[0] == vertex[0]:
                    v1.append(others)
                if others[1] == vertex[1]:
                    v2.append(others)
        # print('v1:', v1)
        # print('v2;', v2)
        for i in v1:
            for j in v2:
                A = abs((j[0] - vertex[0]) * (i[1]-vertex[1])/2)
                triangles.append(A)
                # print('triangle:', triangles)
    # return triangles
    return sum(triangles)


class Rut:
    """
    每一小时，每头奶牛会执行以下二者之一：

如果她当前所在的方格里的草已经被其他奶牛吃掉了，则她会停下。
吃完她当前所在的方格中的所有草，并向她朝向的方向移动一个方格。
经过一段时间，每头奶牛的身后会留下一条被啃秃了的轨迹。

如果两头奶牛在一次移动中移动到了同一个有草的方格，她们会分享这个方格中的草，并在下一个小时继续沿她们朝向的方向移动。

请求出每头奶牛吃到的草的数量。有些奶牛永远不会停下，从而吃到无限多的草。

输入格式（从终端/标准输入读入）：
输入的第一行包含 N。以下 N 行，每行描述一头奶牛的起始位置，包含一个字符 N（表示朝向北面） 或 E（表示朝向东面），以及两个非负整数 x 和
 y（0≤x≤109，0≤y≤109）表示方格的坐标。所有 x 坐标各不相同，所有 y 坐标各不相同。
为了使方向和坐标尽可能明确，如果一头奶牛位于方格 (x,y) 并向北移动，她会到达方格 (x,y+1)。如果她向东移动，她会到达方格 (x+1,y)。

输出格式（输出至终端/标准输出）：
输出 N 行。输出的第 i 行包含输入中的第 i 头奶牛吃到草的方格的数量。如果一头奶牛可以吃到无限多的草，为这头奶牛输出 "Infinity"。
输入样例：
6
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1
输出样例：
5
3
Infinity
Infinity
2
5
    """
    import time

    # lst = [['E', 3, 5], ['N', 5, 3], ['E', 4, 6], ['E', 10, 4], ['N', 11, 2], ['N', 8, 1]]

    # num = int(input())
    # lst = []
    # for i in range(num):
    #     s = input().split()
    #     lst.append(s)
    def __init__(self, lst):
        self.lst = lst

    def Emove(self, s, a, b):
        return s, int(a) + 1, int(b)

    def Wmove(self, s, a, b):
        return s, int(a) - 1, int(b)

    def Nmove(self, s, a, b):
        return s, int(a), int(b) + 1

    def Smove(self, s, a, b):
        return s, int(a), int(b) - 1

    def simulation(self, L):
        lst = []
        for l in L:
            if l == []:
                lst.append([])
            elif l[0] == 'E':
                [s, a, b] = self.Emove(l[0], l[1], l[2])
                lst.append([s, a, b])
            elif l[0] == 'W':
                [s, a, b] = self.Wmove(l[0], l[1], l[2])
                lst.append([s, a, b])
            elif l[0] == 'N':
                [s, a, b] = self.Nmove(l[0], l[1], l[2])
                lst.append([s, a, b])
            elif l[0] == 'S':
                [s, a, b] = self.Smove(l[0], l[1], l[2])
                lst.append([s, a, b])
        return lst

    def solve(self):
        t1 = time.time()
        # dct = {i: [] for i in range(len(lst))}
        L = []
        ans = [_ for i in self.lst]
        step = 0
        t1 = time.time()
        while True:
            step += 1
            for i in self.lst:
                if i:
                    L.append([i[1], i[2]])
            lst = self.simulation(self.lst)
            t01 = time.time()
            for l in lst:
                # print('lst:', lst)
                if l:
                    t11 = time.time()
                    if [l[1], l[2]] in L:
                        # print('found:', [l[1], l[2]], 'in', L)
                        ans[lst.index(l)] = step
                        lst[lst.index(l)] = []
                    t12 = time.time()
                    print('cost:', t12 - t11)
            t02 = time.time()
            print('total cost:', t02 - t01)
            t2 = time.time()
            if t2 - t1 >= 3.5:
                # print('cost:', t2-t1)
                break
        for a in ans:
            if a != _:
                print(a)
            else:
                print('Infinity')


def read(dir):
    lst = []
    with open(dir) as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            l = [i for i in line]
            lst.append(l)
    # lst = lst[1:]
    return lst


if __name__ == '__main__':
    t1 = time.time()
    pass
    t2 = time.time()
    print('cost:', t2-t1)
    pass