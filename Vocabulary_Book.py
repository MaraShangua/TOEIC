import pygame
import sys
import random

pygame.init()

#화면 설정
width, height = 500, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Button Example")


#폰트 설정
# 나눔고딕 폰트 경로 설정
font_path = "C:\\Ab3l\\NanumGothic.ttf"
font = pygame.font.Font(font_path, 24)

white = (255, 255, 255)
black = (0, 0, 0)

# 단어 리스트
words = {"apple": "사과", "banana": "바나나", "orange": "오렌지"}
words_li = list(words.keys())

# 버튼 클래스 정의
class Button:
    def __init__(self, rect, color, hover_color, text, text_color, callback):
        self.rect = rect
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.callback = callback
        self.hovered = False

    def draw(self):
        pygame.draw.rect(screen, self.hover_color if self.hovered else self.color, self.rect)

        font = pygame.font.Font(font_path, 24)  # 폰트 생성
        text_surface = font.render(self.text, True, self.text_color)  # 텍스트 렌더링
        text_rect = text_surface.get_rect(center=self.rect.center)  # 텍스트 위치 조정
        screen.blit(text_surface, text_rect)  # 화면에 텍스트 그리기

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.callback()

def pra():
    # 화면 설정
    screen_width, screen_height = 600, 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("타자 연습 게임")

    # 버튼 생성
    button_rect = pygame.Rect(300, 200, 100, 50)

    button = Button(button_rect, (0, 128, 255), (0, 200, 255), "돌아가기", white, game)

    # 게임 상태
    current_word = random.choice(words_li)
    input_text = ""
    score = 0

    # 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text == current_word:
                        score += 1
                        current_word = random.choice(words_li)
                        input_text = ""
                else:
                    input_text += event.unicode
            
            button.handle_event(event)

        screen.fill(black)

        # 버튼 그리기
        button.draw()

        # 현재 단어와 입력 중인 텍스트 표시
        current_word_surface = font.render(current_word, True, white)
        current_word_kr_surface = font.render(words[current_word], True, white)
        input_text_surface = font.render(input_text, True, white)
        screen.blit(current_word_surface, (100, 100))
        screen.blit(current_word_kr_surface, (400,100))
        screen.blit(input_text_surface, (100, 200))

        # 스코어 표시
        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def test():
    # 화면 설정
    screen_width, screen_height = 500, 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("타자 연습 게임")

    # 버튼 생성
    button_rect = pygame.Rect(300, 200, 100, 50)

    button = Button(button_rect, (0, 128, 255), (0, 200, 255), "돌아가기", white, game)


    # 게임 상태
    current_word = random.choice(words_li)
    input_text = ""
    score = 0

    # 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text == current_word:
                        score += 1
                        current_word = random.choice(words_li)
                        input_text = ""
                else:
                    input_text += event.unicode
            button.handle_event(event)

        screen.fill(black)

        # 버튼 그리기
        button.draw()

        # 현재 단어와 입력 중인 텍스트 표시
        current_word_kr_surface = font.render(words[current_word], True, white)
        input_text_surface = font.render(input_text, True, white)
        screen.blit(current_word_kr_surface, (100,100))
        screen.blit(input_text_surface, (100, 200))

        # 스코어 표시
        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def game():

    # 화면 설정
    width, height = 500, 300
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Button Example")

    # 버튼 생성
    button_rect = pygame.Rect(300, 150, 70, 50)
    button_rect_2 = pygame.Rect(400, 150, 70, 50)

    button = Button(button_rect, (0, 128, 255), (0, 200, 255), "연습", white, pra)
    button_2 = Button(button_rect_2, (0, 128, 255), (0, 200, 255), "영어", white, test)    

    # 이벤트 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button.handle_event(event)
            button_2.handle_event(event)

        # 버튼 그리기
        button.draw()
        button_2.draw()

        # 화면 업데이트
        pygame.display.flip()

    pygame.quit()
    sys.exit()

game()

pygame.quit()
sys.exit()