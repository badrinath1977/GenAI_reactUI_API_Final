# Revert back git add . 
-- git restore --staged .


# Add just the .gitignore
git add .gitignore

# Add only modified files you want
git add package.json vite.config.ts

# Check what’s staged
git status

# Commit when ready
git commit -m "your message"
git push
