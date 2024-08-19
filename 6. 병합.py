import pandas as pd
import os

# 파일들이 위치한 폴더 경로 설정
folder_path = 'C:/Users/medici/project/전기차NEW/전기차등록현황/전처리중/5'  # 실제 폴더 경로로 변경하세요

# 병합된 데이터를 저장할 빈 데이터프레임 생성
merged_df = pd.DataFrame()

# 폴더 내의 모든 CSV 파일에 대해 처리 수행
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):  # CSV 파일만 처리
        file_path = os.path.join(folder_path, filename)
        
        # CSV 파일 로드 (인코딩 설정)
        df = pd.read_csv(file_path, encoding='utf-8')
        
        # 기존 병합된 데이터프레임과 현재 데이터프레임을 병합
        merged_df = pd.concat([merged_df, df], axis=0, ignore_index=True)

# 결과 저장 경로 설정
output_file_path = os.path.join(folder_path, 'merged_data.csv')

# 병합된 데이터 저장
merged_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')

print(f"All files merged and saved as: {output_file_path}")
