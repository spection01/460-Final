def optimize_email_schedule(emails, max_days):
    """
    Figure out the best email sending schedule to maximize conversions.
    emails: list of (conversion_rate, cooldown_days, deadline)
    """
    n = len(emails)

    # Use bitmask DP - dp[day][sent_emails] = best score so far
    dp = {}
    came_from = {}  # track how we got to each state

    dp[(0, 0)] = 0.0

    for day in range(max_days + 1):
        for sent_mask in range(1 << n):
            if (day, sent_mask) not in dp:
                continue

            current_score = dp[(day, sent_mask)]

            # Try sending each unsent email
            for email_idx in range(n):
                if sent_mask & (1 << email_idx):
                    continue  # already sent this one

                conv_rate, cooldown, deadline = emails[email_idx]

                # Can we still send this email
                if day > deadline or day + cooldown > max_days:
                    continue

                next_day = day + cooldown
                new_mask = sent_mask | (1 << email_idx)
                new_score = current_score + conv_rate

                state = (next_day, new_mask)
                if state not in dp or new_score > dp[state]:
                    dp[state] = new_score
                    came_from[state] = (day, sent_mask, email_idx)

    # Find best final state
    best_score = 0
    best_state = None
    for state, score in dp.items():
        if score > best_score:
            best_score = score
            best_state = state

    # Reconstruct the schedule
    schedule = []
    current = best_state
    while current in came_from:
        prev_day, prev_mask, email_id = came_from[current]
        schedule.append((email_id, prev_day))
        current = (prev_day, prev_mask)

    schedule.reverse()
    return best_score, schedule