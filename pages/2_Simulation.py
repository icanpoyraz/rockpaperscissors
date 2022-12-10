import streamlit as st
import random
import time

st.title("Rock, Paper, Scissors - Simulation")

st.subheader('Set the simulation settings below')

strategy = st.selectbox("Pick your strategy", ('Rely on the estimation', 'Always Rock', 'Always Paper', ' Always Scissors', 'Random'))

games_played = st.number_input('Set the number of games played for the simulation (max: 1000)', step=10, value=50, max_value=1000)

st.subheader('Set the estimation accuracy below')

estimation_accuracy = st.slider('Estimation Accuracy', min_value=0, max_value=100, value=70, step=5)

@st.experimental_memo
def start_new_game():
  player_2 = random.random()
  roll_1 = random.random()
  roll_2 = random.random()
  roll_3 = random.random()
  
  if player_2 < 0.33:
    player_2_label="Rock"
    player_2_other=["Paper", "Scissors"]
  elif player_2 >= 0.33 and player_2 < 0.66:
    player_2_label="Paper"
    player_2_other=["Rock", "Scissors"]
  else:
    player_2_label="Scissors"
    player_2_other=["Rock", "Paper"]
  
  if roll_1 > 1 - estimation_accuracy/100:
    player_2_estimate=player_2_label
  else:
    if roll_2 < 0.5:
      player_2_estimate=player_2_other[0]
    else:
      player_2_estimate=player_2_other[1]

  if strategy == 'Rely on the estimation':
    moves = ["Rock", "Paper", "Scissors"]
    winner_moves = ["Paper", "Scissors", "Rock"]
    player_1_label = winner_moves[moves.index(player_2_estimate)]
  elif strategy == 'Always Rock':
    player_1_label = 'Rock'
  elif strategy == 'Always Paper':
    player_1_label = 'Paper'
  elif strategy == 'Always Scissors':
    player_1_label = 'Scissors'
  else:
    if roll_3 < 0.33:
      player_1_label="Rock"
    elif roll_3 >= 0.33 and roll_3 < 0.66:
      player_1_label="Paper"
    else:
      player_1_label="Scissors"

  if player_1_label == 'Rock' and player_2_label == 'Rock':
    result = 'Draw'
  elif player_1_label == 'Rock' and player_2_label == 'Paper':
    result = 'Player 2 wins!'
  elif player_1_label == 'Rock' and player_2_label == 'Scissors':
    result = 'Player 1 wins!'
  elif player_1_label == 'Paper' and player_2_label == 'Rock':
    result = 'Player 1 wins!'
  elif player_1_label == 'Paper' and player_2_label == 'Paper':
    result = 'Draw'
  elif player_1_label == 'Paper' and player_2_label == 'Scissors':
    result = 'Player 2 wins!'
  elif player_1_label == 'Scissors' and player_2_label == 'Rock':
    result = 'Player 2 wins!'
  elif player_1_label == 'Scissors' and player_2_label == 'Paper':
    result = 'Player 1 wins!'
  else:
    result = 'Draw'

  return result

player_1_win = 0
player_2_win = 0
draw = 0
games = 1

if st.button('Run simulation'):
  bar = st.progress(0)
  latest_iteration = st.empty()
  for games in range(games_played + 1):
    latest_iteration.text(f'{int((games/games_played)*100)} % completed...')
    bar.progress(games/games_played)
    time.sleep(0.1)
    if games == games_played:
      break
    start_new_game()
    result = start_new_game()
    if result == 'Player 1 wins!':
      player_1_win += 1
    elif result == 'Player 2 wins!':
      player_2_win += 1
    else:
      draw += 1
    st.experimental_memo.clear()

  st.subheader('Simulation results')
  st.write('Number of games played: ' + str(games))
  st.write('Player 1 strategy: ' + str(strategy))
  st.success('Player 1 wins: ' + str(player_1_win))
  st.success('Player 1 wins percentage: ' + str((player_1_win/games)*100) + '%')
  st.error('Player 2 wins: ' + str(player_2_win))
  st.error('Player 2 wins percentage: ' + str((player_2_win/games)*100) + '%')
  st.warning('Draws: ' + str(draw))
  st.warning('Draws percentage: ' + str((draw/games)*100) + '%')
