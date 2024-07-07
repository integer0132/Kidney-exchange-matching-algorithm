import random

# dfs를 사용하여 최대 길이가 3인 cycle을 찾음
def find_cycles(graph, start, max_length, path=[]):
    # node 추가
    path = path + [start]
    if len(path) > max_length: # cycle 길이가 3 이상이면 제외
        return []
    if len(path) > 1 and path[0] == path[-1]: # cycle이 완성되면 return
        return [path]
    cycles = []

    # 재귀를 사용하여 dfs를 돌려서 cycle 탐색
    for node in range(len(graph)):
        if graph[start][node] == 1 and (node not in path or (node == path[0] and len(path) > 1)):
            new_cycles = find_cycles(graph, node, max_length, path)
            for cycle in new_cycles:
                cycles.append(cycle)
    
    return cycles

# Kidney exchange matching 알고리즘
def kidney_exchange_matching(pairs, compatibility_matrix, number):
    max_cycle_length = 4 # 최대 3방향 교환 가능하도록 설정
    all_cycles = []

    # find_cycles 함수를 통해 최대 3개의 node로 cycle이 형성되는 cycle을 찾음
    cycles = find_cycles(compatibility_matrix, number, max_cycle_length, path=[])

    # cycle에서 첫번째 node와 마지막 node는 동일하므로, 마지막 node를 제거하여 중복 제거
    for cycle in cycles:
        if len(cycle) <= max_cycle_length + 1:
            all_cycles.append(cycle[:-1])

    # 중복되는 사이클 제거
    unique_cycles = []
    for cycle in all_cycles:
        sorted_cycle = sorted(cycle)
        if sorted_cycle not in unique_cycles:
            unique_cycles.append(sorted_cycle)

    # 정렬 시킨후 return
    return sorted(unique_cycles)
    
# 신장 수혜자와 기증자를 쌍으로 하여 20쌍을 만듦
num_pairs = 20
pairs = [(f"Recipient_{i}", f"Donor_{i}") for i in range(num_pairs)]

# 수혜자 * 기증자인 20*20 matrix를 생성하고, 기증이 가능하면 1, 기증이 불가능 하면 0으로 설정
compatibility_matrix = [[random.randint(0, 1) for _ in range(num_pairs)] for _ in range(num_pairs)]

# 수혜자와 기증자 쌍끼리는 기증이 불가능 하도록 설정
for i in range(num_pairs):
    compatibility_matrix[i][i] = 0

print("Compatibility Matrix:")
for row in compatibility_matrix:
    print(row)
print()

# 사이클을 찾기 원하는 수혜자, 기증자 쌍 인덱스 입력
while True:
    number = int(input("input your recipient number (0 ~ 19): "))
    if (number >= 0 and number < 20):
        break

# Kidney exchange matching 알고리즘 실행
cycles = kidney_exchange_matching(pairs, compatibility_matrix, number)

# 매칭이 되는 사이클 출력
print("Matching Cycles:")
for cycle in cycles:
    print([pairs[i] for i in cycle])