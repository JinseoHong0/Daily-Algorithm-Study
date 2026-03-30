import sys

def change_grade_to_int(grade):
    grades = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
    grades_int = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
    
    if grade in grades:
        return grades_int[grades.index(grade)]
    return 0.0

# split(' ') 대신 split()을 써야 빈 문자열('')이 안 생깁니다.
grade_list = sys.stdin.read().split()

tot_hakjeom = 0.0
tot_grade = 0.0

# 3개씩 한 세트이므로 0, 3, 6... 순서로 접근하는 게 안전합니다.
for i in range(0, len(grade_list), 3):
    # 과목: grade_list[i], 학점: grade_list[i+1], 성적: grade_list[i+2]
    hakjeom = float(grade_list[i+1])
    grade_str = grade_list[i+2]

    if grade_str == "P":
        continue  # P는 아예 무시
    
    grade_val = change_grade_to_int(grade_str)
    tot_hakjeom += hakjeom
    tot_grade += (hakjeom * grade_val)

# 결과 출력
if tot_hakjeom != 0:
    # 백준은 round보다 f-string 서식 지정을 선호합니다 (소수점 아래 6자리 고정)
    print(f"{tot_grade / tot_hakjeom:.6f}")
else:
    print(f"{0.0:.6f}")