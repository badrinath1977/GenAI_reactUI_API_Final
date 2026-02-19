# First Time for setup

-- npm install


# Delete Dist folder before building 
-- Remove-Item -Recurse -Force dist

#Build App and create Dist folder
-- npx vite build
-- npm run build 
-- npm run dev (for UI)

# If you want clean builds every time, add:

--"clean": "rimraf dist",
--"rebuild": "npm run clean && npm run build"
## Run this 
-- npm install -D rimraf



