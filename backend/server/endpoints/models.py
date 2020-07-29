from django.db import models

class Symptoms(models.Model):
    SYMPTOMS_CHOICES1 = (
        ('itching','Itching'),
        ('skin_rash','Skin rash'),
        ('nodal_skin_eruptions', 'Nodal skin eruptions'),
        ('continuous_sneezing','Continuous sneezing'),
        ('shivering','Shivering'),
        ('chills','Chills'),
        ('joint_pain','Joint pain'),
        ('stomach_pain','Stomach Pain' ),
        ('acidity','Acidity'),
        ('ulcers_on_tongue','ulcers_on_tongue'),
        ('muscle_wasting','muscle_wasting'),
        ('vomiting','vomiting'),
        ('burning_micturition','burning_micturition'),
        ('spotting_ urination','spotting_ urination'),
        ('fatigue','fatigue'),
        ('weight_gain','weight_gain'),
        ('anxiety','anxiety'),
        ('cold_hands_and_feets','cold_hands_and_feets'),
        ('mood_swings','mood_swings'),
        ('weight_loss','weight_loss'),
        ('restlessness','restlessness')
    ) 
    SYMPTOMS_CHOICES2 = (
        ('lethargy','lethargy'),
        ('patches_in_throat','patches_in_throat'),
        ('irregular_sugar_level'),
        ('cough','cough'),
        ('high_fever','high_fever'),
        ('sunken_eyes','sunken_eyes'),
        ('breathlessness','breathlessness'),
        ('sweating','sweating'),
        ('dehydration','dehydration'),
        ('indigestion','indigestion'),
        ('headache','headache'),
        ('yellowish_skin','yellowish_skin'),
        ('dark_urine','dark_urine'),
        ('nausea','nausea'),
        ('loss_of_appetite','loss_of_appetite'),
        ('pain_behind_the_eyes','pain_behind_the_eyes'),
        ('back_pain','back_pain'),
        ('constipation','constipation'),
        ('abdominal_pain','abdominal_pain'),
        ('diarrhoea','diarrhoea'),
        ('mild_fever','mild_fever'),
    )
    # firstname = models.CharField(max_length=256)
    # lastname = models.CharField(max_length=256)
    # symptoms1 = MultiSelectField(choices=SYMPTOMS_CHOICES1)
    # symptoms2 = MultiSelectField(choices=SYMPTOMS_CHOICES2)
    itching = models.BooleanField(default=False)
    skin_rash = models.BooleanField(default=False)
    nodal_skin_eruptions = models.BooleanField(default=False)
    continuous_sneezing = models.BooleanField(default=False)
    shivering = models.BooleanField(default=False)
    chills = models.BooleanField(default=False)
    joint_pain = models.BooleanField(default=False)
    stomach_pain = models.BooleanField(default=False)
    acidity = models.BooleanField(default=False)
    ulcers_on_tongue = models.BooleanField(default=False)
    muscle_wasting = models.BooleanField(default=False)
    vomiting = models.BooleanField(default=False)
    burning_micturition = models.BooleanField(default=False)
    spotting_urination= models.BooleanField(default=False)
    fatigue = models.BooleanField(default=False)
    weight_gain = models.BooleanField(default=False)
    anxiety = models.BooleanField(default=False)
    cold_hands_and_feets = models.BooleanField(default=False)
    mood_swings = models.BooleanField(default=False)
    weight_loss = models.BooleanField(default=False)
    restlessness = models.BooleanField(default=False)
    lethargy = models.BooleanField(default=False)
    patches_in_throat = models.BooleanField(default=False)
    irregular_sugar_level = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    high_fever = models.BooleanField(default=False)
    sunken_eyes = models.BooleanField(default=False)
    breathlessness = models.BooleanField(default=False)
    sweating = models.BooleanField(default=False)
    dehydration = models.BooleanField(default=False)
    indigestion = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    yellowish_skin= models.BooleanField(default=False)
    dark_urine= models.BooleanField(default=False)
    nausea= models.BooleanField(default=False)
    loss_of_appetite= models.BooleanField(default=False)
    pain_behind_the_eyes= models.BooleanField(default=False)
    back_pain= models.BooleanField(default=False)
    constipation= models.BooleanField(default=False)
    abdominal_pain= models.BooleanField(default=False)
    diarrhoea= models.BooleanField(default=False)
    mild_fever= models.BooleanField(default=False)
    yellow_urine= models.BooleanField(default=False)
    yellowing_of_eyes= models.BooleanField(default=False)
    acute_liver_failure= models.BooleanField(default=False)
    fluid_overload= models.BooleanField(default=False)
    swelling_of_stomach= models.BooleanField(default=False)
    swelled_lymph_nodes= models.BooleanField(default=False)
    malaise= models.BooleanField(default=False)
    blurred_and_distorted_vision= models.BooleanField(default=False)
    phlegm= models.BooleanField(default=False)
    throat_irritation= models.BooleanField(default=False)
    redness_of_eyes= models.BooleanField(default=False)
    sinus_pressure= models.BooleanField(default=False)
    runny_nose= models.BooleanField(default=False)
    congestion= models.BooleanField(default=False)
    chest_pain= models.BooleanField(default=False)
    weakness_in_limbs= models.BooleanField(default=False)
    fast_heart_rate= models.BooleanField(default=False)
    pain_during_bowel_movements= models.BooleanField(default=False)
    pain_in_anal_region= models.BooleanField(default=False)
    bloody_stool= models.BooleanField(default=False)
    irritation_in_anus= models.BooleanField(default=False)
    neck_pain= models.BooleanField(default=False)
    dizziness= models.BooleanField(default=False)
    cramps= models.BooleanField(default=False)
    bruising= models.BooleanField(default=False)
    obesity= models.BooleanField(default=False)
    swollen_legs= models.BooleanField(default=False)
    swollen_blood_vessels= models.BooleanField(default=False)
    puffy_face_and_eyes= models.BooleanField(default=False)
    enlarged_thyroid= models.BooleanField(default=False)
    brittle_nails= models.BooleanField(default=False)
    swollen_extremeties= models.BooleanField(default=False)
    excessive_hunger= models.BooleanField(default=False)
    extra_marital_contacts= models.BooleanField(default=False)
    drying_and_tingling_lips= models.BooleanField(default=False)
    slurred_speech= models.BooleanField(default=False)
    knee_pain= models.BooleanField(default=False)
    hip_joint_pain= models.BooleanField(default=False)
    muscle_weakness= models.BooleanField(default=False)
    stiff_neck= models.BooleanField(default=False)
    swelling_joints= models.BooleanField(default=False)
    movement_stiffness= models.BooleanField(default=False)
    spinning_movements= models.BooleanField(default=False)
    loss_of_balance= models.BooleanField(default=False)
    unsteadiness= models.BooleanField(default=False)
    weakness_of_one_body_side= models.BooleanField(default=False)
    loss_of_smell= models.BooleanField(default=False)
    bladder_discomfort= models.BooleanField(default=False)
    foul_smell_of= models.BooleanField(default=False)
    continuous_feel_of_urine= models.BooleanField(default=False)
    passage_of_gases= models.BooleanField(default=False)
    internal_itching= models.BooleanField(default=False)
    toxic_look_typhos= models.BooleanField(default=False)
    depression = models.BooleanField(default=False)
    irritability= models.BooleanField(default=False)
    muscle_pain= models.BooleanField(default=False)
    altered_sensorium= models.BooleanField(default=False)
    red_spots_over_body= models.BooleanField(default=False)
    belly_pain= models.BooleanField(default=False)
    abnormal_menstruation= models.BooleanField(default=False)
    dischromic_patches= models.BooleanField(default=False)
    watering_from_eyes= models.BooleanField(default=False)
    increased_appetite= models.BooleanField(default=False)
    polyuria= models.BooleanField(default=False)
    family_history= models.BooleanField(default=False)
    mucoid_sputum= models.BooleanField(default=False)
    rusty_sputum= models.BooleanField(default=False)
    lack_of_concentration= models.BooleanField(default=False)
    visual_disturbances= models.BooleanField(default=False)
    receiving_blood_transfusion= models.BooleanField(default=False)
    receiving_unsterile_injections= models.BooleanField(default=False)
    coma= models.BooleanField(default=False)
    stomach_bleeding= models.BooleanField(default=False)
    distention_of_abdomen= models.BooleanField(default=False)
    history_of_alcohol_consumption= models.BooleanField(default=False)
    fluid_overload_1= models.BooleanField(default=False)
    blood_in_sputum= models.BooleanField(default=False)
    prominent_veins_on_calf= models.BooleanField(default=False)
    palpitations= models.BooleanField(default=False)
    painful_walking= models.BooleanField(default=False)
    pus_filled_pimples= models.BooleanField(default=False)
    blackheads= models.BooleanField(default=False)
    scurring= models.BooleanField(default=False)
    skin_peeling= models.BooleanField(default=False)
    silver_like_dusting= models.BooleanField(default=False)
    small_dents_in_nails= models.BooleanField(default=False)
    inflammatory_nails= models.BooleanField(default=False)
    blister= models.BooleanField(default=False)
    red_sore_around_nose= models.BooleanField(default=False)
    yellow_crust_ooze= models.BooleanField(default=False)

    def __str__(self):
        return self.firstname, self.lastname



