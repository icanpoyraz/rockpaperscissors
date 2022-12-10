import streamlit as st
import random

st.title("Rock, Paper, Scissors - Single Play")

st.subheader('Set the estimation accuracy below')

estimation_accuracy = st.slider('Estimation Accuracy', min_value=0, max_value=100, value=70, step=5)

@st.experimental_memo
def start_new_game():
  player_2 = random.random()
  roll_1 = random.random()
  roll_2 = random.random()
  
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
  
  return player_2_label, player_2_estimate, player_2, player_2_other, roll_1, roll_2

st.subheader('Start a new game by clicking below button')

if st.button('Start New Game'):
  st.success('Alright, let the game begin')
  #st.write('player_2: ' + str(player_2))
  #st.write('roll_1: ' + str(roll_1))
  #st.write('roll_2: ' + str(roll_2))
  #st.write('player_2_label: ' + str(player_2_label))
  #st.write('player_2_estimate: ' + str(player_2_estimate))
  #st.write('player_2_other: ' + str(player_2_other))

player_2_label, player_2_estimate, player_2, player_2_other, roll_1, roll_2 = start_new_game()

st.subheader('Click [Get Estimation] button if you would like an estimate about Player 2 move before deciding your move')

if st.button('Get Estimation'):
  st.warning('Estimated Player 2 move is: ' + str(player_2_estimate) + ' (Estimation accuracy = ' + str(estimation_accuracy) + ')')

st.subheader('Now it is your turn, pick your move and click [Play] button below')

player_1_label = st.selectbox("Pick your move", ('Rock', 'Paper', 'Scissors'))

if st.button('Play'):
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
  st.caption('Your move is ' + str(player_1_label))
  st.caption('The actual Player 2 move is ' + str(player_2_label) + ' (estimated move was ' + str(player_2_estimate) + ')')
  if result == 'Player 1 wins!':
    st.success(result)
  elif result == 'Player 2 wins!':
    st.error(result)
  else:
    st.warning(result)

st.subheader('Click [Reset] button below before starting a new game!')

if st.button('Reset'):
   st.experimental_memo.clear()
