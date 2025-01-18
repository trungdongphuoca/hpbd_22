let flippedPieces = 0;

function flipPiece(piece, index) {
    if (!piece.classList.contains('flipped')) {
        piece.classList.add('flipped');
        flippedPieces++;
        
        if (flippedPieces === 9) {
            setTimeout(() => {
                document.getElementById('completeImage').classList.add('show');
                document.getElementById('puzzleCaption').classList.add('show');
            }, 600);
        }
    }
}

function nextImage(currentPage) {
    window.location.href = window.location.pathname + '?current_page=' + (currentPage + 1);
}

function prevImage(currentPage) {
    window.location.href = window.location.pathname + '?current_page=' + (currentPage - 1);
}

function closePopup() {
    const popup = document.getElementById('lovePopup');
    popup.classList.remove('show');
    setTimeout(() => {
        popup.style.display = 'none';
    }, 300);
}

// Initialize popup
document.addEventListener('DOMContentLoaded', function() {
    const popup = document.getElementById('lovePopup');
    setTimeout(() => popup.classList.add('show'), 100);
    
    // Close popup when clicking outside
    popup.addEventListener('click', function(e) {
        if (e.target === this) {
            closePopup();
        }
    });
    
    // Auto-flip center piece
    setTimeout(() => flipPiece(document.querySelectorAll('.puzzle-piece')[4], 4), 500);
}); 