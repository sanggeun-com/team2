import os
import glob
import pandas as pd

# 파일이 위치한 폴더 경로 설정
folder_path = 'C:/Users/medici/project/전기차NEW/전기차등록현황/'  # 실제 폴더 경로로 변경하세요

# 폴더 내의 모든 CSV 파일에 대해 작업을 수행
for file_path in glob.glob(os.path.join(folder_path, '*.csv')):
    try:
        # CSV 파일 로드 (인코딩 설정)
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        print(f"Error reading {file_path} with utf-8 encoding. Trying with cp949.")
        try:
            df = pd.read_csv(file_path, encoding='cp949')
        except UnicodeDecodeError:
            print(f"Failed to read {file_path} with both utf-8 and cp949 encoding. Skipping this file.")
            continue
    
    # 현재 데이터 프레임의 열 개수 확인
    print(f"{file_path} - columns count: {len(df.columns)}")

    # 새로운 컬럼 이름 리스트 설정
    new_columns = [
        '연료별', '차종별', '용도별', '서울', '부산', '대구', '인천', '광주', '대전', '울산',
        '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '계', 'Unnamed'
    ]

    # 현재 데이터 프레임의 열 수와 새로운 컬럼 리스트의 길이를 비교
    if len(df.columns) == len(new_columns):
        df.columns = new_columns
    else:
        print(f"Skipping {file_path} due to column length mismatch.")
        continue
    
    # 1행부터 3행 삭제 (index는 0부터 시작하므로 0, 1, 2번 인덱스의 행을 삭제)
    df = df.drop([0, 1, 2]).reset_index(drop=True)
    
    # 처리된 데이터 저장 (원본 파일 이름에 '_processed'를 추가)
    output_file_path = os.path.join(folder_path, os.path.splitext(os.path.basename(file_path))[0] + '_processed.csv')
    df.to_csv(output_file_path, index=False, encoding='utf-8-sig')
    
    print(f"Processed and saved: {output_file_path}")
