knowledge_base = {
    'flu': {
        'fever': True,
        'cough': True,
        'sore throat': True,
        'body aches': True,
        'fatigue': True,
        'nausea': False,
        'diarrhea': False
    },
    'cold': {
        'fever': False,
        'cough': True,
        'sore throat': True,
        'body aches': False,
        'fatigue': False,
        'nausea': False,
        'diarrhea': False
    },
    'food poisoning': {
        'fever': False,
        'cough': False,
        'sore throat': False,
        'body aches': False,
        'fatigue': False,
        'nausea': True,
        'diarrhea': True
    }
}

def diagnose(symptoms):
    illness = None
    max_count = 0
    for k, v in knowledge_base.items():
        count = 0
        for symptom, present in symptoms.items():
            if present == v[symptom]:
                count += 1
        if count > max_count:
            max_count = count
            illness = k
    return illness

def get_input():
    symptoms = {}
    symptoms['fever'] = input('Do you have a fever? (y/n)').lower() == 'y'
    symptoms['cough'] = input('Do you have a cough? (y/n)').lower() == 'y'
    symptoms['sore throat'] = input('Do you have a sore throat? (y/n)').lower() == 'y'
    symptoms['body aches'] = input('Do you have body aches? (y/n)').lower() == 'y'
    symptoms['fatigue'] = input('Are you feeling fatigued? (y/n)').lower() == 'y'
    symptoms['nausea'] = input('Are you experiencing nausea? (y/n)').lower() == 'y'
    symptoms['diarrhea'] = input('Are you experiencing diarrhea? (y/n)').lower() == 'y'
    return symptoms

def main():
    symptoms = get_input()
    illness = diagnose(symptoms)
    print('Based on your symptoms, you most likely have:', illness)

if __name__ == '__main__':
    main()