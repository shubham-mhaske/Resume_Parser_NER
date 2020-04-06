import pickle
import spacy



def extract_data(text):

    with open('models/my_model.pkl', 'rb') as f:
        model = pickle.load(f)
    nlp = spacy.blank(model['lang'])
    for pipe_name in model['pipeline']:
        pipe = nlp.create_pipe(pipe_name)
        nlp.add_pipe(pipe)
    nlp.from_bytes(model['bytes_data'])

    text = text.lower()
    doc = nlp(text)
    output = dict()
    for ent in doc.ents:
        output[ent.label_] = []
    for ent in doc.ents:
        if ent.text not in output[ent.label_]:
            output[ent.label_].append(ent.text)
        pass
    return output