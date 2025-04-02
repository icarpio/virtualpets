document.addEventListener("DOMContentLoaded", function () {
    var petId = document.getElementById("game-container").getAttribute("data-pet-id");
    var petImageUrl = document.getElementById("game-container").getAttribute("data-pet-image");
    //var petName = document.getElementById("game-container").getAttribute("data-pet-name");
    var hunger = parseInt(document.getElementById("game-container").getAttribute("data-hunger"));
    var energy = parseInt(document.getElementById("game-container").getAttribute("data-energy"));
    var happiness = parseInt(document.getElementById("game-container").getAttribute("data-happiness"));
    var csrfToken = document.getElementById("game-container").getAttribute("data-csrf");

    var config = {
        type: Phaser.AUTO,
        width: 800,
        height: 600,
        parent: 'game-container',
        scene: { preload, create, update }
    };

    var petImage, hungerText, energyText, happinessText;
    var game = new Phaser.Game(config);

    function preload() {
        if (!petImageUrl) {
            console.error('La URL de la imagen es inválida');
        } else {
            this.load.image('background', '/static/images/part3.png');
            var proxyUrl = "/pets/image-proxy/" + encodeURIComponent(petImageUrl);
            this.load.image('pet', proxyUrl);
        }
        this.load.image('hungerButton', '/static/images/b1.png');  
        this.load.image('energyButton', '/static/images/b2.png');
        this.load.image('happinessButton', '/static/images/b3.png');

        this.load.image('hungerIcon', '/static/images/food.png');  
        this.load.image('energyIcon', '/static/images/energy.png');
        this.load.image('happinessIcon', '/static/images/smile.png');
    }

    function create() {
        this.add.image(400, 300, 'background').setScale(1.5);
        petImage = this.add.image(430, 220, 'pet');
        
        this.add.image(50, 100, 'hungerIcon').setScale(0.3);
        this.add.image(50, 160, 'energyIcon').setScale(0.3);
        this.add.image(50, 220, 'happinessIcon').setScale(0.3);
        
        //this.add.text(35, 40, "Mascota: " + petName, { font: "24px Arial", fill: "#ffffff" });

        var hungerButton = this.add.image(200, 510, 'hungerButton').setInteractive().on('pointerdown', () => increaseParameter('hunger'));
        var energyButton = this.add.image(400, 510, 'energyButton').setInteractive().on('pointerdown', () => increaseParameter('energy'));
        var happinessButton = this.add.image(600, 510, 'happinessButton').setInteractive().on('pointerdown', () => increaseParameter('happiness'));

        hungerText = this.add.text(80, 90, 'Hambre: ' + hunger, { font: '20px Arial', fill: '#ffffff' });
        energyText = this.add.text(80, 150, 'Energía: ' + energy, { font: '20px Arial', fill: '#ffffff' });
        happinessText = this.add.text(80, 210, 'Felicidad: ' + happiness, { font: '20px Arial', fill: '#ffffff' });

        hungerButton.setScale(0.16);
        energyButton.setScale(0.16);
        happinessButton.setScale(0.16);
        petImage.setScale(1.7);
         // Volteo continuo de la imagen de la mascota
        this.time.addEvent({
            delay: 1000, // 500ms para alternar
            callback: () => {
                petImage.toggleFlipX(); // Alterna el flipX
            },
            loop: true // Hace que el evento sea continuo
        });
    }

    function update() {
        hungerText.setText('Hambre: ' + hunger);
        energyText.setText('Energía: ' + energy);
        happinessText.setText('Felicidad: ' + happiness);
    }

    function increaseParameter(param) {
        let urlMap = {
            'hunger': `/pets/increase_hunger/${petId}/`,
            'energy': `/pets/increase_energy/${petId}/`,
            'happiness': `/pets/increase_happiness/${petId}/`
        };

        fetch(urlMap[param], {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (param === 'hunger') hunger = data.hunger;
            else if (param === 'energy') energy = data.energy;
            else if (param === 'happiness') happiness = data.happiness;
        })
        .catch(error => console.error('Error:', error));
    }
});
