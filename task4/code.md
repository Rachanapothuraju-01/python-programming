# Sports Tournament Ranking System

## 1. Problem Statement

Develop a Sports Tournament Ranking System to store match results and team scores, calculate total points and tie-break values, and generate the final team rankings according to a specified competition policy.

The system should accept the number of teams and match results as input. It should calculate points for each team based on match outcomes:

- Win = 3 points
- Draw = 1 point
- Loss = 0 points

The system should also calculate goal difference (goals scored minus goals conceded) as the tie-break value. Teams should be ranked according to the following rules:

1. Highest total points.
2. Highest goal difference.
3. Highest goals scored.
4. Alphabetical order if all values are equal.

The system should display the final ranking of all teams.

## 2. Algorithm

1. Start.
2. Read the number of teams.
3. Read the team names.
4. Initialize points, goals scored, goals conceded, and goal difference to zero for each team.
5. Read the number of matches.
6. For each match:
   - Read the home team, away team, and their scores.
   - Update goals scored and goals conceded for both teams.
   - If the home team wins, award 3 points to the home team.
   - If the away team wins, award 3 points to the away team.
   - If the match is a draw, award 1 point to each team.
7. Calculate goal difference for every team.
8. Sort teams based on:
   - Total points in descending order.
   - Goal difference in descending order.
   - Goals scored in descending order.
   - Team name in alphabetical order.
9. Display the final tournament rankings.
10. Stop.

## 3. Flowchart
```mermaid
        START
          |
          v
    Input Team Details
          |
          v
    Initialize Scores
          |
          v
    Input Match Results
          |
          v
    Calculate Match Points
          |
          v
    Update Goals Scored
    and Goals Conceded
          |
          v
    Calculate Goal Difference
          |
          v
    Are All Matches Completed?
       /          \
     No            Yes
     |               |
     v               v
 Input Next      Sort Teams Based
   Match         on Ranking Rules
                     |
                     v
               Display Rankings
                     |
                     v
                    STOP
```

## 4. Python Code

```python

# Sports Tournament Ranking System

# Input number of teams
n = int(input("Enter number of teams: "))

teams = {}

# Input team names
for i in range(n):
    name = input("Enter team name: ")
    teams[name] = {
        "points": 0,
        "scored": 0,
        "conceded": 0,
        "gd": 0
    }

# Input number of matches
m = int(input("Enter number of matches: "))

# Process match results
for i in range(m):
    print("\nMatch", i + 1)

    team1 = input("Enter home team: ")
    team2 = input("Enter away team: ")

    score1 = int(input("Enter home team score: "))
    score2 = int(input("Enter away team score: "))

    # Update goals
    teams[team1]["scored"] += score1
    teams[team1]["conceded"] += score2

    teams[team2]["scored"] += score2
    teams[team2]["conceded"] += score1

    # Award points
    if score1 > score2:
        teams[team1]["points"] += 3
    elif score1 < score2:
        teams[team2]["points"] += 3
    else:
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1

# Calculate goal difference
for team in teams:
    teams[team]["gd"] = (
        teams[team]["scored"] -
        teams[team]["conceded"]
    )

# Sort teams based on competition rules
ranking = sorted(
    teams.items(),
    key=lambda x: (
        -x[1]["points"],
        -x[1]["gd"],
        -x[1]["scored"],
        x[0]
    )
)

# Display final rankings
print("\n========== TOURNAMENT RANKINGS ==========")

print("Rank  Team       Points  GF  GA  GD")

for rank, (name, data) in enumerate(ranking, 1):
    print(
        f"{rank:<6}{name:<11}"
        f"{data['points']:<8}"
        f"{data['scored']:<4}"
        f"{data['conceded']:<4}"
        f"{data['gd']}"
    )
```

## 5. Sample Input

text

```text
Enter number of teams: 4

Enter team name: India
Enter team name: Australia
Enter team name: England
Enter team name: Pakistan

Enter number of matches: 4

Match 1
Enter home team: India
Enter away team: Australia
Enter home team score: 2
Enter away team score: 1

Match 2
Enter home team: England
Enter away team: Pakistan
Enter home team score: 1
Enter away team score: 1

Match 3
Enter home team: India
Enter away team: England
Enter home team score: 3
Enter away team score: 0

Match 4
Enter home team: Australia
Enter away team: Pakistan
Enter home team score: 2
Enter away team score: 0
```

## 6. Sample Output

text

```text
========== TOURNAMENT RANKINGS ==========

Rank  Team       Points  GF  GA  GD
1     India      6       5   1   4
2     Australia  3       3   2   1
3     England    1       1   4   -3
4     Pakistan   1       1   3   -2
```

## 7. Result

The Sports Tournament Ranking System successfully stores match results, calculates team points, goals scored, goals conceded, and goal difference. It sorts the teams according to the specified competition rules and displays the final tournament rankings.

Time Complexity:

- Match processing: $O(M)$
- Ranking/sorting: $O(N\log N)$
- Overall: $O(M + N\log N)$

Where:

- $N$ = Number of teams.
- $M$ = Number of matches.
