# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real-world recommendation platforms use information about both users and content to predict what each person may enjoy. Collaborative filtering finds patterns among users with similar behavior, such as listening to the same songs or adding similar artists to playlists. Content-based filtering instead compares a user's preferences with attributes of the available content. Large platforms can combine these methods with signals such as likes, skips, replays, searches, listening duration, and playlist activity. This simulation uses a simpler content-based approach that does not depend on data from other users.

For each song, the recommender will compare its genre, mood, energy, and acousticness with the user's taste profile. Genre will receive the greatest weight, followed by mood, because these features strongly describe the type and overall vibe of a song. Numerical features will be scored according to how closely they match the user's preference rather than automatically rewarding larger values. The system will calculate a score for every song, sort the songs from highest score to lowest score, and return the top requested recommendations.

Each Song object stores: id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness

Each UserProfile object stores: favorite_genre, favorite_mood, target_energy, likes_acoustic

The initial recommendation score will prioritize genre, mood, energy closeness, and acousticness preference. Tempo, valence, and danceability will remain available for evaluation or future improvements.

**Phase 2 Design Plan**

User Taste Profile

The initial simulation will use the following user profile:

```python
user_profile = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.40,
    "likes_acoustic": True,
}
```

This profile gives the recommender both categorical and numerical preferences. Genre and mood describe the user's preferred musical style and emotional atmosphere. Target energy allows the system to reward songs that are close to a preferred intensity instead of always favoring songs with higher energy. The acoustic preference provides an additional way to distinguish songs with similar genres, moods, or energy levels.

Algorithm Recipe

Each song will receive a relevance score using the following rules:

* Add `2.0` points when the song's genre matches the user's favorite genre.
* Add `1.0` point when the song's mood matches the user's favorite mood.
* Add up to `1.0` point for energy similarity using `1 - abs(song_energy - target_energy)`.
* Add `0.5` point when the song's acousticness matches the user's acoustic preference. An acousticness value of `0.60` or greater will be treated as acoustic.

The highest possible score is `4.5`. After every song has been scored, the system will sort the songs from highest score to lowest score and return the top `k` recommendations.

Data Flow

User preferences + songs.csv => Score each individual song => Record each score and matching reasons => Sort all songs from highest to lowest score => Return the top k recommendations

Potential Biases

This system may over-prioritize exact genre matches because genre receives the largest weight. That could prevent users from discovering songs in other genres that closely match their preferred mood or energy. Exact text matching also treats genres and moods as fixed categories even though real songs may belong to multiple categories. The small, manually created catalog may represent some genres and moods more often than others, giving those categories more opportunities to appear in the recommendations. The binary acoustic preference also simplifies a musical characteristic that exists on a continuous scale.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

Loading songs from data/songs.csv...
Loaded songs: 18

Top recommendations:

1. Sunrise City by Neon Echo
   Score: 4.48
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.98), acoustic preference match (+0.5)

2. Gym Hero by Max Pulse
   Score: 3.37
   Reasons: genre match (+2.0), energy similarity (+0.87), acoustic preference match (+0.5)

3. Rooftop Lights by Indigo Parade
   Score: 2.46
   Reasons: mood match (+1.0), energy similarity (+0.96), acoustic preference match (+0.5)

4. Concrete Crown by Northside Verse
   Score: 1.46
   Reasons: energy similarity (+0.96), acoustic preference match (+0.5)

5. Night Drive Loop by Neon Echo
   Score: 1.45
   Reasons: energy similarity (+0.95), acoustic preference match (+0.5)


**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



