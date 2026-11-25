import os

# Verified count: 119 characters (119 UTF-8 bytes).
LINE = "No deadline was met today. The deadlines formed a union, filed a grievance, and are now on strike until further notice."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(f"Wrote {len(LINE.encode('utf-8'))} bytes to {output_path}")
