"use strict";
console.log('<< https://github.com/ariya/phantomjs >>');
console.log('');

var str = "Les grandes personnes m’ont conseillé de laisser de côté les dessins de serpents boas ouverts ou fermés, et de m’intéresser plutôt à la géographie, à l’histoire, au calcul et à la grammaire. C’est ainsi que j’ai abandonné, à l’âge de six ans, une magnifique carrière de peintre. J’avais été découragé par l’insuccès de mon dessin numéro 1 et de mon dessin numéro 2. Les grandes personnes ne comprennent jamais rien toutes seules, et c’est fatigant, pour les enfants, de toujours et toujours leur donner des explications.";
var cars = str.split(/[!?.]/);

        var i;
        for (i=0;i<cars.length;i++){
            if(cars[i].charAt(0) == " "){
                cars[i] = cars[i].substring(1, cars[i].length);
                console.log("<p>"+cars[i]+".</p>");
                }
        }

phantom.exit();
