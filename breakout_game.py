import pygame

# 1. 초기화
pygame.init()

# 2. 게임 화면 설정
screen_width = 800 # 화면 가로 크기
screen_height = 600 # 화면 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 객체 생성
pygame.display.set_caption("벽돌 깨기 게임")

# 게임 프레임 레이트(초당 화면 업데이트 횟수) 설정
clock = pygame.time.Clock() # Pygame Clock 객체 생성
FPS = 60 # 초당 60 프레임으로 제한

# 패들 초기 위치와 속도 설정
paddle_width = 100
paddle_height = 20
paddle_x = (screen_width / 2) - (paddle_width / 2) # 화면 중앙에 위치
paddle_y = screen_height - 50 # 화면 하단에 50px
paddle_color = (255, 255, 255) # 흰색
paddle_speed = 8 # 패들 이동 속도 (기존 10에서 5로 변경)
                 # 더 낮게 (예: 3), 더 높게 (예: 8) 조절하여 원하는 속도 찾으면 됨

# 공 초기 위치와 속도 설정
ball_radius = 10 # 공의 반지름
ball_x = screen_width // 2 # 화면 중앙
ball_y = screen_height // 2 # 화면 중앙
ball_dx = 5 # 공의 x 방향 속도(dx: delta x)
ball_dy = -5 # 공의 y 방향 속도(dy: delta y, 위로 올라가므로 음수)
ball_color = (255, 255, 0) # 노란색

# 점수 시스템
score = 0 # 현재 점수
font = pygame.font.Font(None, 36) # 폰트 객체 생성 (None은 기본 폰트, 36은 크기)

# 벽돌 설정
brick_width = 75
brick_height = 20
brick_rows = 5 # 5줄의 벽돌
brick_cols = 10 # 한 줄에 10개의 벽돌
brick_spacing = 5 # 벽돌 간 간격
brick_offset_y = 50 # 화면 상단에 벽돌이 시작하는 Y 좌표

bricks = [] # 벽돌 정보를 저장할 리스트 (여기에는 (Rect, color) 튜플이 저장될 것임)

# 벽돌 생성
for row in range(brick_rows):
    for col in range(brick_cols):
        # 각 별돌의 x, y 좌표 계산
        brick_x = col * (brick_width + brick_spacing) + brick_spacing
        brick_y = row * (brick_height + brick_spacing) + brick_offset_y
        
        # 벽돌 색상 (줄마다 다르게)
        if row == 0: brick_color = (255, 0, 0) # 빨강
        elif row == 1: brick_color = (255, 165, 0) # 주황
        elif row == 2: brick_color = (0, 255, 0) # 초록
        elif row == 3: brick_color = (0, 0, 255) # 파랑
        else: brick_color = (128, 0, 128) # 보라

        # 벽돌 정보 (Rect 객체와 색상)를 튜플 형태로 리스트에 추가
        bricks.append((pygame.Rect(brick_x, brick_y, brick_width, brick_height), brick_color))


# 3. 게임 루프
running = True # 게임 실행 여부 플래그

