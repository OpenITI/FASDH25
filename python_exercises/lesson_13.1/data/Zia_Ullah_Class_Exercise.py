import pandas as pd
data = {
    'Country': ['Kenya', 'France', 'Pakistan', 'Brazil', 'Canada'],
    'Delegation': ['Environment', 'Security', 'Health', 'Education', 'Human Rights'],
    'RepresentativeFirstName': ['Amina', 'Louis', 'Zain', 'Carlos', 'Emma'],
    'RepresentativeLastName': ['Omondi', 'Dubois', 'Ahmed', 'Silva', 'Brown'],
    'SpeechesGiven': [3, 5, 4, 2, 6],
    'ResolutionsSponsored': [2, 4, 2, 3, 5],
    'VotesInFavour': [10, 12, 10, 11, 13],
    'Region': ['Africa', 'Europe', 'Asia', 'South America', 'North America']
}

df = pd.DataFrame(data)
