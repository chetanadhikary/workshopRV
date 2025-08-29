import pandas as pd
import streamlit as st
import shelve

with shelve.open("models_data/models") as md:
    model_sgd = md["SGD"]
    model_tree = md["Decision_Tree"]
    model_forest = md["Random_Forest"]

st.title("Diabetes :blue[Prediction]:sunglasses:")

with st.form("status"):
    pregnancy_in = st.slider(
        label="Select number of pregnancies",
        min_value=0,
        max_value=20,
        step=1
    )

    glucose_in = st.slider(
        label="Select Glucose Plasma Value",
        min_value=0,
        max_value=200,
        step=1,
    )

    bp_in = st.slider(
        label="Select Blood Pressure Value",
        min_value=0,
        max_value=125,
        step=1,
    )

    skin_thick_in = st.slider(
        label="Select Skin Thickness Value",
        min_value=0,
        max_value=99,
        step=1,
    )

    insulin_in = st.slider(
        label="Select Insulin Value",
        min_value=0,
        max_value=850,
        step=1,
    )

    bmi_in = st.slider(
        label="Select BMI Value",
        min_value=0.0,
        max_value=70.0,
        step=0.1,
    )

    pedigree_in = st.slider(
        label="Select Diabetes Pedigree Function Value",
        min_value=0.0,
        max_value=2.5,
        step=0.001,
    )

    age_in = st.slider(
        label="Select Age ",
        min_value=1,
        max_value=120,
        step=1,
    )

    model_sel = st.selectbox(
        label="Select Your Model",
        options=["SGD Model",
                 "Decision Tree Model",
                 "Random Forest Model"],
        index=None
    )

    btn_submit = st.form_submit_button("Submit")

dict_models = {"SGD Model": model_sgd,
               "Decision Tree Model": model_tree,
               "Random Forest Model": model_forest}


def format_input_val(**kwargs):
    dict_model_inputs = {key: [val]
                         for key, val in kwargs.items()
                         }
    return pd.DataFrame.from_dict(dict_model_inputs)


if btn_submit and (model_sel is not None):
    st.write(f"You selected {model_sel}")
    st.write(dict_models[model_sel])
    input_df = format_input_val(
        pedi=pedigree_in,
        insu=insulin_in,
        plas=glucose_in,
        age=age_in,
        pres=bp_in,
        mass=bmi_in,
        skin=skin_thick_in,
        preg=pregnancy_in,
    )
    st.write(input_df)
    predicted = (
        "Diabetic"
        if dict_models[model_sel].predict(input_df)
        else
        "Non-Diabetic"
    )
    st.write(predicted)
else:
    st.write("Select a model to predict")
