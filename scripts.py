// Git workflow simulation
document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const workingDirectory = document.getElementById('working-directory').querySelector('.file-list');
    const stagingArea = document.getElementById('staging-area').querySelector('.file-list');
    const repository = document.getElementById('repository').querySelector('.commit-history');
    
    // Buttons
    const modifyBtn = document.getElementById('modify-btn');
    const stageBtn = document.getElementById('stage-btn');
    const commitBtn = document.getElementById('commit-btn');
    const resetBtn = document.getElementById('reset-btn');
    
    // Branch demo elements
    const createBranchBtn = document.getElementById('create-branch');
    const mergeBranchBtn = document.getElementById('merge-branch');
    const mainBranchCommits = document.querySelector('.main-branch .commits');
    const featureBranchCommits = document.querySelector('.branch-feature .commits');
    
    // Command cards
    const commandCards = document.querySelectorAll('.command-card');
    
    // Initialize state
    const files = ['index.html', 'style.css', 'script.js'];
    let modifiedFiles = [];
    let stagedFiles = [];
    let commitCount = 1;
    let featureBranchCreated = false;
    let featureCommits = 0;
    
    // Modify files
    modifyBtn.addEventListener('click', function() {
        if (modifiedFiles.length < files.length) {
            const fileToModify = files[modifiedFiles.length];
            modifiedFiles.push(fileToModify);
            
            const fileElement = workingDirectory.querySelector(`[data-file="${fileToModify}"]`);
            fileElement.classList.add('modified');
            
            // Enable stage button if there are modified files
            stageBtn.disabled = false;
            
            // Show visual feedback
            fileElement.style.transform = 'scale(1.1)';
            setTimeout(() => {
                fileElement.style.transform = 'scale(1.05)';
            }, 200);
        } else {
            alert('All files are already modified!');
        }
    });
    
    // Stage files
    stageBtn.addEventListener('click', function() {
        if (modifiedFiles.length > 0) {
            // Move the first modified file to staging
            const fileToStage = modifiedFiles.shift();
            stagedFiles.push(fileToStage);
            
            const fileElement = workingDirectory.querySelector(`[data-file="${fileToStage}"]`);
            fileElement.classList.remove('modified');
            
            // Create staged file element
            const stagedFileElement = document.createElement('div');
            stagedFileElement.className = 'file staged';
            stagedFileElement.textContent = fileToStage;
            stagedFileElement.dataset.file = fileToStage;
            stagingArea.appendChild(stagedFileElement);
            
            // Enable commit button if there are staged files
            commitBtn.disabled = false;
            
            // Disable stage button if no more modified files
            if (modifiedFiles.length === 0) {
                stageBtn.disabled = true;
            }
            
            // Show visual feedback
            stagedFileElement.style.transform = 'scale(1.1)';
            setTimeout(() => {
                stagedFileElement.style.transform = 'scale(1.05)';
            }, 200);
        }
    });
    
    // Commit files
    commitBtn.addEventListener('click', function() {
        if (stagedFiles.length > 0) {
            // Clear staging area
            stagingArea.innerHTML = '';
            
            // Create commit element
            commitCount++;
            const commitElement = document.createElement('div');
            commitElement.className = 'commit';
            commitElement.textContent = `Commit ${commitCount}`;
            repository.appendChild(commitElement);
            
            // Reset staged files
            stagedFiles = [];
            
            // Disable commit button
            commitBtn.disabled = true;
            
            // Show success animation
            commitElement.style.transform = 'scale(1.2)';
            setTimeout(() => {
                commitElement.style.transform = 'scale(1)';
            }, 300);
        }
    });
    
    // Reset all
    resetBtn.addEventListener('click', function() {
        // Reset modified files
        modifiedFiles = [];
        stagedFiles = [];
        
        // Reset UI
        workingDirectory.querySelectorAll('.file').forEach(file => {
            file.classList.remove('modified');
            file.style.transform = 'scale(1)';
        });
        stagingArea.innerHTML = '';
        
        // Reset repository to initial commit only
        repository.innerHTML = '<div class="commit">Initial commit</div>';
        commitCount = 1;
        
        // Disable buttons
        stageBtn.disabled = true;
        commitBtn.disabled = true;
    });
    
    // Branch demo functionality
    createBranchBtn.addEventListener('click', function() {
        if (!featureBranchCreated) {
            featureBranchCreated = true;
            
            // Create feature branch commits
            featureCommits = 2;
            featureBranchCommits.innerHTML = '';
            
            for (let i = 1; i <= featureCommits; i++) {
                const commitElement = document.createElement('div');
                commitElement.className = 'commit';
                commitElement.textContent = `F${i}`;
                featureBranchCommits.appendChild(commitElement);
            }
            
            // Enable merge button
            mergeBranchBtn.disabled = false;
            
            // Show animation
            featureBranchCommits.parentElement.style.transform = 'translateX(10px)';
            setTimeout(() => {
                featureBranchCommits.parentElement.style.transform = 'translateX(0)';
            }, 300);
        }
    });
    
    mergeBranchBtn.addEventListener('click', function() {
        if (featureBranchCreated) {
            // Add feature commits to main branch
            for (let i = 1; i <= featureCommits; i++) {
                const commitElement = document.createElement('div');
                commitElement.className = 'commit';
                commitElement.textContent = `C${mainBranchCommits.children.length + 1}`;
                mainBranchCommits.appendChild(commitElement);
                
                // Show animation for each new commit
                commitElement.style.transform = 'scale(1.2)';
                setTimeout(() => {
                    commitElement.style.transform = 'scale(1)';
                }, 300);
            }
            
            // Reset feature branch
            featureBranchCommits.innerHTML = '';
            featureBranchCreated = false;
            featureCommits = 0;
            
            // Disable merge button
            mergeBranchBtn.disabled = true;
        }
    });
    
    // Command card interactions
    commandCards.forEach(card => {
        card.addEventListener('click', function() {
            const command = this.dataset.command;
            
            // Visual feedback
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
            
            // Show tooltip or explanation
            alert(`Command: ${command}\n\n${this.querySelector('p').textContent}`);
        });
    });
    
    // Initialize button states
    stageBtn.disabled = true;
    commitBtn.disabled = true;
    mergeBranchBtn.disabled = true;
});