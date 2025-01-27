import pickle
from ai_lab_repo import LaboratoryWorkflow

with open('state_saves/literature_review.pkl', 'rb') as f:
    data = pickle.load(f)

print(data.reference_papers) # NOTHING IN THIS SHIT!! AHHHHHHHH POS