def greedy_email_send(emails, campaign_days):
    """Quick greedy approach - just pick the best email each time"""

    sent_emails = set()
    current_day = 0
    total_score = 0
    schedule = []

    while current_day <= campaign_days:
        # Find the best email we can send right now
        best_email = None
        best_rate = 0

        for i, (rate, cooldown, deadline) in enumerate(emails):
            if i in sent_emails or current_day > deadline:
                continue
            if rate > best_rate:
                best_rate = rate
                best_email = i

        if best_email is None:
            break  # nothing left to send

        # Send it
        _, cooldown, _ = emails[best_email]
        sent_emails.add(best_email)
        schedule.append((best_email, current_day))
        total_score += best_rate
        current_day += cooldown

    return total_score, schedule