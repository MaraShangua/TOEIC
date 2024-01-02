import pandas as pd
import re
import random

def excel():
    # 엑셀 파일 경로
    excel_file_path = 'TOEIC.xlsx'

    # 읽어올 특정 행의 인덱스
    selected_row_index = random.randint(1,1159)  # 예시로 첫 번째 행을 선택

    # 가져올 특정 열의 이름
    selected_eng = '단어'  # 실제 열 이름으로 변경
    selected_kor = '뜻' 

    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file_path)

    # 특정 인덱스의 행 가져오기
    selected_row = df.iloc[selected_row_index]


    # 간추리기

    # 특정 열의 값을 가져오기
    eng_value = selected_row[selected_eng]
    kor_value = selected_row[selected_kor]

    mean_kor= extract_values_inside_brackets(kor_value)

    if mean_kor:
        # mean_kor 리스트가 비어 있지 않은 경우에만 접근
        return [eng_value, mean_kor[0]]
    else:
        # 리스트가 비어 있을 때 처리할 내용
        return [eng_value, "No Meanings"]

def extract_values_inside_brackets(input_string):
    # 정규식 패턴
    pattern = re.compile(r'\[([^\]]+)\]')

    # 정규식과 매치되는 부분 찾기
    matches = pattern.findall(input_string)

    return matches