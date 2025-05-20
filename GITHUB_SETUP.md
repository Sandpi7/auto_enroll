# GitHub Repository Setup Guide

Follow these steps to connect your local repository to GitHub:

## Steps to Initialize the Repository

1. **Create a new repository on GitHub**
   - Go to [GitHub](https://github.com) and sign in
   - Click the "+" icon in the top right and select "New repository"
   - Name the repository `auto_enroll` (or your preferred name)
   - Add a description (optional)
   - Keep it as a Public repository (or make it Private if you prefer)
   - DO NOT initialize with README, .gitignore, or license files
   - Click "Create repository"

2. **Connect your local repository to GitHub**
   - After creating the repository, GitHub will show you setup instructions
   - Copy and run the following commands in your terminal (replace YOUR_USERNAME with your actual GitHub username):

   ```powershell
   git remote add origin https://github.com/YOUR_USERNAME/auto_enroll.git
   git push -u origin master
   ```

3. **Push GitHub Actions workflow**
   - The repository already includes GitHub Actions workflow in `.github/workflows/build.yml`
   - This will automatically build the executable when you push to the main branch

4. **Verify the repository**
   - Go to your GitHub repository page
   - Check that all files have been pushed successfully
   - Navigate to the "Actions" tab to see if the workflow is running

## Setting up GitHub Secrets for Code Signing

Your build workflow requires the following secrets for code signing:

1. `WINDOWS_CERTIFICATE_BASE64`: Your code signing certificate encoded in Base64
2. `WINDOWS_CERTIFICATE_PASSWORD`: The password for your code signing certificate
3. `WINDOWS_CERTIFICATE_SHA1`: The SHA1 fingerprint of your certificate

To add these secrets:
- Go to your repository on GitHub
- Click on "Settings" > "Secrets and variables" > "Actions"
- Click "New repository secret" and add each of the secrets above with their corresponding values

## Next Steps

- Consider adding branch protection rules for your main branch
- Set up GitHub releases for versioned releases of your application
- Add contribution guidelines if you want others to contribute
