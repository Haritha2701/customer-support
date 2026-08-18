import json
import os
import re


# ==========================================
# KNOWLEDGE BASE LOCATION
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

KNOWLEDGE_BASE_PATH = os.path.join(
    BASE_DIR,
    "data",
    "knowledge_base.json"
)


# ==========================================
# LOAD KNOWLEDGE BASE
# ==========================================

def load_knowledge_base():

    with open(
        KNOWLEDGE_BASE_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ==========================================
# CLEAN TEXT
# ==========================================

def clean_text(text):

    text = text.lower()

    # Remove punctuation
    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ==========================================
# GET WORDS
# ==========================================

def get_words(text):

    return set(
        clean_text(text).split()
    )


# ==========================================
# SEARCH KNOWLEDGE
# ==========================================

def search_knowledge(message):

    knowledge_base = load_knowledge_base()

    customer_text = clean_text(message)

    customer_words = get_words(
        customer_text
    )


    best_match = None

    highest_score = 0


    # ======================================
    # CHECK EACH KNOWLEDGE ITEM
    # ======================================

    for item in knowledge_base:

        score = 0


        # ----------------------------------
        # CHECK KEYWORDS
        # ----------------------------------

        for keyword in item["keywords"]:

            keyword_clean = clean_text(
                keyword
            )

            # Exact phrase
            if keyword_clean in customer_text:

                score += 3

            else:

                keyword_words = get_words(
                    keyword_clean
                )

                # Individual keyword words
                for word in keyword_words:

                    if word in customer_words:

                        score += 1


        # ----------------------------------
        # CHECK CATEGORY
        # ----------------------------------

        category = clean_text(
            item["category"]
        )

        if category in customer_text:

            score += 2


        # ----------------------------------
        # CHECK QUESTION
        # ----------------------------------

        question_words = get_words(
            item["question"]
        )


        # Ignore common words
        ignored_words = {
            "what",
            "when",
            "where",
            "how",
            "can",
            "the",
            "your",
            "you",
            "is",
            "my",
            "i",
            "do",
            "does",
            "will",
            "are"
        }


        useful_question_words = (
            question_words
            - ignored_words
        )


        for word in useful_question_words:

            if word in customer_words:

                score += 0.5


        # ----------------------------------
        # SAVE BEST MATCH
        # ----------------------------------

        if score > highest_score:

            highest_score = score

            best_match = item


    # ======================================
    # NO MATCH
    # ======================================

    if best_match is None:

        return {

            "found": False,

            "answer":
                "Sorry, I could not find information about this question.",

            "category": None,

            "confidence": 0

        }


    # ======================================
    # CALCULATE CONFIDENCE
    # ======================================

    confidence = min(
        int(highest_score * 20),
        100
    )


    # Don't consider extremely weak matches
    if confidence < 20:

        return {

            "found": False,

            "answer":
                "Sorry, I could not find information about this question.",

            "category": None,

            "confidence": 0

        }


    # ======================================
    # RETURN RESULT
    # ======================================

    return {

        "found": True,

        "category":
            best_match["category"],

        "answer":
            best_match["answer"],

        "confidence":
            confidence

    }
