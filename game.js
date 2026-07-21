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

// Virtual File Explorer Engine
let virtualFS = null;
let currentFSPath = [];

function getFSNodeAtPath(path) {
    let current = virtualFS;
    for (const folder of path) {
        if (!current || current.type !== 'directory') return null;
        const found = current.children.find(child => child.name === folder);
        if (!found) return null;
        current = found;
    }
    return current;
}

function renderExplorer() {
    const grid = document.querySelector('.explorer-grid');
    const pathText = document.querySelector('.explorer-path');
    if (!grid || !pathText) return;

    // Render path breadcrumb
    pathText.textContent = `Path: /${currentFSPath.join('/')}`;

    // Get current directory contents
    const node = getFSNodeAtPath(currentFSPath);
    if (!node || node.type !== 'directory') {
        grid.innerHTML = '<div style="color: var(--accent-red); padding: 10px;">[ERROR] File system path corrupt.</div>';
        return;
    }

    grid.innerHTML = '';

    // 1. Add "parent directory" link if not root
    if (currentFSPath.length > 0) {
        const parentItem = document.createElement('div');
        parentItem.className = 'explorer-item parent';
        parentItem.innerHTML = `
            <div class="item-icon">📁</div>
            <div class="item-name">[ .. ]</div>
        `;
        parentItem.addEventListener('dblclick', () => {
            currentFSPath.pop();
            playBeep(450, 50);
            renderExplorer();
        });
        grid.appendChild(parentItem);
    }

    // 2. Render children nodes (directories first, then files)
    const sortedChildren = [...node.children].sort((a, b) => {
        if (a.type === b.type) return a.name.localeCompare(b.name);
        return a.type === 'directory' ? -1 : 1;
    });

    sortedChildren.forEach(child => {
        const item = document.createElement('div');
        item.className = `explorer-item ${child.type}`;
        const icon = child.type === 'directory' ? '📁' : '📄';
        item.innerHTML = `
            <div class="item-icon">${icon}</div>
            <div class="item-name">${child.name}</div>
        `;

        // Double click actions
        item.addEventListener('dblclick', () => {
            if (child.type === 'directory') {
                currentFSPath.push(child.name);
                playBeep(450, 50);
                renderExplorer();
            } else {
                playBeep(550, 70);
                openFileModal(child.name, child.content);
            }
        });

        grid.appendChild(item);
    });
}

function initFileExplorer() {
    const explorerEl = document.getElementById('file-explorer-widget');
    if (!explorerEl) return;

    try {
        const fsData = JSON.parse(explorerEl.getAttribute('data-files') || '{}');
        virtualFS = fsData;
        currentFSPath = [];
        renderExplorer();
    } catch (e) {
        console.error('Failed to initialize virtual file system:', e);
    }
}

// Modal text viewer controls
function openFileModal(filename, content) {
    let overlay = document.querySelector('.modal-overlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.className = 'modal-overlay';
        overlay.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <span class="modal-title"></span>
                    <button class="modal-close">CLOSE [X]</button>
                </div>
                <div class="text-viewer">
                    <pre class="line-numbers"></pre>
                    <pre class="text-content"></pre>
                </div>
            </div>
        `;
        document.body.appendChild(overlay);

        // Add close event
        const closeBtn = overlay.querySelector('.modal-close');
        closeBtn.addEventListener('click', closeFileModal);
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) closeFileModal();
        });
    }

    // Set content and filename
    overlay.querySelector('.modal-title').textContent = `📄 VIEWING: ${filename}`;
    
    // Generate line numbers
    const lines = content.split('\n');
    const lineNumsText = lines.map((_, idx) => idx + 1).join('\n');
    
    overlay.querySelector('.line-numbers').textContent = lineNumsText;
    overlay.querySelector('.text-content').textContent = content;

    overlay.style.display = 'flex';
}

function closeFileModal() {
    const overlay = document.querySelector('.modal-overlay');
    if (overlay) {
        playBeep(350, 60);
        overlay.style.display = 'none';
    }
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

    // 4. Initialize File Explorer if element exists
    initFileExplorer();

    // 5. Set up input submit handlers
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

function typeWriterEffect(element) {
    return new Promise((resolve) => {
        const card = element.closest('.dialogue-card');
        if (card) {
            card.style.display = 'flex';
            // Scroll dialogue container dynamically to keep new feeds in view
            const mainStage = document.querySelector('.main-stage-panel');
            if (mainStage) {
                mainStage.scrollTop = mainStage.scrollHeight;
            }
        }
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

// SLA Indicator Logic: Decreases as player goes deeper into the incident
function updateSLAWidget(currentCleanName) {
    const slaBar = document.querySelector('.sla-bar');
    const slaValue = document.querySelector('.sla-value');
    if (!slaBar) return;
    
    const stageContainer = document.getElementById('stage-container');
    if (!stageContainer) {
        // Clear page
        slaBar.style.width = '99.9%';
        slaBar.style.backgroundColor = 'var(--accent-green)';
        if (slaValue) {
            slaValue.textContent = '99.90% (SLA SAFE)';
            slaValue.style.color = 'var(--accent-green)';
        }
        return;
    }
    
    const stageNum = parseInt(stageContainer.getAttribute('data-stage'), 10) || 1;
    
    if (stageNum === 20) {
        slaBar.style.width = '99.9%';
        slaBar.style.backgroundColor = 'var(--accent-green)';
        if (slaValue) {
            slaValue.textContent = '99.90% (SLA SAFE)';
            slaValue.style.color = 'var(--accent-green)';
        }
        return;
    }
    
    // SLA drops slightly per stage
    const percent = 99.90 - ((stageNum - 1) * 0.25);
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
