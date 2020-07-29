from django.shortcuts import render
from .models import Symptoms
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse
# from rest_framework.parsers import JSONParsers
from .serializers import SymptomsSerializers
import pickle
from django.contrib import messages
import joblib
import json
import numpy as np
import pandas as pd
from sklearn import preprocessing
from .forms import PredictorForm


class PredictorView(viewsets.ModelViewSet):
    queryset = Symptoms.objects.all()
    serializer_class = SymptomsSerializers

# @api_view(["POST"])


def DiseasePredictor(unit):
    try:
        model = joblib.load(
            "/Users/Saifur Rehman/Documents/disease_predictor/research/random_forest.joblib")
        # mydata = request.data
        unit = np.array(list(unit.values()))
        unit = unit.reshape(1, -1)
        # print(unit)
        y_pred = model.predict(unit)
        # print("Hello world", y_pred)
        le = joblib.load(
            "/Users/Saifur Rehman/Documents/disease_predictor/research/encoder.joblib")
        disease = le.inverse_transform(y_pred)
        print(disease[0])
        return disease[0]
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def SymptomInput(request):
    if request.method == "POST":
        form = PredictorForm(request.POST)
        if form.is_valid():
            itching = form.cleaned_data['itching']
            skin_rash = form.cleaned_data['skin_rash']
            nodal_skin_eruptions = form.cleaned_data['nodal_skin_eruptions']
            continuous_sneezing = form.cleaned_data['continuous_sneezing']
            shivering = form.cleaned_data['shivering']
            chills = form.cleaned_data['chills']
            joint_pain = form.cleaned_data['joint_pain']
            stomach_pain = form.cleaned_data['stomach_pain']
            acidity = form.cleaned_data['acidity']
            ulcers_on_tongue = form.cleaned_data['ulcers_on_tongue']
            muscle_wasting = form.cleaned_data['muscle_wasting']
            vomiting = form.cleaned_data['vomiting']
            burning_micturition = form.cleaned_data['burning_micturition']
            spotting_urination = form.cleaned_data['spotting_urination']
            fatigue = form.cleaned_data['fatigue']
            weight_gain = form.cleaned_data['weight_gain']
            anxiety = form.cleaned_data['anxiety']
            cold_hands_and_feets = form.cleaned_data['cold_hands_and_feets']
            mood_swings = form.cleaned_data['mood_swings']
            weight_loss = form.cleaned_data['weight_loss']
            restlessness = form.cleaned_data['restlessness']
            lethargy = form.cleaned_data['lethargy']
            patches_in_throat = form.cleaned_data['patches_in_throat']
            irregular_sugar_level = form.cleaned_data['irregular_sugar_level']
            cough = form.cleaned_data['cough']
            high_fever = form.cleaned_data['high_fever']
            sunken_eyes = form.cleaned_data['sunken_eyes']
            breathlessness = form.cleaned_data['breathlessness']
            sweating = form.cleaned_data['sweating']
            dehydration = form.cleaned_data['dehydration']
            indigestion = form.cleaned_data['indigestion']
            headache = form.cleaned_data['headache']
            yellowish_skin = form.cleaned_data['yellowish_skin']
            dark_urine = form.cleaned_data['dark_urine']
            nausea = form.cleaned_data['nausea']
            loss_of_appetite = form.cleaned_data['loss_of_appetite']
            pain_behind_the_eyes = form.cleaned_data['pain_behind_the_eyes']
            back_pain = form.cleaned_data['back_pain']
            constipation = form.cleaned_data['constipation']
            abdominal_pain = form.cleaned_data['abdominal_pain']
            diarrhoea = form.cleaned_data['diarrhoea']
            mild_fever = form.cleaned_data['mild_fever']
            yellow_urine = form.cleaned_data['yellow_urine']
            yellowing_of_eyes = form.cleaned_data['yellowing_of_eyes']
            acute_liver_failure = form.cleaned_data['acute_liver_failure']
            fluid_overload = form.cleaned_data['fluid_overload']
            swelling_of_stomach = form.cleaned_data['swelling_of_stomach']
            swelled_lymph_nodes = form.cleaned_data['swelled_lymph_nodes']
            malaise = form.cleaned_data['malaise']
            blurred_and_distorted_vision = form.cleaned_data['blurred_and_distorted_vision']
            phlegm = form.cleaned_data['phlegm']
            throat_irritation = form.cleaned_data['throat_irritation']
            redness_of_eyes = form.cleaned_data['redness_of_eyes']
            sinus_pressure = form.cleaned_data['sinus_pressure']
            runny_nose = form.cleaned_data['runny_nose']
            congestion = form.cleaned_data['congestion']
            chest_pain = form.cleaned_data['chest_pain']
            weakness_in_limbs = form.cleaned_data['weakness_in_limbs']
            fast_heart_rate = form.cleaned_data['fast_heart_rate']
            pain_during_bowel_movements = form.cleaned_data['pain_during_bowel_movements']
            pain_in_anal_region = form.cleaned_data['pain_in_anal_region']
            bloody_stool = form.cleaned_data['bloody_stool']
            irritation_in_anus = form.cleaned_data['irritation_in_anus']
            neck_pain = form.cleaned_data['neck_pain']
            dizziness = form.cleaned_data['dizziness']
            cramps = form.cleaned_data['cramps']
            bruising = form.cleaned_data['bruising']
            obesity = form.cleaned_data['obesity']
            swollen_legs = form.cleaned_data['swollen_legs']
            swollen_blood_vessels = form.cleaned_data['swollen_blood_vessels']
            puffy_face_and_eyes = form.cleaned_data['puffy_face_and_eyes']
            enlarged_thyroid = form.cleaned_data['enlarged_thyroid']
            brittle_nails = form.cleaned_data['brittle_nails']
            swollen_extremeties = form.cleaned_data['swollen_extremeties']
            excessive_hunger = form.cleaned_data['excessive_hunger']
            extra_marital_contacts = form.cleaned_data['extra_marital_contacts']
            drying_and_tingling_lips = form.cleaned_data['drying_and_tingling_lips']
            slurred_speech = form.cleaned_data['slurred_speech']
            knee_pain = form.cleaned_data['knee_pain']
            hip_joint_pain = form.cleaned_data['hip_joint_pain']
            muscle_weakness = form.cleaned_data['muscle_weakness']
            stiff_neck = form.cleaned_data['stiff_neck']
            swelling_joints = form.cleaned_data['swelling_joints']
            movement_stiffness = form.cleaned_data['movement_stiffness']
            spinning_movements = form.cleaned_data['spinning_movements']
            loss_of_balance = form.cleaned_data['loss_of_balance']
            unsteadiness = form.cleaned_data['unsteadiness']
            weakness_of_one_body_side = form.cleaned_data['weakness_of_one_body_side']
            loss_of_smell = form.cleaned_data['loss_of_smell']
            bladder_discomfort = form.cleaned_data['bladder_discomfort']
            foul_smell_of = form.cleaned_data['foul_smell_of']
            continuous_feel_of_urine = form.cleaned_data['continuous_feel_of_urine']
            passage_of_gases = form.cleaned_data['passage_of_gases']
            internal_itching = form.cleaned_data['internal_itching']
            toxic_look_typhos = form.cleaned_data['toxic_look_typhos']
            depression = form.cleaned_data['depression']
            irritability = form.cleaned_data['irritability']
            muscle_pain = form.cleaned_data['muscle_pain']
            altered_sensorium = form.cleaned_data['altered_sensorium']
            red_spots_over_body = form.cleaned_data['red_spots_over_body']
            belly_pain = form.cleaned_data['belly_pain']
            abnormal_menstruation = form.cleaned_data['abnormal_menstruation']
            dischromic_patches = form.cleaned_data['dischromic_patches']
            watering_from_eyes = form.cleaned_data['watering_from_eyes']
            increased_appetite = form.cleaned_data['increased_appetite']
            polyuria = form.cleaned_data['polyuria']
            family_history = form.cleaned_data['family_history']
            mucoid_sputum = form.cleaned_data['mucoid_sputum']
            rusty_sputum = form.cleaned_data['rusty_sputum']
            lack_of_concentration = form.cleaned_data['lack_of_concentration']
            visual_disturbances = form.cleaned_data['visual_disturbances']
            receiving_blood_transfusion = form.cleaned_data['receiving_blood_transfusion']
            receiving_unsterile_injections = form.cleaned_data['receiving_unsterile_injections']
            coma = form.cleaned_data['coma']
            stomach_bleeding = form.cleaned_data['stomach_bleeding']
            distention_of_abdomen = form.cleaned_data['distention_of_abdomen']
            history_of_alcohol_consumption = form.cleaned_data['history_of_alcohol_consumption']
            fluid_overload_1 = form.cleaned_data['fluid_overload_1']
            blood_in_sputum = form.cleaned_data['blood_in_sputum']
            prominent_veins_on_calf = form.cleaned_data['prominent_veins_on_calf']
            palpitations = form.cleaned_data['palpitations']
            painful_walking = form.cleaned_data['painful_walking']
            pus_filled_pimples = form.cleaned_data['pus_filled_pimples']
            blackheads = form.cleaned_data['blackheads']
            scurring = form.cleaned_data['scurring']
            skin_peeling = form.cleaned_data['skin_peeling']
            silver_like_dusting = form.cleaned_data['silver_like_dusting']
            small_dents_in_nails = form.cleaned_data['small_dents_in_nails']
            inflammatory_nails = form.cleaned_data['inflammatory_nails']
            blister = form.cleaned_data['blister']
            red_sore_around_nose = form.cleaned_data['red_sore_around_nose']
            yellow_crust_ooze = form.cleaned_data['yellow_crust_ooze']
            myDict = (request.POST).dict()
            features = joblib.load(
                "/Users/Saifur Rehman/Documents/disease_predictor/research/features.joblib")
            data = {}

            for each in features:
                if myDict.get(each) == "on":
                    data[each] = True
                else:
                    data[each] = False
            # print(data)

            # print(features)
            # data = pd.DataFrame(myDict)
            # print(data)
            prediction = DiseasePredictor(data)
            messages.success(
                request, 'Predicted disease is: {}'.format(prediction))

    form = PredictorForm()

    return render(request, "Home/home.html", {'form': form})


# source env/Scripts/activate
