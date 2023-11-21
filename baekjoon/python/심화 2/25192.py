def gomgomi(n):
    gomgom = set()
    cnt = 0
    for _ in range(n):
        word = input()

        # ENTER가 아니고, 새로 접속한 사람이 아니면 횟수 증가
        if word != 'ENTER':
            gomgom.add(word)
        # ENTER이면, 기존에 접속한 회원 정보 초기화
        elif word == 'ENTER':
            cnt+=len(gomgom)
            gomgom.clear()
    cnt+=len(gomgom)
    return cnt


print(gomgomi(int(input())))