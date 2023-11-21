# n = int(input())
# n_cards = list(input().split())
# n_dict = {n_card: True for n_card in n_cards}

# m = int(input())
# m_cards = list(input().split())

# print(n_dict)
# for m_card in m_cards:
#     try:
#         n_dict[m_card] 
#         print(1, end=' ')
#     except:
#         print(0, end=' ')

# n = int(input())
# n_cards = list(input().split())
# n_dict = {n_card: True for n_card in n_cards}

# m = int(input())
# m_cards = list(input().split())

# print(n_dict)
# for m_card in m_cards:
#     if n_dict.get(m_card) == True:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')



n = int(input())
n_cards = list(input().split())
n_cards.sort()

m = int(input())
m_cards = list(input().split())

for m_card in m_cards:
    flag=True
    start = 0
    end = len(n_cards)-1

    while start<=end:
        mid=(start+end)//2

        if n_cards[mid]==m_card:
            print(1, end=' ')
            flag = False
            break
        elif n_cards[mid] < m_card:
            start=mid+1
        else:
            end=mid-1

    if flag:
        print(0, end=' ')



