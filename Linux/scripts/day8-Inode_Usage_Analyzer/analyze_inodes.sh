#!/usr/bin/bash
# Analyze inode usage on a specified filesystem and report if usage exceeds a given threshold.

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filesystem> (e.g., /dev/sda1 or /home)" >&2
    exit 1
fi

# Assign the argument to a variable
DIR_PATH="$1"

# 3. Check if TARGET_DIR is a valid, existing directory. If not, show error and exit.
if [ ! -d "$DIR_PATH" ]; then
    echo "Error: '$DIR_PATH' is not a valid directory." >&2
    exit 1
fi
# 4. Print a clear header for the report.
echo "Inode Usage Report for '$DIR_PATH'"
echo "-----------------------------------"
# 5. Find all subdirectories within TARGET_DIR.
find "$DIR_PATH" -mindepth 1 -type d | while read -r subdir; do
# 6. For each subdirectory found, count the number of files inside it.
    count=$(find "$subdir" -maxdepth 1 -type f | wc -l)
# 7. Format the output to show the count and the directory name.
    echo "$count files in $subdir"
# 8. Sort the final output numerically in descending order to show the largest consumers first.
done | sort -nr

