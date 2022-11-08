import re, random

with open('dict.txt', 'rt', encoding='utf-8') as f:
    s = f.read()

pat = re.compile('^[ㄱ-ㅎ가-힣]+$')
wordDict = dict()
hanbangSet = set()

# 한글로만 이루어져있고, 길이가 2 이상인 단어만 추출
for i in sorted([i for i in s.split() if pat.match(i) and len(i) >= 2], key=lambda x:-len(x)):
    if i[0] not in wordDict:
        wordDict[i[0]] = set()
    wordDict[i[0]].add(i)



print('\n 이겨볼테면 이겨봐라! GuPhaGO')
print(' Ctrl+Z를 입력하면 기권할 수 있습니다.')
round, win, lose = 0, 0, 0

while True:
    # 라운드 시작
    round += 1
    print("\n" + "-" * 50)
    print("\n %d라운드를 시작합니다. 현재 %d승 %d패" % (round, win, lose))
    lastWord = ''
    alreadySet = set()
    firstTurn = True
    resetRound = False

    while True:
        # CPU 턴
        print()
        if firstTurn:
            lastWord = random.choice(list(wordDict[random.choice(list(wordDict.keys()))]))
            alreadySet.add(lastWord)
            print(' CPU : ' + lastWord)
            firstTurn = False
        else:
            firstLetter = lastWord[-1]
            if not list(filter(lambda x: x not in alreadySet, wordDict.get(firstLetter, set()))):
                # 라운드 종료
                print(' CPU : ^Z')
                print('\n [결과] CPU가 기권했습니다. 당신의 승리입니다!')
                win += 1
                break
            else:
                nextWords = sorted(filter(lambda x: x not in alreadySet, wordDict[firstLetter]), key=lambda x:-len(x))[:random.randint(20, 50)]
                lastWord = nextWords[random.randint(0, random.randrange(0, len(nextWords)))]
                alreadySet.add(lastWord)
                print(' CPU : ' + lastWord)

        # 유저 턴
        while True:
            print()
            try:
                yourWord = input(' YOU : ')
            except:
                print('\n [결과] 당신은 기권했습니다. CPU의 승리입니다!')
                print(' [힌트] ', end='')
                print(', '.join(list(filter(lambda x: x not in alreadySet, wordDict.get(lastWord[-1], set())))[:3]))
                resetRound = True
                lose += 1
                break
            firstLetter = yourWord[0]
            if firstLetter != lastWord[-1]:
                print(" [오류] '" + lastWord[-1] + "' (으)로 시작하는 단어를 입력하세요.")
            elif yourWord in alreadySet:
                print(' [오류] 이미 나온 단어입니다.')
            elif yourWord not in wordDict.get(firstLetter, set()):
                print(' [오류] 사전에 없는 단어입니다.')
            else:
                alreadySet.add(yourWord)
                lastWord = yourWord
                break
        if resetRound:
            # 라운드 종료
            break