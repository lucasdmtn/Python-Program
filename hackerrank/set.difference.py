
english_number=int(input())
english_student= list(map(str,raw_input().split()))
french_number=int(input())
french_student = list(map(str,raw_input().split()))
print(len(set(english_student).difference(set(french_student))))