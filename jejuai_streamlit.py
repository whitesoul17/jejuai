import requests
import streamlit as st

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "161f34e0-974b-11ef-994e-b7bbb9cee7dd8faa499b-e5cb-4bc3-8657-afbb5c7f7da8"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
while True:
    #qu = input("제주도에 대해 궁금한 것을 물어봐 주세요>>")
    qu = st.text_input("저희 회사에 대해 궁금한 것을 저에게 물어보세요! 질문이 끝나시면 '나가기'를 입력해주세요.>>")
    if len(qu)>0:
        if qu == '나가기':
            break

        demo = classify(qu)

        label = demo["class_name"]
        confidence = demo["confidence"]

        #if confidence<70:
            #st.write("질문을 이해하지 못했어요. 다시 질문해 주시겠어요?")
        #elif label == "Food":
            #st.write("제주도라면 고기국수를 먹어보세요. 어디든 다 맛있답니다.유명 흑돼지집에서 흑돼지고기를 먹어보는 것도 좋겠어요")
        #elif label == "Cafe":
            #st.write("애월에는 예쁘고 유명한 카페들이 많아요. 어디든 전망도 좋고 커피도 맛있으니 그 중에서 골라보세요. 참, 요즘에 도넛집도 핫하다고 해요")
        #elif label == "Hot_Place":
            #st.write("제주도에서 올레길 한번은 걸어보는 것도 좋겠죠? 저녁엔 야시장을 둘러 보는 것도 추천해요. 무엇보다 제주하면 바다죠? 예쁜 세화해변도 추천해요")
        # CHANGE THIS to do something different with the result
        st.write ("result: '%s' with %d%% confidence" % (label, confidence))
     else 
        input("검색어를 입력해 주세요")
    while True:
        ans_qu()    
