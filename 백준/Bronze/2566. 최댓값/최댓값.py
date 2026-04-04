import sys

# 1. 입력을 한 번에 다 읽어온 뒤, 공백이나 줄바꿈을 기준으로 모두 쪼갭니다.
# 이렇게 하면 81개의 숫자가 순서대로 리스트에 담깁니다.
data = sys.stdin.read().split()

max_num = -1  # 최댓값을 저장할 변수 (0~99 범위이므로 -1로 초기화)
max_row = 0   # 행 번호
max_col = 0   # 열 번호

# 2. 81개의 데이터를 9x9 격자로 생각하며 확인합니다.
for i in range(9):        # 행 (0~8)
    for j in range(9):    # 열 (0~8)
        # i*9 + j 공식을 사용하면 1차원 리스트를 2차원처럼 인덱싱할 수 있습니다.
        current_val = int(data[i * 9 + j])
        
        if current_val > max_num:
            max_num = current_val
            max_row = i + 1  # 문제는 1행부터 시작하므로 +1
            max_col = j + 1  # 문제는 1열부터 시작하므로 +1

# 3. 출력 형식에 맞게 출력
print(max_num)
print(max_row, max_col)