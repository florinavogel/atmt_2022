import matplotlib.pyplot as plt

# BLEU score
beam_size = range(26)[1:]
bleu_score = [17.1, 19.0, 19.1, 18.6, 20.0,19.7, 20.9, 20.8, 22.0, 22.2, 22.6, 22.2, 22.7, 22.6, 22.1, 22.1, 21.9, 21.9,
              21.8, 21.8, 21.5, 21.5, 21.3, 21.2, 21.4]
brevity_penalty = [1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 0.988, 0.975,
                   0.949, 0.934, 0.920, 0.920, 0.873, 0.864, 0.848, 0.842, 0.831, 0.820, 0.790]

plt.plot(beam_size, bleu_score, '-ok', color='red')
plt.xlabel('beam size')
plt.ylabel('BLEU score')
plt.title('BLEU score depending on beam size')
# plt. show()

# BLEU score + brevity penalty
# Creating plot with bleu score
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('beam size')
ax1.set_ylabel('BLEU score', color=color)
ax1.plot(beam_size, bleu_score, color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

# add twin axis with brevity penalty
ax2 = ax1.twinx()

color = 'tab:green'
ax2.set_ylabel('brevity penalty', color=color)
ax2.plot(beam_size, brevity_penalty, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

# Adding title
plt.title('Bleu score and brevity penalty depending on beam size')

# Show plot
plt.show()
