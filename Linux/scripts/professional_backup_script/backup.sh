#!/bin/bash
# A simple backup script that copies files from a source directory to a backup directory.


#check if the correct number of arguments is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_directory> <backup_directory>" >&2
    exit 1
fi

# assign arguments to variables
SOURCE_DIR="$1"
DEST_DIR="$2"

#check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Source directory '$SOURCE_DIR' does not exist." >&2
    exit 1
fi
#check if destination directory exists, if not create it
if [ ! -d "$DEST_DIR" ]; then
    echo "Destination directory '$DEST_DIR' does not exist. Creating it..."
    mkdir -p "$DEST_DIR"
fi


#create a timestamped filename for the backup
TIMESTAMP=$(date +"%Y-%m-%d-%H-%M-%S")
FILENAME="backup-$TIMESTAMP.tar.gz"

#print status message
echo "Backing up '$SOURCE_DIR' to '$DEST_DIR/$FILENAME'..."
# create the backup using tar
tar -czvf "$DEST_DIR/$FILENAME" "$SOURCE_DIR" 

#check if the tar command was successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully."
    echo "Backup file: $DEST_DIR/$FILENAME"
else
    echo "Backup failed. Please check for errors." >&2
    exit 1
fi







    



