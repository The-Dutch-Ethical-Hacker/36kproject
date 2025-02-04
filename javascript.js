// Start de camera en toon de feed op het scherm
async function setupCamera() {
    const videoElement = document.getElementById('video-feed');
    const cameraSelect = document.getElementById('camera-select');
    const selectedCamera = cameraSelect.value;

    const constraints = {
        video: {
            facingMode: selectedCamera // Kies voor de front camera of achter camera
        }
    };

    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        videoElement.srcObject = stream;
    } catch (error) {
        console.error("Camera could not be accessed:", error);
        alert("Er is een fout opgetreden bij het openen van de camera.");
    }
}

// Stuur een frame naar de backend voor voorspelling
function startPrediction() {
    const videoElement = document.getElementById('video-feed');
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');

    // Zorg ervoor dat het canvas de juiste afmetingen heeft
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;

    // Teken het huidige frame op het canvas
    ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

    // Zet de afbeelding om naar een Base64-gecodeerde string
    const imageData = canvas.toDataURL('image/jpeg');

    // Verstuur de afbeelding naar de backend voor voorspelling
    fetch('/start-prediction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            image: imageData
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction-text').innerText = `Voorspelling: Het balletje zal vallen op nummer ${data.prediction}.`;
    })
    .catch(error => {
        console.error('Er ging iets mis!', error);
        document.getElementById('prediction-text').innerText = 'Er is een fout opgetreden.';
    });
}

// Zorg ervoor dat de camera wordt ingeschakeld wanneer de pagina wordt geladen
window.onload = setupCamera;
