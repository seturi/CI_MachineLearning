def survival_classifier(seat_belt, highway, speed, age):
    # 코드를 쓰세요
    # 질문 노드: 안전 벨트를 했나요?
    if seat_belt:
        return 0  # 했으면 생존 리턴
    else:
        # 질문 노드: 사고가 고속도로였나요?
        if highway:
            # 질문 노드: 시속 100km를 넘었나요?
            if speed > 100:
                # 질문 노드: 사고자 나이가 50을 넘었나요?
                if age > 50:
                    return 1  # 사고자 나이가 50을 넘었으면 사망 리턴
                else:
                    return 0  # 사고자 나이가 50을 넘지 않았다면 생존 리턴
            else:
                return 0  # 시속 100km를 넘지 않았다면 생존 리턴
        else:  
            return 0  # 고속도로가 아니였다면 생존 리턴

print(survival_classifier(False, True, 110, 55))
print(survival_classifier(True, False, 40, 70))
print(survival_classifier(False, True, 80, 25))
print(survival_classifier(False, True, 120, 60))
print(survival_classifier(True, False, 30, 20))