'''
anxiety
cold_hands_and_feets
mood_swings
weight_loss
restlessness
lethargy
patches_in_throat
irregular_sugar_level
cough
high_fever
sunken_eyes
breathlessness
sweating
dehydration
indigestion
headache
yellowish_skin
dark_urine
nausea
loss_of_appetite
pain_behind_the_eyes
back_pain
constipation
abdominal_pain
diarrhoea
mild_fever
yellow_urine
yellowing_of_eyes
acute_liver_failure
fluid_overload
swelling_of_stomach
swelled_lymph_nodes
malaise
blurred_and_distorted_vision
phlegm
throat_irritation
redness_of_eyes
sinus_pressure
runny_nose
congestion
chest_pain
weakness_in_limbs
fast_heart_rate
pain_during_bowel_movements
pain_in_anal_region
bloody_stool
irritation_in_anus
neck_pain
dizziness
cramps
bruising
obesity
swollen_legs
swollen_blood_vessels
puffy_face_and_eyes
enlarged_thyroid
brittle_nails
swollen_extremeties
excessive_hunger
extra_marital_contacts
drying_and_tingling_lips
slurred_speech
knee_pain
hip_joint_pain
muscle_weakness
stiff_neck
swelling_joints
movement_stiffness
spinning_movements
loss_of_balance
unsteadiness
weakness_of_one_body_side
loss_of_smell
bladder_discomfort
foul_smell_of
continuous_feel_of_urine
passage_of_gases
internal_itching
toxic_look_(typhos)
depression 
irritability
muscle_pain
altered_sensorium
red_spots_over_body
belly_pain
abnormal_menstruation
dischromic _patches
watering_from_eyes
increased_appetite
polyuria
family_history
mucoid_sputum
rusty_sputum
lack_of_concentration
visual_disturbances
receiving_blood_transfusion
receiving_unsterile_injections
coma
stomach_bleeding
distention_of_abdomen
history_of_alcohol_consumption
fluid_overload.1
blood_in_sputum
prominent_veins_on_calf
palpitations
painful_walking
pus_filled_pimples
blackheads
scurring
skin_peeling
silver_like_dusting
small_dents_in_nails
inflammatory_nails
blister
red_sore_around_nose
yellow_crust_ooze
['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', ('stomach_pain','stomach_pain ), ('acidity','Acidity), 
'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', '
cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine',
'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 
'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 
'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool'
'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels',
'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts',
'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 
'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell',
'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 
'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum',
'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 

'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 
'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 
'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
'''

































#saif
#saif123