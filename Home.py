import streamlit as st

st.title("Rock, Paper, Scissors")
st.write('by Ihsancan Ozpoyraz - 2022')

st.write('This mini-game was programmed to illustrate the concept of decision-making under uncertainty for the blog post titled "Rock, Paper and Scissors: Which one to go with?"')
st.write('Here is the link for the blog post: [link here]')

st.write('In the single-play mode, the game allows you (Player 1) to get estimates about the possible move of your opponent (Player 2) in the next round before the round starts. In this way, you can pick the winning move and hope to come out on top. The estimates are generated randomly however, an estimation accuracy that should be set by you at the beginning of the game is taken into account (the aim is to mimic an imperfect AI-powered predictive model). You can vary this percentage between 0% and 100% (the default setting is 70%). Eventually, the estimate could or not be correct on a single instance (unless you set the estimation accuracy to 100%) and relying on the estimate provided could let you either win or lose on the round. You can try it yourself; select "Single Play" on the menu left-hand side, and follow the instructions to play.
')
         
st.write('Losing a game based on a false estimation does not mean estimations are useless. In the long run, your total number of wins is expected to converge to the estimation accuracy that has been set and you may anticipate dominating the opponent as the rounds continue (unless you set the estimation accuracy below 50%). For example, after 10 rounds you may still not be dominating the game despite 70% estimate accuracy (e.g., 4 wins, 4 losses, 2 draws - see below example). However, as the game progresses and the number of rounds increases, you are bound to get more wins and your rate of wins should eventually become closer to the estimation accuracy that has been set at the beginning (see below example). Go ahead and try this yourself; select "Simulation" on the game menu and run a simulation. You can set the number of rounds (up to 1000). You will notice that the more rounds you play, the closer your winning rate will get to the estimation accuracy (unless you pick a strategy other than "rely on the estimation"). If you want to experiment with different outcomes, you can pick different strategies: Always rock, always paper, always scissors or random.')

st.write('Essentially, if the estimations you get are proven to be reasonably reliable and you are consistent with a reasonable decision strategy (i.e., rely on the estimate and play accordingly), you can expect the strategy to pay off in the long run.')
