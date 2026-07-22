import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        ranked_songs = sorted(
            self.songs,
            key=lambda song: score_song(vars(user), vars(song))[0],
            reverse=True,
        )
        return ranked_songs[:max(k, 0)]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        _, reasons = score_song(vars(user), vars(song))
        return ", ".join(reasons) if reasons else "No strong feature matches."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    score = 0.0
    reasons = []

    favorite_genre = user_prefs.get(
        "favorite_genre",
        user_prefs.get("genre", ""),
    )
    favorite_mood = user_prefs.get(
        "favorite_mood",
        user_prefs.get("mood", ""),
    )
    target_energy = float(
        user_prefs.get(
            "target_energy",
            user_prefs.get("energy", 0.0),
        )
    )

    if song["genre"].strip().lower() == str(favorite_genre).strip().lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].strip().lower() == str(favorite_mood).strip().lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_similarity = max(
        0.0,
        1.0 - abs(float(song["energy"]) - target_energy),
    )
    score += energy_similarity
    reasons.append(f"energy similarity (+{energy_similarity:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic")

    if likes_acoustic is not None:
        song_is_acoustic = float(song["acousticness"]) >= 0.60

        if song_is_acoustic == bool(likes_acoustic):
            score += 0.5
            reasons.append("acoustic preference match (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = (
            ", ".join(reasons)
            if reasons
            else "No strong feature matches."
        )
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(
        scored_songs,
        key=lambda result: result[1],
        reverse=True,
    )

    return ranked_songs[:max(k, 0)]
