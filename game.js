// Operation: Blackout - Core Game Engine (game.js)

// Helper: Calculate SHA-256 hash of a string
async function calculateSHA256(message) {
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

// Audio Context helper for Retro Terminal Beeps
let audioCtx = null;
function playBeep(frequency, duration, type = 'sine') {
    try {
        if (!audioCtx) {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        const oscillator = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();

        oscillator.type = type;
        oscillator.frequency.value = frequency;
        
        gainNode.gain.setValueAtTime(0.05, audioCtx.currentTime); // Low volume
        gainNode.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + duration / 1000);

        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);

        oscillator.start();
        oscillator.stop(audioCtx.currentTime + duration / 1000);
    } catch (e) {
        console.warn('Audio feedback failed or blocked by browser policy:', e);
    }
}

// Get current filename from URL
function getCurrentFilename() {
    const path = window.location.pathname;
    const filename = path.substring(path.lastIndexOf('/') + 1);
    return filename || 'index.html';
}

// Initialize Page Guard & Loading state
document.addEventListener('DOMContentLoaded', async () => {
    const currentFile = getCurrentFilename();
    const cleanName = currentFile.replace('.html', '');
    
    // 1. Route Guard
    const isMain = currentFile === 'index.html' || currentFile === '';
    const isStage1 = cleanName === 'a7f93b2c';
    
    if (!isMain && !isStage1) {
        const authKey = 'auth_' + cleanName;
        if (localStorage.getItem(authKey) !== 'true') {
            console.warn('Access Denied. Redirecting to terminal lobby...');
            window.location.href = 'index.html';
            return;
        }
    }

    // 2. Register current page in history for resume feature
    if (!isMain) {
        localStorage.setItem('current_stage_file', currentFile);
    }

    // 3. Trigger text typing effect for dialogue or system log
    const typingElements = document.querySelectorAll('.typing-text');
    for (const el of typingElements) {
        await typeWriterEffect(el);
    }

    // 4. Set up input submit handlers
    const terminalInput = document.querySelector('.terminal-input');
    const submitBtn = document.querySelector('.submit-btn');
    const stageContainer = document.getElementById('stage-container');

    if (terminalInput && stageContainer) {
        // Auto-focus terminal input
        terminalInput.focus();
        document.addEventListener('click', () => {
            terminalInput.focus();
        });

        // Submit listener
        const handleSubmit = async () => {
            const val = terminalInput.value.trim();
            if (!val) return;
            
            terminalInput.value = ''; // Clear prompt
            appendLog(`investigator@his-system:~$ ${val}`, 'system-log');
            
            // Normalize: lowercase, remove spaces
            const normalizedVal = val.toLowerCase().replace(/\s+/g, '');
            const inputHash = await calculateSHA256(normalizedVal);
            
            const expectedHash = stageContainer.getAttribute('data-verify');
            
            if (inputHash === expectedHash) {
                // SUCCESS
                playBeep(600, 100);
                setTimeout(() => playBeep(850, 150), 100);
                
                appendLog('CRITICAL: VERIFICATION SUCCESSFUL. DECRYPTING NEXT NODE...', 'success-log');
                
                // Calculate next stage filename
                const nextFileHash = (await calculateSHA256(cleanName + normalizedVal)).substring(0, 8);
                const nextFilename = nextFileHash + '.html';
                
                // Authorize next stage
                localStorage.setItem('auth_' + nextFileHash, 'true');
                localStorage.setItem('current_stage_file', nextFilename);
                
                appendLog(`REDIRECTING TO: ${nextFilename}`, 'success-log');
                
                setTimeout(() => {
                    window.location.href = nextFilename;
                }, 1500);
            } else {
                // FAILURE
                playBeep(180, 250, 'sawtooth');
                appendLog('ERROR: INVALID PASSCODE OR LOGICAL ANOMALY DETECTED.', 'error-log');
                
                // Shake effect on container
                const grid = document.querySelector('.main-stage-panel');
                if (grid) {
                    grid.classList.add('shake');
                    setTimeout(() => grid.classList.remove('shake'), 500);
                }
            }
        };

        submitBtn.addEventListener('click', handleSubmit);
        terminalInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                handleSubmit();
            }
        });
    }

    // Dynamic SLA Indicator calculation
    updateSLAWidget(cleanName);
});

// Helper: Typewriter typing animation
function typeWriterEffect(element) {
    return new Promise((resolve) => {
        const text = element.getAttribute('data-text') || element.textContent;
        element.textContent = '';
        element.classList.add('cursor-blink');
        
        let index = 0;
        const speed = 25; // ms per character
        
        function type() {
            if (index < text.length) {
                element.textContent += text.charAt(index);
                index++;
                setTimeout(type, speed);
            } else {
                element.classList.remove('cursor-blink');
                resolve();
            }
        }
        type();
    });
}

