"""
데이터 파일을 불러오기 위해서는 pandas 라이브러리 이용
pandas import 후, read_csv 함수 사용하여 csv 파일 불러오기
"""

import pandas as pd
data = pd.read_csv('파일경로/파일이름.csv')

# 문제 ------------------------------
# data 폴더에 있는 test.csv 파일과 train.csv 파일을 불러와 보세요.

import pandas as pd

train = 'data 폴더에있는 train.csv 파일 불러오는 코드 작성'
test = 'data 폴더에있는 test.csv 파일 불러오는 코드 작성'

# 답 --------------------------------

import pandas as pd

train = pd.read_csv('data/train.csv') 
test = pd.read_csv('data/test.csv')

