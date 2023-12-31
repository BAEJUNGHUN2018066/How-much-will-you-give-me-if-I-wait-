def calculate_future_value(매달_투자_금액, 연_이자율, 저축_기간, 매달마다_저축할_횟수):
    future_value = 0  # future_value 변수를 초기화합니다.

    for year in range(저축_기간):
        for month in range(12):
            future_value += 매달_투자_금액  # 매달 저축 금액을 더함

    future_value *= (1 + 연_이자율) * (매달마다_저축할_횟수/12)

    return future_value

은행 = input("은행을 선택하세요 (신한, 하나, 농협, 기업):")
은행별_정보 = {
    "신한": {"연_이자율": 0.055, "저축_기간": 3, "최대_투자_금액": 400000},
    "하나": {"연_이자율": 0.045, "저축_기간": 2, "최대_투자_금액": 300000},
    "농협": {"연_이자율": 0.06, "저축_기간": 4, "최대_투자_금액": 500000},
    "기업": {"연_이자율": 0.05, "저축_기간": 3, "최대_투자_금액": 500000}
}

if 은행 in 은행별_정보:
    은행정보 = 은행별_정보[은행]
    연_이자율 = 은행정보["연_이자율"]
    저축_기간 = 은행정보["저축_기간"]
    최대_투자_금액 = 은행정보["최대_투자_금액"]
    print(f"{은행} 은행, 저축기한은 {저축_기간}년입니다.")
else:
    print("지원하지 않는 은행입니다.")
    exit()

# 얼마를 넣을건지 입력값 받기
매달_투자_금액 = float(input(f"매달 얼마를 넣을건가요? (1 ~ {최대_투자_금액}원 사이):"))
if 1 <= 매달_투자_금액 <= 최대_투자_금액:
    매달마다_저축할_횟수 = int(input("1년에 몇 번 넣으실건가요?"))
    future_value = calculate_future_value(매달_투자_금액, 연_이자율, 저축_기간, 매달마다_저축할_횟수)
    print(f"{은행} 은행, {저축_기간}년 후의 적금 가치는 {future_value:.2f}원 입니다.")
else:
    print(f"1 ~ {최대_투자_금액}원 사이의 금액을 입력해야 합니다.")