// Helper: Append log to terminal body
function appendLog(message, className) {
    const terminalBody = document.querySelector('.terminal-body');
    if (!terminalBody) return;
    
    const output = terminalBody.querySelector('.terminal-output');
    if (!output) return;
    
    const p = document.createElement('p');
    p.className = className || '';
    p.textContent = message;
    
    output.appendChild(p);
    
    // Auto scroll to bottom
    terminalBody.scrollTop = terminalBody.scrollHeight;
}

// SLA Indicator Logic: Decreases as player goes deeper into the incident, representing urgency
function updateSLAWidget(currentCleanName) {
    const slaBar = document.querySelector('.sla-bar');
    const slaValue = document.querySelector('.sla-value');
    if (!slaBar) return;
    
    // Stage filename list for SLA scaling
    const stages = [
        "a7f93b2c", "b4bcdd0d", "83e5e934", "13b3bfc6", "48b42551",
        "db590ac0", "4ae9c668", "e3ad4d0a", "cee89b5e", "524cfb66",
        "e3307ab7", "16417f5b", "94e06050", "c70ec350", "aac380d4",
        "ef5ad16e", "0e3d9fd2", "58addc3e", "60268820", "6c46331e", "8505f529"
    ];
    
    const idx = stages.indexOf(currentCleanName);
    if (idx === -1) {
        slaBar.style.width = '100%';
        if (slaValue) slaValue.textContent = '100.00%';
        return;
    }
    
    if (idx === 20) { // Clear screen
        slaBar.style.width = '99.9%';
        slaBar.style.backgroundColor = 'var(--accent-green)';
        if (slaValue) {
            slaValue.textContent = '99.90% (SLA SAFE)';
            slaValue.style.color = 'var(--accent-green)';
        }
        return;
    }
    
    // Simulate SLA dropping down as time goes by, representing mounting crisis
    // Starting at 99.90%, dropping to ~95% near stage 19
    const percent = 99.90 - (idx * 0.25);
    slaBar.style.width = `${percent}%`;
    if (slaValue) {
        slaValue.textContent = `${percent.toFixed(2)}%`;
        if (percent < 98.5) {
            slaValue.style.color = 'var(--accent-red)';
            slaBar.style.backgroundColor = 'var(--accent-red)';
        } else {
            slaValue.style.color = 'var(--accent-magenta)';
            slaBar.style.backgroundColor = 'var(--accent-magenta)';
        }
    }
}

// Lobby functions
function startNewGame() {
    localStorage.clear();
    localStorage.setItem('auth_a7f93b2c', 'true'); // Auth Stage 1
    window.location.href = 'a7f93b2c.html';
}

function resumeGame() {
    const currentFile = localStorage.getItem('current_stage_file');
    if (currentFile) {
        window.location.href = currentFile;
    } else {
        startNewGame();
    }
}

function checkResumeAvailable() {
    const resumeBtn = document.getElementById('resume-btn');
    const currentFile = localStorage.getItem('current_stage_file');
    if (resumeBtn) {
        if (currentFile && currentFile !== 'index.html') {
            resumeBtn.style.display = 'inline-block';
        } else {
            resumeBtn.style.display = 'none';
        }
    }
}

// Trigger resume button visibility check on index.html
document.addEventListener('DOMContentLoaded', () => {
    checkResumeAvailable();
});

// Clipboard Copy Helper with visual feedback and sound
function copyToClipboard(text, btn) {
    if (!text) return;
    
    function showFeedback() {
        playBeep(700, 60); // Soft beep
        const originalText = btn.textContent;
        btn.textContent = 'COPIED!';
        btn.style.borderColor = 'var(--accent-green)';
        btn.style.color = 'var(--accent-green)';
        
        setTimeout(() => {
            btn.textContent = originalText;
            btn.style.borderColor = '';
            btn.style.color = '';
        }, 1200);
    }

    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(showFeedback).catch(err => {
            console.error('Failed to copy using clipboard API: ', err);
            fallbackCopy(text);
        });
    } else {
        fallbackCopy(text);
    }
    
    function fallbackCopy(val) {
        const textArea = document.createElement("textarea");
        textArea.value = val;
        textArea.style.top = "0";
        textArea.style.left = "0";
        textArea.style.position = "fixed";
        textArea.style.opacity = "0";
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        try {
            document.execCommand('copy');
            showFeedback();
        } catch (err) {
            console.error('Fallback copy failed: ', err);
        }
        document.body.removeChild(textArea);
    }
}
