from DP import optimize_email_schedule
from greedy import greedy_email_send

# Full test dataset
test_datasets = [
    # Test Case #1
    (
        [
            (0.5, 2, 6),
            (0.6, 3, 5),
            (0.3, 1, 4),
            (0.7, 2, 8)
        ],
        10
    ),
    # Test Case #2
    (
        [
            (0.15, 2, 6),
            (0.16, 3, 5),
            (0.13, 1, 4),
            (0.17, 2, 8)
        ],
        10
    ),
    # Test Case #3
    (
        [
            (0.2, 2, 3),
            (0.15, 3, 5),
            (0.16, 4, 18),
            (0.09, 4, 10),
            (0.1, 3, 22),
            (0.12, 5, 7),
            (0.18, 5, 25),
            (0.22, 4, 30)
        ],
        30
    ),
    # Test Case #4
    (
        [
            (0.17, 2, 20),
            (0.09, 1, 24),
            (0.18, 2, 4),
            (0.23, 3, 4),
            (0.15, 3, 23),
            (0.15, 5, 6),
            (0.19, 5, 20),
            (0.14, 4, 27)
        ],
        30
    ),
    # Test Case #5
    (
        [
            (0.09, 1, 23),
            (0.14, 4, 15),
            (0.14, 1, 23),
            (0.18, 1, 3),
            (0.13, 3, 27),
            (0.22, 2, 8),
            (0.09, 4, 6),
            (0.13, 3, 16)
        ],
        30
    )
]

def run_all_tests():
    for idx, (emails, D) in enumerate(test_datasets, 1):
        print(f"--- Test Case #{idx} ---")
        dp_score, dp_sched = optimize_email_schedule(emails, D)
        g_score, g_sched = greedy_email_send(emails, D)
        print(f"DP Score: {dp_score:.2f}, Schedule: {dp_sched}")
        print(f"Greedy Score: {g_score:.2f}, Schedule: {g_sched}")
        print()

if __name__ == "__main__":
    run_all_tests()
