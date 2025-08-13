import streamlit as st
from langdetect import detect
from PIL import Image
import pytesseract

# AI ықтималдығын есептейтін функция
def compute_ai_likelihood(text):
    ai_keywords = ['model', 'algorithm', 'data', 'neural', 'network', 'training', 'learning']
    text = text.lower()
    count = 0
    for word in ai_keywords:
        if word in text:
            count += 1
    likelihood = count / len(ai_keywords)
    return likelihood

# Streamlit интерфейсі
st.title("AI Detector")
st.write("Қазақша, орысша және ағылшынша мәтіндер үшін AI ықтималдығын тексеру")

# Мәтінді тексеру
user_text = st.text_area("Мәтінді енгізіңіз:")
if user_text:
    try:
        lang = detect(user_text)
        st.write(f"Тіл анықталды: {lang}")
    except:
        st.write("Тілді анықтау мүмкін болмады")
    
    score = compute_ai_likelihood(user_text)
    st.write(f"AI ықтималдығы: {score*100:.1f}%")
    if score > 0.5:
        st.write("Бұл мәтін AI арқылы жазылған болуы мүмкін.")
    else:
        st.write("Бұл мәтін адамның жазғанына ұқсайды.")

# Суреттен мәтін шығару және тексеру
uploaded_file = st.file_uploader("Суретті жүктеңіз", type=["png","jpg","jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Жүктелген сурет', use_column_width=True)
    text_from_image = pytesseract.image_to_string(image)
    st.write("Суреттен алынған мәтін:")
    st.write(text_from_image)
    
    score_img = compute_ai_likelihood(text_from_image)
    st.write(f"AI ықтималдығы сурет мәтіні үшін: {score_img*100:.1f}%")
    if score_img > 0.5:
        st.write("Бұл мәтін AI арқылы жазылған болуы мүмкін.")
    else:
        st.write("Бұл мәтін адамның жазғанына ұқсайды.")

