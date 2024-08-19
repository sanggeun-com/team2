import pandas as pd
import os

# 파일들이 위치한 폴더 경로 설정
folder_path = 'C:/Users/medici/project/전기차NEW/전기차등록현황/전처리중/2'  # 실제 폴더 경로로 변경하세요

# 폴더 내의 모든 CSV 파일에 대해 처리 수행
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):  # CSV 파일만 처리
        file_path = os.path.join(folder_path, filename)
        
        # CSV 파일 로드 (인코딩 설정)
        df = pd.read_csv(file_path, encoding='utf-8')
        
        # "용도별" 컬럼의 내용이 빈칸(NULL)인 행 모두 삭제
        df_cleaned = df.dropna(subset=['용도별'])
        
        # 결과 저장 경로 설정 (파일 이름에 '_cleaned' 추가)
        output_file_path = os.path.join(folder_path, filename.replace('.csv', '_cleaned.csv'))
        
        # 처리된 데이터 저장
        df_cleaned.to_csv(output_file_path, index=False, encoding='utf-8-sig')
        
        print(f"Processed and saved: {output_file_path}")
