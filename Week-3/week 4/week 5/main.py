from collections import deque

# Step 1: Initialize
application_inbox = deque()   # Queue (FIFO)
processed_history = []        # Stack (LIFO)

# Step 2: Ingest Data (messy input)
raw_applications = [" TechCorp ", "bio-gen", "  AlphaLabs", "FinTechX  "]

for app in raw_applications:
    clean_name = app.strip().lower()
    application_inbox.append(clean_name)

print("=== Applications Loaded into Queue ===")
print(application_inbox)
print()

# Step 3: Process (FIFO)
print("=== Processing Applications ===")

while application_inbox:
    current_app = application_inbox.popleft()  # FIFO
    print(f"Approving: {current_app}")
    processed_history.append(current_app)      # push to stack

print()

# Step 4: Undo (LIFO)
print("=== Undo Last פעולה ===")

if processed_history:
    last_app = processed_history.pop()  # LIFO
    print(f"Reverting approval for: {last_app}")
else:
    print("No applications to revert.")