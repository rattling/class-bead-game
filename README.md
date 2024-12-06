# class-bead-game
*The game of game of games...*

We'll start with casino-style games like cards and roulette, then move on to team games, strategy games, and real-world games like prediction markets.

The *"game of games"* is about creating games, using the Class Bead Game to master disciplines like software engineering, data science, AI, and behavioral sciences.

The *"game of game of games"* explores how life is full of games, with the Class Bead Game making the rules, odds, and strategies fully transparent to help us play better.

# Development Setup

1. Create a 3.11 pipenv environment and install the dependencies:

```bash
pipenv install
pipenv shell
```
2. Install the casino package in editable mode:

NOTE: keeping our package outside of Pipfile to ease deployment later

```bash
pip install -e .
```
3. Run the game main menu:

```bash
python casino/main.py
```

# Roadmap For Developers
We will sometimes code from scratch rather than use an external package for both transparency and learning. Mileage will vary. I don't fancy recreating Matplotlib!

## Epoch 1: The Casino
Lets build the casino as a simple web application with start on agents, simulation and analytics.

### **Phase 1: Core Game Framework**
- [ ] Build foundational game components:
  - [x] Create `MSDie` class for dice rolls.
  - [x] Create `Cup` class for managing multiple dice.
  - [x] Create `Game` class to handle gameplay.
  - [ ] Write a basic CLI for interacting with the game.
- [ ] Implement scoring system:
  - [ ] Define scoring patterns (e.g., pairs, straights).
  - [ ] Create a `Scorer` class to evaluate dice rolls.
  - [ ] Integrate scoring into gameplay.
- [ ] Integrate basic algorithms:
  - [ ] Write frequency counters for roll patterns.
  - [ ] Use sorting algorithms for detecting sequences.
- [ ] Write unit tests for core components.

**Phase 2: Multiple Games and Management**  
**Phase 3: User Experience Enhancements**  
**Phase 4: Simulation Framework**  
**Phase 5: Analytics and Insights**  
**Phase 6: Backend Framework**  
**Phase 7: Simple Web UI**  
**Phase 8: Deployment**  

## Epoch 2: Beating the Casino/Beyond the Casino?
Some of the crazy stuff we flagged in the vision above.

# For Learners

The repo is a learning tool. There will also be youtube videos on some of the milestone tags with learnings and tips.

You might want to do a basic Python course or two first. This repo will support late beginner/early intermediate and eventually advanced Python developers.

## Prerequisites
- Basic Python programming
- Basic object-oriented programming
- Basic Git and GitHub
- Basic command line usage
- Python environments with pip and Pipenv

There are many routes such as w3schools, freeCodeCamp, Codecademy (free tier), Real Python tutorials, YouTube beginner courses just the Python official documentation. There are some great paid options too with quality teaching.


## Get Going

## Epoch 1 The Casino: Coding Challenges

Fork the repository and clone it to your local machine. If you want to complete any milestone code, just pull the previous milestone tag and start from there. You will find a next_milestone_challenge.md file in the milestone tag with a challenge to complete. Then checkout the next milestone tag to compare solutions.
For example, checkout  e1p1m1_blank_slate to get the challenge for e1p1m2_project_setup.

**Checkout the Tag for a Milestone:**
   ```bash
   git checkout <tag-name>
   ```

### Phase 1 Tags - Core Game Framework

| Tag Name                | Description                                  | Learnings
|-------------------------|----------------------------------------------|----------------------------------------------------|
| `e1p1m1_blank_slate`    | The starting point, with minimal setup.      | Fork a repo, run it's test script, set up IDE      |
| `e1p1m2_project_setup`  | Basic project structure and setup.           | Setup the repo folders, env & application package |
| `e1p1m3_die_game_basic` | Basic `Die` class with rolling functionality & rounds| Basic, working class structure and informal test,  list comprehension, generators  |
| `e1p1m4_die_game_varying` | Enhanced `Die` with custom sides and multiple rolls. | OOP single responsibility, functional programming, typehints, a little maths |
| `e1p1m4_die_game_multiple` | Multiple and more interesting dice games: Farkle and Pig. Basic CLI to play them | Strategy pattern, CLI |

---



