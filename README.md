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

The recommender was tested with four profiles representing different musical preferences, including one intentionally conflicting profile.

**High-Energy Pop**

```text
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
```

**Chill Lofi**

```text
1. Midnight Coding by LoRoom
   Score: 4.48
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.98), acoustic preference match (+0.5)

2. Library Rain by Paper Lanterns
   Score: 4.45
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.95), acoustic preference match (+0.5)

3. Focus Flow by LoRoom
   Score: 3.50
   Reasons: genre match (+2.0), energy similarity (+1.00), acoustic preference match (+0.5)

4. Spacewalk Thoughts by Orbit Bloom
   Score: 2.38
   Reasons: mood match (+1.0), energy similarity (+0.88), acoustic preference match (+0.5)

5. Coffee Shop Stories by Slow Stereo
   Score: 1.47
   Reasons: energy similarity (+0.97), acoustic preference match (+0.5)
```

**Deep Intense Rock**

```text
1. Storm Runner by Voltline
   Score: 4.49
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.99), acoustic preference match (+0.5)

2. Gym Hero by Max Pulse
   Score: 2.47
   Reasons: mood match (+1.0), energy similarity (+0.97), acoustic preference match (+0.5)

3. Golden Barrio by Luna Mar
   Score: 1.48
   Reasons: energy similarity (+0.98), acoustic preference match (+0.5)

4. Concrete Crown by Northside Verse
   Score: 1.44
   Reasons: energy similarity (+0.94), acoustic preference match (+0.5)

5. Electric Horizon by Nova Circuit
   Score: 1.44
   Reasons: energy similarity (+0.94), acoustic preference match (+0.5)
```

**Conflicting Sad Workout**

```text
1. Gym Hero by Max Pulse
   Score: 3.47
   Reasons: genre match (+2.0), energy similarity (+0.97), acoustic preference match (+0.5)

2. Sunrise City by Neon Echo
   Score: 3.42
   Reasons: genre match (+2.0), energy similarity (+0.92), acoustic preference match (+0.5)

3. Blue Sunday by The Harbor Choir
   Score: 1.56
   Reasons: mood match (+1.0), energy similarity (+0.56)

4. Storm Runner by Voltline
   Score: 1.49
   Reasons: energy similarity (+0.99), acoustic preference match (+0.5)

5. Golden Barrio by Luna Mar
   Score: 1.48
   Reasons: energy similarity (+0.98), acoustic preference match (+0.5)
```

The first three profiles produced intuitive first-place recommendations. The conflicting profile produced a more surprising result. Although `Blue Sunday` matched the requested melancholic mood, `Gym Hero` and `Sunrise City` ranked higher because they matched the pop genre, high-energy target, and non-acoustic preference. This demonstrates that several matching features can outweigh one mood match.

I temporarily reduced the genre-match weight from `2.0` to `1.0` and doubled the maximum energy-similarity contribution from `1.0` to `2.0`. For the High-Energy Pop profile, `Rooftop Lights` moved above `Gym Hero` because its energy was closer to the target and it also matched the requested happy mood. This showed that reducing the genre weight allowed other features to influence the ranking more strongly.

The change made the system more sensitive to energy, but it did not necessarily make every recommendation more accurate. For the Conflicting Sad Workout profile, `Blue Sunday` dropped out of the top five even though it matched the melancholic mood. High-energy songs from unrelated genres ranked above it because the doubled energy score became dominant. This experiment demonstrated that adjusting a weight can reduce one bias while creating another.


---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

The recommender relies on exact genre and mood matches, so it cannot recognize that differently labeled songs may still have similar musical qualities. The genre weight can dominate the ranking when a song also matches the user's energy and acoustic preferences. For the conflicting pop, melancholic, and high-energy profile, energetic pop songs ranked above the melancholic song because several matching features outweighed one mood match. The catalog contains only 18 manually selected songs, so users whose preferences are not well represented have fewer meaningful options. The binary acoustic preference and fixed `0.60` threshold also simplify a characteristic that exists on a continuous scale.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This project helped me understand how recommender systems turn user preferences and item features into ranked predictions. My biggest learning moment was discovering how strongly the selected weights affect the results. The conflicting user profile and weight-shift experiment showed that a recommendation can look logical while still underrepresenting an important preference.

AI tools helped me generate edge cases, inspect the scoring math, and explain the rankings in plain language. I still needed to verify every suggestion by reading the code, running the tests, and comparing the actual terminal output. I was surprised that a simple weighted algorithm could create recommendations that felt personalized. If I continued the project, I would expand the catalog, support more detailed preferences, use user feedback, and improve variety among the top results.


