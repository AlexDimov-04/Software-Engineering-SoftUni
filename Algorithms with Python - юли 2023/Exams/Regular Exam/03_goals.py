def find_the_best_seq(goals):
    seq_length = len(goals)
    dp = [[goals[i]] for i in range(seq_length)]

    for i in range(1, seq_length):
        for j in range(i):
            if goals[i] >= goals[j] and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [goals[i]]

    best_seq = max(dp, key=len)
    return best_seq


goals_seq = [int(x) for x in input().split(', ')]

print(' '.join(map(str, find_the_best_seq(goals_seq))))
