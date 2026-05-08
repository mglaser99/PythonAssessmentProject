# PythonAssessmentProject


## Launch the Project

1. cd into the `PythonAssessmentProject` directory

2. Install dependencies

        poetry install

3. Start the application

        poetry run python -m src.main
    The API will be available at http://localhost:8000

### Example Usage

Using curl:

    curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d "{\"reference\":\"Higgs boson in particle physics\",\"other\":[\"Best soup recipes\",\"Basel activities\",\"Particle physics at CERN\"]}"

Running the test script `test.py`

    poetry run python test.py

## Implementation Details
Embedding Model: [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
Similarity Metric: Cosine similarity

## GenAI Usage
- GitHub Copilot was used for some of the commit messages.
- ChatGPT was used to generate the example inputs used in the `test.py` file and to refine the README