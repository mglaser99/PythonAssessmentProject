from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
import numpy as np

class allMiniLM:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
        self.model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

    def __mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def sentence_embeddings(self, sentences: list[str]):
        # Tokenize sentences
        encoded_input = self.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

        # Compute token embeddings
        with torch.no_grad():
            model_output = self.model(**encoded_input)

        # Perform pooling
        sentence_embeddings = self.__mean_pooling(model_output, encoded_input['attention_mask'])

        # Normalize embeddings
        sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

        embeddings = [(s, t) for s,t in zip(sentences, sentence_embeddings)]

        return embeddings

    def most_similar(self, reference: str, others: list[str]):
        reference_embedding = self.sentence_embeddings([reference])
        others_embeddings = self.sentence_embeddings(others)

        cosine_dist = torch.nn.CosineSimilarity(dim=0)

        similarities = [cosine_dist(reference_embedding[0][1], e[1]) for e in others_embeddings]

        index_max = np.argmax(similarities)

        return others_embeddings[index_max][0]



if __name__=="__main__":
    model = allMiniLM()
    print(model.most_similar("Higgs boson in particle physics", ["Best soup recipes", "Basel activities", "Particle physics at CERN"]))
