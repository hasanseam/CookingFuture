


testCase = int(input())

for i in range(testCase):
    feedbackString = input()

    if feedbackString.find("010")!=-1 or feedbackString.find("101")!=-1:
        print ("Good")
    else:
        print("Bad")