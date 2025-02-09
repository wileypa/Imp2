import matplotlib.pyplot as plt

sequence_lengths = [500, 1000, 2000, 3000, 4000, 5000]
times = [1.1467, 4.9203, 20.4309, 47.5140, 87.0305, 136.3115]

plt.figure(figsize=(8, 6))

plt.plot(times, sequence_lengths, marker='o', linestyle='-', color='b', label="Time taken")

plt.xscale('log')
plt.xticks(times, [f'{time:.2f}' for time in times])
plt.yticks(sequence_lengths)

plt.xlabel('Time Taken (seconds)')
plt.ylabel('Sequence length')
plt.title('Time Taken vs Sequence Length')

plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()

plt.savefig('time_vs_sequence_length.png', dpi=300)
plt.close()
