# class-bead-game
The game of game of games

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


# Roadmap: Class Bead Game

This roadmap outlines the phases for developing the Class Bead Game project, starting with core functionality and progressively adding features like simulations, analytics, and deployment. Each phase builds on the previous to create a fully functional and scalable system.

## **Phase 1: Core Game Framework**
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

## **Phase 2: Multiple Games and Management**
- [ ] Add additional games to the casino:
  - [ ] Extend the dice game with advanced rules (e.g., rerolls).
  - [ ] Add a second game (e.g., blackjack or card-based).
- [ ] Build a `CasinoManager`:
  - [ ] Manage multiple games in a session.
  - [ ] Track player profiles and sessions.
  - [ ] Record results for game history.
- [ ] Enhance CLI:
  - [ ] Add menus for selecting games and players.
  - [ ] Allow saving/loading of game sessions.

## **Phase 3: User Experience Enhancements**
- [ ] Improve the CLI experience:
  - [ ] Add navigation for game options and stats.
  - [ ] Format output for better readability.
  - [ ] Handle errors and invalid inputs gracefully.
- [ ] Add persistence:
  - [ ] Save player profiles and results to a file.
  - [ ] Reload data at the start of a session.

## **Phase 4: Simulation Framework**
- [ ] Introduce agent-based simulations:
  - [ ] Create AI players with configurable behaviors:
    - [ ] Risk-averse players.
    - [ ] Risk-seeking players.
  - [ ] Simulate games to build a large history of gameplay data.
- [ ] Focus on scalability:
  - [ ] Simulate thousands of games in batches.
  - [ ] Store results efficiently for analysis.

## **Phase 5: Analytics and Insights**
- [ ] Build an analytics layer:
  - [ ] Analyze game history for patterns:
    - [ ] Common dice rolls.
    - [ ] Win/loss ratios.
    - [ ] Player tendencies (e.g., cautious vs. aggressive).
  - [ ] Generate statistical reports for key metrics.
- [ ] Implement visualizations:
  - [ ] Create charts for dice probabilities, player stats, etc.
  - [ ] Export results to plain text, JSON, or simple visual formats.

## **Phase 6: Backend Framework**
- [ ] Develop a minimal FastAPI-like framework:
  - [ ] Map routes to Python functions.
  - [ ] Handle request parsing and validation.
  - [ ] Return responses in JSON or HTML formats.
- [ ] Keep it lightweight and modular for easy integration.

## **Phase 7: Simple Web UI**
- [ ] Build a browser-based UI:
  - [ ] Serve static HTML/CSS files using Python.
  - [ ] Add vanilla JavaScript for interactivity (e.g., dice roll updates).
  - [ ] Display leaderboards and player stats dynamically.
- [ ] Add basic routing for UI pages (e.g., homepage, game stats).

## **Phase 8: Deployment**
- [ ] Package and deploy the application:
  - [ ] Host the backend on a cloud platform (e.g., AWS, Heroku).
  - [ ] Serve the web UI alongside the backend.
  - [ ] Add CI/CD pipelines for automated testing and deployment.
- [ ] Ensure the system is scalable:
  - [ ] Optimize for performance under larger workloads.
  - [ ] Monitor and debug any deployment issues.

## **Beyond Phase 8**
- [ ] Upgrade any part of the system:
  - [ ] Add new games to the casino.
  - [ ] Improve the analytics layer with machine learning.
  - [ ] Enhance the frontend with modern frameworks like React or Vue.
  - [ ] Scale up deployment for real-world use cases.
