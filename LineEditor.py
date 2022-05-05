List = []
def Line_Editor(List):
    a = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ")
    if a == 'i':
        b = input("입력행 번호 : ")
        c = input("입력행 내용 : ")
        List.insert(int(b), str(c))
        Line_Editor(List)
    elif a == 'p':
        print(List)

"""정답
while문 True로 무한반복 돌리기"""