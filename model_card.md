# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeMatch 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

VibeMatch 1.0 is a classroom music recommender simulation designed to generate a ranked list of songs based on a user's stated preferences. It compares preferences for genre, mood, energy, and acousticness with the attributes of each song in the catalog. The system assumes that the user can describe their current musical preferences using these four features. It is intended for educational exploration rather than use as a production recommendation service for real users.

VibeMatch should not be used as a commercial recommendation system or as evidence of a person's identity, personality, or emotional state. It should not replace a real music platform that uses larger datasets, listening history, and user feedback.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The recommender gives every song a score based on how closely it matches a user's preferences. An exact genre match adds `2.0` points, while an exact mood match adds `1.0` point. Energy is scored by measuring how close the song's energy value is to the user's target energy, with a maximum contribution of `1.0` point. A song also receives `0.5` points when its acoustic classification matches the user's acoustic preference.

After scoring every song, the system sorts the songs from highest score to lowest score and returns the requested number of recommendations. Each result includes an explanation showing which features contributed to its score. I replaced the starter placeholder logic with CSV loading, numerical conversions, weighted scoring, ranking, and recommendation explanations.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The model uses a catalog of 18 fictional songs stored in `data/songs.csv`. Each song includes an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness value. The catalog includes genres such as pop, lofi, rock, R&B, Latin, classical, hip-hop, folk, EDM, country, soul, and others. It also includes moods such as happy, chill, intense, romantic, peaceful, energetic, nostalgic, euphoric, hopeful, and melancholic.

I expanded the original catalog by adding eight songs so the recommender could test a wider range of genres and moods. However, the dataset is still small and manually created. It does not represent the full variety of musical styles, cultures, artists, listeners, or complex combinations of musical taste.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The recommender works well when a user's preferred genre and mood are directly represented in the catalog. It produced reasonable first-place results for the High-Energy Pop, Chill Lofi, and Deep Intense Rock profiles. The energy-similarity calculation also works well because it rewards songs that are close to the user's target instead of automatically favoring songs with higher energy.

Another strength is that every recommendation includes a plain-language explanation of its score. For example, `Sunrise City` ranked first for High-Energy Pop because it matched the requested genre and mood, had an energy level close to the target, and matched the non-acoustic preference. These explanations make the system's decisions easier to understand.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The recommender relies on exact genre and mood matches, so it cannot recognize that differently labeled songs may still have similar musical qualities. The genre weight can dominate the ranking when a song also matches the user's energy and acoustic preferences. For the conflicting pop, melancholic, and high-energy profile, energetic pop songs ranked above the melancholic song because several matching features outweighed one mood match. The catalog contains only 18 manually selected songs, so users whose preferences are not well represented have fewer meaningful options. The binary acoustic preference and fixed `0.60` threshold also simplify a characteristic that exists on a continuous scale.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I evaluated the recommender using four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicting Sad Workout. I reviewed the first five recommendations for each profile and checked whether the songs matched the requested genre, mood, energy, and acoustic preference. The first three profiles produced intuitive first-place recommendations. The conflicting profile revealed that several matching features can outweigh one important mood preference.

- High-Energy Pop favored `Sunrise City`, while Chill Lofi favored `Midnight Coding`. The first song matched pop, happy, high-energy, and non-acoustic preferences, while the second matched lofi, chill, moderate-energy, and acoustic preferences.
- High-Energy Pop and Deep Intense Rock both favored energetic songs, but their first-place results differed because their genre and mood preferences were different.
- High-Energy Pop placed `Sunrise City` first, while Conflicting Sad Workout placed `Gym Hero` first because `Gym Hero` was closer to the conflicting profile's higher energy target.
- Chill Lofi emphasized acoustic and lower-energy songs, while Deep Intense Rock emphasized non-acoustic and high-energy songs.
- Chill Lofi and Conflicting Sad Workout produced very different lists because their genre, mood, energy, and acoustic preferences pointed in opposite directions.
- Deep Intense Rock and Conflicting Sad Workout both favored high-energy songs, but the conflicting profile gave additional weight to pop instead of rock.

I also ran a temporary weight-shift experiment that reduced the genre weight from `2.0` to `1.0` and doubled the energy contribution. `Rooftop Lights` moved above `Gym Hero` for the High-Energy Pop profile because mood and energy became more influential relative to genre. However, `Blue Sunday` disappeared from the Conflicting Sad Workout top five because high-energy songs received too much influence. This showed that changing a weight can reduce one weakness while introducing another, so I restored the original weights after recording the results.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

If I continued developing VibeMatch, I would:

- Add preferences for tempo, valence, and danceability.
- Allow users to choose how important each preference is.
- Improve diversity so the top results do not all have similar features.
- Use multiple genres and moods for each song instead of one exact label.
- Learn from user feedback such as likes, skips, and repeated plays.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment was seeing how much a small weight change could affect the entire recommendation list. The rules were simple, but changing genre from `2.0` to `1.0` and doubling energy caused several songs to move. It also caused `Blue Sunday` to disappear from the conflicting profile's top five. This showed me that a recommendation can appear reasonable while still being shaped by assumptions chosen by the developer.

AI tools helped me brainstorm test profiles, check scoring logic, and explain unexpected results. However, I still needed to review the code, run the tests, and compare the actual terminal output with the suggested results. One experiment initially changed only the genre weight because the energy multiplier was still `1.0`. Double-checking the code and output helped me catch that issue.

I was surprised that a basic weighted scoring algorithm could still produce recommendations that felt personalized. The system did not learn from real listening behavior, but matching genre, mood, energy, and acousticness was enough to create noticeably different lists. This helped me understand that recommendation systems do not need to be extremely complex to influence what users see.

If I extended this project, I would add more songs, allow songs to have multiple genres and moods, and collect feedback from users. I would also test methods that balance preference matching with discovery so users are not repeatedly shown the same types of music.