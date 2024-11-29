# class-bead-game
The game of game of games...

OK, what are the games? We will start with casino style games of chance like cards and roulette and evolve team games, games of strategy and even real-world games like prediction markets, 

What about the "game of games?" This is the game of creating games. For those who like this sort of thing, we will use the Class Bead Game to practice technical disciplines such as software engineering, data science, AI and behavioural sciences and gain mastery over them.

Fine, how about the "game of game of games?". Life is full of games and we are playing inside of games all the time, sometimes unwittingly. The Class Bead Game will be different. It will be fully transparent. We will know the rules, the odds, the strategies and the outcomes. We will learn how we play the games of life and how we can play them better.

If you don't want to look under the hood, that's it. Check out the Class Bead Game, coming soon. If you want to look under the hood and tinker, read on...

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
We will eschew the use of external libraries as much as possible so that we can learn fundamentals. We will relax this when necessary or when we have already covered those topics in earlier versions.

## Epoch 1: The Casino
Lets build the casino as a simple web application, simulate players with agents and run the games. We may surface some rudimentary insights for players to learn from. These milestones might move around a little as we learn more about the problem space.

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

You may not want to make contributions to the repository yet, that's fine. It's also a learning tool. You can pull the tagged commits below to take a challenge and then compre it to the tag for the finished article. There will also be youtube videos on some of the milestone tags with learnings and tips.

You might want to do a basic Python course or two first. This repo will support early late beginner/early intermediate Python developer.

## Prequisites
- Basic Python programming
- Basic object-oriented programming
- Basic Git and GitHub
- Basic command line usage
- Python environments with pip and Pipenv

There are many routes but here are some good options:


## Get Going

## Epoch 1 The Casino: Coding Challenges

Fork the repository and clone it to your local machine. If you want to complete any milestone code, just pull the previous milestone tag and start from there. You will find a next_milestone_challenge.md file in the milestone tag with a challenge to complete. You can compare your solution to the next milestone tag.

**Checkout the Tag for a Milestone:**
   ```bash
   git checkout <tag-name>
   ```


| Phase | Tag Name                | Description                                  |
|-------|-------------------------|----------------------------------------------|
| 1     | `e1p1m1_blank_slate`    | The starting point, with minimal setup.      |
| 1     | `e1p1m2_project_setup`  | Basic project structure and setup.           |
| 1     | `e1p1m3_die_game_basic` | Basic `Die` class with rolling functionality.|
| 1     | `e1p1m4_die_game_varying` | Enhanced `Die` with custom sides and multiple rolls. |

---



