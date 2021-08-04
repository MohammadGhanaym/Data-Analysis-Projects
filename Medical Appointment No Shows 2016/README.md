<a id='intro'></a>
## Introduction

> This dataset contains 110527  medical appointments associated with 14 variables (characteristics). The most important one if the patient show-up or no-show at the appointment. I will try to know what is characteristics of the patients that no-show. I will answer some questions like Are the majority of the patients that no-shows female or male?

#### Columns

- PatientId

Identification of a patient
- AppointmentID

Identification of each appointment
- Gender

Male or Female . Female is the greater proportion, woman takes way more care of they health in comparison to man.
- AppointmentDay

The day of the actuall appointment, when they have to visit the doctor.
- ScheduledDay

The day someone called or registered the appointment, this is before appointment of course.
- Age

How old is the patient.
- Neighbourhood

Where the appointment takes place.
- Scholarship

True of False . Observation, this is a broad topic, consider reading this article https://en.wikipedia.org/wiki/Bolsa_Fam%C3%ADlia
- Hipertension

True or False
- Diabetes

True or False
- Alcoholism

True or False
- Handcap

True or False
- SMS_received

1 or more messages sent to the patient.
- No-show

True or False.

### Exploration Questions
- Are the majority of patients female or male? 
- Are the majority of patients have diabetes? 
- Are the majority of patients have alcoholism?
- Do the majority of patients take the scholarship?
- Do the patients that no-shows have Hypertension?
- Are the majority of the patients that no-shows female or male?
- Do the majority of the patients that no-shows took the scholarship or not?
- Do the patients that no-show at the appointment have diabetes?
- Do the patients, that no-show at the appointment have alcoholism?
- Do the patients that no-show at the appointment handicapped?
- Does the appointment place affect whether the patient no-show?
- Does the patients that no-show received SMSs?
- What age group that most likely to no-show at the appointment?
- Does waiting time affect if people no-show appointments or not?

## Conclusions
1. It seems that most patients are females.
2. The minority of patients had diabetes since 92.84 % of the patients didn't have diabetes.
3. The minority of patients had alcoholism since 96.96 % of the patients didn't have alcoholism.
4. Most patients didn't take the scholarship.
5. Most patients didn't have hypertension 6. Most patients go on time, representing 79.90% of all patients.
7. 13.15% of all patients are females and no-show at the appointment
8. 6.95% of all patients are males and no-show at the appointment.
9. 18.81% of all patients didn't have diabetes and no-show at the appointment.
10. 1.29% of all patients have diabetes and no-show at the appointment.
11. 19.50% of all patients didn't have alcoholism and no-show at the appointment.
12. 0.61% of all patients have alcoholism and no-show at the appointment.
13. 17.77% of all the patients didn't take the scholarship and didn't no-show at the appointment.
14. 2.33% of all the patients took the scholarship, but they didn't no-show at the appointment.
15. 16.73% of all patients didn't have hypertension and no-show at the appointment.
16. 3.38% of all patients have hypertension and no-show at the appointment.
17. 19.78% of all patients weren't handicapped and no-show at the appointment.
18. 0.32% of all patients were handicapped and no-show at the appointment.
19. Most of the appointment was in JARDIM CAMBURI neighborhood.
20. 11.19% of all patients didn't receive SMSs and no-show at the appointment.
21. 8.91% of all patients receive SMSs and no-show at the appointment.
22. The average waiting time for people who no-show appointments are bigger than for those who don't do so. This is means that the more the waiting time is, the more people who no-show appointments.
23. The characteristics of patients that no-show at the appointment:
    - Most patients who no-show at the appointment are females where they represent 65.42% of all patients who no-show.
    - Most patients who no-show at the appointment didn't have diabetes, representing 93.59% of all patients who no-show.
    - Most patients who no-show at the appointment didn't have alcoholism, representing 96.98% of all patients who no-show.
    - Most of the patients that didn't no-show at the appointment didn't take the scholarship, representing 88.41% of the patients who no-show.
    - Most patients who no-show at the appointment didn't have hypertension, representing 83.20% of all patients who no-show.
    - Most patients who no-show at the appointment weren't handicapped, representing 98.39% of all patients who no-show.
    - Most of the appointment was in JARDIM CAMBURI neighborhood.
    - In general, most patients who no-show at the appointment didn't receive SMSs, representing 55.67% of all patients who no-show.
    - In general, the patients in the age group -1:18 and 18:37 are most likely to no-show at the appointment, representing 28.53% and 28.72% respectively. 
**Limitations:**
- I think there are missing features. For instance, If we have a column that indicates whether the patient is employed or not, it will help us get a better conclusion. 
- I had some difficulty understand the data. I was confused between the 'AppointmentDay' column and the 'ScheduledDay' column. I do some search to know what they mean. Also, the 'age' column and the 'handicap' column have confusing values.