# 이 코드 위쪽으로 전역 변수 정의하는 곳
while running:
    # 3-1. 이벤트 처리
    for event in pygame.event.get(): # 발생한 모든 이벤트 순회
        if event.type == pygame.QUIT: # 창 닫기 버튼(X) 눌렀을 때
            running = False # 게임 종료 플래그 False로 설정
        # 키보드 누름 이벤트 처리(패들 움직임) - 이 부분 부자연스러움
        # if event.type == pygame.KEYDOWN: # 키가 눌렸을 때
        #     if event.key == pygame.K_LEFT: # 왼쪽 방향키
        #         paddle_x -= paddle_speed
        #     if event.key == pygame.K_RIGHT: # 오른쪽 방향키
        #         paddle_x += paddle_speed

    
    # 3-2. 게임 상태 업데이트
    # 현재 눌려있는 키 상태 가져오기
    keys = pygame.key.get_pressed() # 키보드 모든 키의 눌림 상태 가져옴(True/False)

    if keys[pygame.K_LEFT]: # 왼쪽 방향키가 눌려있으면
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]: # 오른쪽 방향키가 눌려있으면
        paddle_x += paddle_speed

    # 패들이 화면 밖으로 나가지 않도록 경계 설정
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > screen_width - paddle_width:
        paddle_x = screen_width - paddle_width
    
    # 여기에 공 위치 업데이트, 충돌 처리, 점수 계산 등 들어갈 예정
    # 공 위치 업데이트
    ball_x += ball_dx
    ball_y += ball_dy
    
    # 공이 화면 경계에 부딥혔을 때 방향 전환
    if ball_x - ball_radius < 0 or ball_x + ball_radius > screen_width:
        ball_dx *= -1 # 방향 속도 반전
    if ball_y - ball_radius < 0: # 공이 위쪽 벽에 부딪혔을 때
        ball_dy *= -1 # y 방향 속도 반전
    # 공이 아래쪽 화면 밖으로 나갔을 때 (게임 오버 조건)
    if ball_y + ball_radius > screen_height:
        print("게임 오버!")
        running = False # 게임 종료

    # 패들과 공 충돌 처리
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

    if paddle_rect.colliderect(ball_rect):
        ball_dy *= -1
        ball_y = paddle_y - ball_radius # 공이 패들에 박히지 않도록 조정
   
    # 공과 벽돌 충돌 처리 (이 부분 수정)
    # 깨진 벽돌을 저장할 임시 리스트
    bricks_to_remove = [] 
    for brick_rect, brick_color in bricks: # 튜플로 저장했으므로, Rect와 color를 분리해서 받음
        if ball_rect.colliderect(brick_rect): # 공과 벽돌이 충돌했을 때 (Rect 객체만 사용)
            ball_dy *= -1 # 공의 y 방향 속도 반전 (튕겨나가도록)
            bricks_to_remove.append((brick_rect, brick_color)) # 충돌한 벽돌을 제거 리스트에 추가 (튜플 전체)
            
            score += 100 # 벽돌 하나당 100점 증가
            break # 한 번에 하나의 벽돌만 충돌하도록 (옵션)

    # 충돌한 벽돌 제거
    for brick_item in bricks_to_remove: # 제거할 아이템(튜플)을 그대로 받음
        bricks.remove(brick_item)
    
    # 3-3. 화면 그리기
    screen.fill((0, 0, 0)) # 화면 검은색으로 채우기 (R, G, B)

    # 패들 그리기(사각형)
    pygame.draw.rect(screen, paddle_color, (paddle_x, paddle_y, paddle_width, paddle_height))

    # 공 그리기(원)
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    # 벽돌 그리기 (이 부분 수정)
    for brick_rect, brick_color in bricks: # 튜플로 저장했으므로, Rect와 color를 분리해서 받음
        pygame.draw.rect(screen, brick_color, brick_rect) # Rect와 color를 따로 전달
    
    # 점수 표시
    score_text = font.render(f"Score: {score}", True, (255, 255, 255)) # 텍스트 객체 생성 (텍스트, 안티앨리어싱, 색상)
    screen.blit(score_text, (10, 10)) # 화면의 (10, 10) 위치에 텍스트 그리기

    # 3-4. 화면 업데이트
    pygame.display.update() # 화면 새로 고침

    # 게임 프레임 속도 제어
    clock.tick(FPS)

# 4. 게임 종료
pygame.quit()


'''
게임 개발 피드백
0531(토) 오후 2:27
pygame.key.get_pressed() 함수를 사용하기 전 패들 움직임이 부자연스러워서 게임하기 불편했음
왼쪽, 오른쪽 키보드 누를 때마다 한번씩만 패들 움직일 수 있음 즉 키를 누르고 있는 동안 계속 움직이도록 처리해야 됨

0531(토) 오후 2:31
패들의 해당 방향으로 계속 부드럽게 움직임 확인함 즉, 조작감이 좋아짐
하지만 패들의 이동속도가 너무 빨라서 조정 필요함
-> paddle_speed 변수 값 변경
FPS는 초당 화면이 몇 번 업데이트되는지 나타냄
FPS가 높으면 같은 paddle_speed 값이더라도 더 짧은 시간에 여러 번 이동하여 더 빠르게 느껴짐
현재 FPS는 60으로 설정. 보통 60 FPS는 게임에 부드러운 움직임을 제공하는 적절한 값이며,
이 값을 낮추는 것은 게임의 전반적인 부드러움 해칠 수 있음
따라서 paddle_speed 조절하는 것이 가장 권장되는 방법

0531(토) 오후 2:34
paddle_speed = 10에서 5로 변경 시, 약간 느려서 답답함
그래서 8로 수정

0531(토) 오후 2:53
[오류 발생]
bricks[-1].color = brick_color # Rect 객체에 color 속성 추가(편의상)
    ^^^^^^^^^^^^^^^^
AttributeError: 'pygame.rect.Rect' object has no attribute 'color'

[생각]
기존에 작성한 코드가 Rect 객체에서 color 속성 추가 부분이 pygame.Rect 객체에 존재하지 않는 속성을
임의로 추가하려고 했기 때문에 문제가 발생했음. pygame.Rect는 충돌 감지와 위치/크기 정보를 담는 객체이지,
그리는 색상 정보를 직접 담는 객체는 아님

[해결 방법]
bricks 리스트에 pygame.Rect 객체만 저장하는 것이 아니라, 벽돌의 Rect 객체와 해당 별돌의 color를
함께 저장하도록 구조를 변경해야 된다. -> 튜플이나 딕셔너리 사용 -> 나는 튜플 사용해서 (Rect 객체, color) 형태로 저장
'''