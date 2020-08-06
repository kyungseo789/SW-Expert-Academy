import base64
T = int(input())
def base64_string(txt):
    return base64.b64decode(txt).decode('utf-8')

for t in range(1, T+1):
    word = input()
    answer = base64_string(word)   
    
    print(f'#{t} {answer}')