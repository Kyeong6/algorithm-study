"""
방문 길이:
게임 캐릭터 4가지 명령어를 통해 움직이려 한다.
U: 위쪽으로 한 칸가기
D: 아래쪽으로 한 칸 가기
R: 오른쪽으로 한 칸 가기
L: 왼쪽으로 한 칸 가기
캐릭터는 좌표평면의 (0,0) 위치에서 시작, 경계는 (-5~5, -5~5)

제약조건:
1. dirs는 string형으로 주어지며, 'U','D','R','L'이외의 문자는 주어지지 않음
2. dirs의 길이는 500이하 자연수

입출력 예시
dirs | answer
ULURRDLLU | 7

분석:
- 중복 제거 필요 -> set()
- 음수 좌표 포함
    - 좌표 문제: '좌표 범위 벗어나는 경우 체크' 필요
- 구현 문제 같은 경우 코드가 길어지므로, 여러 함수로 나누어서 진행해보기
"""

# 좌표평면 벗어나는지 체크
def is_valid_move(nx, ny):
    # 원점을 (0,0)이 아닌 (5,5)로 설정하여 음수 좌표 대비
    return 0 <= nx < 11 and 0 <= ny < 11

# 명령어를 통해 다음 좌표 결정
def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'L':
        nx ,ny = x-1, y
    elif dir == 'R':
        nx, ny = x+1, y
    
    return nx, ny

def soultion(dirs):
    x, y = 5, 5
    # 중복 제거
    ans = set()

    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        
        # 벗어난 좌표 인정 x
        if not is_valid_move(nx, ny):
            continue

        ans.add((x,y,nx,ny))
        ans.add((nx,ny,x,y))
        # 좌표 이동에 따른 업데이트
        x,y = nx, ny
    
    return len(ans)/2
