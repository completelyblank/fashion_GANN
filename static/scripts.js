document.getElementById('generate-button').addEventListener('click', () => {
    fetch('http://localhost:5000/generate', {
        method: 'POST'
    })
    .then(response => response.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        document.getElementById('generated-image').src = url;
    })
    .catch(error => console.error('Error:', error));
});
