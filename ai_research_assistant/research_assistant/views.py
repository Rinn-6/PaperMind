import os
import spacy
import tempfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .utils import extract_text_from_pdf
from .gemini_api import summarize_text, extract_insights, generate_citation

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

class ResearchPaperAnalysisView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        pdf_file = request.FILES.get("file")
        if not pdf_file:
            return Response({"error": "No file uploaded"}, status=400)

        # ✅ Save the file in a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            for chunk in pdf_file.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name

        try:
            text = extract_text_from_pdf(temp_file_path)

            # ✅ NLP Analysis with spaCy
            doc = nlp(text)
            named_entities = [(ent.text, ent.label_) for ent in doc.ents]  # Extract named entities

            # ✅ Generate responses
            summary = summarize_text(text)
            insights = extract_insights(text)
            citation = generate_citation(text)

        finally:
            os.remove(temp_file_path)  # ✅ Delete temp file after processing

        return Response({
            "summary": summary,
            "insights": insights,
            "citation": citation,
            "named_entities": named_entities,  # ✅ Added NLP insights
        })
