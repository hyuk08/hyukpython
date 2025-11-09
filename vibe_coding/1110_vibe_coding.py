"""
Vibe Coding - Python 데모 프로그램
다양한 Python 기능을 보여주는 예제입니다.
"""

import datetime
import json
from typing import List, Dict

def greet(name: str = "Vibe Coding") -> str:
    """인사말을 반환하는 함수"""
    return f"안녕하세요, {name}님!"

def calculate_sum(numbers: List[int]) -> int:
    """숫자 리스트의 합을 계산"""
    return sum(numbers)

def create_user_info(name: str, age: int, hobbies: List[str]) -> Dict:
    """사용자 정보 딕셔너리를 생성"""
    return {
        "name": name,
        "age": age,
        "hobbies": hobbies,
        "created_at": datetime.datetime.now().isoformat()
    }

def main():
    """메인 함수 - 다양한 기능을 실행"""
    print("=" * 50)
    print(greet("코딩하는 당신"))
    print("=" * 50)
    
    # 숫자 계산 예제
    numbers = [1, 2, 3, 4, 5, 10, 20]
    total = calculate_sum(numbers)
    print(f"\n[계산] 숫자 리스트 {numbers}의 합: {total}")
    
    # 사용자 정보 생성 예제
    user = create_user_info(
        name="개발자",
        age=25,
        hobbies=["코딩", "음악", "독서"]
    )
    print(f"\n[사용자 정보]")
    print(json.dumps(user, indent=2, ensure_ascii=False))
    
    # 리스트 컴프리헨션 예제
    squares = [x**2 for x in range(1, 6)]
    print(f"\n[제곱수] 1부터 5까지의 제곱수: {squares}")
    
    # 딕셔너리 컴프리헨션 예제
    word_lengths = {word: len(word) for word in ["Python", "코딩", "프로그래밍"]}
    print(f"\n[단어 길이] {word_lengths}")
    
    print("\n" + "=" * 50)
    print("[완료] 이 파일은 AI가 자동으로 생성했습니다!")
    print("=" * 50)

if __name__ == "__main__":
    main()
