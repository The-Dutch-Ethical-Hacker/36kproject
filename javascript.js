const videoElement = document.getElementById('video-feed');
const startButton = document.getElementById('start-button');
const cameraSelect = document.getElementById('camera-select');

// Start de camera en toon de feed op het scherm
async function setupCamera() {
    const selectedCamera = cameraSelect.value;

    const constraints = {
        video: {
            facingMode: selectedCamera
        }
    };

    try {
        // Verkrijg toegang tot de camera
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        videoElement.srcObject = stream;
    } catch (error) {
        console.error("Camera kon niet worden geopend:", error);
        alert("Er is een fout opgetreden bij het openen van de camera.");
    }
}

// Zet de camera op bij het klikken op de knop
startButton.addEventListener('click', setupCamera);

// Functie voor voorspelling (voorbeeld)
function startPrediction() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');

    // Zorg ervoor dat het canvas de juiste afmetingen heeft
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;

    // Teken het huidige frame van de video
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
