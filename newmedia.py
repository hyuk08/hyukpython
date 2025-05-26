import pandas as pd

names = ["방재준", "한승혁", "최재훈", "윤건영", "안현준", 
         "박가린", "김예지", "정찬하", "김예원", "조수인"]

grades = ["2학년", "2학년", "2학년", "3학년", "2학년", 
          "2학년", "2학년", "2학년", "2학년", "3학년"]

majors = ["디지털아트"] * 10

df = pd.DataFrame({
    "이름": names,
    "학년": grades,
    "전공": majors
})


df.to_csv("newmedia.csv", index=False, encoding='utf-8-sig')


#pandas라는 라이브러리를 추가로 사용했습니다!