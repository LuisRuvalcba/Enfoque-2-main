from transformers import BertTokenizer, BertForNextSentencePrediction
import torch

# Ejemplo de documentos de texto
documents = [
    "Machine learning is the study of computer algorithms that improve automatically through experience.",
    "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence.",
    "Information retrieval (IR) is the process of obtaining information from a collection of documents.",
    "Document retrieval is the task of finding documents that are relevant to an information need from a large collection."
]

# Consulta de búsqueda
query = "Machine learning and natural language processing"

# Tokenizamos la consulta y los documentos utilizando BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
encoded_query = tokenizer.encode_plus(query, return_tensors='pt', add_special_tokens=True, max_length=512, truncation=True)
encoded_documents = [tokenizer.encode_plus(doc, return_tensors='pt', add_special_tokens=True, max_length=512, truncation=True) for doc in documents]

# Utilizamos BERT para predecir si la consulta sigue al documento
model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')
scores = []

with torch.no_grad():
    for encoded_doc in encoded_documents:
        input_ids = torch.cat((encoded_doc['input_ids'], encoded_query['input_ids']), dim=1)
        token_type_ids = torch.cat((encoded_doc['token_type_ids'], encoded_query['token_type_ids']), dim=1)
        attention_mask = torch.cat((encoded_doc['attention_mask'], encoded_query['attention_mask']), dim=1)
        outputs = model(input_ids, token_type_ids=token_type_ids, attention_mask=attention_mask)
        scores.append(outputs.logits[:, 0].item())

# Ordenamos los documentos por puntaje de relevancia y mostramos los más relevantes
most_relevant_index = max(range(len(scores)), key=lambda i: scores[i])
most_relevant_doc = documents[most_relevant_index]
relevance_score = scores[most_relevant_index]

print("Documento mas relevante:")
print(most_relevant_doc)
print("Puntaje de relevancia:", relevance_score)
