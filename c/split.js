"use strict";
console.log('<< https://github.com/ariya/phantomjs >>');
console.log('');

var str = "Quand j’en rencontrais une qui me paraissait un peu lucide, je faisais l’expérience sur elle de mon dessin numéro 1 que j’ai toujours conservé. Je voulais savoir si elle était vraiment compréhensive. Mais toujours elle me répondait : « C’est un chapeau. » Alors je ne lui parlais ni de serpents boas, ni de forêts vierges, ni d’étoiles. Je me mettais à sa portée. Je lui parlais de bridge, de golf, de politique et de cravates. Et la grande personne était bien contente de connaître un homme aussi raisonnable.";
var cars = str.split(/[!?.]/);

var i;
for (i=0;i<cars.length;i++){
    if(cars[i].charAt(0) == " "){
        cars[i] = cars[i].substring(1, cars[i].length);
        
        }
    console.log("<p>"+cars[i]+".</p>");
}

phantom.exit();
