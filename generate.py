
import os
import random
import subprocess
from datetime import date, timedelta

# Simulated contribution date range
start_date = date(2025, 1, 1)
end_date = date(2026, 10, 20)

random.seed(42)
current_date = start_date
total_commits = 0

while current_date <= end_date:

    # Randomly choose active days
    if random.random() < 0.65:

        # Generate 1 to 4 demo commits
        commits_today = random.randint(1, 4)

        for i in range(commits_today):

            timestamp = (
                f"{current_date.isoformat()}"
                f"T{10 + i:02d}:00:00+05:00"
            )

            with open("activity.txt", "a") as file:
                file.write(
                    f"Simulated activity: "
                    f"{current_date} - {i + 1}\n"
                )

            subprocess.run(
                ["git", "add", "activity.txt"],
                check=True
            )

            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = timestamp
            env["GIT_COMMITTER_DATE"] = timestamp

            subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    f"Demo activity {current_date}"
                ],
                env=env,
                check=True,
                stdout=subprocess.DEVNULL
            )

            total_commits += 1

    current_date += timedelta(days=1)

print(f"Created {total_commits} simulated commits.")
print("Done!")
