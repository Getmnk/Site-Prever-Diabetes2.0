import pickle
import pandas as pd
import streamlit as st
import numpy as py

pickle_in = open("diabete.pkl", "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Bem-vindo ao Previsor de Diabete"

def predict_disease(HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age):
    """Função para prever a diabete com base nas entradas do usuário.
    
    Args:
        HighBP (int): pressão alta do usuário.
        HighChol (int): colesterol alta do usuário.
        CholCheck (int): colesterol checado do usuário.
        BMI (int): imc do usuario.
        Smoker (int): usuário fuma ou não.
        Stroke (int): usuário já teve avc.
        HeartDiseaseorAttack (int): coração do usuário.
        PhysActivity (int): atividas fisicas do usuário.
        Fruits (int): usuário come frutas.
        Veggies (int): usuário come vegetais
        HvyAlcoholConsump (int): usuário bebe muito alcool.
        AnyHealthcare (int): usuário tem plano de saúde.
        NoDocbcCost (int): usuário queria ir no medico, mas não pode por conta do preço.
        GenHlth (int): saúde geral do usuário.
        MentHlth (int): saúde mental do usuário.
        PhysHlth (int): dor fisica do usuário.
        DiffWalk (int): dificuldade andar do usuário.
        Sex (int): sexo do usuário.
        Age (int): idade do usuário.
        
    Returns:
        prediction: Resultado da previsão.
    """
    prediction = classifier.predict([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age]])
    return prediction

def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Aplicativo de Previsão de Diabetes (TESTE)</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
  
    HighBP = st.selectbox("Tem pressão alta?", ["Não", "Sim"])
    HighChol = st.selectbox("Tem colesterol alta?", ["Não", "Sim"])
    CholCheck = st.selectbox("Teve seu colesterol checado nos ultimos 5 anos?", ["Não", "Sim"])
    BMI = st.number_input("Seu IMC?", min_value=12, max_value=98, step=1)
    Smoker = st.selectbox("Você já fumou 5 pacotes de cigarro durante a vida?", ["Não", "Sim"])
    Stroke = st.selectbox("Você já teve um AVC?", ["Não", "Sim"])
    HeartDiseaseorAttack = st.selectbox("Você tem Doença arterial coronariana ou já teve ataque do coração?", ["Não", "Sim"])
    PhysActivity = st.selectbox("Você se exercitou nos ultimos 30 dias (não incluindo trabalho)?", ["Não", "Sim"])
    Fruits = st.selectbox("Você consome alguma fruta uma ou mais vezes por dia?", ["Não", "Sim"])
    Veggies = st.selectbox("Você consome algum vegetal uma ou mais vezes por dia?", ["Não", "Sim"])
    HvyAlcoholConsump = st.selectbox("Você consome bastante alcool?", ["Não", "Sim"])
    AnyHealthcare = st.selectbox("Você tem plano de saúde?", ["Não", "Sim"])
    NoDocbcCost = st.selectbox("Você já quis ir no médico, mas não conseguiu por conta do preço?", ["Não", "Sim"])
    GenHlth = st.number_input("Sua saúde geral? 1 = excelente, 2 = muito boa, 3 = boa, 4 = normal, 5 = ruim", min_value=1, max_value=5, step=1)
    MentHlth = st.number_input("Dias de saúde mental ruim?", min_value=0, max_value=30, step=1)
    PhysHlth = st.number_input("Dias de doença física ou lesão nos últimos 30 dias?", min_value=0, max_value=30, step=1)
    DiffWalk = st.selectbox("Você tem uma grande dificuldade de andar ou subir escadas?", ["Não", "Sim"])
    Sex = st.selectbox("Seu Sexo?", ["Feminino", "Masculino"])
    Age = st.number_input("Sua idade? 1 = 18-24, 2 = 25-29, 3 = 30-34, 4 = 35-39, 5 = 40-44, 6 = 45-49, 7 = 50-54, 8 = 55-59, 9 = 60-64, 10 = 65-69, 11 = 70-74, 12 = 75-79, 13 = 80+", min_value=1, max_value=13, step=1)


    HighBP = 0 if HighBP == "Não" else 1
    HighChol = 0 if HighChol == "Não" else 1
    CholCheck = 0 if CholCheck == "Não" else 1
    Smoker = 0 if Smoker == "Não" else 1
    Stroke = 0 if Stroke == "Não" else 1
    HeartDiseaseorAttack = 0 if HeartDiseaseorAttack == "Não" else 1
    PhysActivity = 0 if PhysActivity == "Não" else 1
    Fruits = 0 if Fruits == "Não" else 1
    Veggies = 0 if Veggies == "Não" else 1
    HvyAlcoholConsump = 0 if HvyAlcoholConsump == "Não" else 1
    AnyHealthcare = 0 if AnyHealthcare == "Não" else 1
    NoDocbcCost = 0 if NoDocbcCost == "Não" else 1
    Stroke = 0 if Stroke == "Não" else 1
    HeartDiseaseorAttack = 0 if HeartDiseaseorAttack == "Não" else 1
    PhysActivity = 0 if PhysActivity == "Não" else 1
    DiffWalk = 0 if DiffWalk == "Não" else 1
    Sex = 0 if Sex == "Feminino" else 1
  
    if st.button("Prever"):
        result = predict_disease(HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age)
        st.success('Resultado da previsão: {}'.format("Sim" if result[0] == 1 else "Não"))

   
if __name__ == '__main__':
    main()

