#!/bin/bash

# Exit the script if any command fails
set -e

# Check if a commit message is provided
if [ -z "$1" ]; then
  echo "Error: Commit message is required."
  echo "Usage: ./git_push.sh \"Your commit message\""
  exit 1
fi

# Store the commit message from the first argument
commit_message="$1"

# Add all changes to staging
echo "Adding changes to staging..."
git add .

# Commit the changes
echo "Committing changes..."
git commit -m "$commit_message"

# Push to the 'origin' branch
echo "Pushing to origin..."
git push origin main  # Replace 'main' with your branch name if it's different

# Success message
echo "Code successfully pushed to GitHub!"
