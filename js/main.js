document.getElementById('birthdayForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const fullName = document.getElementById('fullName').value.trim();
    const birthDate = new Date(document.getElementById('birthDate').value);
    const correctDate = new Date('2003-01-18');
    
    if (fullName === 'Ngô Khánh Linh' && 
        birthDate.getDate() === correctDate.getDate() &&
        birthDate.getMonth() === correctDate.getMonth() &&
        birthDate.getFullYear() === correctDate.getFullYear()) {
        
        window.location.href = 'birthday.html';
    } else {
        document.getElementById('errorMessage').classList.remove('d-none');
    }
}); 